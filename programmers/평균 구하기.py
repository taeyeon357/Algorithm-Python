def solution(arr):
    answer = 0
    answer = sum(arr)/len(arr)
    return answer

arr1 = [1,2,3,4]
arr2 = [5,5]

print(solution(arr1))
print(solution(arr2))