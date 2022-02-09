# 풍선 터뜨리기
'''
일렬로 나열된 풍선들의 번호가 담긴 배열 a가 주어집니다. 
위에 서술된 규칙대로 풍선들을 1개만 남을 때까지 터트렸을 때 
최후까지 남기는 것이 가능한 풍선들의 개수를 return 하도록 solution 함수를 완성

입출력 예
a	                                    result
[9,-1,-5]	                            3
[-16,27,65,-2,58,-92,-71,-68,-61,-33]	6
'''

def solution(a):
    # 맨 처음 값과 맨 끝 값은 살아남을 수 있으므로 2
    answer = 2
    if 0 <= len(a) <= 2:
        return len(a)

    left, right = a[0], a[-1]

    # 왼쪽에서 출발해 왼쪽 값보다 크면 1 추가 
    for i in range(1, len(a)-1):
        if a[i] < left:
            answer += 1
            left = a[i]
        
        # 오른쪽에서 출발해 오른쪽 값보다 크면 1 추가
        if right > a[-1-i]:
            answer += 1
            right = a[-1-i]

    # 왼쪽과 오른쪽 값이 같으면 -1
    if left == right:
        answer = answer - 1

    return answer