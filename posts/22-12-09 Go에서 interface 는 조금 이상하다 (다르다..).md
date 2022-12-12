---
title: Go에서 interface 는 조금 이상하다 (다르다..)
date: 2022-12-09
---

## 주제 : #Go #Interface

## ✏️ 메모

일반적으로 interface를 사용하는 경우는 implements로 유형을 "고정"시키는 경우라고 나는 생각한다. 하지만 Go에서의 implements 키워드는 뿐 아니라 비슷한 키워드를 제공하지 않는다.

Go에서 인터페이스 자료형은 "암시적"이다. 전달하는 유형이 인터페이스가 요청하는 유형과 "일치"한다면 컴파일이 된다. (IDE의 힌팅을 받지 못하는 것은 너무 별로라고 생각한다..)

예를 들어 암시적으로 `Shape` 인퍼페이스를 만족하는 `Circle`과 `Rectangle` 이 있다고 하면, 이 둘을 인자로 받고 싶다면 `Shape` 인터페이스의 도움을 받으면 되는 것이다.

## 🔗 참고문헌

- [Example #1](https://gobyexample.com/interfaces)

## 🔗 연결문서
