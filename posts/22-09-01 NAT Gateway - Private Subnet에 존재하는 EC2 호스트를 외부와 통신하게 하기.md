---
title: NAT Gateway - Private Subnet에 존재하는 EC2 호스트를 외부와 통신하게 하기
date: 2022-09-01
---

## NAT Gateways 란

Network Address Translation 의 약어로 Private Subnet의 인스턴스가 다른 VPC, 온프레미스 네트워크 또는 인터넷 서비스에 연결하는 데 사용할 수 있는 서비스이다. (AWS 피셜)

내게는 군대 근무 중에 자주 접한 용어라 그다지 낯설진 않은 용어이다. 그 당시 내가 이해하고 있던 NAT의 주목적은 사설 네트워크에 있는 여러 대의 호스트를 “단 하나”의 공인 IP 주소를 통해 인터넷에 접속할 수 있게 하는 것이라고 이해하였다. 실제로 군 내부 사설망은 NAT를 통해 외부 사설망을 투명하게 유지하는 것이 가능하다라고 생각할 수 있다.

정리하자면 내부 망에서는 사설 IP 주소를 통해 서로 통신하지만, 외부망(인터넷)에 연결하기 위해서는 NAT를 통해 공인 IP 주소로 변환되는 것이다. (여담이지만 전역한지 꽤 지났는데도, 공인 IP 들이 기억이 난다. 🥲)

AWS에서 NAT 게이트웨이를 설정한다면 당연하게 Elastic IP가 필요하다는 사실도 이해가 되는가?

## 실제 적용

1.  Public Subnet에 NAT gateway를 Elastic IP를 할당하여 생성
2.  Private Subnet Route Table에 NAT gateway를 추가
3.  위 작업이 완료되면 내부 Private Host에서 외부 인터넷으로 접근 가능

결론: Private Subnet에서 외부 (0.0.0.0/0)으로 요청시 라우트 테이블을 통해 먼저 NAT Gateway로 접근하게 되고, Public Subnet에 위치한 인터넷 게이트웨이로 외부와 통신하게 된다.

> NAT Gateway는 Private Subnet 인스턴스를 인터넷에 연결해야 하기 때문에 Public Subnet에 배치해야 합니다.

다시 한번 자세히 이야기하자면, 인터넷 게이트웨이(IGW)는 Public IP를 보유중인 호스트를 외부와 연결시켜주는 역할이다. 일반적으로 퍼블릭 서브넷에 위치한 배스천 호스트를 생각하면 혹은 외부로 노출되는 퍼블릭 호스트들을 생각하면 다들 Elastic IP를 하나씩 할당받고 있음을 알 수 있다. 하지만, 프라이빗 서브넷에 위치한 호스트들은 NAT Gateway에 할당된 Elastic IP 하나만을 가지고 인터넷 게이트웨이를 거쳐서 외부와 통신하게 된다.

## 참고자료

- [](<https://medium.com/awesome-cloud/aws-vpc-difference-between-internet-gateway-and-nat-gateway-c9177e710af6#:~:text=NAT%20Gateway%20(NGW)%20is%20a,a%20connection%20with%20those%20instances>)[https://medium.com/awesome-cloud/aws-vpc-difference-between-internet-gateway-and-nat-gateway-c9177e710af6#:~:text=NAT](https://medium.com/awesome-cloud/aws-vpc-difference-between-internet-gateway-and-nat-gateway-c9177e710af6#:~:text=NAT) Gateway (NGW) is a,a connection with those instances.
