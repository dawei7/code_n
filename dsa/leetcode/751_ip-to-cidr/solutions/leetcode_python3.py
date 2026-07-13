from typing import List


class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        current = 0
        for octet in ip.split("."):
            current = (current << 8) | int(octet)

        blocks = []
        remaining = n

        while remaining:
            aligned_size = current & -current
            if aligned_size == 0:
                aligned_size = 1 << 32
            remaining_size = 1 << (remaining.bit_length() - 1)
            block_size = min(aligned_size, remaining_size)
            prefix_length = 32 - (block_size.bit_length() - 1)

            address = ".".join(
                str((current >> shift) & 255) for shift in (24, 16, 8, 0)
            )
            blocks.append(f"{address}/{prefix_length}")
            current += block_size
            remaining -= block_size

        return blocks
