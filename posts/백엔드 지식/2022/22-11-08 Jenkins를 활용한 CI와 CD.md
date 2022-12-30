---
title: Jenkins를 활용한 CI와 CD
date: 2022-11-08
---

## 주제 : #Jenkins #CI/CD

## ✏️ 메모

### CI/CD란?

- Continuous Integration => 뭘 통합한다는 걸까?
  - 여러 개발자들의 코드 베이스를 계속해서 통합하는 것
- Continuous Delivery => 뭘 배달한다는 걸까?
  - 사용자에게 서비스를 지속적으로 배달한다.
  - 코드베이스가 항상 배포가능한 상태를 유지하는 것.
- Continuous Deployment
  - 코드베이스를 사용자가 사용가능한 환경에서 배포하는 것을 자동화함.

요약하면 각각의 개발자들이 개발을 하는 개발 환경을 사용자가 사용 가능한 서비스로 전달하는 것. 모든 과정을 지속 가능한 형태로 또 가능하다면 자동으로 해서 개발자와 사용자 사이의 격차를 없애는 것이다. 이러한 과정에는 코드를 빌드하고, 테스트하고 배포하는 활동이 있다.

### CI와 함께라면?

- 10명의 개발자가 열심히 개발 => 커밋! => 로컬 테스트 통과 실패.. => 커밋! => 코드베이스 머지 => 만족!
  - 가능한 최대한 많이 빨리빨리 내 코드를 코드베이스에 합치자.
  - 테스트 코드 없는 무서운 코드를 애초에 코드베이스에서 쫓아내자.

### CD와 함께라면?

- QA 엔지니어와 같은 내부 사용자 혹은 실제 production 환경의 사용자에게 지속적이고 안정적으로 서비스를 제공한다.

### 젠킨스 넌 누구냐?

- 자바 런타임 위에서 동작하는 자동화 서버!
  - 다양한 플러그인들을 활용해서 각종 자동화 작업을 처리할 수 있음
  - 일련의 자동화 작업의 순서들의 집합인 Pipeline을 통해 CI/CD 파이프라인을 구축함
- 빌드, 테스트, 배포 등 모든 것을 자동화해주는 자동화 서버!
- 플러그인
  - 정말 많은 플러그인이 존재하지만..
  - 대표적인 플러그인들
    - Credentials Plugin
      - 배포에 필요한 각종 리소스에 접근하기 위한 키 등을 저장
    - Git Plugin
    - Pipeline
      - 여러 플러그인들을 용도에 맞게 사용하고 정의함으로써 파이프라인을 통해 서비스가 배포됨
      - 두 가지 형태의 Pipeline syntax가 존재 (Declarative, Scripted pipeline), 최신인 Declarative syntax를 이용하자.

### 젠킨스 설치해보기

```bash
$ brew install jenkins

$ brew services start jenkins
# $ brew services stop jenkins
# $ brew services restart jenkins
```

- 처음 localhost:8080으로 웹 서비스에 접속하면 패스워드 파일 경로를 주고 복붙해달라고 한다.
- 추천받는 플러그인을 설치받도록 하자.

#### 개발 프로세스

1. 개발자가 자신의 PC에서 개발을 진행한다.
2. 다른 개발자가 작성한 코드와 차이가 발생하지 않는지 내부 테스트를 진행한다. (githook)
3. 진행한 내용을 다른 개발자들과 공유하기 위해 git과 같은 SCM에 올린다. (develop 브랜치)
4. develop 브랜치의 내용을 개발 환경에 배포하기 전에 테스트와 Lint 등 코드 포맷팅을 진행한다.
5. 배포하기 위한 빌드 과정을 거친다.
6. 코드를 배포한다.

#### 여러 배포 환경의 관리

여러 배포 환경의 관리에서 핵심은 "인프라를 모듈화하여 어떤 것이 변수인지 잘 설정하고 이를 잘 설계하는 것!"

가령 APP_ENV처럼 현재 배포하고자 하는 것이 무슨 환경인지 설정하고 앱 내에서 사용하는 다양한 변수들을 APP_ENV에 맞게 잘 가져다 쓰는 것이 핵심.

서비스 내부의 변수 뿐만 아니라 클라우드 리소스를 많이 활용해서 개발하는 요즘에는 클라우드 리소스 내에서 인프라별 키관리가 매우 중요해서 aws system manager의 parameter store와 같은 키 관리 서비스를 쓰는 것을 강추.

### 예제와 함께하는 실습

1. 웹 사이트 코드를 작성한다.
2. 웹 사이트 코드를 빌드 해서 S3에 업로드한다.
3. Node 기반 백엔드 코드를 작성한다.
4. 컴파일, 테스트를 하고 도커 이미지를 빌드 후 ECR에 푸시한다.
5. 업로드한 ECR 이미지로 ECS 서비스를 재시작한다.

#### 해야할 일

- 깃헙 연동

  - 젠킨스가 깃헙 레포지토리에 접근할 수 있도록 "깃헙 액세스 토큰"을 생성한다.
  - "Jenkins 관리" > "Manage Credentials" > "System" > "Global Credentials" > "Add credentials" 로 접근한다.

- AWS 연동
  - 젠킨스가 AWS 서비스에 접근할 수 있도록 "액세스 키"와 "시크릿 키"를 IAM에서 받아온다.
  - "secret text"로 똑같이 credentials에 추가해준다.

## 🔗 참고문헌

- [T아카데미 강좌](https://www.youtube.com/watch?v=JPDKLgX5bRg&ab_channel=SKplanetTacademy)
- [amazon linux에 젠킨스 설치하는 법](https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/)

## 🔗 연결문서

- [[templates/{{date}}]]
