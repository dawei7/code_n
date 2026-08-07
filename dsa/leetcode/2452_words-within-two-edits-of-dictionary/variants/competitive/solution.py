from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        answer = []

        for query in queries:
            for word in dictionary:
                differences = 0
                for query_letter, word_letter in zip(query, word):
                    if query_letter != word_letter:
                        differences += 1
                        if differences > 2:
                            break
                if differences <= 2:
                    answer.append(query)
                    break

        return answer
