from bs4 import BeautifulSoup

import urllib.request

html = urllib.request.urlopen("http://www.swu.ac.kr/www/swuniversity.html")
result=BeautifulSoup(html.read(), "html.parser")

search=result.findAll("a")

print("*** 서울여자대학교 학과 및 홈페이지 정보 ***\n")
print("학과\t\t\t\t 홈페이지")
  
index=0  
for s in search:  
    if "대학원" in s.text or "교육원" in s.text or "자율전공학부" == s.text or "공동기기실" == s.text:   #자율전공학부, 바롬인성교육원, 기초교육원, 대학원 제외하기 위한 조건
        continue
    else :
        link=s['href']
        f_link="http://www.swu.ac.kr"+link   #학과 선택시 나오는 페이지 링크
        m_html = urllib.request.urlopen(f_link)
        m_result=BeautifulSoup(m_html.read(), "html.parser")
        m=m_result.find("a", {"class", "btn btn_xl btn_blue_gray"})
        if m is None or m['href']=="bacha_28.html" or m['href']== "/www/bacha_28.html":  #홈페이지가 존재하지 않는 경우
            print(s.text+"\t\t\t홈페이지가 존재하지 않음")
        else :
            print(s.text+"\t\t\t"+m['href'])
        
        


        



    