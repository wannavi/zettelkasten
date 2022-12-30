---
title: Active Record vs Data Mapper
date: 2022-10-24
---

# 주제 : #ORM

## ✏️ 메모

ORM 을 사용할 때 사용하는 대표적인 두 패턴에 대해서 알아보자.

### Active Record Pattern

- 모델을 통해서 데이터베이스에 접근할 수 있는 방식이다.
  - 이름 그대로 모델이 "액티브"해졌다는 느낌으로 받아들이면 된다.
- 간혹 다른 사람들의 소스를 보면 엔티티 클래스 정의에서 `extends BaseEntity`라는 코드를 볼 수 있는데, 이 부분이 바로 액티브 레코드 패턴을 적용하는 방식이다.
- 아래 코드를 보는 편이 이해가 쉬울 듯하니 살펴보도록 하자.

```typescript
@Entity()
export class User extends BaseEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;
}
```

```typescript
const user = new User();
user.name = "John Doe";

await user.save(); // 👉 원래라면 repository를 통해야 하는 부분

const users = await User.find({ skip: 2, take: 5 }); // 👉 다음과 같이 static 메서드들도 추가된다.
```

- 따라서 액티브 레코드 패턴을 적용하면 `Repository`나 `EntityManager`의 도움이 필요 없어짐을 확인할 수 있다.
  - 그 뿐만이 아니라 레포지토리 패턴에서 내부에 정의하된 메서드들을 엔티티 내부로 옮겨 정의하는 식으로 처리한다.

### Data Mapper Pattern

- 일반적으로 더 접하게 되는 패턴인데, 엔티티와 레포지터리를 확실하게 구분하는 방식이다.
  - 엔티티가 하는 일은 거의 없고 매핑해주는 역할을 한다고 생각하면 된다.
- 일반적으로 데이터 매퍼 패턴이 유지보수의 관점에서 더 좋으므로 고민하여 적용하자.
  - 유지보수에 좋은 이유는 레포지토리 레이어를 구분하는 것이 의존성이 더 줄어들기 때문이다.

## 🔗 참고문헌

- [typeorm](https://orkhan.gitbook.io/typeorm/docs/active-record-data-mapper)

## 🔗 연결문서
