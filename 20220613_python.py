'''
자동 분석 공정 실적 분석
'''
# 실적 가져올 정보 입력하기
# 제품/원료 > 공정/세척 > 기간/CampaignNO/BatchNo > 시간/사용량/Tag Value
from cProfile import label
from winreg import QueryReflectionKey
from numpy import sort
import pymssql
import datetime
import pandas as pd

# material_type=input('1.제품, 2.원료 : ')
# material_ID=input('물질 ID : ') 

# Process_type=input('1.공정, 2.세척 : ')

# period=input('기간을 입력해주세요. Ex) 20220614 20220616 _ 전체 기간 - 0 ').split(' ')

# search_type=input('1.Campaign No., 2.Batch No.: ')  

# Campaign_No=input('Campaign No.를 입력하세요. (Campaign No. List 보기 - 0) : ')

# Batch_No=input('Batch No.를 입력하세요. (Batch No. List 보기 - 0) : ')

# search_value_type=input('1. 작업실적, 2. 원료 사용량, 3. Tag 값 :')

def database_dataload(database_name,userID, userPW, sql):
    conn = pymssql.connect(host=r"61.97.14.141", database=database_name, user=userID,password=userPW)
    cursor = conn.cursor()
    cursor.execute(sql)
    al_row = cursor.fetchall()
    al_list= [list(i) for i in al_row]
    dataframe = pd.DataFrame(al_list)
    conn.close()
    return dataframe

    

def CampaignNo_list(Product_ID, stardate='',enddate=''):
    #Campaign No.를 불러오려면 SAP I/F필요할 것 같음 사전 확인 필요
    
    return

def BatchNo_list(CampaignNO='', stardate='',enddate='', rawmaterial_ID=''):
    #Campaign No. > BR list 불러오기 Campaign No.와 마찬가지로 SAP I/F 필요할 것으로 보임
    #WMS에서 불러올 수 있는지 사전 확인 필요
    return

def operation_list(ProductID, BatchNO, stardate='',enddate=''):
    #공정 별 공정 내역 list로 반환 필요
    #WMS database에 record 있는 것 확인함.
    #공정 변화가 있을 경우 seq.로 일단 순서로 합친 후, process name이 같은 곳에 시간 뿌려질 수 있도록 진행
    database_name= 'TEST-SAPIF'
    userID='wmsa'
    userPW='skbt#$erver1'
    sql=('''
        select DISTINCT A.itemcode,A.orderno,A.lotno, B.operationcode ,operationname ,convert(datetime,concat(substring(A.strdate,1,4),'-',substring(A.strdate,5,2),'-',substring(A.strdate,7,2),' ',substring(A.strtime,1,2),':',substring(A.strtime,3,2),':',substring(A.strtime,5,2))) as str , 
        convert(datetime,concat(substring(A.enddate,1,4),'-',substring(A.enddate,5,2),'-',substring(A.enddate,7,2),' ',substring(A.endtime,1,2),':',substring(A.endtime,3,2),':',substring(A.endtime,5,2))) as ed,A.manhr ,A.machinehr
        FROM (SELECT  *, ROW_NUMBER() OVER(PARTITION BY confirmno ORDER BY convert(datetime,concat(substring(insertdate,1,4),'-',substring(insertdate,5,2),'-',substring(insertdate,7,2),' ',substring(inserttime ,1,2),':',substring(inserttime,3,2),':',substring(inserttime,5,2))) DESC) as rn FROM E_MakingWorktime) A
        join E_MakingOperation B
        on A.confirmno = B.confirmno
        where A.itemcode= '%s'
        OR A.lotno = '%s' 
        ORDER BY B.operationcode;
        '''%(ProductID, BatchNO))
    operation_list_df=database_dataload(database_name,userID, userPW, sql)
    operation_list_df=operation_list_df.drop_duplicates([3,4])
    operation_list_df.reset_index(drop=False,inplace=True)
    return operation_list_df[[3,4]]

print(operation_list('100271','211009028N'))

def Time_result(BatchNO, stardate='',enddate=''):
    #공정 별 작업 시간 list로 반환 필요
    #WMS database에 record 있는 것 확인함.
    return

def Tag_value(BatchNO, operation_seq , Tag_ID,stardate='',enddate=''):
    #MES Database table에 존재함. 
    #Batch No. 확인 > 시간 확인 join 시간 내의 Tag ID의 Value
    #Batch No. vs Tag ID,  시간 vs Value 값으로 구현 가능하도록 List or dataframe로 반환
    return


def material_list(BatchNO, stardate='',enddate=''):
    #MES Database table에 존재함. 
    #Batch No. 확인 > BOM list 확인 
    #BOM 변화가 있을 경우 seq.로 일단 순서로 합친 후, 사용량이 원료 순서&이름과 같은 곳에 뿌려질 수 있도록 진행
    return

def Wt_result(BatchNO, materialname, stardate='',enddate=''):
   
    return


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