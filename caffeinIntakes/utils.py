import math


def calculate_caffeine_absorption(amount, time_since_intake):
    pass


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
        # for t1 in range(intake_time, intake_time + 5):
        #     time_since_intake = t1 * interval_minute - intake_time * interval_minute
        #     result[t1] += calculate_caffeine_absorption(
        #         amount, time_since_intake)

        for t2 in range(intake_time, len(result)):
            time_since_intake = t2 * interval_minute - intake_time * interval_minute
            result[t2] += calculate_caffeine_elimination(
                amount, time_since_intake)

    return result


if __name__ == '__main__':
    # 카페인 섭취 예시 (시간, 섭취량)
    intake_list = [(0, 100), (240, 100),]

    # 총 8시간(480분) 동안의 카페인 흡수량 계산
    total_time = 480
    caffeine_levels = process_caffeine_intake(intake_list, total_time)

    print(caffeine_levels)
