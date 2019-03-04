import sys
import PyQt5
#from PyQt5 import sip
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import json
import requests
import fastText as ft
import pandas as pd
import requests
from konlpy.tag import Twitter

from pandas import Series

model = ft.load_model('model.txt')


data0 = Series(['벚꽃','축하','추카','화이팅','파이팅','화팅','할 수 있','사랑','감사','봄봄봄','좋아해','꽃','고마워','따듯','따뜻','예쁘','분홍','조아','쪼아','핑크','봄이'])
data0.name = u'\U0001F338'
data1 = Series(['노래','콘서트','음악','즐거','응원','룰루','생일 축하','생일 추카','라이브','공연','노래','강남스톼일','강남스타일','목소리'])
data1.name = u'\U0001F3B5'
data2 = Series(['flight','비행기','출국','비행','입국','슝슝','뱅기','배송','다녀와','공항','airport','Airport','떠나','여행'])
data2.name = u'\U00002708'
data3 = Series(['ㅠㅠ','ㅜㅜ','흑흑','눈물','미안','죄송','감기','더위','땀땀','삐질','주륵','주르륵','룸곡','흙흙','또르르','ㄸㄹㄹ','또릅'])
data3.name = u'\U0001F4A6'
data4 = Series(['클로버','굿모닝', '굳모닝','행복', '즐거', '파이팅', '행운', '행복', '힘내', '희망', '새해', 'nice', '잘 어울', '건강', '생일 축하','생일 추카','다녀와','응원','굿럭','굳럭','luck'])
data4.name = u'\U0001F340'
data5 = Series(['리본','축하','선물','이벤트','추카해','사랑해','생일','분홍','핑크','예쁘','쭈카해','ribbon'])
data5.name = u'\U0001F390'
data6 = Series(['달빛','새벽','잘자','night','굳나잇','굿나잇','굿나이트','Night','주무세요','꾸세요','dream','굿밤','둥근달','굳밤','자야지','새벽','자요','쉬세요','꿈에서','달님','좋은 밤','좋은 꿈','안녕히 주무','꿈꾸세요'])
data6.name = u'\U0001F319'
data7 = Series(['해바라기','꽃','봄봄봄','노랑','노란','짝사랑','봄이'])
data7.name = u'\U0001F33B'
data8 = Series(['초록','여름','행복','새롭게','자연','nature','싱그럽','싱그러'])
data8.name = u'\U0001F33F'
data9 = Series(['농구','운동','스포츠','체육'])
data9.name = u'\U0001F3C0'
data10 = Series(['달려','바람','도망','총총'])
data10.name = u'\U0001F4A8'
data11 = Series(['총공','컴백','투표','급구','삐뽀삐뽀','주의','위험','경고','비상'])
data11.name = u'\U0001F6A8'
data12 = Series(['방송','본방사수','촬영','드라마','JTBC','출연','채널','티비','MBC','SBS','KBS2','tvN','KBS','예고','첫방','TV','시청','생중계','중계'])
data12.name = u'\U0001F4FA'
data13 = Series(['크리스마스','Christmas','겨울','첫눈','snow','눈사람','눈길','클스마스'])
data13.name = u'\U000026CA'
data14 = Series(['풋풋','새싹','봄에는','봄이','씨앗','풀잎','봄봄봄'])
data14.name = u'\U0001F331'
data15 = Series(['노래','음악','음표','라이브','멜로디','즐거','신나','콘서트','목소리','공연','떠나','여행'])
data15.name = u'\U0001F3B6'
data16 = Series(['Morning','굿모닝','morning','햇살','모닝','굳모닝','더워','좋은 아침','태양','sun','따듯','따뜻'])
data16.name = u'\U00002600'
data17 = Series(['최고','쵝오','멋진','왕자','공주','대단','왕관','크라운','우승','일등'])
data17.name = u'\U0001F451'
data18 = Series(['화이팅','파이팅','화팅','응원','힘내','파팅','홧팅','팟팅','아자아자','주먹','부셔','뿌셔','맞짱','할 수 있','힘힘'])
data18.name = u'\U0000270A'
data19 = Series(['콘서트','노래','라이브','마이크','노래방','목소리','LIVE','무대','공연','음악','녹음','가수'])
data19.name = u'\U0001F3A4'
data20 = Series(['겨울','크리스마스','Christmas','동결','눈송이','추워','snow','춥다','눈이','첫눈','멜크','얼음'])
data20.name = u'\U00002744'
data21 = Series(['꽃','봄이','튤립','고마워','빨간','빨강'])
data21.name = u'\U0001F337'
data22 = Series(['비가','우산','Rain','rain','빗소리','소나기','태풍','비 온다','비 입니다','비 옵니다','장마','비오는','비가 온다','천둥','비가 와','비와','비 와','장마','비 온다','비온다'])
data22.name = u'\U00002614'
data23 = Series(['투표','여러분','공지','안내','홍보'])
data23.name = u'\U0001F4E2'
data24 = Series(['딸기','베리','과일','딸바','스트로베리'])
data24.name = u'\U0001F353'
data25 = Series(['바나나','서디페','과일','바나나우유','빠나나','딸바','banana','버내나'])
data25.name = u'\U0001F34C'
data26 = Series(['드라이브','운전','부릉','붕붕','자동차','주행','시동','뛰뛰','달려','이동 중','출장','가는 길','빵빵'])
data26.name = u'\U0001F697'
data27 = Series(['담배','금연','흡연','현타','식후땡','담타'])
data27.name = u'\U0001F6AC'
data28 = Series(['크리스마스','업데이트','Christmas','멜크','천주교','성당','공지','띵동','종소리'])
data28.name = u'\U0001F514'
data29 = Series(['달달','허니','뚝뚝','꿀잼','꾸르잼','허니잼','허늬잼','꿀이','꿀잠','달콤','꿀떨어','꿀 떨어','개꿀','꿀벌'])
data29.name = u'\U0001F36F'
data30 = Series(['노래','피아노','건반'])
data30.name = u'\U0001F3B9'
data31 = Series(['경찰','철컹','삐용삐용','삐뽀','삐뽀삐뽀','잡으러','삐용','비상','경찰차','짭새'])
data31.name = u'\U0001F693'
data32 = Series(['풍악을','풍악','색소폰','악기'])
data32.name = u'\U0001F3B7'
data33 = Series(['교회','하나님','아멘','기도','하느님','예수'])
data33.name = u'\U000026EA'
data34 = Series(['배고파','배곱','배고프','라면','식사','음식','떡국','냠냠','요리','맛점','김치','우동','찌개','국수'])
data34.name = u'\U0001F372'
data35 = Series(['바이올린','헨리','악기'])
data35.name = u'\U0001F33B'
data36 = Series(['크리스마스','Christmas','메리크리스마스','christmas','트리','산타','christmas','성탄','성탄절','클스마스','멜크'])
data36.name = u'\U0001F384'
data37 = Series(['노래','멜로디','음악'])
data37.name = u'\U0001F3BC'
data38 = Series(['쪽쪽','입술','뽀뽀','사랑해','립스틱','입술이','입술','섹시','메이크업','키스','뽑뽀','립밤','틴트','입쯀'])
data38.name = u'\U0001F444'
data39 = Series(['와인','치얼스','칵테일','맥주','파티','치얼쓰','와인잔','포도주','축배'])
data39.name = u'\U0001F377'
data40 = Series(['체리','과일','앵두'])
data40.name = u'\U0001F352'
data41 = Series(['비타민','건강','힐링','감기','병원','영양제','아프지마','치료','약을','알약','만병통치','치유','쾌유','영양제','아푸지마'])
data41.name = u'\U0001F48A'
data42 = Series(['머니','통장','용돈','입금','월급','현금','돈을','탕진잼','세뱃돈','로또','부자','돈다발','달러','환전','탕진'])
data42.name = u'\U0001F4B5'
data43 = Series(['오렌지','낑깡','비타민','자몽','상큼한','감귤','상큼','한라봉','귤이','제주도'])
data43.name = u'\U0001F34A'
data44 = Series(['삐뽀','삐용','구급차','앰뷸런스','응급실','병원'])
data44.name = u'\U0001F691'
data45 = Series(['고구마','답답이','다이어트'])
data45.name = u'\U0001F360'
data46 = Series(['녹차','커피','밀크티','라떼','홍차','카페','아메리카노','말차','음료','그린티','커퓌'])
data46.name = u'\U0001F375'
data47 = Series(['촬영','카메라','찰칵','프리뷰','포토타임','셀카','사진','찍사'])
data47.name = u'\U0001F4F7'
data48 = Series(['할로윈','유령','영혼','귀신'])
data48.name = u'\U0001F47B'
data49 = Series(['꽃다발','생일 축하','결혼','부케','꽃','결혼 축하','신부'])
data49.name = u'\U0001F490'
data50 = Series(['문의','예약','전화','연락'])
data50.name = u'\U0000260E'
data51 = Series(['편지','러브레터','쪽지','디엠'])
data51.name = u'\U0001F48C'
data52 = Series(['취향 저격','탕탕','빵야','총 쏴','자살','저격','총알','죽자','죽을래','취저','죽고 싶','죽음','쥬금','주금','죽는다','총 맞'])
data52.name = u'\U0001F52B'
data53 = Series(['월드컵','축구','손흥민','스포츠','이승우','FIFA','피파','K리그','EPL','챔스','엘클라시코','축구공'])
data53.name = u'\U000026BD'
data54 = Series(['야자수','코코밥','하와이','여름','코밥이','제주도','오키나와','알로하','코밥','정글','제주'])
data54.name = u'\U0001F334'
data55 = Series(['인기상','챔피언','빌보드','트로피','최고의','베스트','1위','win','수상','신인상','본상','대상','크라운','어워즈','어워드','시상식','우승','상 받았','수상 소감','수상소감','2관왕','3관왕','4관왕','트리플'])
data55.name = u'\U0001F3C6'
data56 = Series(['총총','간다','호다닥','달려','후다닥','뛰어','총공','잡으러','달리기','모시러','가즈아','도망','총총'])
data56.name = u'\U0001F3C3'
data57 = Series(['복숭아','피치','과일','과즙','복숭','설리'])
data57.name = u'\U0001F351'
data58 = Series(['크리스마스','산타','Christmas','christmas','메리 크리스마스','클스마스','클쓰마스','멜크'])
data58.name = u'\U0001F385'
data59 = Series(['도서관','독서','공부','서점','잡지','소설','신청서','성경','시험','셤'])
data59.name = u'\U0001F4DA'
data60 = Series(['팔레트','그림','캔버스','물감','Palette','화가','팬아트','수채화','채색','알록','일러스트','Art','스케치','미술','고흐','예술','아트','색칠'])
data60.name = u'\U0001F3A8'
data61 = Series(['초밥','스시','음식','일식','맛있','배고','배곱','먹고 싶'])
data61.name = u'\U0001F363'
data62 = Series(['달력','캘린더','날짜','기간','며칠','몇 일'])
data62.name = u'\U0001F4C6'
data63 = Series(['호비','다그닥','말타','승마'])
data63.name = u'\U0001F345'
data64 = Series(['음식','식사','배고파','냠냠','코코밥','햇반','집밥','챙겨 먹','밥 먹','든든하게','쌀밥','쌀 밥','밥을','저녁밥','아침밥','밥도','밥길','챙겨 드세','맛점','맛저','밥힘','마싯','맛나','밥 있','밥솥'])
data64.name = u'\U0001F35A'
data65 = Series(['악어','뱀뱀','공룡'])
data65.name = u'\U0001F40A'
data66 = Series(['포도','과일','보라','청포도','상큼'])
data66.name = u'\U0001F347'
data67 = Series(['코끼리','동물','태국'])
data67.name = u'\U0001F418'
data68 = Series(['라면','음식','짬뽕','배고파','배가 고프','배고프','식사','냉면','우동','먹고 싶','라멘','국수'])
data68.name = u'\U0001F35C'
data69 = Series(['바지','패션','청바지','데님','화보','캘빈클라인','옷'])
data69.name = u'\U0001F456'
data70 = Series(['드라이브','자동차','운전','부릉','빨리','출발','여행','다녀오겠습','고고','가는 길','빵빵'])
data70.name = u'\U0001F699'
data71 = Series(['벌레','무당벌레'])
data71.name = u'\U0001F41E'
data72 = Series(['출근','퇴근','버스','부릉','탑승','교통','출발','붕붕','bus','여행','도착','wheels','운행','빨리'])
data72.name = u'\U0001F68C'
data73 = Series(['자전거','운동','페달','달려','따릉이'])
data73.name = u'\U0001F6B4'
data74 = Series(['우산','비가','비 오네','비 와','날씨','비 온다','비 오','이슬비','소나기','장마'])
data74.name = u'\U0001F302'
data75 = Series(['김밥','주먹밥','배고파','배곱','배고프','삼각김밥','음식','맛있','드세','오니기리','밥먹','밥 먹'])
data75.name = u'\U0001F359'
data76 = Series(['헬기','헬리콥터','헬리'])
data76.name = u'\U0001F681'
data77 = Series(['케이블카'])
data77.name = u'\U0001F6A0'
data78 = Series(['촛불','뜨거','덥다','화끈','열기','응원','더워','후끈','불금','퐈이아','퐈이야','파이팅','힘내','빠이야','불타','열심','불 타'])
data78.name = u'\U0001F525'
data79 = Series(['열심','축하','짝짝짝','박수','응원','성원','쵝오','최고','대박','파이팅','좋아','생일','기대','우왕','우와','감사','힘내','잘했'])
data79.name = u'\U0001F44F'
data80 = Series(['잘자','앗뇽','안녕','악수','Bye','주무세','바이','인사','빠이','출국','잘 다녀','안뇽','빠빠','악수','반가워','고마워','방가','하이','수고했','만나','오랜만','굿모닝','굳모닝','쫀아침'])
data80.name = u'\U0001F44B'
data81 = Series( ['노래','파이팅','축하','재밌','댄스','춤','신나','즐거','행복','감사','클럽','땐스'])
data81.name = u'\U0001F483'
data82 = Series(['응가','똥','구리다','구리네','개구려'])
data82.name = u'\U0001F4A9'
data83 = Series(['샤이니','다이아','캐럿','빛나','다이아몬드','반짝'])
data83.name = u'\U0001F48E'
data84 = Series(['산책','도보순례','걸어','동행','가고 있','도보 순례','걷고'])
data84.name = u'\U0001F6B6'
data85 = Series( ['break','커피','Coffee','티타임','티 타임','카페','커퓌','커픠','라떼','아메리카노','음료'])
data85.name = u'\U00002615'
data86 = Series( ['통장','용돈','머니','입금','만원'])
data86.name = u'\U0001F4B8'
data87 = Series(['반지','사랑','결혼','기념일','겨론','보석','커플링','선물','악세사리'])
data87.name = u'\U0001F48D'
data88 = Series(['도넛','도우넛','당충전','당 충전','던킨','디저트','간식','서디페','달달','달콤'])
data88.name = u'\U0001F369'
data89 = Series(['식사','포크','음식','냠냠','맛있','배고파','배고 프','요리','밥 먹','밥먹','치킨','고기','먹겠','잘 먹','맛점','밥먹','레스토랑'])
data89.name = u'\U0001F374'
data90 = Series(['주사','보톡스','필러','병원','건강','독감','감기','아프','아파','콜록','의사','성형'])
data90.name = u'\U0001F489'
data91 = Series( ['눈물','비가','이슬','비오','비 와','비 온'])
data91.name = u'\U0001F4A7'
data92 = Series( ['알람','타임','몇시','모닝콜','굿모닝','굳모닝','시계','시간','임박','종료','몇 시'])
data92.name = u'\U000023F0'
data93 = Series(['초코','초콜렛','초콜릿','쪼꼬','서디페','쪼코','달달','달다','발렌타인','쵸코','누텔라','Choco','choco','Chocolat','군것질','간식'])
data93.name = u'\U0001F36B'
data94 = Series(['졸업','수료','축하','학사모','쫄업','대학','졸사'])
data94.name = u'\U0001F393'
data95 = Series(['신발','운동화','스니커즈'])
data95.name = u'\U0001F45F'
data96 = Series(['아이스크림','빙수','디저트','설빙','파르페','배스킨','베스킨','아스크림','간식','후식','카페','군것질'])
data96.name = u'\U0001F368'
data97 = Series(['파스타','스파게티','파슽하','음식','식사','레스토랑'])
data97.name = u'\U0001F35D'
data98= Series(['에코백','가방','핸드백'])
data98.name = u'\U0001F45C'
data99 = Series(['안경','선글라스'])
data99.name = u'\U0001F453'
data100 = Series(['파인애플','과일','파인에플','상콤','상큼'])
data100.name = u'\U0001F34D'
data101 = Series(['빌라','건물'])
data101.name = u'\U0001F3E1'
data102 = Series(['수박','서디페','화채','과일','여름','빨간맛','빨간 맛'])
data102.name = u'\U0001F349'
data103 = Series(['구두','신데렐라','쇼핑','신발','잇템','공주','곤쥬','곤듀'])
data103.name = u'\U0001F460'
data104 = Series(['오빠 차','오빠차','간다','간닷','간드아','가즈아','드라이브','부릉부릉','자동차','출바알','출발','교통','퇴근','출근','운전','발송','택배','빵빵','고속도로','귀경길','귀성길'])
data104.name = u'\U0001F698'
data105 = Series(['애기','우유','귀여워','아가','아기','젖병','응애'])
data105.name = u'\U0001F37C'
data106 = Series(['벌레','애벌레','꿈틀','지네','징그'])
data106.name = u'\U0001F41B'
data107 = Series( ['고양이','냥이','야옹','cat','동물','집사'])
data107.name = u'\U0001F408'
data108 = Series(['병아리','귀여워','삐약','노랑','노란','귀엽','기욥','짹짹','동물'])
data108.name = u'\U0001F423'
data109 = Series(['병아리','귀여워','삐약','노랑','노란','귀엽','기욥','짹짹','동물'] )
data109.name = u'\U0001F424'
data110 = Series( ['닭','치킨','박근혜','동물','꼬꼬','박그네','후다닥','동물','치맥'])
data110.name = u'\U0001F413'
data111 = Series(['강아지','푸들','귀여워','간장 치킨','간장치킨','동물','댕댕이','멍멍이'])
data111.name = u'\U0001F429'
data112 = Series(['목욕','욕조','샤워','반신욕','굿밤','굳밤','씻고','씻자','씻을','여유','씻기'])
data112.name = u'\U0001F6C0'
data113 = Series(['보드','운동','레포츠','레저','레져','액티비티','스포츠','스키','스노우보드'])
data113.name = u'\U0001F3C2'
data114 = Series(['낙타','동물','사하라','사막'])
data114.name = u'\U0001F42B'
data115 = Series(['소방차','긴급','사다리','불이나','소방','불났','불 났','화재','소방관','119'])
data115.name = u'\U0001F692'
data116 = Series(['멜론','스밍','과일','메론','메로나'])
data116.name = u'\U0001F348'
data117 = Series(['고기','소고기','황소','사냥','사냥감','들소','동물'])
data117.name = u'\U0001F402'
data118 = Series( ['버스','교통','출근','퇴근','부릉','출발','여행','간다','간드앗','간드아','출퇴근'])
data118.name = u'\U0001F683'
data119 = Series( ['부릉','농사','트랙터','운전','경운기'] )
data119.name = u'\U0001F69C'
data120 = Series(['공책','필기구','필기도구','공부','노트','책','필기'])
data120.name = u'\U0001F4D2'
data121 = Series(['시계','시간','몇시','몇 시','일어나','기상','지각'])
data121.name = u'\U0001F564'
data122 = Series(['열심','화이팅','파이팅','화팅','파팅','아자','응원','힘내','야호','얏호','아싸','신나'])
data122.name = u'\U0001F64C'
data123 = Series(['해골','조심','주의','괴물','못생','무한도전','무한 도전'])
data123.name = u'\U0001F480'
data124 = Series(['축하','고마워','행복','사랑','예쁜','향기','꽃','봄봄봄','봄이','예쁘','추카','감사'])
data124.name = u'\U0001F33A'
data125 = Series(['군밤','맛밤','밤송이','크러쉬밤','밤밤이','가을'])
data125.name = u'\U0001F330'
data126 = Series(['공주님','공주','예뻐','예쁘다','왕자','퀸카','여왕','곤쥬','공쥬','여신'])
data126.name = u'\U0001F478'
data127 = Series(['칼','찔러','칼답','찔러','죽어','죽여','살인','협박','범죄','죽는'])
data127.name = u'\U0001F52A'
data128 = Series(['싹둑','가위','컷','미용실','묭실','머리 자르','미장원'])
data128.name = u'\U00002702'
data129 = Series(['할로윈','호박','Halloween','핼로윈'])
data129.name = u'\U0001F383'
data130 = Series(['애기','baby','베베','응애','베이비','아가','어린이','어리니','신생아','아기'])
data130.name = u'\U0001F476'
data131 = Series(['케이크','birthday','생일 축하','카페','간식','케이꾸','케이키','디저트','추카','달달','서디페','케익','달콤','생축'])
data131.name = u'\U0001F370'
data132 = Series(['공부','연필','샤프','펜'])
data132.name = u'\U0000270F'
data133 = Series(['열쇠','KEY','key','Key'])
data133.name = u'\U0001F511'
data134 = Series(['오렌지','과일','상큼','자몽','tangerine','오렌쥐','귤','주황','상콤','제주'])
data134.name = u'\U0001F34A'
data135 = Series(['가족','엄마','아빠','화목','사랑','엄빠','가정'])
data135.name = u'\U0001F46A'
data136 = Series(['원피스','쇼핑','드레스','사복','패션','예쁘','옷','shopping','공주'])
data136.name = u'\U0001F457'
data137 = Series(['나무','초록','산책','산','숲'])
data137.name = u'\U0001F333'
data138 = Series(['냄새','킁킁','nose','눈코입','이목구비','오똑'])
data138.name = u'\U0001F443'
data139 = Series(['고기','소고기','동물','우유','한우','횡성'])
data139.name = u'\U0001F42E'
data140 = Series(['고래','뿌우','바다','아쿠아리움'])
data140.name = u'\U0001F40B'
data141 = Series(['병원','구급차','덕통사고','사고','덕통','삐뽀','삐뽀삐뽀','119','삐용','응급','앰뷸런스'])
data141.name = u'\U0001F691'
data142 = Series(['꿀벌','블락비','몬스타엑스','웽웽','벌들','말벌','벌침','벌레'])
data142.name = u'\U0001F41D'
data143 = Series(['쇼핑','지갑','선물','루이까또즈','가방'])
data143.name = u'\U0001F45B'
data144 = Series(['기차','지하철','ktx','KTX','쟈철','전철','1호선','2호선','3호선','4호선','5호선','6호선','7호선','8호선','9호선','분당선','코레일'])
data144.name = u'\U0001F688'
data145 = Series(['번쩍','블링','멋진','멋지','간지','간g','간G','스웩','수웩','swag','반짝','빛나','빛난','간쥐'])
data145.name = u'\U00002728'
data146 = Series(['열심','맞짱','화이팅','파이팅','홧팅','빠샤','힘내','응원','주먹','부셔','뿌셔','아자'])
data146.name = u'\U0001F44A'
data147 = Series(['메롱','헥헥','혓바닥','까꿍'])
data147.name = u'\U0001F445'
data148 = Series(['Birthday','birthday','축하','생일','생일 축하','이벤트','추카','선물','기념','포장'])
data148.name = u'\U0001F381'
data149 = Series(['가을','낙엽','계절','단풍','쓸쓸','우울','외롭'])
data149.name = u'\U0001F342'
data150 = Series(['영상','촬영','직캠','비디오','캠코더'])
data150.name = u'\U0001F4F9'
data151 = Series(['선인장','초록','사막','오아시스'])
data151.name = u'\U0001F335'
data152 = Series(['팬더','귀여','귀엽','다크서클','판다','동물'])
data152.name = u'\U0001F43C'
data153 = Series(['칵테일','음료','휴가','맛술'])
data153.name = u'\U0001F379'
data154 = Series( ['호랑이','어흥','동물','으르렁','호랑','호랭이','포돌이','맹수','표범'])
data154.name = u'\U0001F42F'
data155 = Series(['컴퓨터','컴터','노트북','놋북','데스크탑','컴공','콤퓨터'])
data155.name = u'\U0001F4BB'
data156 = Series( ['고래','바다','물고기','아쿠아리움','수영','뿌우'])
data156.name = u'\U0001F433'
data157 = Series( ['사과','과일','애플','apple','상큼'])
data157.name = u'\U0001F34E'
data158 = Series(['비키니','수영복','여름','수영','베럴','휴가','다이어트','섹시','sexy','핫','hot'])
data158.name = u'\U0001F459'
data159 = Series(['빙수','아이스크림','팥빙수','후식','설빙','아스크림','디저트'])
data159.name = u'\U0001F367'
data160 = Series(['탐정','범인','돋보기','관찰','실험','셜록'])
data160.name = u'\U0001F50D'
data161 = Series(['할아버지','꽃할배','할배','할아부지','어르신','할아범'])
data161.name = u'\U0001F474'
data162 = Series(['드래곤'])
data162.name = u'\U0001F409'
data163 = Series(['동물','양치기','양아치','양띠'])
data163.name = u'\U0001F411'
data164 = Series(['문어','타코야끼','오징어','낙지','타코야키','쭈꾸미','해산물'])
data164.name = u'\U0001F419'
data165 = Series(['앨범','씨디','CD','dvd','DVD','디비디','음반'])
data165.name = u'\U0001F4C0'
data166 = Series(['푸딩','디저트','간식','후식','달콤'])
data166.name = u'\U0001F36E'
data167 = Series(['모자'])
data167.name = u'\U0001F452'
data168 = Series(['동물'])
data168.name = u'\U0001F40F'
data169 = Series(['유카타','기모노','일본','오사카'])
data169.name = u'\U0001F458'
data170 = Series(['음식','배고파','이자카야','오뎅','꼬치'])
data170.name = u'\U0001F362'
data171 = Series(['편지','메일','우편','우체통','우체국'])
data171.name = u'\U0001F4EC'
data172 = Series(['막걸리','소주','사케','막걸리','모듬전'])
data172.name = u'\U0001F376'
data173 = Series(['기차'])
data173.name = u'\U0001F686'
data174 = Series(['똑똑','열어','열어봐','들어가','문열어','문 열어','나가','방탈출','출구','탈주','탈동'])
data174.name = u'\U0001F6AA'
data175 = Series(['피자','음식','핏짜','피맥','피짜','피쟈','핏자','PIZZA','pizza'])
data175.name = u'\U0001F355'
data176 = Series(['축하','장미','꽃','발렌타인','Valentine','추카','기념'])
data176.name = u'\U0001F339'
data177 = Series(['생일','축하','생일 축하','생축','생추크','벌쓰데이','Birthday','birthday','추카','케이크','케익','BIRTHDAY'])
data177.name = u'\U0001F382'
data178 = Series(['가을','단풍','메이플','낙엽'])
data178.name = u'\U0001F341'
data179 = Series( ['시구','두산','야구','응원','한국시리즈'])
data179.name = u'\U000026BE'
data180 = Series(['치킨','꼬꼬','닭발','삼계탕','초복','닭갈비','꼬끼오','불닭','닭가슴살','닭'])
data180.name = u'\U0001F414'
data181 = Series(['치킨','치맥','닭다리','바삭바삭','야식','양념','후라이드','황금올리브','멕시카나','치느님','뿌링클'])
data181.name = u'\U0001F357'
data182 = Series(['아이스크림','디저트','아스크림','베스킨','배스킨','후식','달달'])
data182.name = u'\U0001F366'
data183 = Series(['새우','새우튀김','에비','쉬림프'])
data183.name = u'\U0001F364'
data184 = Series(['롤러코스터','놀이공원','롯데월드','에버랜드'])
data184.name = u'\U0001F3A2'
data185 = Series(['테니스','스포츠'])
data185.name = u'\U0001F3BE'
data186 = Series(['학교','학생','공부','과제','시험'])
data186.name = u'\U0001F3EB'
data187 = Series(['안전'])
data187.name = u'\U0001F3ED'
data188 = Series(['넥타이','셔츠'])
data188.name = u'\U0001F454'
data189 = Series(['디엠','메일','DM','문의','뎀','쪽지','편지'])
data189.name = u'\U0001F4E8'
data190 = Series(['촬영','직캠','카메라','캠코더','감독','비디오'])
data190.name = u'\U0001F3A5'
data191 = Series(['기차','탑승'])
data191.name = u'\U0001F684'
data192 = Series(['뱀뱀','뱀','스네이크'])
data192.name = u'\U0001F40D'
data193 = Series(['나무','크리스마스','소나무','초록','자연'])
data193.name = u'\U0001F332'
data194 = Series(['옥수수','콘치즈','옥슈슈','콘칩','콘 치즈'])
data194.name = u'\U0001F33D'
data195 = Series(['식빵','토스트','샌드위치','빵집','빵떡','빠아앙','빵순이','파리바게트','파바','파리바게뜨','빵 먹','빵먹'])
data195.name = u'\U0001F35E'
data196 = Series(['감자','감튀','감자 튀김','감자튀김','롯데리아','맥도날드','맥날','맘스터치','프렌치프라이','패스트푸드'])
data196.name = u'\U0001F35F'
data197 = Series(['사탕','화이트데이','캔디','군것질'])
data197.name = u'\U0001F36D'
data198 = Series(['수영장','swim','수영'])
data198.name = u'\U0001F3CA'


