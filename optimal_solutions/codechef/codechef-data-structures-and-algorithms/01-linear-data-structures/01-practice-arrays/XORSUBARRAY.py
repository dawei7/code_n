


def solve():
    class Solution:
        def countSubarraysWithXOR(self, arr, k):
            freq = defaultdict(int)  # Stores count of prefix XORs
            prefix_xor = 0
            count = 0

            for num in arr:
                prefix_xor ^= num  # Current prefix XOR

                # If the prefix XOR itself equals k
                if prefix_xor == k:
                    count += 1

                # If there exists a prefix XOR that when XORed with current gives k
                count += freq[prefix_xor ^ k]

                # Store the current prefix XOR in the map
                freq[prefix_xor] += 1

            return count


if __name__ == "__main__":
    solve()
