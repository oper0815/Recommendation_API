# Recommednation Fullstack project
추천 모델 생성 후 웹배포 과정까지 진행하는 미니 프로젝트로 다음 과정을 통해 진행됩니다. 최종 시나리오는 사용자가 웹페이지에서 제시된 영화 중 재밌게 봤던/관심이 있는 영화를 선택하면 이를 기반으로 콘텐츠를 추천해줍니다. 개발 과정은 다음과 같습니다.
1) 모델 생성
2) Flask를 통한 실시간 inference
3) 웹 페이지 만들기

```
**Run**
python app.py
http://localhost:9090/check 
```
* * *

### 1. Item2vec을 통한 콘텐츠 추천 모델 생성
###### 네이버 영화 데이터셋
* 네이버 영화 시청 이력을 활용했습니다. Small dataset이기 때문에 추천 성능은 낮을 것이며 추천 성능을 높이기 위해서는 데이터 크기를 늘려야합니다.
* naver_movie_dataset.csv를 참고해주세요.
###### 추천 모델 - Item2vec 
* 추천 모델의 배포가 목적이었기 때문에 추천 모델은 간단하고 가벼운 **Item2vec** 모델을 채택했습니다. 시청 이력을 sequence로 취급 후 데이터셋을 시퀀스 길이로 전처리 후 Word2vec 라이브러리인 Gensim을 활용하여 학습합니다. 이후 프론트앤드 연동을 위한 dictionary를 만들어줍니다.
* recommendation_word2vec.ipynb를 참고해주세요.

### 2. Flask를 통한 실시간 inference
* 가장 기본적인 Flask 기능을 사용했으며, 사용자에게 콘텐츠 선택을 유도할 콘텐츠 풀을 생성합니다.
* 실시간 Inference를 위해 dictionary와 모델을 띄웁니다.
* app.py를 참고해주세요.
* 
### 3. Bootstrap, Jinja2로 웹에 띄우기
* 기본 HTML 보다는 Bootstrap을 통해 보다 나은 UI 제공
* Jinja2를 통해 파이썬 코드를 HTML에 적용하였습니다.
* list2.html : 초기 화면 (localhost:9090/check)
* output.html : 추천 결과 화면

### To-be
* 현재 이미지가 넷플릭스 기본 이미지로 되어있는데 DB연동 후 포스터 이미지를 연동하는 프로세스로 변경
* 모델 추가
* 데이터셋 추가 or 변경
* 사용자에게 복수 영화를 선택할 수 있게 구성 후 이를 입력으로 받아 모델 적용하는 구조로 변경
