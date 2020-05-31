from bs4 import BeautifulSoup
import urllib.response
import urllib.request
import requests
import os


html = urllib.request.urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=726214&weekday=tue")   #가져올 웹툰 url
result=BeautifulSoup(html.read(), "html.parser")



search=result.find("div", {"class", "detail"})   #웹툰 제목 가져오기
title_a=search.find("h2").get_text()
title_b=search.find("span").get_text()    #작가 이름 들어감
title=title_a.replace(title_b, "")    #웹툰 제목에서 작가부분 없애기 위한 과정
title=title.strip()   #제목 공백 제거
print(title)

os.mkdir(title)   #웹툰 이름으로 폴더 만들기
os.chdir(title)

search=result.findAll("td", {"class", "title"})  #회차 제목 가져오기
epi_list=[]  #회차 이름 리스트
epi_url=[]   #회차 url 리스트

index=0
for e in search:  #회차 이름으로 폴더만들기
    epi_list.append(e.get_text(" ", strip=True))
    epi_url.append(e.find("a").get('href'))  #회차 url 가져옴
    os.mkdir(epi_list[index])
    index+=1


opener=urllib.request.build_opener()   #이미지 다운로드 막히는 거 가능하게 해주는 코드
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

epi=0
for u in epi_url:
    src_list=[] #이미지 태그 src를 저장
    image_list=[] #진짜 이미지 url 저장(썸네일 제외한 웹툰 이미지 링크만 저장하는 리스트)
    html = urllib.request.urlopen("https://comic.naver.com"+u)   #해당 회차 url 가져옴
    result=BeautifulSoup(html.read(), "html.parser")
    search=result.findAll("img")

    for s in search :
        src_list.append(s.get('src'))
    
    for i in range(0, len(src_list), 1) :
        text="image-comic"     #웹툰 이미지 src에는 "image-comic"이 포함되어 있어서 해당 문자열을 포함하는 이미지 주소를 image_list에 넣어줌 
        src_string=str(src_list[i])
        if text in src_string :
            image_list.append(src_list[i])
        index+=1
     
    
    index=1
    for i in image_list :
        path=epi_list[epi]+"/"
        urllib.request.urlretrieve(i, path+str(index)+".jpg")
        index+=1

    epi+=1  





