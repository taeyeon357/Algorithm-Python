def solution(n):
    answer = 0
    
    str_n = str(n);
    
    for s in str_n:
        answer += int(s)

    return answer


#testcase
print(solution(123))
print(solution(987))