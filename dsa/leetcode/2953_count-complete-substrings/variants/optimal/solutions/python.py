def solve(word: str, k: int) -> int:
    def count_segment(start: int, end: int) -> int:
        length = end - start
        subtotal = 0

        for distinct in range(1, 27):
            window = distinct * k
            if window > length:
                break

            frequency = [0] * 26
            exactly_k = 0

            for right in range(start, end):
                added = ord(word[right]) - ord("a")
                if frequency[added] == k:
                    exactly_k -= 1
                frequency[added] += 1
                if frequency[added] == k:
                    exactly_k += 1

                if right - start >= window:
                    removed = ord(word[right - window]) - ord("a")
                    if frequency[removed] == k:
                        exactly_k -= 1
                    frequency[removed] -= 1
                    if frequency[removed] == k:
                        exactly_k += 1

                if right - start + 1 >= window and exactly_k == distinct:
                    subtotal += 1

        return subtotal

    answer = 0
    segment_start = 0

    for index in range(1, len(word)):
        if abs(ord(word[index]) - ord(word[index - 1])) > 2:
            answer += count_segment(segment_start, index)
            segment_start = index

    return answer + count_segment(segment_start, len(word))
