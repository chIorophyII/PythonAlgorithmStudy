def find(parents, money, number, answer):
    # ��ȣ���� ���� �����ų� �� ���� ������ ����
    if parents[number] == number or money // 10 == 0:
        answer[number] += money
        return
    send = money // 10
    mine = money - send
    answer[number] += mine
    find(parents, send, parents[number], answer)
    return


def solution(enroll, referral, seller, amount):
    n = len(enroll)  # �� ��� ��(��ȣ ���� X)
    answer = [0] * (n + 1)  # ��ȣ ����
    d = {}  # �̸�-��ȣ�� key-value�� ������ ��ųʸ�
    parents = [i for i in range(n + 1)]  # ���� �ڽ��� �θ�� �ʱ�ȭ
    # �̸�-��ȣ�� ��ųʸ��� ����
    for i in range(n):
        d[enroll[i]] = i + 1
    # ��õ�� �Է�
    for i in range(n):
        if referral[i] == "-":  # ��ȣ�� ��õ��
            parents[i + 1] = 0
        else:
            parents[i + 1] = d[referral[i]]
    # ĩ�� ����
    for i in range(len(seller)):
        find(parents, amount[i] * 100, d[seller[i]], answer)
    return answer[1:]