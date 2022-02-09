# 소수 찾기
'''
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성

입출력 예
numbers	return
"17"	3
"011"	2
'''

from itertools import permutations

def solution(numbers):
    answer = 0
    
    # 각 자리수로 나눔
    nums = [n for n in numbers]
    element = []

    # 만들 수 있는 숫자 조합을 만듦
    for i in range(len(numbers)):
        element += list(permutations(nums, i))

    permu = {int(''.join(p)) for p in element}

    for n in permu:
        if n < 2:
            continue
        
        check = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                check = False
                break
        if check:
            answer.append(n)

    return len(set(answer))
    
numbers = "011"