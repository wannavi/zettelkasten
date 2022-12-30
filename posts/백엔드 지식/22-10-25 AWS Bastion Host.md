---
title: AWS Bastion Host
date: 2022-10-25
---

# 주제 : #AWS #Bastion

## ✏️ 메모

### 오버워치 바스티온인가요? 예, 맞습니다.

일단 뜻부터 알아야 모든지 이해하기 쉽다. Bastion은 “요새"를 뜻하는 단어이다. 따라서 외부에서 접근하는 것을 차단하는 무엇인가라고 생각하면 벌써 절반은 넘게 알아가는 것이다.

### 설정 방법

#### 1. VPC 및 서브넷 설정

- VPC - 가상의 사설망을 만든다. (실제 독립망 구축에 드는 노력을 생각하면..)
  - Name tag : 내가 이름 지을 때 쓰는 관례인데 배포용 혹은 테스트용을 구분하기 위해 앞부분에 `prod-` 혹은 `test-` 를 붙여서 만든다.
  - CIDR : 10.0.0.0/16 (잘 모르겠다면 관련 포스트를 읽어보자.)
- Internet Gateway (igw) - VPC가 외부 인터넷과 소통할 수 있게 한다.
  - Name tag : `prod-[프로젝트명]-igw` 와 같은 형식으로 생성한다.
  - 생성하고 나면 Attach 버튼이 활성화되는데, 이때 위에서 만든 VPC를 연결한다.
- Public Subnet - 서브넷은 VPC의 일부분이라 생각하면 되는데, 이중 외부와 통신이 가능한 부분이 Public Subnet이다.
  - 먼저, VPC로 위에서 만든 것을 선택한다.
  - Name tag : `prod-[프로젝트명]-public-subnet-a` 와 같은 형식으로 생성한다.
  - CIDR : 10.0.10.0/24
  - AZ : ap-northeast-2a
- Private Subnet - 주요 서비스가 돌아갈 내부 서브넷
  - 먼저, VPC로 위에서 만든 것을 선택한다.
  - Name tag : `prod-[프로젝트명]-private-subnet-a` 와 같은 형식으로 생성한다.
  - CIDR : 10.0.20.0/24
  - AZ : ap-northeast-2a
- Public Routing Table
  - VPC를 생성할때 기본적으로 이에 대응되는 라우팅 테이블이 생성되었을 것이다.
    - 이름을 `prod-[프로젝트명]-public-rt` 으로 수정하여 사용하자.
  - 위 Routing Table에서 Edit Routes 를 선택하고, Add Route를 추가한다. 이때 Destination은 모든 IP 접근을 뜻하는 0.0.0.0/0을 적어주고, Target으로는 위에서 생성한 인터넷 게이트웨이(igw)를 추가하면 된다.
    - 이제 라우팅 테이블에 두 개의 라우트가 존재하는데, 하나는 VPC 내부 라우팅을 담당하는 기본 라우트와 외부 인터넷과 통신하는 라우트가 존재합니다.
    - 참고로 기본 라우트 규칙 때문에, 설정한 CIDR 대역 내에서의 통신은 VPC 내부로만 통신이 가능합니다. (그래서 사설 IP 대역을 사용하는 것이고요)
  - 이후 `Public Subnet` 과 연결시켜 준다.
- Private Routing Table
  - 이름을 `prod-[프로젝트명]-private-rt` 으로 만들자.
  - 이후 `Private Subnet` 과 연결시켜 준다.

#### 2. 보안 그룹(Security Group) 설정

- Bastion Host용 보안 그룹
  - Name tag : `prod-[프로젝트명]-bastion-sg`
  - VPC : 위에서 생성한 VPC
  - Inbound Rule - 내 서버를 향해 들어오는 트래픽에 대한 정책 (외부 → 내부)
    - Type : `SSH`
    - Source : `내 IP` 또는 `위치 무관`
