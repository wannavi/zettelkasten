---
title: express, koa는 쓰기가 어렵다.
date: 2022-10-01
---

가장 큰 이유는 제대로 쓰려면 너무나 많은 세팅을 해야된다는 것이다. 특히 "타입스크립트" 환경에서 이 둘을 이용해 잘 써보려면 코드가 중복되는 부분도 생기고, 쓸데없이 비대해진다는 느낌을 지울 수가 없게 된다. 그렇다고 자바스크립트 그 자체로 쓰려니 ide의 도움을 받을 수 있는 영역도 확 줄어들어버려 점점 쓰기가 싫어지게 된 것이다.

특히 nestjs나 스프링 등을 접하고 난 뒤로 에러핸들링, 요청 검증 등의 영역에서 매우 편리함을 느끼게 되었는데, 이러한 부분에서 지원이 너무 아쉽다고 생각된다. 그리고 테스트 코드를 짜기 위해 controller, service 등의 레이어를 나누게 되면 내 마음에 들지 않고 너무 파편화되어 나눠진다는 느낌이 들기 시작했다. 추후 차선책으로 `routing-controllers`의 도움을 받아 코드를 마이그레이션 해보기도 하였지만 `routing-controllers` 를 깔면 아마 의존성 문제 때문에 시간을 낭비하게 될 확률이 높다. (지금은 모르겠지만...)

결국 또 nest.js 로 돌아오게 된다.. 최근 nest.js보다 좀 더 가볍게 쓰고 싶다는 생각이 들어서 여러가지를 찾아보게 되었는데, 예전에 한 번보고 별로라고 생각했던 `fastfiy`가 눈에 들어오게 되었다. 내가 위에서 말한 express, koa를 사용할 때 불편했던 점들이 잘 개선되어 있는 것 같고 (schema라는 개념, 그리고 plugin), 속도도 다른 것과 비교하여 월등하다고 하니 안쓸 이유가 없는 것 같다.

가끔씩 자기만의 라이브러리를 짜서 활용하는 분들을 몇몇봤는데, 그 때는 이해가 안되었지만 이제는 조금씩 해볼만한 작업이라고 생각이 들고 있다. 그리고 자바 스프링 환경이 괜히 칭송받는게 아니라는 말도 점차 이해가 되고 있는 것 같다. 하지만, 다음 번에는 golang 기반으로 서버를 구성해보려고 한다. ㅎㅎ
