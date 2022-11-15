# FinalProject

https://github.com/Thxnya/FinalProject<br>
EasyOCR 학습 : https://thxanalysis.tistory.com/category/EasyOCR

## 최종 프로젝트 - AI기반 영상 내 정보 탐지 서비스 개발



📰 프로젝트 개요<br/>
---
인터넷 강의 수강생을 위해서 편의성 제공 서비스를 개발하려고 합니다.<br/>
<br/>
코로나 시대를 지나며 이러닝 이용률과 시장이 커지고 있습니다.<br/>
하지만 대면강의와 비교해서 불편한 점이 많습니다.<br/>
불편함을 해소하기 위해서 여러가지 딥러닝 모델과 크롤링 등을 이용하여<br/>
편의성 제공 웹서비스를 개발하려고 합니다.<br/>



💬 프로젝트 결론<br/>
---
인터넷 강의 수강생들에게 편의를 제공해주는 영상 내 텍스트 인식, QnA, 해시태그, 영상추천 기능을 구현해보았습니다.<br/>
<br/>
다양한 플랫폼에 적용하여 영상 내 텍스트 자동 추출 기능을 활용이 가능할 것으로 생각합니다.<br/>
특히, 시각장애인을 대상으로 하여 음성인식을 이용한 맞춤형 교육 플랫폼으로 활용방안도 가능할 것이라 생각합니다.<br/>



⚡ 발표 자료<br/>
---
## 현황분석 및 기획
<img src="https://user-images.githubusercontent.com/104615422/194770779-b10e3686-d235-4fc1-a9c9-cc7818c2670d.jpg" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615422/194770782-bf284cea-8dcc-455b-923e-1540fe4c32db.jpg" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615422/194770783-ad603b1e-a159-4e4f-ad93-a16473ac2cc0.jpg" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615422/194770784-998652da-27b9-4510-9b27-67fceae690e7.jpg" width="60%" height="60%">

---

## 영상 내 텍스트 인식
###  - 텍스트 인식(EasyOCR)
<img src="https://user-images.githubusercontent.com/104615422/194770785-1976f200-0aa8-4b44-881e-8164475cf401.jpg" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615422/194770788-25ec10f9-890c-4dda-b8cd-dbec38df2234.jpg" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615422/194770789-db56e3ce-55c1-4a43-935c-365eaf98b6af.jpg" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615422/194770792-a5e504c7-e294-4b9f-b857-f5eb2d267b61.jpg" width="60%" height="60%">

###  - 전이학습 결과

<img src="https://user-images.githubusercontent.com/104615422/194770793-925c539d-193c-4106-a790-c51262dcf630.JPG" width="60%" height="60%">

---

##  - 질의응답
###  - 음성인식
###  - 키워드 추출 및 크롤링
<img src="https://user-images.githubusercontent.com/104615422/194770795-565a5362-be6e-41ca-ae6e-84ce1c336ad5.jpg" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615422/194770796-eb843981-5316-41ef-bdf1-2f2b833fcfa8.jpg" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615422/194770798-a64fa9dc-d78e-4605-a4fe-fb866d4867e3.jpg" width="60%" height="60%">

---

## - EasyOCR 학습결과

### - 정답<br>

<br>

회귀계수들의 유의성 F-통계량으로 확인<br>
모형이 얼마나 설명력을 갖는가?<br> 결정계수로 확인<br>
모형이 데이터를 잘 적합하고 있는가?<br> 잔차와 종속변수의 산점도로 확인<br>
데이터가 전제하는 가정을 만족시키는가?<br> 선형성, 독립성, 등분산성, 비상관성, 정상성을 만족하는지 확인<br>
<br>

### - 기본모델<br>

<br>

회귀계수들의 유의성 '['-통계량으로 확인<br>
모형이 얼마나 설명력'올' 갖는가?<br> 결정계수로 확인<br>
모형이 데이터'률' 잘 적합하고 있는가?<br> 잔차와 종속변수의 산점도로 확인<br>
데이터가 전제하는 가정'올' 만족시키'논'가?<br> 선형성, 독립성'' 등분산성'' 비상관성'.' 정상성을 만족하는지 확인<br>
<br>

#### 8개 틀림<br>

<br>

### - 일반학습<br>

<br>

'죄'귀'게'수'뭄'의 유'타'성 F'H''본''제''광'으로 '작'인<br>
'손''콩'이 '곰'마나 '솜'명'루''음' '핏'는가'7'<br> '꼼'정계수로 '탁'인<br>
'손'형이 데이터'틀' 잘 적'잡'하고 있는가'7'<br> 잔차와 종속변수의 산점도로 '락'인<br>
데이터가 '쩐'제하는 가'경''용' '안''즉'시'기'는가'이'<br> 선'콩''데''' '뿌''점''덧''' '퉁'분산'덧''' 비'성'관'덧''' 정'a''덧''용' '안''후'하'든'지 '락'인<br>
<br>

#### 52개 틀림<br>

<br>

### - 전이학습<br>

<br>

회귀계수들의 유의성 F''통계량으로 확인<br>
모형이 얼마나 설명'려'을 '강'는가'7'<br> 결정계수로 '획'인<br>
모형이 데이터'틀' 잘 적합하고 있는가'7'<br> 잔차와 종속변수의 산점도로 확인<br>
데이터가 전제하는 가정을 만'죽'시키는가'7'<br> 선형성'' 독립성'' 등'본'산성'' 비상관성'' 정상성을 만'죽'하는지확인<br>
<br>

#### 15개 틀림
