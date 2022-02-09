# 줄 서는 방법
'''
사람의 수 n과, 자연수 k가 주어질 때, 
사람을 나열 하는 방법을 사전 순으로 나열 했을 때, 
k번째 방법을 return하는 solution 함수를 완성

입출력 예시
n	k	result
3	5	[3,1,2]
'''

import math

def solution(n,k):
    # 1부터 n 까지의 숫자를 생성
    # people = [i+1 for i in range(n)] -> 시간초과
    people = [i for i in range(1, n+1)]
    answer = []
    k = k-1

    while people:
        # n개 숫자를 줄 세울 때 맨 앞자리가 바뀌는 주기는 (n-1)! 이므로
        # k번째 순열의 첫 번째 자리는 k를 (n-1)!로 나눈 몫을 인덱스로 설정
        idx = k // math.factorial(n-1)
        # 해당 인덱스에 있는 숫자를 answer에 추가 후 people에서 제거
        answer.append(people.pop(idx))

        # 앞 자리를 설정했다면 n을 1씩 줄여 같은 숫자를 추가
        # 만약 0이 되면 그 때부터는 순열을 순서대로 추가
        k = k % math.factorial(n-1)
        n -= 1
    
    return answer