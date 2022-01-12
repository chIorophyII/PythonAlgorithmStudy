'''
�޴� ������
���� ���
- ���� �� �մ� �ֹ��� �� ���� ���� �Բ� �ֹ��� ��ǰ�޴��� �����ؼ� �ڽ��丮�� �޴� ����
- �ڽ��丮 �޴��� �ּ� 2���� �̻� ��ǰ�޴��� ����
- �ּ� 2�� �̻� �մ����� ����� ����
- orders�� �� �մԵ��� �ֹ��� ��ǰ�޴���
- course�� ��ǰ �޴����� ����
- ������ ���� ���°� �߰��Ѵ�.

���� Ǯ��
1. �� �ڽ����� �������� �̾Ƴ��� �߰��Ѵ�.
2. �� �ڽ����� �������� �߰��� ���� counter �Լ��� ������ ���Ѵ�.
3. ���յ� �޴��� 2���̻��̰� ���� �Ŵ� ���� �ְ��ΰ��� ���Ѵ�.
'''


from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for num in course:
        count = [] # �� �ڽ����� ���� ������ ����Ʈ ����
        for order in orders:
            order = combinations(sorted(order), num) # ���� ����� �ڽ����� �����Ѵ�.
            count += order
        courseFood = Counter(count) # �� �ֹ��Ѱ��� �����Ѱ��� ������ ���Ѵ�.
        # ���ǿ� �°� �߰��Ѵ�.
        answer += [''.join(key) for key, value in courseFood.items() if (value > 1 and  max(courseFood.values()) == value)]
            
    return sorted(answer) # ���ڿ� ������� �����ؼ� �����Ѵ�.


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))