![메인이미지](readme_main.jpg)

## 1. 시나리오 설정
----------------------
배경: 
- 저출산 : 한국은 전 세계 최저 수준의 출산율과 급격한 지방 인구 감소로 인해 사회경제적 문제가 매우 심각함
- 수도권과밀화(지방 공동화) : 수도권 집중화로 인한 주택/교통 문제,   지방 경제 약화 등이 발생하고 있음.

페르소나 :
- 이름 : 이경영
- 소속 : 국토교통부 도시발전계획과 데이터분석팀

목표 :
- 2030년까지 출산율 1.3 회복 
- 2030년까지 지역 균형발전
- 이를 위한 데이터 기반 정책 수립

## 2. 분석 목표 및 방법
-------------------------------
분석 목표:

- 저출산 문제: 출생률 감소 원인 파악 (결혼율, 이혼율, 지역별 차이 등).

- 수도권 과밀화: 지역별 인구 증감 추세, 수도권 집중 요인 분석.



분석 방법:

- 시계열 분석: 출생률, 사망률, 자연증가율 추이.

- 지역별 비교: 수도권 vs. 비수도권의 결혼율, 이혼율, 인구 이동 데이터 연관성 분석.

- 상관관계 분석: 경제·사회 지표(예: 주택 가격, 일자리)와 출산율 간 관계 탐색.



## 3. 데이터셋 피쳐 설명
----------------------------
- Date: 날짜 (월/일/년)

- Region: 지역

- Birth: 출생자 수

- Birth_rate: 출생률

- Death: 사망자 수

- Death_rate: 사망률

- Divorce: 이혼 건수

- Divorce_rate: 이혼률

- Marriage: 결혼 건수

- Marriage_rate: 결혼률

- Natural_growth: 자연증가 인구 (출생 - 사망)

- Natural_growth_rate: 자연증가율

## 4. 가설 설정
저출산 문제:

- 가설 1: 결혼율 감소가 출생률 하락의 주요 원인일것이다.

- 가설 2 : 지역별 경제 수준과 출산율의 상관관계가 높을것이다.(추가데이터수집필요)(지역별 경제소득 데이터) / [이현희]

- 가설 3: 수도권의 높은 생활비가 출산 기피로 이어진다.(추가데이터수집필요)(수도권 물가지수 데이터)
  
- 가설 4 : 20~30대의 높은 실업률이 결혼율 감소에  주요 원인일것이다.(추가데이터수집필요/2030실업률 데이터)

지방 공동화:

- 가설 1: 지방의 낮은 혼인율이 인구 감소를 가속화한다.

- 가설 2 : 지방의 고령화 지수(사망률 대비 출생률)가 수도권보다 높다.(추가데이터수집필요/2030실업률 데이터)

- 가설 3: 지방의 청년 인구 유출이 자연증가율 마이너스로 연결된다.(추가데이터수집필요/전국 인구수 및 인구이동 데이터)

- 가설 4: 수도권으로의 인구 유입이 지방 인구 감소를 가속화한다.(추가데이터수집필요/전국 인구수 및 인구이동 데이터)


## 5. 팀 커밋 컨벤션

Docs : 문서작성
- 예시) git commit -m "Docs : README.md 문서작업"

Feat : 새로운 기능 추가
- 예시) git commit -m "Feat: "메인 페이지 내비게이션 추가"
- 예시) git commit -m "Feat: "회원 가입 기능 구현"

Design : CSS코드수정
- 예시) git commit -m "Design: "메인 페이지 CSS 생성"

Rename: 파일 혹은 폴더명을 수정만 한 경우
- 예시) git commit -m "Rename: "index.html -> main.html 변경"

Test : 테스트코드
- 예시) git commit -m "Test: "API 통신 테스트"


Refactor: 리팩토링 

Fix : 버그 수정

Extra : 그외에 기타 커밋내용