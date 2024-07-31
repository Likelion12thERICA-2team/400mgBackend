import math


def calculate_caffeine_absorption(amount, time_since_intake):
    absorption_start = 10  # 흡수 시작 시간 (분)
    full_absorption = 45   # 완전 흡수 시간 (분)

    if time_since_intake < absorption_start:
        return 0
    elif time_since_intake < full_absorption:
        # 선형 흡수 가정
        return amount * (time_since_intake - absorption_start) / (full_absorption - absorption_start)
    else:
        return amount


def calculate_caffeine_elimination(amount, time):
    half_life = 342  # 반감기 (분)
    return amount * math.exp(-(math.log(2)/half_life) * time)


def process_caffeine_intake(intake_list, total_time):
    print(intake_list)

    interval_minute = 10  # 10분 간격

    # 이전 12시간 + 이후 total_time시간 동안의 카페인 흡수량 계산
    num_interval = (total_time + (12 * 60)
                    ) // interval_minute + 1  # 10분 간격으로 계산
    # 인덱스 71이 12시간 후를 의미(현재 시간)
    result = [0] * num_interval

    for intake_time, amount in intake_list:
        intake_time = intake_time // interval_minute
        time_since_intake = 72 - intake_time
        print(intake_time)
        for t in range(time_since_intake, num_interval):

            # print(time_since_intake)
            absorbed = calculate_caffeine_absorption(amount, t)
            remaining = calculate_caffeine_elimination(
                absorbed, t)
            result[t] += remaining

    return result


if __name__ == '__main__':
    # 카페인 섭취 예시 (시간, 섭취량)
    intake_list = [(0, 100), (240, 100),]

    # 총 8시간(480분) 동안의 카페인 흡수량 계산
    total_time = 480
    caffeine_levels = process_caffeine_intake(intake_list, total_time)

    print(caffeine_levels)
