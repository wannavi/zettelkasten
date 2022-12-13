---
title: 
date: 2022-12-13
tags:
 - 태그 1
---

## 메모

```go
package main

import "fmt"

type Tree struct {
	Value int
	Left  *Tree
	Right *Tree
}

func Walk(t *Tree, ch chan int) {
	defer close(ch)
	var walk func(t *Tree)
	walk = func(t *Tree) {
		if t == nil {
			return
		}
		walk(t.Left)
		ch <- t.Value
		walk(t.Right)
	}
	walk(t)
}

func Same(t1, t2 *Tree) bool {
	ch1, ch2 := make(chan int), make(chan int)

	go Walk(t1, ch1)
	go Walk(t2, ch2)

	for {
		v1, ok1 := <-ch1
		v2, ok2 := <-ch2

		if v1 != v2 || ok1 != ok2 {
			return false
		}

		if !ok1 {
			break
		}
	}

	return true
}

func main() {
	t1 := Tree{
		Value: 3,
		Left: &Tree{
			Value: 1,
			Left:  &Tree{Value: 1},
			Right: &Tree{Value: 2},
		},
		Right: &Tree{
			Value: 8,
			Left:  &Tree{Value: 5},
			Right: &Tree{Value: 13},
		},
	}
	t2 := Tree{
		Value: 3,
		Left: &Tree{
			Value: 1,
			Left:  &Tree{Value: 1},
			Right: &Tree{Value: 2},
		},
		Right: &Tree{
			Value: 8,
		},
	}

	fmt.Println(Same(&t1, &t2))
}
```

- main 부분을 테스트 코드로 작성해보는 것도 좋은 훈련이 될 것이라 생각한다. ^^

## 참고문헌


## 연결문서

