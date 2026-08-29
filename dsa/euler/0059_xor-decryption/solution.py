import itertools
import os


def solve(filepath: str = "") -> int:
    """Decrypt the message using a 3-character lowercase key and find the sum of ASCII values of the original text.

    Mathematical Principles Applied:
    1. Bitwise XOR Decryption:
       Let C_i be the ciphertext byte and K_{i mod 3} be the key byte.
       By XOR self-inversion: P_i = C_i ^ K_{i mod 3}.

    2. Key Space Brute Force:
       The key consists of 3 lowercase English letters ('a'..'z').
       Key space size = 26^3 = 17,576 combinations.

    3. English Language Frequency Filter:
       Valid English plaintext contains high-frequency words such as " the ", " of ", " and ".
       First key matching all three word filters yields the decrypted message.

    Time Complexity: O(26^3 * L) where L ≈ 1200 bytes (executes in ~0.03s).
    Space Complexity: O(L) memory for plaintext byte array.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0059_xor-decryption/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "cipher.txt")

    # Read cipher text file
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Parse comma-separated ciphertext byte integers
    cipher = [int(x) for x in text.strip().split(",") if x.strip()]

    # ASCII code range for lowercase letters 'a'..'z' (97..122)
    alphabet = range(ord("a"), ord("z") + 1)

    # Search all 26^3 = 17,576 3-letter key combinations
    for key in itertools.product(alphabet, repeat=3):
        # Decrypt byte array using XOR with cyclic key
        plain = [b ^ key[i % 3] for i, b in enumerate(cipher)]

        # Convert decrypted bytes to ASCII character string
        decoded = "".join(chr(c) for c in plain)

        # Heuristic filter for common English words
        if " the " in decoded and " of " in decoded and " and " in decoded:
            # Return sum of ASCII values of decrypted plaintext
            return sum(plain)

    return -1


if __name__ == "__main__":
    print(solve())
