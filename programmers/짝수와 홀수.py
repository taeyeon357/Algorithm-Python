def solution(num):
    answer = ''
    
    if num %2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

#테스트 케이스
print(solution(3))
print(solution(4))