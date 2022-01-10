'''
���� ä�ù�
���� ���
- "[�г���]���� ���Խ��ϴ�.",  "[�г���]���� �������ϴ�." ���
- �г��� ���� ��� �ΰ���
1. ä�ù��� ���� ��, ���ο� �г������� �ٽ� ����.
2. ä�ù濡�� �г����� �����Ѵ�.
- ���������� ���� ������ ����� ���� �Ǵ� �޽����� ���ڿ� �迭 ���·� return �Ѵ�.

���� Ǯ��
1. ���̵� : �г��� key value ������ ���� ����
2. ���������� ����� �г��� �������� ���� �ؼ� ���� �Ҷ� ���̵�� ���Դ� �����ٸ� �߰��Ѵ�.
3. Enter �϶� dicŸ�Կ� �����ϰ� id �� ���Դٰ� �߰��Ѵ�.
4. Leave �϶� id�� �����ٰ� �����Ѵ�.
5. Chnage Ű���� �̸� ���� �����Ѵ�.
6. ���������� id�� ���� �Ѱ��� �г��� ���� �۾��Ѵ�.

'''

user = {} #dic Type ���� ����

def solution(record):
    answer = []
    for data in record:
        infor = data.split() # ���� �������� ����Ʈ�� �����.
        if infor[0] == 'Enter': # ��� ����
            user[infor[1]] = infor[2] # Ű�� �� �̸� �����Ѵ�.
            answer.append((infor[1], 'E'))  # ID�� ��� ���ٰ� ǥ���Ѵ�.
        elif infor[0] == 'Leave': # ������
            answer.append((infor[1], 'L')) # ID�� �����ٰ� ǥ���Ѵ�.
        elif infor[0] == 'Change': # �г��� ���� �Ҷ�
            user[infor[1]] = infor[2]
            
    # ���������� ����Ѱ��� id �� �г���, ���� �ڵ� ���� ������ �����Ѵ�.           
    return [user[data[0]] + ('���� ���Խ��ϴ�.' if data[1] == 'E' else '���� �������ϴ�.') for data in answer]

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))