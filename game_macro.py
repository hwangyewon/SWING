from selenium import webdriver

driver=webdriver.Chrome('C:/Users/yso00/Desktop/설치파일/chromedriver')

driver.get('http://zzzscore.com/1to50/?ts=1591411226743') #접속할 url

btn=driver.find_elements_by_xpath('//*[@id="grid"]/div[@style]')
num=1
while(num<=25):  #1~25
    for i in btn :
        if(i.text==str(num)):
            i.click()
            num+=1
      
                
btn=driver.find_elements_by_xpath('//*[@id="grid"]/div[@style]')
while(num<=50):    #25~50
    for i in btn :
        if(i.text==str(num)):
            i.click()
            num+=1
                
