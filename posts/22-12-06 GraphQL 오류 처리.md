---
title: GraphQL 오류 처리
date: 2022-12-06
---

## 주제 : #GraphQL #Error

## ✏️ 메모

Apollo Server가 GrapQL 연산을 수행할 때 에러를 던지게 되면 `errors` 라는 배열을 포함해서 클라이언트에 응답을 보내게 됩니다.

- 에러 발생 시 `errors` 배열을 추가해서 응답한다.
  - 아래는 개인 프로젝트에서 `unauthorized 에러의 응답값 입니다.
- 배열의 각 에러에는 `extension` 필드가 존재하고, 에러 코드와 `stacktrace` 와 같은 유용한 정보들을 포함해서 응답합니다.

```json
{
  "errors": [
    {
      "message": "Unauthorized",
      "extensions": {
        "code": "UNAUTHENTICATED",
        "response": {
          "statusCode": 401,
          "message": "Unauthorized"
        }
      }
    }
  ],
  "data": null
}
```

### 커스텀 에러

개인 프로젝트에서 사전 정의된 커스텀 에러를 `apollo-server-express` 내에 있는 `ApolloError` 구현체를 통해 구현할 수 있었습니다.

```ts
import { ApolloError } from "apollo-server-express";

export class InternalServerErrorException extends ApolloError {
  constructor() {
    super("Internal server error", "INTERNAL_SERVER_ERROR");
  }
}
```

ApolloError는 생성자로 `message`, `code`, `extensions` 를 받으므로 이를 기반으로 커스텀 에러를 잘 생성할 수 있습니다. 또한 제 프로젝트에서는 `HttpExcetpion`과 사전 정의된 `ApolloError`를 제외하고는 에러 정보를 클라이언트에 전달하지 않기 위해(보안상 문제) 미들웨어에서 이를 잘 처리하도록 코드를 짜고 시작합니다.

## 🔗 참고문헌

- [Apollo DOCS - Error handling](https://www.apollographql.com/docs/apollo-server/data/errors/)

## 🔗 연결문서
