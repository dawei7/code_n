def solve(words: list[str]) -> int:
    current = {(words[0][0], words[0][-1]): len(words[0])}

    for word in words[1:]:
        first = word[0]
        last = word[-1]
        length = len(word)
        next_states = {}

        for (left, right), total in current.items():
            append_key = (left, last)
            append_length = total + length - (right == first)
            next_states[append_key] = min(next_states.get(append_key, float("inf")), append_length)

            prepend_key = (first, right)
            prepend_length = total + length - (last == left)
            next_states[prepend_key] = min(next_states.get(prepend_key, float("inf")), prepend_length)

        current = next_states

    return min(current.values())
