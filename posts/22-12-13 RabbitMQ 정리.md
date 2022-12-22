---
title: RabbitMQ 정리
date: 2022-12-13
tags:
 - RabbitMQ
---

## 메모

- `RabbitMQ`는 메시지 브로커입니다. 
	- 메시지를 수락(accept)하거나 포워드(forward)할 수 있습니다.
	- 우체통에 편지를 넣어두면 언젠간 도착하는 과정에서 RabbitMQ는 우체통의 역할을 맡고 있습니다.

### 용어 정리

- `Producing` : 단순히 보내는 것에 불과하지 않습니다. 또한 메시지를 보내는 프로그램을 "producer" 라고 부릅니다.
- `Queue` : `RabbitMQ` 내에 있는 우체통에 불과합니다. RabbitMQ와 애플리케이션을 통해 전달되는 메시지들은 큐안에만 저장됩니다. 커다란 메시지 버퍼로 호스트의 메모리와 디스크에 대해서만 제약적입니다. 많은 "producers"에서 여러 메시지를 생성하여 하나의 큐로 보낼 수 있습니다. 그리고 많은 "consumer" 들은 하나의 큐로부터 데이터를 받아올 수 있습니다.
- `Consuming`: 받는 것(receiving)과 비슷한 의미로 쓰입니다. "consumer"는 메시지를 받기를 기다리는 프로그램들을 의미합니다.

### Round-robin dispatching (라운드 로빈)

태스크 큐의 장점 중 하나는 작업을 쉽게 병렬 처리할 수 있다는 점입니다. 또한 워커를 추가하면 된다는 점에서 손쉽게 스케일 업 할 수 있습니다. 

만약 메시지를 worker 여러 대가 계속 받아서 처리(consume)한다고 하면 어떻게 분배될지 이야기해봅시다. 

![[Pasted image 20221213174212.png]]



## 참고문헌

- https://www.rabbitmq.com/tutorials/tutorial-one-python.html

## 연결문서

