'''
���� Ǯ��
1. �迭�� � ���� �ڽ��� ���� Ȥ�� ������ ��� �� �� ���⿡ �ڱ⺸�� ū ���� ������ ��, ���������� ����� ���� �����մϴ�.
2. �迭�� �հ� �ڿ��� ���� �˻縦 �����Ͽ� ���� ���⿡�� �ڽ��� ���� ���� ��, ������ ��� result �迭�� True�� ��´�.
3. sum(result)���� ���ı��� ����� ���� ������ ǳ������ ������ return.
'''

def solution(a):
    result = [False for _ in range(len(a))]
    minFront, minRear = float("inf"), float("inf")
    for i in range(len(a)):
        if a[i] < minFront:
            minFront = a[i]
            result[i] = True
        if a[-1-i] < minRear:
            minRear = a[-1-i]
            result[-1-i] = True
    return sum(result)

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))