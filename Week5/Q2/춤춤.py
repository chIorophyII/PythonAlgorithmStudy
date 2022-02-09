# 최고의 집합
'''
집합의 원소의 개수 n과 모든 원소들의 합 s가 매개변수로 주어질 때, 
최고의 집합을 return 하는 solution 함수를 완성

입출력 예
n	s	result
2	9	[4, 5]
2	1	[-1]
2	8	[4, 4]
'''

def solution(n, s):
    answer = []

    # n == s 일때 1의 합으로 나타낼 수 있음
    # n > s 일때 [-1]을 return
    if n > s:
        return [-1]

    # 합의 원소들 중 곱셈이 가장 큰 숫자배열은 숫자 간 차이가 얼마 나지 않은 중심에 모인 숫자들
    
    # s를 n만큼 나눈 배열을 생성
    for i in range(n):
        answer.append(s//n)

    # 배열의 합이 s보다 작을 동안 배열에 번갈아가며 1을 추가
    for j in range(s - sum(answer)):
        answer[j] += 1
            
    return sorted(answer)