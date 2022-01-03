def make_after_arranging(list): # 짝수 먼저 출력하는 함수
    n = list.pop() # 리스트 맨 마지막 요소를 제거하여 변수 n에 대입
    if n % 2 == 0: #짝수
        after_arranging.insert(0, n) #리스트 맨 앞에 추가
    else: #홀수
        after_arranging.append(n) #리스트 맨 뒤에 추가
    
    if len(list) != 0: #리스트 안에 요소가 있을 경우
        make_after_arranging(list) #재귀함수 호출
    
after_arranging=[] #결과값 리스트 전역 변수
count = int(input("몇개의 숫자를 입력하세겠습니까? >> ")) #몇개의 숫자를 입력할것인지 입력

before_arranging=[] #입력값 리스트 변수
for i in range(count): # 숫자 입력하기
    num = int(input(">>"))
    before_arranging.append(num)

print("Before arranging >> ",before_arranging)
make_after_arranging(before_arranging) # 함수를 이용하여 after_arranging 리스트에 결과 대입
print("After arranging >> ", after_arranging)
