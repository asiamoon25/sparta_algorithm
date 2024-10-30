def solution(n, times):
    # 최소 시간과 최대 시간의 초기 범위를 설정합니다.
    left = 1  # 최소 시간은 1분
    right = max(times) * n  # 최대 시간은 가장 오래 걸리는 심사관이 모든 사람을 심사하는 경우

    # 이분 탐색 시작
    while left < right:
        mid = (left + right) // 2  # 중간값
        # mid 시간 동안 모든 심사관들이 심사할 수 있는 총 인원 수를 계산
        total_people = sum(mid // time for time in times)

        # n명 이상의 인원을 심사할 수 있다면 시간을 줄이기 위해 right 값을 낮춥니다.
        if total_people >= n:
            right = mid
        else:
            left = mid + 1

    return left  # 최소 시간을 반환