dataa = Series([data0,data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30,data31,data32,data33,data34,data35,data36,data37,data38,data39,data40,data41,data42,data43,data44,data45,data46,data47,data48,data49,data50,data51,data52,data53,data54,data55,data56,data57,data58,data59,data60,data61,data62,data63,data64,data65,data66,data67,data68,data69,data70,data71,data72,data73,data74,data75,data76,data77,data78,data79,data80,data81,data82,data83,data84,data85,data86,data87,data88,data89,data90,data91,data92,data93,data94,data95,data96,data97,data98,data99,data100,data101,data102,data103,data104,data105,data106,data107,data108,data109,data110,data111,data112,data113,data114,data115,data116,data117,data118,data119,data120,data121,data122,data123,data124,data125,data126,data127,data128,data129,data130,data131,data132,data133,data134,data135,data136,data137,data138,data139,data140,data141,data142,data143,data144,data145,data146,data147,data148,data149,data150,data151,data152,data153,data154,data155,data156,data157,data158,data159,data160,data161,data162,data163,data164,data165,data166,data167,data168,data169,data170,data171,data172,data173,data174,data175,data176,data177,data178,data179,data180,data181,data182,data183,data184,data185,data186,data187,data188,data189,data190,data191,data192,data193,data194,data195,data196,data197,data198])



