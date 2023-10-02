def solution(participant, completion):
    answer = ''
    result = dict();
    for p in participant:
        if p in result.keys():
            # print("already")
            result[p] += 1
        else:
            # print("new")
            result[p] = 1
            
    for c in completion:
        result[c] -= 1
        
    for k, v in result.items():
        if v > 0:
            answer = k
    print
    return answer


participant = 	["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))