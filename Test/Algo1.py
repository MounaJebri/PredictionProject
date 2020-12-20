def solution(N, A):
    # write your code in Python 3.6
    RESP = [0] * N
    MAX = N + 1
    current_max = 0
    current_min = 0
    for operation in A:
        if operation != MAX:
            if RESP[operation-1] <= current_min:
                RESP[operation-1] = current_min + 1
            else:
                RESP[operation-1] += 1

            if RESP[operation-1] > current_max:
                current_max = RESP[operation-1]
        else:
            if current_min == current_max:
                current_min += 1
            else:
                current_min = current_max

    for i, val in enumerate(RESP):
        if val < current_min:
            RESP[i] = current_min
    return RESP