CalUI = 'Emoji.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)
        self.progressBar.setValue(0)
        self.setFixedSize(1920,1080)
        self.sample_line1.setStyleSheet("QPushButton {border:none}")
        self.sample_line2.setStyleSheet("QPushButton {border:none}")
        self.sample_line3.setStyleSheet("QPushButton {border:none}")
        self.sample_line4.setStyleSheet("QPushButton {border:none}")
        self.sample_line5.setStyleSheet("QPushButton {border:none}")


        self.pushButton.clicked.connect(self.send) ## 버튼을 눌렀을때 괄호안에 들어간 함수 실행
        self.pushButton.clicked.connect(self.send2)
        self.pushButton.clicked.connect(self.send3)
        self.pushButton.clicked.connect(self.correction)

        self.sample_line1.clicked.connect(self.exampleShow1)
        self.sample_line2.clicked.connect(self.exampleShow2)
        self.sample_line3.clicked.connect(self.exampleShow3)
        self.sample_line4.clicked.connect(self.exampleShow4)
        self.sample_line5.clicked.connect(self.exampleShow5)

        self.btn_reset.clicked.connect(self.btn_rechange)


    def send(self):
        f = self.lineEdit.font()
        f.setPointSize(17)
        self.lineEdit.setFont(f)
        exist_line_text = self.lineEdit.text()
        #네이버 맞춤법 검사기
        url2='https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy?_callback=mycallback&q=' + exist_line_text + '&where=nexearch&color_blindness=0&_=1544439622507'

        response=[]
        a = requests.get(url2).text
        response.append(a)


        t = pd.DataFrame({"url" : response})
        json_string = t.url.map(lambda x : x.replace('mycallback(','').replace(');',''))
        json_string = pd.DataFrame({"json": json_string})
        json_string = json_string.json[json_string.json.str.contains('DOCTYPE')==False].reset_index().drop(['index'],axis=1)
        result = json_string.json.map(lambda x : json.loads(x))
        ss = []
        for i in range(len(result)):
           a = result[i]['message']['result']['notag_html']
           ss.append(a)

        ss=str(ss)[2:len(str(ss))-2]
        
        emojilist = []
        for i in range(len(dataa)):
            a = 0
            for k in range(len(dataa[i])):
                if dataa[i][k] in ss:
                    a += 1
            if a > 0:
                emojilist.append(dataa[i].name)

        stremoji1 = ''.join(emojilist)
        self.text_output.setText(stremoji1)

    def send2(self):
        exist_line_text = self.lineEdit.text()
        #네이버 맞춤법 검사기
        url2='https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy?_callback=mycallback&q=' + exist_line_text + '&where=nexearch&color_blindness=0&_=1544439622507'

        response=[]
        a = requests.get(url2).text
        response.append(a)


        t = pd.DataFrame({"url" : response})
        json_string = t.url.map(lambda x : x.replace('mycallback(','').replace(');',''))
        json_string = pd.DataFrame({"json": json_string})
        json_string = json_string.json[json_string.json.str.contains('DOCTYPE')==False].reset_index().drop(['index'],axis=1)
        result = json_string.json.map(lambda x : json.loads(x))
        ss = []
        for i in range(len(result)):
           a = result[i]['message']['result']['notag_html']
           ss.append(a)

        #ss=str(ss)
        conclu = model.predict(ss,5)
        a=[]
        for i in range(len(conclu[0])):
            if conclu[0][i] == '__label__1':
                a.append(u'\U0001F44D')
            elif conclu[0][i] == '__label__13' :
                a.append(u'\U0001F622')
            elif conclu[0][i] == '__label__0':
                a.append(u'\U0001F44C')
            elif conclu[0][i] == '__label__2':
                a.append(u'\U0001F601')
            elif conclu[0][i] == '__label__3':
                a.append(u'\U0001F602')
            elif conclu[0][i] == '__label__4':
                a.append(u'\U0001F608')
            elif conclu[0][i] == '__label__5':
                a.append(u'\U0001F60A')
            elif conclu[0][i] == '__label__6':
                a.append(u'\U0001F60D')
            elif conclu[0][i] == '__label__7':
                a.append(u'\U0001F60F')
            elif conclu[0][i] == '__label__8':
                a.append(u'\U0001F612')
            elif conclu[0][i] == '__label__9':
                a.append(u'\U0001F614')
            elif conclu[0][i] == '__label__10':
                a.append(u'\U0001F615')
            elif conclu[0][i] == '__label__11':
                a.append(u'\U0001F618')
            elif conclu[0][i] == '__label__12':
                a.append(u'\U0001F621')
            elif conclu[0][i] == '__label__14':
                a.append(u'\U0001F629')
            elif conclu[0][i] == '__label__15':
                a.append(u'\U0001F62D')
            elif conclu[0][i] == '__label__16':
                a.append(u'\U0001F633')
            elif conclu[0][i] == '__label__17':
                a.append(u'\U0001F635')
            elif conclu[0][i] == '__label__18':
                a.append(u'\U0001F637')
            else :
                a.append(u'\U0001F64F')

        print(a)
        self.sentiment_output.setText(",".join(a))


        smValue=conclu[1][0]*100
        self.progressBar.setValue(smValue)

        COMPLETED_STYLE1 = """
        QProgressBar{
              text-align : center
        }

        QProgressBar::chunk {
               background-color: red;
         }
         """
        COMPLETED_STYLE2 = """
        QProgressBar{
              text-align : center
        }

        QProgressBar::chunk {
               background-color: yellow;
         }
         """
        COMPLETED_STYLE3 = """
        QProgressBar{
              text-align : center
        }

        QProgressBar::chunk {
               background-color: green;
         }
         """
        COMPLETED_STYLE4 = """
        QProgressBar{
              text-align : center
        }

        QProgressBar::chunk {
               background-color: blue;
         }
         """

        if smValue <=25:
             self.setStyleSheet(COMPLETED_STYLE1)
        elif smValue <=50:
             self.setStyleSheet(COMPLETED_STYLE2)
        elif smValue <=75:
             self.setStyleSheet(COMPLETED_STYLE3)
        else :
             self.setStyleSheet(COMPLETED_STYLE4)



    def send3(self):
        exist_line_text = self.lineEdit.text()
        #네이버 맞춤법 검사기
        url2='https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy?_callback=mycallback&q=' + exist_line_text + '&where=nexearch&color_blindness=0&_=1544439622507'

        response=[]
        a = requests.get(url2).text
        response.append(a)


        t = pd.DataFrame({"url" : response})
        json_string = t.url.map(lambda x : x.replace('mycallback(','').replace(');',''))
        json_string = pd.DataFrame({"json": json_string})
        json_string = json_string.json[json_string.json.str.contains('DOCTYPE')==False].reset_index().drop(['index'],axis=1)
        result = json_string.json.map(lambda x : json.loads(x))
        ss = []
        for i in range(len(result)):
           a = result[i]['message']['result']['notag_html']
           ss.append(a)

        ss=str(ss)[2:len(str(ss))-2]
        twitter = Twitter()
        token=twitter.pos(ss)

        for i in range(len(token)):
            if i==0:
                self.token1.setText(token[i][0])
            elif i==1:
                self.token2.setText(token[i][0])
            elif i==2:
                self.token3.setText(token[i][0])
            elif i==3:
                self.token4.setText(token[i][0])
            elif i==4:
                self.token5.setText(token[i][0])
            elif i==5:
                self.token6.setText(token[i][0])
            elif i==6:
                self.token7.setText(token[i][0])
            elif i==7:
                self.token8.setText(token[i][0])
            elif i==8:
                self.token9.setText(token[i][0])
            elif i==9:
                self.token10.setText(token[i][0])
            elif i==10:
                self.token11.setText(token[i][0])

    def correction(self):
        exist_line_text = self.lineEdit.text()
        #네이버 맞춤법 검사기
        url2='https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy?_callback=mycallback&q=' + exist_line_text + '&where=nexearch&color_blindness=0&_=1544439622507'

        response=[]
        a = requests.get(url2).text
        response.append(a)


        t = pd.DataFrame({"url" : response})
        json_string = t.url.map(lambda x : x.replace('mycallback(','').replace(');',''))
        json_string = pd.DataFrame({"json": json_string})
        json_string = json_string.json[json_string.json.str.contains('DOCTYPE')==False].reset_index().drop(['index'],axis=1)
        result = json_string.json.map(lambda x : json.loads(x))
        ss = []
        for i in range(len(result)):
           a = result[i]['message']['result']['notag_html']
           ss.append(a)
        ss=str(ss)[2:len(str(ss))-2]
        self.lineEdit.setText(ss)

    def btn_rechange(self):
        self.token1.show()
        self.token2.show()
        self.token3.show()
        self.token4.show()
        self.token5.show()
        self.token6.show()
        self.token7.show()
        self.token8.show()
        self.token9.show()
        self.token10.show()

    def exampleShow1(self):
        word=self.sample_line1.text()
        self.lineEdit.setText(word)
        QtCore.QTimer.singleShot(1000, self.send)
        QtCore.QTimer.singleShot(1000, self.send2)
        QtCore.QTimer.singleShot(1000, self.send3)
        QtCore.QTimer.singleShot(1000, self.correction)

    def exampleShow2(self):
        word=self.sample_line2.text()
        self.lineEdit.setText(word)
        QtCore.QTimer.singleShot(1000, self.send)
        QtCore.QTimer.singleShot(1000, self.send2)
        QtCore.QTimer.singleShot(1000, self.send3)
        QtCore.QTimer.singleShot(1000, self.correction)

    def exampleShow3(self):
        word=self.sample_line3.text()
        self.lineEdit.setText(word)
        QtCore.QTimer.singleShot(1000, self.send)
        QtCore.QTimer.singleShot(1000, self.send2)
        QtCore.QTimer.singleShot(1000, self.send3)
        QtCore.QTimer.singleShot(1000, self.correction)

    def exampleShow4(self):
        word=self.sample_line4.text()
        self.lineEdit.setText(word)
        QtCore.QTimer.singleShot(1000, self.send)
        QtCore.QTimer.singleShot(1000, self.send2)
        QtCore.QTimer.singleShot(1000, self.send3)
        QtCore.QTimer.singleShot(1000, self.correction)

    def exampleShow5(self):
        word=self.sample_line5.text()
        self.lineEdit.setText(word)
        QtCore.QTimer.singleShot(1000, self.send)
        QtCore.QTimer.singleShot(1000, self.send2)
        QtCore.QTimer.singleShot(1000, self.send3)
        QtCore.QTimer.singleShot(1000, self.correction)


app = QApplication(sys.argv)

main_dialog = MainDialog()

main_dialog.show()

app.exec_()


# In[ ]:
