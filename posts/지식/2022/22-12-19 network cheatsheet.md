## Connecting - #UTP #SWITCH

- Q. 1000BASE-T는 어떤 속도로 실행되는가? 또한 어떤 종류의 케이블이 사용되는가?’
    
    A. 1000BASE-T를 해석하는 법을 알아야한다. 1000 Mbps(= 1 Gbps)라는 뜻이므로 1Gbps로 전송되고 T는 UTP 케이블이라는 뜻이다.
    
- Q. 어떤 타입의 UTP 케이블이 호스트와 스위치를 연결하는데 사용되는가? 스위치와 스위치의 경우는 어떠한가?
    
    A. 호스트는 스트레이트 케이블을 사용하여 스위치에 연결됩니다. 이는 스위치가 RX 및 TX 와이어 쌍을 반대로 설정했기 때문입니다. 이러한 방식으로 호스트는 전송 쌍을 스위치가 수신하는 쌍에 맞춰 정렬합니다.
    
    스위치를 다른 스위치에 연결할 때 두 스위치는 쌍을 반대로 합니다. 이것은 우리가 크로스오버 케이블을 사용해야 한다는 것을 의미합니다. 케이블이 쌍을 바꿈으로써 다시 수신과 함께 라인을 전송합니다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c061ab4e-31dc-4ae2-bbf1-c72378e807dd/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e9ad3fbc-2a91-4ede-a8ec-d1de592b5879/Untitled.png)
    
- Q. 그렇다면 왜 비슷한 단말끼리는 `cross-over` 케이블 방식을 사용하는가?
    
    [Why do similar devices use a cross-over cable instead of a straight-through cable?](https://superuser.com/questions/1061159/why-do-similar-devices-use-a-cross-over-cable-instead-of-a-straight-through-cabl)
    
- Q. Auto-MDIX가 필요한 경우는 언제인가?
    
    1Gbps 이상의 속도가 필요하다면 Auto-MDIX가 필요하다.
    
- Q. 언제 fiber 케이블을 UTP 케이블 대신 사용할 것인가 (혹은 필요한가)? 그리고 멀티 모드 대신 싱글 모드가 필요한 때는 언제인가?
    
    fiber 케이블이 선호되는 경우는 몇 가지 없다. 먼저 장거리를 송신해야할 때, 그리고 자기적 간섭(EMI)이 심한 장소에서 네트워크 환경을 구축해야 할 때.
    
    매우 긴 케이블을 가지고 있다면, 우리는 이를 single-mode로 동작시켜야 할 것이다. 이건 더 비싸지만 적절한 하드웨어와 함께라면 40km는 전송할 수 있다.
    
- Q. bend radius는 무엇인가? bend radius를 신경써야하는 타입의 케이블은 어떤 것이 있는가?
    
    bend radius는 코너에서 얼마나 케이블이 꺾이는 정도에 대한 수치이다. ‘fiber cable’이 유리로 만들어져서 매우 중요한 값이고, 너무 심하면 유리가 깨질 수도 있다.
    
- Q. “full duplex”를 지원하기 위해서 필요한 것은 무엇인가?
    
    케이블링의 종류에 달려 있다. 예를 들어 ‘fibre’의 경우는 dual-cores 여야지 full duplex를 지원한다. 여기서 하나의 코어는 전송, 하나의 코어는 수신용이다. 
    
    UTP 케이블에서는 수신용 한쌍, 송신용 한쌍이 각각 최소로 요구된다. 
    

## Addressing

- Q. 누가 MAC 주소를 컴퓨터에 할당하는가? 컴퓨터는 MAC 주소를 몇 개나 가지고 있는가?
    
    모든 Network Interface Card(NIC)는 고유(burned-in)의 MAC 주소가 주어진다. 제조사에 의해 새겨진 값이라 `Burned In Address` (BIA)라고 불리기도 한다. 달리 말하면 모든 단말에는 NIC당 하나의 MAC 주소를 가지고 있음을 알 수 있다.
    
    하지만 `virtualization` 개념에서 (예를 들어 VM을 띄운다던지) 가상의 MAC 주소가 할당될 수 있는데 이는 나중에 더 자세히 살펴보자.
    
- Q. “local segment”에 메시지를 보내기 위해서, IP 주소가 필요한가?
    
    트래픽의 종류에 따라 결정된다. (필요할 수도 안 할 수도…)
    
    오늘날 대부분의 트래픽은 IP 주소를 요구한다. 그 말은 “single network segment”에서도 IP 주소는 사용된다는 말이다.
    
    그러나 IP주소를 필요로 하지 않는 트래픽이 존재하는 것도 사실이다. 예를 들어 CDP와 spanning-tree가 그 예이다. 이 둘에 대해서는 나중에 더 자세히 알아보자.
    
    또한 “기술적으로” 로컬 세그먼트에서 통신하는데에는 IP 주소를 필요로 하지 않는다.
