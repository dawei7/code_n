from collections import Counter, deque


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        colors = "RYBGW"

        def collapse(state: str) -> str:
            while state:
                pieces = []
                removed = False
                start = 0
                while start < len(state):
                    end = start + 1
                    while end < len(state) and state[end] == state[start]:
                        end += 1
                    if end - start >= 3:
                        removed = True
                    else:
                        pieces.append(state[start:end])
                    start = end
                if not removed:
                    return state
                state = "".join(pieces)
            return ""

        hand_counts = Counter(hand)
        initial_counts = tuple(hand_counts[color] for color in colors)
        initial_board = collapse(board)
        if not initial_board:
            return 0

        queue = deque([(initial_board, initial_counts, 0)])
        visited = {(initial_board, initial_counts)}

        while queue:
            state, counts, used = queue.popleft()
            for position in range(len(state) + 1):
                for index, color in enumerate(colors):
                    if counts[index] == 0:
                        continue
                    if position > 0 and state[position - 1] == color:
                        continue
                    joins_color = position < len(state) and state[position] == color
                    splits_pair = (
                        0 < position < len(state)
                        and state[position - 1] == state[position]
                        and state[position] != color
                    )
                    if not joins_color and not splits_pair:
                        continue

                    remaining = list(counts)
                    remaining[index] -= 1
                    next_counts = tuple(remaining)
                    next_board = collapse(state[:position] + color + state[position:])
                    if not next_board:
                        return used + 1
                    next_state = (next_board, next_counts)
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_board, next_counts, used + 1))

        return -1
