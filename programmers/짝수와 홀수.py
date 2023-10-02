def solution(num):
    answer = ''
    
    if num %2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

#testcase
print(solution(3))
print(solution(4))