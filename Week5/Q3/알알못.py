'''
���� Ǯ��
1. 1 ���� ���� ��ŭ ���� ���� �Ѵ�.
2. �� ���� ��ŭ ���� �����ؼ� �Ҽ� �Ǵ��Ѵ�.
3. set���� �ߺ��� ���� �ϰ� ���� ��ȯ �Ѵ�.
'''
from itertools import permutations

def solution(numbers):
    answer = []                                   
    nums = [n for n in numbers]                   # numbers�� �ϳ��� �ڸ� ��
    per = []                                      
    for i in range(1, len(numbers)+1):            # numbers�� �� ���ڵ��� ������ ��� ��� �����
        per += list(permutations(nums, i))        # i���� ��������
    new_nums = [int(("").join(p)) for p in per]   # �� ���������� �ϳ��� int�� ���ڷ� ��ȯ

    for n in new_nums:                            # ��� int�� ���ڿ� ���� �Ҽ����� �Ǻ�
        if n < 2:                                 # 2���� ���� 1,0�� ��� �Ҽ� �ƴ�
            continue
        check = True            
        for i in range(2,int(n**0.5) + 1):        # n�� ������ ���� ���� ���ڱ����� ������
            if n % i == 0:                        # �ϳ��� �����������ٸ� �Ҽ� �ƴ�!
                check = False
                break
        if check:
            answer.append(n)                      # �Ҽ��ϰ�� answer �迭�� �߰�

    return len(set(answer))                       # set�� ���� �ߺ� ���� �� ��ȯ

print(solution("17"))
print(solution("011"))