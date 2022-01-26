# 여행경로
'''
항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 
방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성

입출력 예시
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	
return = ["ICN", "JFK", "HND", "IAD"]
'''

def solution(tickets):
    answer = []
    route = dict()

    # 출발지 : [도착지1, 도착지2]
    for t in tickets:
        if t[0] in route:
            route[t[0]].append(t[1])
        else:
            route[t[0]] = [t[1]]
            
    # 값 역순으로 정렬
    for start in route.keys():
        route[start].sort(reverse = True)

    start = ["ICN"]
    while start:
        target = start[-1]
        if target not in route or len(route[target]) == 0:
            answer.append(start.pop())
        else:
            start.append(route[target].pop())
    
    return answer[::-1]