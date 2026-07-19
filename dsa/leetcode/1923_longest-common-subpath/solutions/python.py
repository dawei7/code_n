def solve(n: int, paths: list[list[int]]) -> int:
    del n
    ordered_paths = sorted(paths, key=len)
    base = 100_003
    modulus_one = 1_000_000_007
    modulus_two = 1_000_000_009

    def hashes(path: list[int], length: int) -> set[tuple[int, int]]:
        if length == 0:
            return {(0, 0)}

        power_one = pow(base, length, modulus_one)
        power_two = pow(base, length, modulus_two)
        hash_one = 0
        hash_two = 0
        for value in path[:length]:
            encoded = value + 1
            hash_one = (hash_one * base + encoded) % modulus_one
            hash_two = (hash_two * base + encoded) % modulus_two

        result = {(hash_one, hash_two)}
        for right in range(length, len(path)):
            outgoing = path[right - length] + 1
            incoming = path[right] + 1
            hash_one = (
                hash_one * base + incoming - outgoing * power_one
            ) % modulus_one
            hash_two = (
                hash_two * base + incoming - outgoing * power_two
            ) % modulus_two
            result.add((hash_one, hash_two))
        return result

    def shared(length: int) -> bool:
        common = hashes(ordered_paths[0], length)
        for path in ordered_paths[1:]:
            common.intersection_update(hashes(path, length))
            if not common:
                return False
        return True

    low = 0
    high = len(ordered_paths[0])
    while low < high:
        middle = (low + high + 1) // 2
        if shared(middle):
            low = middle
        else:
            high = middle - 1
    return low
