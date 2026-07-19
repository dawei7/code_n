from collections import deque


def solve(s: str, words: list[str]) -> str:
    alphabet = sorted(set(s).union(*(set(word) for word in words)))
    char_index = {char: index for index, char in enumerate(alphabet)}

    children: list[dict[str, int]] = [{}]
    longest = [0]
    for word in words:
        state = 0
        for char in word:
            next_state = children[state].get(char)
            if next_state is None:
                next_state = len(children)
                children[state][char] = next_state
                children.append({})
                longest.append(0)
            state = next_state
        longest[state] = max(longest[state], len(word))

    state_count = len(children)
    transitions = [[0] * len(alphabet) for _ in range(state_count)]
    for state, edges in enumerate(children):
        for char, next_state in edges.items():
            transitions[state][char_index[char]] = next_state

    failure = [0] * state_count
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

    result: list[str] = []
    active = 0
    was_bold = False
    for index, char in enumerate(s):
        active += difference[index]
        is_bold = active > 0
        if is_bold and not was_bold:
            result.append("<b>")
        elif was_bold and not is_bold:
            result.append("</b>")
        result.append(char)
        was_bold = is_bold
    if was_bold:
        result.append("</b>")
    return "".join(result)
