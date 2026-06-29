def merge_sorted_arrays(first, second):
    merged_array = []
    i = 0
    j = 0
    n = len(first)
    m = len(second)
    while i < n and j < m:
        if first[i] <= second[j]:
            merged_array.append(first[i])
            i += 1
        else:
            merged_array.append(second[j])
            j += 1
    while i < n:
        merged_array.append(first[i])
        i += 1
    while j < m:
        merged_array.append(second[j])
        j += 1
    return merged_array

def solve():
    n = int(input())
    first = list(map(int, input().split()))
    m = int(input())
    second = list(map(int, input().split()))
    merged_array = merge_sorted_arrays(first, second)
    print(' '.join(map(str, merged_array)))


if __name__ == "__main__":
    solve()
