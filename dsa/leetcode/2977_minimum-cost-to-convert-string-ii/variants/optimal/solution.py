from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        identifiers = {}
        for word in original + changed:
            if word not in identifiers:
                identifiers[word] = len(identifiers)

        count = len(identifiers)
        infinity = 10**30
        distance = [[infinity] * count for _ in range(count)]
        for word_id in range(count):
            distance[word_id][word_id] = 0

        for start, end, price in zip(original, changed, cost):
            first = identifiers[start]
            second = identifiers[end]
            distance[first][second] = min(distance[first][second], price)

        for middle in range(count):
            for first in range(count):
                through_middle = distance[first][middle]
                if through_middle == infinity:
                    continue
                for second in range(count):
                    candidate = through_middle + distance[middle][second]
                    if candidate < distance[first][second]:
                        distance[first][second] = candidate

        children = [{}]
        terminal = [-1]
        for word, word_id in identifiers.items():
            node = 0
            for character in word:
                next_node = children[node].get(character)
                if next_node is None:
                    next_node = len(children)
                    children[node][character] = next_node
                    children.append({})
                    terminal.append(-1)
                node = next_node
            terminal[node] = word_id

        n = len(source)
        best = [infinity] * (n + 1)
        best[0] = 0

        for start in range(n):
            if best[start] == infinity:
                continue
            if source[start] == target[start]:
                best[start + 1] = min(best[start + 1], best[start])

            source_node = 0
            target_node = 0
            for end in range(start, n):
                source_node = children[source_node].get(source[end], -1)
                target_node = children[target_node].get(target[end], -1)
                if source_node == -1 or target_node == -1:
                    break

                source_id = terminal[source_node]
                target_id = terminal[target_node]
                if source_id != -1 and target_id != -1:
                    price = distance[source_id][target_id]
                    if price != infinity:
                        best[end + 1] = min(best[end + 1], best[start] + price)

        return -1 if best[n] == infinity else best[n]
