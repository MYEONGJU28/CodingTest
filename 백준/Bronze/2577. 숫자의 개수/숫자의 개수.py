a=int(input())
b=int(input())
c=int(input())
result=list(str(a*b*c)) #a,b,c 곱한 값을 문자열(str)로 변환 후 list[]로 묶음
 
for i in range(10): 
    print(result.count(str(i))) #count 함수는 문자열만 사용가능 -> i를 문자열로 바꾼 뒤 출력