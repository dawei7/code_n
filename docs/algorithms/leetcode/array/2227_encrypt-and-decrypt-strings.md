# Encrypt and Decrypt Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2227 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Design, Trie |
| Official Link | [encrypt-and-decrypt-strings](https://leetcode.com/problems/encrypt-and-decrypt-strings/) |

## Problem Description & Examples
### Goal
Design an encrypter from a character-to-string mapping and a dictionary. Encryption replaces every character and concatenates the mapped strings. Decryption reports how many dictionary words encrypt to a supplied ciphertext; it does not need to reconstruct those words.

### Function Contract
**Inputs**

- Constructor inputs `keys` and `values` define corresponding character mappings, and `dictionary` lists valid plaintext words.
- `encrypt(word1)` receives a plaintext word.
- `decrypt(word2)` receives an encrypted string.

**Return value**

`encrypt` returns the mapped ciphertext, or an empty string if a character has no mapping. `decrypt` returns the number of dictionary entries whose encryption exactly equals its input.

### Examples
**Example 1**

- Input: `keys = ["a", "b", "c", "d"]`, `values = ["ei", "zf", "ei", "am"]`, `dictionary = ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]`; operation: `encrypt("abcd")`
- Output: `"eizfeiam"`

**Example 2**

- Input: the same encrypter; operation: `decrypt("eizfeiam")`
- Output: `2`

**Example 3**

- Input: `keys = ["a"]`, `values = ["xy"]`, `dictionary = ["a", "aa"]`; operations: `encrypt("aa")`, `decrypt("xy")`
- Output: `"xyxy"`, then `1`

---

## Underlying Base Algorithm(s)
Store the direct character mapping for encryption. During construction, encrypt every dictionary word and count the resulting ciphertexts in a hash map. Encryption is a linear mapping pass; decryption becomes one hash lookup. Counting encrypted dictionary forms also naturally handles different words that collide to the same ciphertext.

---

## Complexity Analysis
- **Time Complexity**: construction is `O(D)`, where `D` is the total dictionary characters; `encrypt` is `O(length(word1))`; `decrypt` is `O(length(word2))` for hashing
- **Space Complexity**: `O(D)`
