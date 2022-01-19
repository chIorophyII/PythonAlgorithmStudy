# 합승  택시 요금
'''
지점의 개수 n, 출발지점을 나타내는 s, A의 도착지점을 나타내는 a, 
B의 도착지점을 나타내는 b, 지점 사이의 예상 택시요금을 나타내는 fares가 
매개변수로 주어집니다. 
이때, A, B 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다고 
가정할 때, 최저 예상 택시요금을 계산해서 return 하도록 solution 함수를 완성
만약, 아예 합승을 하지 않고 각자 이동하는 경우의 예상 택시요금이 더 낮다면, 
합승을 하지 않아도 됩니다.

제한사항
fares 배열의 크기는 2 이상 n x (n-1) / 2 이하입니다.
- 예를들어, n = 6이라면 fares 배열의 크기는 2 이상 15 이하입니다. 
  (6 x 5 / 2 = 15)
- fares 배열의 각 행은 [c, d, f] 형태입니다.
- c지점과 d지점 사이의 예상 택시요금이 f원이라는 뜻입니다.

입출력 예시
n, s, a, b = 6,4,6,2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], 
         [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
result = 82
'''

import heapq

def dijkstra(graph, start):
    # 다른 노드와의 거리를 무한대로 설정
    distances = {node : float('inf') for node in graph}
    # 시작 노드의 거리는 0
    distances[start] = 0
    queue = []

    # 큐에 노드, 거리 순으로 값을 넣음
    heapq.heappush(queue, [distances[start], start])

    while queue:
        # 가장 낮은 거리를 가진 노드, 거리를 추출
        cur_distance, cur_node = heapq.heappop(queue)

        # 추출된 거리보다 저장된 거리가 더 작으면 큐의 다음 데이터로 넘어감
        if distances[cur_node] < cur_distance:
            continue
        
        # 대상인 노드에서 인접한 노드와의 거리를 반복
        for adj_node, weight in graph[cur_node].items():
            # 현재 노드에서 인접한 노드를 지나갈 때까지의 거리를 더함 
            distance = cur_distance + weight
            
            # 저장된 거리보다 가중치가 더 작으면 해당 노드의 거리 변경
            if distance < distances[adj_node]:
                distances[adj_node] = distance
                # 다음 인접 거리를 계산하기 위해 큐에 삽입
                heapq.heappush(queue, [distance, adj_node])

    return distances

def solution(n, s, a, b, fares):
    answer = []
    dic = dict()

    # 노드 수만큼 key 생성
    for i in range(n):
        dic[i+1] = {}

    # 각 노드, 거리에 대해 값으로 삽입
    for f in fares:
        dic[f[0]][f[1]] = f[2]
        dic[f[1]][f[0]] = f[2]
    
    can = dijkstra(dic, s)

    answer.append(can[a] + can[b])
    # 시작점을 제외한 나머지 노드에 대해
    for i in range(1, n+1):
        if i == s:
            continue
        mid = i
        temp = dijkstra(dic, mid)
        answer.append(can[mid] + temp[a] + temp[b])

    return min(answer)

'''
다익스트라 알고리즘을 사용
'''