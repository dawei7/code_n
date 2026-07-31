def solve(prevRoom: list[int]) -> int:
    modulus = 1_000_000_007
    room_count = len(prevRoom)
    children = [[] for _ in range(room_count)]
    for room in range(1, room_count):
        children[prevRoom[room]].append(room)

    order = [0]
    for room in order:
        order.extend(children[room])

    subtree_size = [1] * room_count
    for room in reversed(order[1:]):
        subtree_size[prevRoom[room]] += subtree_size[room]

    factorial = 1
    subtree_product = 1
    for value in range(1, room_count + 1):
        factorial = factorial * value % modulus
    for size in subtree_size:
        subtree_product = subtree_product * size % modulus

    return factorial * pow(subtree_product, modulus - 2, modulus) % modulus
