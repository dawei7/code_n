def solve(arr: list[int]) -> int:
    suffix_minimum = [0] * len(arr)
    suffix_minimum[-1] = arr[-1]
    for index in range(len(arr) - 2, -1, -1):
        suffix_minimum[index] = min(arr[index], suffix_minimum[index + 1])

    chunks = 1
    prefix_maximum = arr[0]
    for index in range(len(arr) - 1):
        prefix_maximum = max(prefix_maximum, arr[index])
        if prefix_maximum <= suffix_minimum[index + 1]:
            chunks += 1
    return chunks
