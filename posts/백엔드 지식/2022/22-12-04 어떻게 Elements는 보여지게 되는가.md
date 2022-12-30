---
title: 어떻게 Elements는 보여지게 되는가
date: 2022-12-04
---

## 주제 : #CSS #display

## ✏️ 메모

### inline-level vs block-level

블록 속성은 컨텐츠에 관계없이 차지할 수 있는 모든 너비(width)를 채우게 됩니다. 반면에 인라인 속성은 컨텐츠가 차지하는 만큼만 너비를 가지게 되고 별도의 개행이 생기지 않습니다. 이러한 특성 때문에 블록 속성은 "heading", "structural element"와 같이 큰 조각의 컨텐츠를 담당하고 인라인 속성은 "few words"나 "highlight, bold"와 같이 몇몇 단어를 포함하는 경우에 쓰입니다.

기본적으로 html 태그들은 기본값들이 지정되어있지만 `display` 속성을 이용해서 이를 변경할 수 있습니다. 또한 inline-block 이라는 값은 block-level element처럼 box model properties를 지정할 수 있게 해주지만, 다른 elements 사이에 inline으로 표현되는 것은 유지됩니다.

### What is the Box Model?

박스 모델 컨셉에 있어서, 모든 element는 직사각형이고 width, height, padding, borders, and margins와 같은 properties들을 갖습니다. 따라서 페이지에 그려지는 모든 요소들을 사각형으로 볼 수 있는 시선 또한 프론트 개발자에게는 매우 중요하다고 할 수 있습니다.

모든 element가 직사각형이라고 위에서 말했듯이 이 사이즈를 결정하는 몇몇 중요한 properties가 있습니다. 그 중에서도 width, height가 중요하다고 볼 수 있는데 이는 `display` property에 의해서 결정되는 요소입니다. 컨텐츠에 의해서 결정될지 혹은 width, height를 명시해서 결정될지에 대한 이야기이죠. 또한 padding, border, margin 요소가 있는데 이는 일반적으로 box의 바깥쪽 영역을 확장시키는 역할을 합니다.

실제로 그려지는 영역의 너비는 아래와 같이 계산될 수 있는 것이죠.

`margin-right` + `border-right` + `padding-left` +
`width` +
`padding-left` + `border-left` + `margin-left`

하지만 이와 같은 방식은 실제 개발자들에게 많은 혼동을 가져다 줍니다. 400px로 그려지길 원했는데, margin, padding 등에 의해 492px이 그려진다면 헷갈릴 뿐 아니라, 사이즈를 맞추는 것도 어려워지기 마련입니다.

### Box Sizing

위와 같은 문제점 때문에 box model을 위한 다른 계산 방법들이 필요하게 되었습니다. CSS3 에서는 `box-sizing` property를 도입하였습니다. `content-box`, `padding-box`, `border-box` 방식이 있는데 약간씩 다른 계산방식이므로 살펴보도록 하겠습니다.

- `Padding Box`: padding을 width와 height에 포함하여 계산하도록 바꾸는 방식입니다. 만약 이 방식에서 padding이 20이고, width가 400이면 실제 width는 400으로 계산되게 됩니다. 만약 이 상태에서 padding이 커지게 된다면 컨텐츠 사이즈가 축소되게 되는 것 입니다.
  - 참고로 padding-box는 이제는 deprecated된 값입니다. (웬만하면 사용하지 말것!)
- `Border Box`: `border`과 `padding`을 width, height 영역에 포함시키는 방식입니다.
- 또한 `margin`은 box-sizing 방식에 관계없이 항상 더해지는 영역임을 기억하면 암기하기 쉬울 것 입니다.

위 스펙이 생긴 뒤로 가장 선호되는 `box-sizing` 방식은 바로 `border-box` 입니다. 이 방식을 이용하면 더욱 계산하기 편하게 됩니다. 예를 들어 우리가 400 pixels 너비를 원한다면, width를 이 값으로 설정하고 padding, border를 적용하면 됩니다. 또한 40% 와 같은 상대 단위와도 쉽게 결합시켜 사용할 수 있으므로 확장성도 있습니다.

단점이 있다면 그건 바로 CSS3 명세이므로 모든 브라우저에서 지원되지는 않는다는 점입니다. 다행히도 현재 대부분의 브라우저에서 지원한다는 점이므로 우리는 크게 신경쓸 필요는 없습니다. 다만, 어느 브라우저에서 이슈가 발생할 수 있는지 정도는 알 수 있어야 합니다.

## 🔗 참고문헌

## 🔗 연결문서
