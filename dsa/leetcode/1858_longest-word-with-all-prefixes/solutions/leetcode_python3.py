from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        children = [{}]
        terminal_word = [None]

        for word in words:
            node = 0
            for character in word:
                next_node = children[node].get(character)
                if next_node is None:
                    next_node = len(children)
                    children[node][character] = next_node
                    children.append({})
                    terminal_word.append(None)
                node = next_node
            terminal_word[node] = word

        answer = ""
        stack = [0]
        while stack:
            node = stack.pop()
            for next_node in children[node].values():
                word = terminal_word[next_node]
                if word is None:
                    continue
                if len(word) > len(answer) or (
                    len(word) == len(answer) and word < answer
                ):
                    answer = word
                stack.append(next_node)

        return answer
