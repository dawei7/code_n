


def solve():
    def frequency_based_sort(n, arr):
        # Initialize a count dictionary to count frequencies (since max value is 100)
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1

        # Create a list of tuples (value, frequency)
        freq_list = [(value, freq) for value, freq in count.items()]

        # Sort the list by frequency (ascending) and by value (ascending if frequencies are the same)
        freq_list.sort(key=lambda x: (x[1], x[0]))

        # Output the sorted list based on frequency
        for value, freq in freq_list:
            print(f"{value} " * freq, end="")

    if __name__ == "__main__":
        n = int(input())
        arr = list(map(int, input().split()))

        # Function call to perform frequency-based sorting
        frequency_based_sort(n, arr)


if __name__ == "__main__":
    solve()
