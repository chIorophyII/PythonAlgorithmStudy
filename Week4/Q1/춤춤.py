# 타겟 넘버
'''
사용할 수 있는 숫자가 담긴 배열 numbers, 
타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 
타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성
'''
# bfs 알고리즘 사용
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0,0)]) # 초기 합, 인덱스

    while queue:
        add, idx = queue.popleft()

        # 인덱스가 numbers의 길이와 같아지고 합이 타겟과 같으면
        if idx == len(numbers):
            if add == target:
                answer += 1

        # 인덱스가 numbers의 길이보다 작을 때
        else:
            num = numbers[idx] # num에 값 추가
            queue.append((add+num, idx+1)) # 합에 숫자를 더함
            queue.append([add-num, idx+1]) # 합에서 숫자를 뺌

    return answer   