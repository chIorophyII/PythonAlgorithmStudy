'''
Ÿ�ϳѹ�
�������
1. n���� ���� �ƴ� ����
2. �� ���� ������ ���� �������� Ÿ�� �ѹ� ����
3. ��� ���ϱ�

���� Ǯ��
1. BFS ��� ���
2. queue ����ϱ����� deque ���
3. numbers�� ���ڸ� ���ϰų� �� ��츦 ���������� �߰����ش�.
4. �ᱹ leaves����Ʈ�� ��� ��� ����� ���� �ȴ�. ���� target���� ���ؼ� ��� ���.

'''

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

print(solution([1,1,1,1,1], 3))