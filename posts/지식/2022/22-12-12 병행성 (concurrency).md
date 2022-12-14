---
title: 병행성 (concurrency)
date: 2022-12-12
---

## 주제 : #OS #Concurrency #thread

## 정리

- **임계 영역(critical section)**: 보통 변수나 자료 구조와 같은 공유 자원을 접근하는 코드의 일부분을 말한다.
- **경쟁 조건(race condition)**: 멀티 쓰레드가 거의 동시에 임계영역을 실행하려고 할 때 발생하며 공유 자료 구조를 모두가 갱신하려고 시도한다면 깜짝 놀랄 의도하지 않는 결과를 만든다.
- **비결정적(indeterminate)**: 프로그램은 하나 또는 그 이상의 경쟁 조건을 포함하여 그 실행 결과가 각 쓰레드가 실행된 시점에 의존하기 때문에, 프로그램의 결과가 실행할 때마다 다르다. 결과는 컴퓨터 시스템에서 일반적으로 기대하는 바와 달리 결정적이지 않다.
- 이와 같은 문제들을 회피하려면 쓰레드는 **상호 배제(mutual exclusion)**라는 기법의 일종을 사용하여서 하나의 쓰레드만이 임계 영역에 진입할 수 있도록 보장한다. 그 결과로 경쟁을 피할 수 있고 프로그램 실행 결과를 결정론적으로 얻을 수 있게 된다.

## 메모

### 서문

실제 컴퓨터에는 **멀티 쓰레드** 프로그램들이 있다. 각 **쓰레드**는 독립된 객체로서 프로그램 내에서 프로그램을 대신하여 일을 한다. 이 쓰레드들은 메모리에 접근하는데, 쓰레드 입장에서 메모리는 위에서 이야기한 복숭아와 같다. 따라서 **쓰레드들이 메모리를 접근하는 것을 조정하지 않으면 프로그램이 예상처럼 동작하지 않을 수도 있게 된다.**

이를 운영체제에서 다뤄야 하는 이유는 첫 쨰로 운영체제는 락(lock)과 컨디션 변수(conditional variables)와 같은 기본 동작으로 멀티쓰레드 프로그램을 지원해야 한다. 또한 운영체제는 그 자체로 최초의 동시 프로그램이기 때문이다. 운영체제가 관리하고 있는 메모리 영역을 조심스럽게 접근하지 않으면 큰일이 일어나게 된다.

### 개요

- **프로세스와 쓰레드 비교**
  - 하나의 쓰레드의 상태는 프로세스의 상태와 매우 유사하다. 쓰레드는 어디서 명령어들을 불러 들일지 추적하는 프로그램 카운터(PC)와 연산을 위한 레지스터들을 가지고 있다.
  - 만약 두 개의 쓰레드가 하나의 프로세서에서 실행 중이라면 실행하고자 하는 쓰레드 (T2)는 반드시 문맥 교환(context switch)을 통해서 실행 중인 쓰레드 (T1)과 교체되어야 한다. 쓰레드 간의 문맥 교환은 T1이 사용하던 레지스터들을 저장하고 T2가 사용하던 레지스터의 내용으로 복원한다는 점에서 프로세스의 문맥 교환과 유사하다.
    - 프로세스에서 프로세스의 상태를 PCB(process control block)에 저장하듯이 프로세스의 쓰레드들의 상태를 저장하기 위해서는 하나 또는 그 이상의 TCB(thread control block)이 필요하다.
  - 가장 큰 차이점은 쓰레드 간의 문맥 교환에서는 주소 공간을 그대로 사용한다는 것이다 (사용하고 있던 페이지 테이블을 그대로 사용하면 된다.)
- **단일 쓰레드 프로세스와 멀티 쓰레드 프로세스 비교**
  - ![[public/스크린샷 2022-12-12 오후 2.59.55.png]]
  - 두 개의 쓰레드가 실행되는 경우 두 개의 스택이 할당되는 모습을 볼 수 있다. 스택에서 할당되는 변수들이나 매개 변수, 리턴 값, 그리고 그 외에 스택에 넣는 것들은 해당 쓰레드의 스택인 쓰레드-로컬 저장소(thread-local storage)라 불리는 곳에 저장된다.

### 예제: 쓰레드 생성

```c
#include <assert.h>
#include <pthread.h>
#include <stdio.h>

void *mythread(void *arg) {
  printf("%s\n", (char *)arg);
  return NULL;
}

int main(int argc, char *argv[]) {
  pthread_t p1, p2;
  int rc;

  printf("main: begin\n");

  rc = pthread_create(&p1, NULL, mythread, "A");
  assert(rc == 0);
  rc = pthread_create(&p2, NULL, mythread, "B");
  assert(rc == 0);

  rc = pthread_join(p1, NULL);
  assert(rc == 0);
  rc = pthread_join(p2, NULL);
  assert(rc == 0);

  printf("main: end\n");

  return 0;
}
```

위 코드는 두 개의 쓰레드 (T1과 T2)를 생성한 후에 메인 쓰레드가 `pthread_join()` 을 호출하여 특정 쓰레드의 동작의 종료를 대기한다. 이 프로그램의 가능한 실행 순서가 여러 개 있다는 점을 주목하자. `pthread_join()` 을 통해 대기하기 이전에 각 쓰레드에서 리턴이 일어날 수도 있고, 그 반대의 경우도 가능하다는 뜻이다. 또한 쓰레드 1이 쓰레드 2 보다 먼저 생성된 경우라도 만약 스케줄러가 쓰레드 2를 먼저 실행하면 "B"가 "A"보다 먼저 출력될 수도 있다.