- Private Host용 보안 그룹
  - Name tag : `prod-[프로젝트명]-private-sg`
  - VPC : 위에서 생성한 VPC
  - Inbound Rule
    - Type : `모든 ICMP - Any IPv4, SSH - Bastion 보안 그룹`
    - Source : 위에서 생성한 `Bastion Host용 보안 그룹`

#### 3. EC2 생성 (Bastion Host + Private Host)

- Bastion Host - 문지기 역할을 하는 서버, 배스천 호스트를 통해서만 내부 접근 가능
  - Name tag : `prod-[프로젝트명]-ec2-bastion`
  - instance type : `t2.micro`
  - Subnet : 위에서 생성한 `Public Subnet`
  - Security Group : 위에서 생성한 `Bastion Host용 보안 그룹`
  - Elastic IP : 할당
- Private Host - 서비스가 올라갈 호스트, 외부로부터 고립되어 있음.
  - Name tag : `prod-[프로젝트명]-ec2-private`
  - instance type : `t2.micro`
  - Subnet : 위에서 생성한 `Private Subnet`
  - Security Group : 위에서 생성한 `Private Host용 보안 그룹`
  - Elastic IP : 할당 X

#### 4. Bastion을 통한 Private EC2 접속 시도

- 할당된 공인 IP와 pem 키를 통해 Bastion 호스트에 SSH 접근
  - `ssh -i ~/.ssh/[이름].pem [ec2-user@](<mailto:ec2-user@3.35.95.30>)[Public IP]`
- 접속 완료 시, Private Host에 Ping Test (위 보안 그룹에서 ICMP 허용)
  - 아래와 같이 핑이 정상적으로 보내지면 성공적으로 완료한 것이다!

![[public/Pasted image 20221025152024.png]]

- Private Subnet에 위치한 EC2에 접근하고 싶은데, 현재 상황에서는 Bastion에 별도의 pem 키가 존재하지 않기 때문에 불가능하다는 사실을 알 수 있다.
- 그렇다면 ssh를 통해 파일을 전송하는 커맨드인 scp를 이용하여 로컬에서 Bastion 호스트로 pem 키를 업로드하면 되는 것이다.
  - `scp -i [Bastion Pem key] [upload file] [user]@[host ip]:[path]`
- 이제 다시 Bastion host 로 접속하면 해당 경로에 파일이 업로드 된 것을 확인할 수 있.다ㄷ
  - 이제 아래 명령어를 통해 Bastion에서 Private EC2로 접속하겠다.
  - `chmod 400 [uploaded pem key]`
  - `ssh -i [uploaded pem key] ec2-user@[private ip]`

![[public/Pasted image 20221025152100.png]]

### 마치면서

그래서 배스천 호스트를 두면 더 안전한가?

- 특정 IP만 특정 접근 권한을 가지도록 강제할 수 있다.
- 모든 접근 이력을 배스천 호스트에서 책임지면 된다.

### 더 나아가기

하지만 배스천 호스트 방식은 번거롭고 귀찮은 점이 많다. (사실, 배스천 호스트를 두는 게 보안적으로 유의미한가라는 질문이 나올 수도 있다. 해당 내용은 추후에 다른 글을 통해서 알아보도록 하자.)

대안으로 AWS Systems Manager(SSM)을 통해 접근하는 방법도 있으니 살펴보도록 하자.

- [](https://aws.amazon.com/ko/premiumsupport/knowledge-center/systems-manager-ssh-vpc-resources/)[https://aws.amazon.com/ko/premiumsupport/knowledge-center/systems-manager-ssh-vpc-resources/](https://aws.amazon.com/ko/premiumsupport/knowledge-center/systems-manager-ssh-vpc-resources/)
- [](https://musma.github.io/2019/11/29/about-aws-ssm.html)[https://musma.github.io/2019/11/29/about-aws-ssm.html](https://musma.github.io/2019/11/29/about-aws-ssm.html)

## 🔗 참고문헌

## 🔗 연결문서

- [[posts/백엔드 지식/22-09-01 NAT Gateway - Private Subnet에 존재하는 EC2 호스트를 외부와 통신하게 하기]]
