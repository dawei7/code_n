def solve(arr, k, threshold):
    target = k * threshold
    window = sum(arr[:k])
    answer = int(window >= target)
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        if window >= target:
            answer += 1
    return answer
