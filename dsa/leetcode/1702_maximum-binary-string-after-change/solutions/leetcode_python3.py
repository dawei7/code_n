class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        first_zero = binary.find("0")
        if first_zero == -1:
            return binary

        zero_count = binary.count("0")
        remaining_zero = first_zero + zero_count - 1
        return "1" * remaining_zero + "0" + "1" * (len(binary) - remaining_zero - 1)
