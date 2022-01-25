'''
��Ʈ��ũ
�������
1. ��Ʈ��ũ: ��ǻ�� ��ȣ ���� ������ ��ȯ�� �� �ֵ��� ����� ���¸� �ǹ�
2. ��ǻ���� ���� n, ���ῡ ���� ������ ��� 2���� �迭 computers
3. ��Ʈ��ũ ���� ���� ���ϱ�

���� Ǯ��
1. dfs ������� Ǭ��.
2. �ƹ���忡�� ���ۿ��� �湮�Ѵ�.
3. �湮 ������ ���� +1
4. �湮���� ���� ��忡�� �ٽ� ����Ѵ�.
'''

def dfs(root, visited, computers):
    visited[root] = True # �湮���� ǥ��
    for i in range(len(visited)): # len(visited) = n
        # root-i�� �մ� ������ �ְ�, ����i�� ���� �湮 ���ߴٸ�
        if computers[root][i] and not visited[i]: 
            computers[root][i], computers[i][root] = 0, 0 # ���� �湮�� ����(������׷����ϱ�, ���� ��� ����)
            dfs(i, visited, computers) # ����i�� �̿���� Ž���� ���� dfs()ȣ��

def solution(n, computers):
    answer = 0 # ��Ʈ��ũ ����
    visited = [False]*n # �湮���� �Ǵ�
    for i in range(n):
        if not visited[i]: # ���� �湮���� ���� ����
            dfs(i, visited, computers) 
            answer += 1 # ��Ʈ��ũ ���� ����
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))