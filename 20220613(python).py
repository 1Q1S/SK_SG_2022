'''
자동 분석 공정 실적 분석
'''
# 실적 가져올 정보 입력하기

# Case1=제품별 (시간, 원료), (공정, 세척)
    # 공정/세척 타입 선택  > 시간, 원료 선택
    # 1차 Case1 선택 시 , 캠페인 list-up > 복수 선택 가능 및 전체 선택    
    # 캠페인 별 Batch No list-up > 복수 선택 가능 및 전체 선택

# Case2=캠페인별 (시간, 원료), (공정, 세척)
    # 공정/세척 타입 선택 > 시간, 원료 선택
    # 캠페인 선택 후, 캠페인 별 Batch No list-up > 복수 선택 가능 및 전체 선택
    
# Case3=Batch No. (시간 원료)    

# Case4=기간별 (시간, 원료), (공정, 세척)
    # 공정/세척 타입 선택  > 시간, 원료 선택    

# Case5=사용 원료 별 : (원료)
    # 공정/세척/ALL 타입 선택
    # Item-Batch No. 별 개별 원료 사용량 및 전체 원료 사용량 표시

## 필요한 기능 ##
# 0. DB 호출 기능 
#  ## DB 명 정리 필요 
#  - Campaign DB: 
#  - Batch No DB:
#  - Tag 값 DB:
#  - 원료 실적 DB:
#  - 작업 실적 DB: 
# 1. 조건에 맞는 캠페인 List-up (Item ID/ALL, 기간)
# 2. Campaign No. 별 Batch No. 정리 (Item ID/ALL, Campiagn No/ALL, 세척/공정/ALL, 기간)
# 3. Batch No. 별 작업 실적 정리 (Item ID/ALL, Campaign No/ALL, Batch No/All, 온도/압력/교반속도/원료/복수선택, 기간)
#  - 해당 기간내에 시간별로 온도/압력/교반속도/원료 전부 정리
# 4. Data 정리 (Tag/원료/시간, 기간)
# 5. Table (*Name, *X축 data, *Y축)
#  - X축 기준 Y 축 Data Table 생성 및 View, Total, Average 등 출력
# 6. 그래프 유형별 Data 받아서 그리기 (*Name, *X축 data, *Y축)
#  - X 축 기준 Y축 Stack 그래프 (각 실 선 및 Data에 Name 표시)
#  - 평균선 기준 Dev. 값 



# Data 실적 가져오기 (DBMS)