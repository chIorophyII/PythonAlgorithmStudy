# 광고 삽입
'''
"죠르디"의 동영상 재생시간 길이 play_time, 
공익광고의 재생시간 길이 adv_time, 
시청자들이 해당 동영상을 재생했던 구간 정보 logs가 매개변수로 주어질 때, 
시청자들의 누적 재생시간이 가장 많이 나오는 곳에 공익광고를 삽입하려고 합니다
이때, 공익광고가 들어갈 시작 시각을 구해서 return 하도록 solution 함수를 완성
만약, 시청자들의 누적 재생시간이 가장 많은 곳이 여러 곳이라면, 
그 중에서 가장 빠른 시작 시각을 return 하도록 합니다.
'''

# 시각을 숫자(초)로 나타내는 함수
def time_to_num(time): 
    hour, minu, sec = time.split(':')
    return int(hour) * 3600 + int(minu) * 60 + int(sec)

# 숫자(초)를 시각으로 나타내는 함수
def num_to_time(time): 
    hour = time // 3600
    hour = '0' + str(hour) if hour < 10 else str(hour)
    time %= 3600
    minu = time // 60
    minu = '0' + str(minu) if minu < 10 else str(minu)
    time = time % 60
    sec = '0' + str(time) if time < 10 else str(time)
    return hour + ':' + minu + ':' + sec

def solution(play_time, adv_time, logs):
    # 전체 시간, 광고 시간을 숫자(초)로 변경
    p_time = time_to_num(play_time)
    a_time = time_to_num(adv_time)          
    # 전체 초를 배열로 담기
    total = [0 for i in range(p_time + 1)]

    # 로그를 시작, 끝으로 분리해 시작에는 1, 끝에는 -1을 추가
    for l in logs:
        start, end = l.split('-')
        start = time_to_num(start)
        end = time_to_num(end)
        total[start] += 1
        total[end] -= 1

    # 특정 초에 시청하는 인원 파악하기 위해 이전 숫자에 현재 숫자 더함
    for i in range(1, len(total)): 
        total[i] += total[i - 1]

    # 누적 시청 인원 파악하기 위해 같은 과정 반복
    for i in range(1, len(total)):
        total[i] += total[i - 1]

    most_view = 0 # 가장 많이 시청한 사람 수
    max_time = 0  # 가장 많이 시청한 시간
    for i in range(a_time - 1, p_time):
        if i >= a_time:
            if most_view < total[i] - total[i - a_time]:
                most_view = total[i] - total[i - a_time]
                max_time = i - a_time + 1
        else:
            if most_view < total[i]:
                most_view = total[i]
                max_time = i - a_time + 1

    return num_to_time(max_time)

'''
데이터 형변환을 한꺼번에 하기 위해
zip 함수를 썼더니 런타임 에러가 남
효율성 문제에서는 이 부분을 주의할 필요가 있을 것 같다
'''