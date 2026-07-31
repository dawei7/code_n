import heapq


def solve(s: str) -> str:
    frequencies = [0] * 26
    for character in s:
        if character != "?":
            frequencies[ord(character) - ord("a")] += 1

    heap = [(frequency, index) for index, frequency in enumerate(frequencies)]
    heapq.heapify(heap)
    additions = [0] * 26

    for character in s:
        if character == "?":
            frequency, index = heapq.heappop(heap)
            additions[index] += 1
            heapq.heappush(heap, (frequency + 1, index))

    answer = list(s)
    index = 0
    for position, character in enumerate(answer):
        if character != "?":
            continue
        while additions[index] == 0:
            index += 1
        answer[position] = chr(ord("a") + index)
        additions[index] -= 1

    return "".join(answer)
