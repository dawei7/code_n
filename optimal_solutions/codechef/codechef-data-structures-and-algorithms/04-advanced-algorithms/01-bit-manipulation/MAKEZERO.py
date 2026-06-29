


def solve():
    def sol():
        _n = int(input())  # Read the number of elements
        _v = list(map(int, input().split()))  # Read the list of elements
        _bit = [0] * 30  # Initialize a list to count bits
        _ans = 0  # Initialize answer variable

        for _i in range(_n):
            _current_value = _v[_i]  # Get the current value
            for _j in range(30):
                if (_current_value & (1 << _j)):  # Check if the j-th bit is set
                    _bit[_j] += 1  # Increment the count for this bit

        for _j in range(30):
            if _bit[_j] > 0:  # Check if the bit was set in any number
                _ans += 1  # Increment answer if the bit is set in any number

        print(_ans)  # Output the result

    if __name__ == "__main__":
        _test_cases = int(input())  # Read the number of test cases
        for _ in range(_test_cases):
            sol()  # Solve for each test case


if __name__ == "__main__":
    solve()
