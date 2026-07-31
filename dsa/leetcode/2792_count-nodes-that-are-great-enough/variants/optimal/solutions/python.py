from bisect import insort


def solve(root, k: int) -> int:
    summaries = {}
    answer = 0
    stack = [(root, False)]

    while stack:
        node, expanded = stack.pop()

        if node is None:
            continue

        if not expanded:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
            continue

        left = summaries.pop(id(node.left), []) if node.left else []
        right = summaries.pop(id(node.right), []) if node.right else []
        merged = []
        left_index = 0
        right_index = 0

        while len(merged) < k and (
            left_index < len(left) or right_index < len(right)
        ):
            if right_index == len(right) or (
                left_index < len(left)
                and left[left_index] <= right[right_index]
            ):
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        if len(merged) == k and node.val > merged[-1]:
            answer += 1

        insort(merged, node.val)
        if len(merged) > k:
            merged.pop()

        summaries[id(node)] = merged

    return answer
