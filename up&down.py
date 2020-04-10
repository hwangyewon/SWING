record=[]  #기록 입력할 리스트

while True :
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    mode=int(input("1. 게임시작 2. 기록확인 3. 게임종료\n>>"))
    

    if mode==1:    #'게임시작' 선택한 경우
        from random import randint
        ans=randint(1,101)   #정답 생성(1~100 범위)
        print(ans)
        start=1   #입력 가능한 시작범위 
        end=100   #입력 가능한 끝범위
        for i in range (1,11):   #입력받은 숫자 판단과정
            num=int(input("%d번째 숫자 입력(%d~%d) : " %(i, start, end)))
            if num<ans :  #입력받은 숫자가 정답보다 작은 경우
                print("UP")
                start=num  #시작범위를 갱신함

            elif num==ans :  #정답맞춘 경우
                record.append(i)   #기록 리스트에 기록이 추가됨
                print("정답입니다!!")
                print("%d번째만에 맞추셨습니다" %i)
                record.sort()   #최고기록 판단하기 위해 기록리스트 오름차순 정렬
                if record[0]==i:  #1위 기록과 맞춘 횟수가 동일한지 판단 
                    print("최고기록 갱신~!")
                break

            elif num>ans :   #입력받은 숫자가 정답보다 큰 경우
                i+=1   
                print("DOWN")
                end=num  #끝범위를 갱신함
        if num!=ans :   #10번내에 맞추지 못한 경우 출력멘트
            print("입력횟수를 초과하였습니다. 게임오버!")
        
    

    if mode==2:  #'기록확인' 선택한 경우
        record.sort()  #오름차순으로 정렬
        for j in range(0,len(record)):
            print("%d %d" %(j+1, record[j]))

    if mode==3:  #'게임종료' 선택한 경우 반복문 나감
        print("UP & DOWN 게임이 종료됩니다.")
        break


