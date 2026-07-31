from heapq import heappop, heappush


def solve(n: int, m: int) -> int:
    digit_count = len(str(n))
    limit = 10**digit_count
    lower_bound = 0 if digit_count == 1 else limit // 10

    is_prime = bytearray(b"\x01") * limit
    is_prime[0:2] = b"\x00\x00"
    for value in range(2, int(limit**0.5) + 1):
        if is_prime[value]:
            start = value * value
            count = (limit - 1 - start) // value + 1
            is_prime[start:limit:value] = b"\x00" * count

    if is_prime[n] or is_prime[m]:
        return -1

    distances = [10**18] * limit
    distances[n] = n
    queue = [(n, n)]

    while queue:
        cost, value = heappop(queue)
        if cost != distances[value]:
            continue
        if value == m:
            return cost

        place = 1
        for _ in range(digit_count):
            digit = value // place % 10

            if digit < 9:
                neighbor = value + place
                if not is_prime[neighbor]:
                    next_cost = cost + neighbor
                    if next_cost < distances[neighbor]:
                        distances[neighbor] = next_cost
                        heappush(queue, (next_cost, neighbor))

            if digit > 0:
                neighbor = value - place
                if neighbor >= lower_bound and not is_prime[neighbor]:
                    next_cost = cost + neighbor
                    if next_cost < distances[neighbor]:
                        distances[neighbor] = next_cost
                        heappush(queue, (next_cost, neighbor))

            place *= 10

    return -1
