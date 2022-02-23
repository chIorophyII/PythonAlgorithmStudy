# 가장 긴 팰린드롬

def solution(s):
    answer = 1

    for start in range(len(s)): # 0,1,2,3,4,5
        for end in range(start+2, len(s)+1): # 2,3,4,5,6
            a = s[start:end] # a = s[0:3] aba
            if len(a) < answer: # 2 
                continue
            if a == a[::-1]:
                answer = max(answer, end-start) # answer

    return answer