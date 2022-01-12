'''
���� �˻�
���� ���: �� �������� �´� ������ � �ִ��� �����´�.

ǰ��
1. �ܼ��ϰ� ������ for�� �����͵��� for�� ������ ��Ȯ���� ������ ȿ�������� ��������.
2. info ���� ���ڿ��� ����������� ����Ʈ�� �����.
3. Ű����� ���� �� �ִ� ��� ���� �����.
4. �������� ��ųʸ� �����. 
5. �������� ������� value�� �߰��Ѵ�.
6. ��ųʸ� �� ���Ҹ��� value ������ �������� ����
7.  query�� �ѹ��� ���鼭, info��ųʸ��� Ž���ϰ� �Ǵµ�, query�� key���� info��ųʸ��� Ű������ �����ϸ� �� info��ųʸ��� value������ �´�.
8. ������ ���������� ���� �������� �Ѵ� �͵��� ������ �̺�Ž���� ���� ���ϸ� �ȴ�.
'''

from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        infol = info[i].split()  # info���� ���ڿ��� ������ �������� �и�
        mykey = infol[:-1]  # info�� �������ܺκ��� key�� �з�
        myval = infol[-1]  # info�� �����κ��� value�� �з�

        for j in range(5):  # key��� ���� �� �ִ� ��� ���� ����
            for c in combinations(mykey, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(myval))  # �� ������ key���� ���� �߰�
                else:
                    info_dict[tmp] = [int(myval)]

    for k in info_dict:
        info_dict[k].sort()  # dict���� ���յ��� ���������� ����

    for qu in query:  # query�� ���������� key�� value�� �и�
        myqu = qu.split(' ')
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while 'and' in qu_key:  # and ����
            qu_key.remove('and')
        while '-' in qu_key:  # - ����
            qu_key.remove('-')
        qu_key = ''.join(qu_key)  # dict�� keyó�� ���ڿ��� ����

        if qu_key in info_dict:  # query�� key�� info_dict�� key�� �����ϸ�
            scores = info_dict[qu_key]

            if scores:  # score����Ʈ�� ���� �����ϸ�
                enter = bisect_left(scores, int(qu_val))

                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer