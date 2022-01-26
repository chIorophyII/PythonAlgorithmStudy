# 단어 변환
'''
두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 
최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 
return 하도록 solution 함수를 작성

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
'''

# dfs 알고리즘 사용
def solution(begin, target, words):
    answer = 0
    stack = [begin]
    visited = [0 for i in words]

    # target이 없으면 0
    if target not in words:
        return 0

    while stack:
        s = stack.pop()
        # target이면 반환
        if s == target:
            return answer
        
        for w in range(len(words)):
            cnt = 0
            for i in range(len(words[w])):
                # 단어가 다른 경우
                if words[w][i] != s[i]:
                    cnt += 1
            # 하나만 다를 경우
            if cnt == 1:
                # 방문 했으면 제외
                if visited[w] == 1:
                    continue
                # 방문 하지 않았으면 추가
                else:
                    visited[w] = 1
                stack.append(words[w])
        answer += 1

    return answer