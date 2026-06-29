import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    arr = data[1:1 + n]
    target = sorted(((value, i) for i, value in enumerate(arr)))
    current_pos = list(range(n))
    pos_of_index = list(range(n))
    swaps = []
    for sorted_pos, (_, original_index) in enumerate(target):
        where = pos_of_index[original_index]
        if where == sorted_pos:
            continue
        swaps.append((sorted_pos, where))
        left_original = current_pos[sorted_pos]
        current_pos[sorted_pos], current_pos[where] = (current_pos[where], current_pos[sorted_pos])
        pos_of_index[original_index] = sorted_pos
        pos_of_index[left_original] = where
    print(len(swaps))
    for a, b in swaps:
        print(a, b)


if __name__ == "__main__":
    solve()
