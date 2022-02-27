import heapq

def solution(land, height):
    N = len(land)  # land�� ����

    visited = [[False for _ in range(N)] for _ in range(N)]  # �湮�ߴ���
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)] # �̵��� ����
    queue = [] # ��?

    queue.append((0, 0, 0))  # ť�� �ʱⰪ ����
    visit_count = 0  # �湮 Ƚ��
    max_count = N * N  # �ִ� �湮 ���� Ƚ��
    value = 0  # ��ٸ� ��ġ���

    while(visit_count < max_count):
        print(queue)
        v, y, x = heapq.heappop(queue)
        if visited[y][x]:  # �̹� �湮�ߴٸ�
            continue # �ѱ��
        visited[y][x] = True  # �湮 �Ϸ�

        visit_count += 1  # �湮 Ƚ�� + 1
        value += v  # ��ٸ� ��ġ ��� �߰�

        c_height = land[y][x]  # �� ��ǥ�� height
        for ay, ax in move:
            ny, nx = y + ay, x + ax  # �̵��� ��ǥ�� y, x
            if move2(ny, nx, N, visited):  # �̵� �������� üũ
                n_height = land[ny][nx]  # �̵��� ��ǥ�� height

                if abs(n_height - c_height) > height:  # ��ٸ��� �ʿ��� ��� �ʿ��� ����� ������ �� 
                    heapq.heappush(queue, (abs(n_height - c_height), ny, nx))
                else:  # ��ٸ� ���� �湮 ������ ��ǥ�� ����� 0�� �ش�
                    heapq.heappush(queue, (0, ny, nx))
    return value