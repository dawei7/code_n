


def solve():
    def find_combinations(index, arr, target, current, result):
        # Base case: target reached
        if target == 0:
            result.append(list(current))
            return

        # Out of range or negative target
        if index == len(arr) or target < 0:
            return

        # Include current element (can reuse)
        if arr[index] <= target:
            current.append(arr[index])
            find_combinations(index, arr, target - arr[index], current, result)
            current.pop()

        # Skip current element
        find_combinations(index + 1, arr, target, current, result)


if __name__ == "__main__":
    solve()
