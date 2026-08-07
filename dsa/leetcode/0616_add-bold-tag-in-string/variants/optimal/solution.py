from collections import deque
from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        alphabet = sorted(set(s).union(*(set(word) for word in words)))
        char_index = {char: index for index, char in enumerate(alphabet)}

        children = [{}]
        longest = [0]
        for word in words:
            state = 0
            for char in word:
                if char not in children[state]:
                    children[state][char] = len(children)
                    children.append({})
                    longest.append(0)
                state = children[state][char]
            longest[state] = max(longest[state], len(word))

        transitions = [[0] * len(alphabet) for _ in children]
        for state, edges in enumerate(children):
            for char, next_state in edges.items():
                transitions[state][char_index[char]] = next_state

        failure = [0] * len(children)
        queue = deque(children[0].values())
        while queue:
            state = queue.popleft()
            longest[state] = max(longest[state], longest[failure[state]])
            for char, index in char_index.items():
                child = children[state].get(char)
                if child is None:
                    transitions[state][index] = transitions[failure[state]][index]
                else:
                    failure[child] = transitions[failure[state]][index]
                    queue.append(child)

        difference = [0] * (len(s) + 1)
        state = 0
        for end, char in enumerate(s):
            state = transitions[state][char_index[char]]
            length = longest[state]
            if length:
                difference[end - length + 1] += 1
                difference[end + 1] -= 1

        answer = []
        active = 0
        was_bold = False
        for index, char in enumerate(s):
            active += difference[index]
            is_bold = active > 0
            if is_bold and not was_bold:
                answer.append("<b>")
            elif was_bold and not is_bold:
                answer.append("</b>")
            answer.append(char)
            was_bold = is_bold
        if was_bold:
            answer.append("</b>")
        return "".join(answer)
