from collections import deque


def solve(status, candies, keys, contained_boxes, initial_boxes):
    owned = set(initial_boxes)
    opened = set()
    queue = deque(box for box in initial_boxes if status[box] == 1)
    total = 0

    while queue:
        box = queue.popleft()
        if box in opened or status[box] == 0:
            continue
        opened.add(box)
        total += candies[box]
        for key in keys[box]:
            if status[key] == 0:
                status[key] = 1
                if key in owned and key not in opened:
                    queue.append(key)
        for child in contained_boxes[box]:
            owned.add(child)
            if status[child] == 1 and child not in opened:
                queue.append(child)
    return total
