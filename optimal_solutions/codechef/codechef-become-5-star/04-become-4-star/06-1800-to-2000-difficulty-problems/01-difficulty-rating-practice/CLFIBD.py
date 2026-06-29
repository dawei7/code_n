


def solve():
    def is_dynamic_string(s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        if len(freq) < 3:
            return "Dynamic"

        f = sorted(freq.values())

        def check_sequence(arr):
            return all(arr[i] == arr[i-1] + arr[i-2] for i in range(2, len(arr)))

        return "Dynamic" if (check_sequence(f) or 
                             (len(f) >= 3 and check_sequence([f[1], f[0]] + f[2:]))) else "Not"

    for _ in range(int(input())):
        print(is_dynamic_string(input().strip()))


if __name__ == "__main__":
    solve()
