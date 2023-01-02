---
title: Code Coverage and Quality
date: 2022-10-20
---

# 주제 : #test #code-coverage

## ✏️ 메모

### Code Coverage

- 코드 커버리지는 테스팅에서 얼마나 많은 코드가 평가되는지에 대한 수치에요.
  - 코드 커버리지를 추가하면, 테스트되고 있지 않은 코드를 찾아낼 수 있어요.
- 아래는 실제 pytest-cov를 통해 커버리지를 평가한 결과에요.

```bash
fastapi-tdd-docker on  main [?] on 🐳 v20.10.12 via project took 36.1s
➜ docker-compose exec web python -m pytest --cov="."
================================================================================= test session starts ==================================================================================
platform linux -- Python 3.10.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /usr/src/app
plugins: cov-3.0.0, anyio-3.6.2
collected 6 items

tests/test_ping.py .                                                                                                                                                             [ 16%]
tests/test_summaries.py .....                                                                                                                                                    [100%]

---------- coverage: platform linux, python 3.10.1-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
app/__init__.py               0      0   100%
app/api/__init__.py           0      0   100%
app/api/crud.py              15      0   100%
app/api/ping.py               6      0   100%
app/api/summaries.py         20      0   100%
app/config.py                13      2    85%
app/db.py                    17      7    59%
app/main.py                  18      3    83%
app/models/__init__.py        0      0   100%
app/models/pydantic.py        5      0   100%
app/models/tortoise.py        9      1    89%
tests/__init__.py             0      0   100%
tests/conftest.py            21      0   100%
tests/test_ping.py            5      0   100%
tests/test_summaries.py      31      0   100%
---------------------------------------------
TOTAL                       160     13    92%


================================================================================== 6 passed in 5.70s ===================================================================================

```

- 흔히 100% test coverage라고 회사를 홍보하는 문구로도 쓰여요.
  - 그 말은 즉슨, 모든 코드 라인에 대해서 테스트 코드가 작성되어져 있다는 것이겠지요?
  - 그렇지만 100% 라는 수치가 모든 시나리오를 다루고 있다고는 말할 수는 없어요.

### Code Quality

- 코드 퀄리티를 유지하기 위해서 흔히 도입하는 것이 바로 `Linter`에요.
  - 파이썬에서는 Flake8 등이 있고, 노드 계열에서는 유명한 eslint가 있어요.
-

## 🔗 참고문헌

## 🔗 연결문서
