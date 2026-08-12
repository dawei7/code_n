# XOR Decryption - Optimal Approach

## Algorithm Explanation

Decrypt a cyclic 3-byte XOR encrypted ASCII message in `cipher.txt` where the password consists of three lowercase letters `[a-z]^3`.

### Search Strategy:
1. Iterate over all $26^3 = 17576$ candidate key tuples $(k_1, k_2, k_3)$ where $k_i \in [\text{'a'}, \dots, \text{'z'}]$.
2. Decrypt message using XOR: `plain[i] = cipher[i] ^ key[i % 3]`.
3. Test if the decrypted plain-text string contains common English word markers (`" the "`, `" of "`, `" and "`).
4. Upon locating the unique valid English decryption, compute and return `sum(plain)`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(26^3 \cdot L)$ where $L = 1201$ bytes. Runs in $< 0.1\text{s}$.
- **Space Complexity:** $\mathcal{O}(L)$ - Decrypted byte array buffer.
