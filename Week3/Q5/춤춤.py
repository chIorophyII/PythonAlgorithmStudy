# 외벽 점검
'''
문제
외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 
각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist가 매개변수로 주어질 때, 
취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 return 하도록 solution 함수를 완성

입출력 예시
n	weak	            dist	        result
12	[1, 5, 6, 10]	    [1, 2, 3, 4]	2
12	[1, 3, 4, 9, 10]	[3, 5, 7]	    1
'''

from itertools import permutations

def solution(n, weak, dist):
    # 원형을 일자로 변경하기 위해 길이를 2배로 늘림
    weak2 = len(weak)
    for w in range(weak2):
        weak.append(weak[w] + n)

    # 최솟값 구하기 위해 1을 더해서 초기화
    answer = len(dist) + 1

    # 0부터 weak2-1 까지의 위치를 각각 시작점으로 설정
    for start in range(weak2):

        # 친구를 나열하는 모든 경우의 수 각각에 대해 확인
        for f in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 점검할 수 있는 마지막 위치
            position = weak[start] + f[count-1]
            # 시작점부터 모든 취약 지점을 확인

            for i in range(start, start+weak2):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[i]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[i] + f[count-1]
                    
            answer = min(answer, count) # 최솟값 계산
    
    if answer > len(dist):
        return -1
    
    return answer