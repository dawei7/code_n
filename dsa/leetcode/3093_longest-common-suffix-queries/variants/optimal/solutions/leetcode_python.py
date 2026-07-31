from typing import List


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        children = [{}]
        best = [-1]

        for index, word in enumerate(wordsContainer):
            node = 0
            priority = (len(word), index)

            if best[node] == -1 or priority < (
                len(wordsContainer[best[node]]),
                best[node],
            ):
                best[node] = index

            for char in reversed(word):
                next_node = children[node].get(char)
                if next_node is None:
                    next_node = len(children)
                    children[node][char] = next_node
                    children.append({})
                    best.append(-1)

                node = next_node
                if best[node] == -1 or priority < (
                    len(wordsContainer[best[node]]),
                    best[node],
                ):
                    best[node] = index

        answer = []
        for query in wordsQuery:
            node = 0
            for char in reversed(query):
                next_node = children[node].get(char)
                if next_node is None:
                    break
                node = next_node
            answer.append(best[node])

        return answer
