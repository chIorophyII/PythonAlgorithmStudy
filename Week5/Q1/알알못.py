'''
���� Ǯ��
1. �� �迭 ���� (n -1) factorial ����Ѵ�.
2. �迭�� ���° �ε��� �� ���� ã�´�.
3. �迭�� ���� �� ���� ���� ���� �ݺ��Ѵ�.
'''

import math

def solution(n, k):
    answer = []
    array = list(range(1, n+1))
    count = 1
    
    while n:
        temp = math.factorial(n) // n
        index = k // temp
        k = k % temp
        if k == 0:
            answer.append(array.pop(index - 1))
        else:
            answer.append(array.pop(index))
        print(answer, temp, index, k)
        n -= 1
    return answer

print(solution(3, 5))
