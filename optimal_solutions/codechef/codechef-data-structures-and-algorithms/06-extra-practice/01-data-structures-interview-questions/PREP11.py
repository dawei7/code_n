def canAllocate(books, students, maxPages):
    count = 1
    current_sum = 0
    for pages in books:
        if current_sum + pages > maxPages:
            count += 1
            current_sum = pages
            if count > students:
                return False
        else:
            current_sum += pages
    return True

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        students = int(input_data[index])
        index += 1
        books = list(map(int, input_data[index:index + n]))
        index += n
        low = max(books)
        high = sum(books)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if canAllocate(books, students, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        results.append(str(ans))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
