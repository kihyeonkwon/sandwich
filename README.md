1. https://github.com/kihyeonkwon/sandwich

2. python 3.9.7 / django 4.0.1
   DefaultRouter와 ViewSet으로 네가지 재료들의 CRUD를 담당하고 Sandwich의 경우 Customization을 했습니다.

Sandwich Create : JSON으로 재료들을 프론트에서 넘겨받습니다. 남은 재료가 1개 이상인지 확인, 재료가 과다하게 선택된지 학인, 에러가 없다면 재료를 차감하고 가격을 정산하여 샌드위치를 만듭니다.

Sandwich Destroy : url로 받은 pk값으로 샌드위치 객체를 불러옵니다. 재료들의 재고를 각각 1씩 올려주고 샌드위치를 파괴합니다. Respnose로 원재료들과 가격을 보내줍니다.

openapi-schema.yml에 api 명세서가 나와있으며 drf-yasg를 이용해서 swagger 또한 적용되어 있습니다.
sandwichapp/tests.py 에 테스트케이스가 작성되어 있습니다.

재료의 수정반영 / 삭제미반영을 위해 django-safedelete의 SOFT_DELETE를 사용했습니다.

리스트의 필터링을 위해 django-filter가 사용됐습니다.

drf가 제공하는 pagingation을 settings.py에서 설정해서 사용했습니다.

3.  soft_delete의 존재를 몰라서 model에 대한 많은 고민을 했습니다.
    필요 이유와 사용방법까지 알게돼 즐거웠습니다.

sandwich의 price를 views.py에서 하나하나 더해야되는 것이 맞나 고민이 듭니다.
처음에는 serializer에서 serializermethodfield를 통해서 만들어서 마음에는 들었는데 model field가 아니다 보니 filering이 안되는 문제가 있었습니다.
model안에서 method를 정의해서 field의 price들을 다 더해서 갖고오는 것이 가능한지 해도되는건지 views의 domain을 침해하는건지에 대해 궁금증이 있습니다.

마찬가지로 inventory_count도 views.py에서 하나하나 더하고 빼는것이 맞는지 고민이 듭니다.
OOP 공부를 할때 하나의 클래스안에 전체 population에 대한 int 기록이 있다면 **init**과 **del** 에서 조작을 해준것처럼
model에서 method를 만들어서 관리를 해줄수 없나라는 궁금증이 있습니다.
