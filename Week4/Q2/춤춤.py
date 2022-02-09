# 네트워크
'''
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 
매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성
'''

# bfs 알고리즘 사용
from collections import deque

def solution(n, computers):
    answer = 0
    queue = deque([0])
    visited = [0]*n

    while 0 in visited:
        z = visited.index(0)
        queue.append(z)

        while queue:
            node = queue.popleft()
            visited[node] = 1
            
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    queue.append(i)
                    visited[i] = 1
        answer += 1

    return answer