이처럼 컴퓨터의 병행성이라는 주제는 실행 순서를 예측하기 어렵다는 점에서 먼저 어렵다고 할 수 있다. 하지만 더 큰 문제는 데이터의 공유라는 주제에서 발생한다.

### 훨씬 더 어려운 이유: 데이터 공유

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#include "common.h"
#include "common_threads.h"

int max;
volatile int counter = 0;

void *mythread(void *arg) {
  char *letter = arg;
  int i; // stack (private per thread)
  printf("%s: begin [addr of i: %p]\n", letter, &i);

  for (i = 0; i < max; i++) {
    counter = counter + 1;
  }
  printf("%s: done\n", letter);

  return NULL;
}

int main(int argc, char *argv[]) {
  if (argc != 2) {
    fprintf(stderr, "usage: main-first <loopcount>\n");
    exit(1);
  }
  max = atoi(argv[1]);

  pthread_t p1, p2;
  printf("main: begin [counter = %d] [%x]\n", counter, (unsigned int)&counter);
  Pthread_create(&p1, NULL, mythread, "A");
  Pthread_create(&p2, NULL, mythread, "B");
  // join waits for the threads to finish
  Pthread_join(p1, NULL);
  Pthread_join(p2, NULL);
  printf("main: done\n [counter: %d]\n [should: %d]\n", counter, max * 2);
  return 0;
}

```

```bash
➜ ./t1 100000000
main: begin [counter = 0] [44d8000]
A: begin [addr of i: 0x16b9b6fac]
B: begin [addr of i: 0x16ba42fac]
B: done
A: done
main: done
 [counter: 102667398]
 [should: 200000000]
```

코드를 쭉 읽고, 우리가 기대하는 값과 실제 값이 다르다는 점을 알 수 있습니다. (위에서 102667398, 200000000)

우리는 지금까지 컴퓨터라면 "결정론"적인 결과를 내야한다고 배워왔고, 위 결과는 이러한 우리의 상식과 다르다고 할 수 있습니다. 그렇다면 이러한 결과는 왜 일어나는 걸까요?

### 제어 없는 스케줄링

counter 갱신을 위해서 실제 컴파일러가 어셈블리 코드를 어떤 식으로 만들어내는지 확인해야 한다.

```assembly
mov 0x8049alc, %eax
add $0xl, $eax
mov %eax, 0x8049alc
```

일어나는 일을 간략하게 정리해보면

- counter 값을 증가시키기 위해 메모리 영역의 값을 레지스터에 옮기고, 증가시킨뒤, 이를 다시 해당 메모리에 씁니다.
- 쓰레드간에 컨텍스트 스위칭이 일어나면 현재 레지스터 정보를 쓰레드 전용 레지스터인 TCB에 저장한뒤 원래 컨텍스트로 돌아올 때 다시 해당 쓰레드로 복구합니다.
- 위 과정 중에서 counter (0x8049alc)가 의도한 값이 아닌 값으로 결정되기도 합니다.

이러한 명령어의 실행 순서에 따라 결과가 달라지는 상황을 **경쟁 조건(race condition)**이라고 부른다. 문맥 교환이 때에 맞지 않게 실행되는 운이 없는 경우 잘못된 결과를 얻게 된다. (이러한 경우를 비결정적이라고 한다.)

멀티 쓰레드가 같은 코드를 실행할 때 경쟁 조건이 발생하기 때문에 이러한 코드 부분을 `임계 영역(critical section)` 이라고 부른다. **공유 변수 (또는 더 일반적으로 공유 자원)를 접근하고 하나 이상의 쓰레드에서 동시에 실행되면 안되는 코드를 임계 영역이라 부른다.**

이러한 코드에서 필요한 것은 상호 배제(mutual exclusion)이다. 이 속성은 하나의 쓰레드가 임계 영역 내의 코드를 실행 중일 때는 다른 쓰레드가 실행할 수 없도록 보장해준다. 

### 원자성에 대한 바람

명령어 하나로 위 동작을 수행한다면 인터럽트 발생을 막아보자!p

-  `memory-add 0x8049alc, $0x1`와 같은 명령어가 존재하고 하드웨어는 이 명령어가 원자적으로 실행되는 것을 보장한다고 하자. **그렇다면 하드웨어가 원자성을 보장해주기 때문에 명령어 수행 도중에 인터럽트가 발생하지 않는다.** 
	- 근데 일반적인 상황에서 이러한 명령어는 존재하지 않는다!.. 병행성을 가지는 B-tree를 설계해야하고 값을갱신한다고 할때, 원자적으로 B-tree를 갱신하는 어셈블리 명령어를 원할까? 그건 아니라고 본다.

하드웨어적으로는 동기화 함수(synchronization primitives) 구현에 필요한 기본적인 명령어 몇 개만 필요하다. 결과적으로 병행 실행이라는 어려운 상황에서 하드웨어 동기화 명령어와 운영체제의 지원을 통해 한 번에 하나의 쓰레드만 임계 영역에서 실행하도록 구성된,  "제대로 잘 작동하는" 멀티 쓰레드 프로그램을 작성할 수 있다.

결론: **동기화 함수를 사용하여 순차적인 명령어들을 원자적 실행 단위로 만들 것이다**. 


## 참고문헌

- OSTEP

## 연결문서
