'''
���� Ǯ��
1. N���� s�� ũ�Ⱑ ū ���� �Ұ����ؼ� ū ��� -1 �����Ѵ�.
2. n�� ������..
3. �׸��� �������� ������ ��ŭ �� �ε��� +1 �� ���ش�.
'''

def solution(n, s):
    # �ڿ��� n���� ������ n���� ���� s�� ���� ���� �����Ƿ� [-1]�� �����Ѵ�
    if n > s: return [-1]
    result = []
    # s�� n���� ���� ���� n���̵��� �ʱⰪ�� ���Ѵ�.
    initial = s // n
    for _ in range(n):
        result.append(initial)
    idx = len(result) - 1
    # s�� n���� ���� �򿡼� ��������ŭ �� ���� 1�� �����ش�.
    for _ in range(s % n):
        result[idx] += 1
        idx -=1
    return result

print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))