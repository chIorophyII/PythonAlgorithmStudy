# 지형 이동

from collections import deque
import heapq
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def solution(land, height):
    answer = 0
    visited = [[0]*len(land) for i in range(len(land))]
    heap = [[0,0,0]]

    while heap:
        v, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = 1
        answer += v

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < len(land) and 0 <= ny < len(land) and visited[nx][ny] == 0:
                if abs(land[x][y] - land[nx][ny]) > height:
                    heapq.heappush(heap, [abs(land[x][y] - land[nx][ny]), nx, ny])
                else:
                    heapq.heappush(heap, [0, nx, ny])

    return answer