from typing import List


def solve(cookies: List[int], k: int) -> int:
    cookies.sort(reverse=True)
    loads = [0] * k
    answer = sum(cookies)

    def search(bag_index: int) -> None:
        nonlocal answer
        if bag_index == len(cookies):
            answer = min(answer, max(loads))
            return

        bag = cookies[bag_index]
        used = set()
        for child in range(k):
            if loads[child] in used or loads[child] + bag >= answer:
                continue
            used.add(loads[child])
            loads[child] += bag
            search(bag_index + 1)
            loads[child] -= bag

    search(0)
    return answer
