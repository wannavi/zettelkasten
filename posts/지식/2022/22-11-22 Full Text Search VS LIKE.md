---
title: Full Text Search VS LIKE
date: 2022-11-22
---

## 주제 : #DB

## ✏️ 메모

### 배경

- `%찾고 싶은 단어%`와 같이 LIKE로 검색을 하게 되면 인덱스를 활용하지 못합니다.
  - `찾고 싶은 단어%` 와 같은 경우만 가능합니다.
- 이러한 경우에 원하는 키워드를 제대로 찾기 위해 사용할 수 있는 대안이 `Full Text Search` 입니다.

### 전체 텍스트 카탈로그 만들기

- 전체 텍스트 인덱스를 만드려면 먼저 전체 텍스트 카탈로그가 있어야 합니다.
- `CREATE FULLTEXT CATALOG FX_title_teacher GO`

## 🔗 참고문헌

- [MS 전체 텍스트 검색](https://learn.microsoft.com/ko-kr/sql/relational-databases/search/full-text-search?view=sql-server-ver16)
- [postgresql](http://rachbelaid.com/postgres-full-text-search-is-good-enough/)

## 🔗 연결문서
