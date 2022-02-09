# 큰 수 만들기
'''
문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. 
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 
문자열 형태로 return 하도록 solution 함수를 완성하세요.
'''

def solution(number, k):
    num = []

    for n in number:
        # 제거할 수가 남아있고 해당 숫자가 num의 마지막 숫자보다 클 때
        while num and k > 0 and num[-1] < n:
            num.pop()
            k -= 1
        num.append(n)

    answer = ''.join(num[:len(number)-k])

    return answer
