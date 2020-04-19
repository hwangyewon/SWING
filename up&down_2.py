import os.path

def case(num, start, end):   #입력받은 숫자가 범위 내인지 확인하는 함수
    if num>end or num<start :  #범위 밖
        return False
    if num<=end and num>=start: #범위 내
        return True


record=[]  #기록 입력할 리스트
nicks=[]  #닉네입 입력할 리스트

if os.path.isfile("record.txt")==True:  #"record.txt" 파일이 있으면 내용을 읽어옴
    f=open("record.txt", 'r')
    lines=f.readlines()
    for i in range(0, len(lines), 2):  #lines리스트에서 0,2,4... 인덱스에는 숫자 정보가 들어가 있음
        record.append(int(lines[i].rstrip('\n')))   #숫자를 문자열에서 정수로 바꿔주고 오른쪽의 개행문자를 제거함

    for i in range(1, len(lines), 2):  #lines리스트에서 1,3,5... 인덱스에는 닉네임 정보가 들어가 있음
        nicks.append(lines[i].rstrip('\n'))    #닉네임 정보에서 맨끝의 개행문자를 제거함
        
while True :
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    mode=int(input("1. 게임시작 2. 기록확인 3. 게임종료\n>>"))
    

    if mode==1:    #'게임시작' 선택한 경우
        from random import randint
        ans=randint(1,101)   #정답 생성(1~100 범위)
        print(ans)
        start=1   #입력 가능한 시작범위 
        end=100   #입력 가능한 끝범위
        for i in range (1,11):   #입력받은 숫자의 범위 판단과정
            num=int(input("%d번째 숫자 입력(%d~%d) : " %(i, start, end)))
            while case(num, start, end)==False:
                print("범위를 초과하는 수를 입력하셨습니다. 다시 입력해주세요.")
                num=int(input("%d번째 숫자 입력(%d~%d) : " %(i, start, end)))
    
            if case(num, start, end)==True: #입력받은 숫자가 범위 내인경우
                if num<ans :  #입력받은 숫자가 정답보다 작은 경우
                    print("UP")
                    start=num+1  #시작범위를 갱신함

                elif num==ans :  #정답맞춘 경우
                    print("정답입니다!!")
                    print("%d번째만에 맞추셨습니다" %i)
                    
                    if len(record)==0:  #최고기록 여부 확인
                        print("최고기록 갱신~!")
                        nick=input("닉네임을 입력하세요 >> ")
                        record.append(i)
                        nicks.append(nick)
                        break
                    elif record[0]>=i:  #1위 기록보다 맞춘 횟수가 적은지 판단
                        print("최고기록 갱신~!")
                        nick=input("닉네임을 입력하세요 >> ")
                        record.insert(0, i)   #기록 리스트에서 제일 첫번째 위치에 데이터 삽입
                        nicks.insert(0, nick)
                        break
                    else : break
                    
                elif num>ans :   #입력받은 숫자가 정답보다 큰 경우
                    print("DOWN")
                    end=num-1  #끝범위를 갱신함

            
        if num!=ans :   #10번내에 맞추지 못한 경우 출력멘트
            print("입력횟수를 초과하였습니다. 게임오버!")

        
    if mode==2:  #'기록확인' 선택한 경우
        for j in range(0,len(record)):
            print("%d %s %d" %(j+1, nicks[j], record[j]))

    if mode==3:  #'게임종료' 선택한 경우 반복문 나감
        f=open("record.txt", 'w')
        for i in range(0, len(record)):
            f.write(str(record[i])+"\n")
            f.write(nicks[i]+"\n")
        f.close()
        print("UP & DOWN 게임이 종료됩니다.")
        break


