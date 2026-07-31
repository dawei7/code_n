class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:
        if sum(weight for _, weight in items) < capacity:
            return -1

        items.sort(key=lambda item: item[0] / item[1], reverse=True)
        answer = 0.0

        for price, weight in items:
            taken = min(capacity, weight)
            answer += price * taken / weight
            capacity -= taken

            if capacity == 0:
                return answer
