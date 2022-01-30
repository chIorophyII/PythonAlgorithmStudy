'''
�������
1."ICN" ���׿��� ����մϴ�.
2. 2���� �迭 tickets�� �Ű������� �־��� ��, �湮�ϴ� ���� ��θ� �迭�� ��� return

����Ǯ��
1. Ű : �� ���� ������ �ٲ۴�.
2.  bfs ����� ����Ѵ�.
3. stack�� 'INC' ���� �����ؼ� Ű�� ã���鼭 ���� ��θ� ��´�.

'''

from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])
    for key in routes.keys():
        routes[key].sort(reverse=True)
    stack = ['ICN']
    while stack:
        tmp = stack[-1]
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))