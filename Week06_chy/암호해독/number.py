
'   + -- + - + -   '
'   + --- + - +   '
'   + -- + - + -   '
'   + - + - + - +   '

def solution(code) :
    answer=''
    for i in code:
        if i=='+':
            answer+='1'
        elif i=="-":
            answer+='0'
    return answer

for i in range(4):
    code = input("암호를 입력하시오: ")
    print(solution(code))


