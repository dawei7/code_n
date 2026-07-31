# Encrypt and Decrypt Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2227 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Design, Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/encrypt-and-decrypt-strings/) |

## Problem Description

### Goal

Build an `Encrypter` from parallel arrays `keys` and `values` plus a dictionary of permitted plaintext words. Each character in `keys` is unique, and its corresponding value is a two-character replacement. Encrypt a plaintext by concatenating its replacements in order; if any character has no mapping, encryption fails and returns the empty string.

To decrypt an even-length ciphertext, divide it into two-character blocks. A block may correspond to more than one key because different keys can share a value, so several plaintexts may be possible. The `decrypt` operation must return how many of those possibilities occur in `dictionary`, rather than listing or choosing one of them.

### Function Contract

**Inputs**

- `operations`: A sequence beginning with `"Encrypter"` and followed by `"encrypt"` or `"decrypt"` method names.
- `arguments`: Arguments aligned with `operations`; construction receives `keys`, `values`, and `dictionary`, while each later operation receives one word.

Let $D$ be the total number of characters across `dictionary`, and let $Q$ be the total number of characters supplied to all later method calls.

The key array contains at most 26 unique lowercase letters. Every mapped value has length two, the dictionary contains at most 100 unique words of length at most 100, and at most 200 method calls follow construction.

**Return value**

Return one result per operation. Construction contributes `null`; `encrypt` contributes the mapped ciphertext or `""` when a character is unmapped; and `decrypt` contributes the number of dictionary words whose encryption equals the supplied ciphertext.

### Examples

**Example 1**

- Input: `operations = ["Encrypter", "encrypt", "decrypt"]`, with constructor arguments `keys = ["a", "b", "c", "d"]`, `values = ["ei", "zf", "ei", "am"]`, `dictionary = ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]`, followed by `"abcd"` and `"eizfeiam"`
- Output: `[null, "eizfeiam", 2]`

**Example 2**

- Input: `keys = ["a"]`, `values = ["xy"]`, `dictionary = ["a", "aa"]`; then encrypt `"aa"` and decrypt `"xy"`
- Output: `[null, "xyxy", 1]`

**Example 3**

- Input: `keys = ["a", "b"]`, `values = ["zz", "zz"]`, `dictionary = ["a", "b", "ab"]`; then decrypt `"zz"`
- Output: `[null, 2]`
