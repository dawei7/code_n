def solve(s: str) -> list[int]:
    last_position = {character: index for index, character in enumerate(s)}
    partitions = []
    partition_start = 0
    partition_end = 0

    for index, character in enumerate(s):
        partition_end = max(partition_end, last_position[character])
        if index == partition_end:
            partitions.append(index - partition_start + 1)
            partition_start = index + 1

    return partitions
