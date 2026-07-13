def solve(arr):
    keep = arr[0]
    delete = 0
    answer = arr[0]
    for value in arr[1:]:
        delete = max(delete + value, keep)
        keep = max(keep + value, value)
        answer = max(answer, keep, delete)
    return answer
