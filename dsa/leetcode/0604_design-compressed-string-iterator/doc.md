# Design Compressed String Iterator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 604 |
| Difficulty | Easy |
| Topics | Array, String, Design, Iterator |
| Official Link | [LeetCode](https://leetcode.com/problems/design-compressed-string-iterator/) |

## Problem Description
### Goal
Design an iterator for a compressed string made of consecutive letter-and-count runs, where a positive count may contain multiple digits. The iterator must expose `next()`, which returns the next character of the expanded sequence, and `hasNext()`, which reports whether another character remains without consuming it.

Process calls in order while keeping the string compressed rather than materializing the potentially much larger expansion. Once all runs are exhausted, `hasNext()` returns `False` and every later `next()` call returns one space character. Repeated calls must preserve the remaining count within the current run before advancing to the next encoded letter.

### Function Contract
**Inputs**

- `compressedString: str`: consecutive letter-and-positive-count runs, with counts possibly containing several digits
- `operations: list[list[str]]`: app-local calls, each either `["next"]` or `["hasNext"]`

**Return value**

- A list containing each operation result in order
- `next()` returns the next expanded character, or one space character after exhaustion
- `hasNext()` reports whether another character remains without consuming it

### Examples
**Example 1**

- Input: `compressedString = "L1e2t1C1o1d1e1"`
- Output of repeated `next()` calls: the characters in `"LeetCode"`

**Example 2**

- Input: `compressedString = "a12"`
- Output: twelve `"a"` characters before exhaustion

**Example 3**

- Input: call `hasNext()` several times before `next()`
- Output: each availability check is `True`, and the next character is still unconsumed

### Required Complexity

- **Time:** $O(C + q)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Keep only the current run**

Store an index into the compressed string, the current character, and its remaining repetition count. Do not create the expanded string or a list of all runs.

**Parse a run only when needed**

When `next()` is called with no repetitions left, read the character at the compressed index, then parse all following digits into one count. Each compressed character and digit is advanced past exactly once across the iterator's lifetime.

**Consume exactly one character**

After ensuring a current run exists, decrement its remaining count and return its character. If neither a current count nor another encoded run remains, return the required space sentinel.

**Make availability checks nonconsuming**

`hasNext()` is true when the current run still has repetitions or the compressed index has not reached the end. It changes no state, so repeated checks cannot skip output.

**Why the iterator matches the expansion**

Every parsed run records exactly the encoded character and count. Each successful `next()` removes one unit from the earliest run with remaining units, so it returns characters in the same order as full run-length expansion. A new run is parsed only after its predecessor reaches zero, and exhaustion is recognized only after the final run is consumed.

#### Complexity detail

Let `C` be the compressed-string length and `q` the number of operations. Parsing advances through each of the `C` encoded characters once, while every operation does constant work apart from that amortized parsing, for $O(C + q)$ total time. The iterator stores only scalar state beyond the input, so auxiliary space is $O(1)$; the app-local result list is output space.

#### Alternatives and edge cases

- **Eagerly decompress:** makes later calls simple but can require $O(E)$ construction time and space for expanded length `E`, which may be far larger than `C`.
- **Preparse all runs:** avoids expanded storage and has the same total time, but uses $O(C)$ additional run storage.
- **One-digit count parsing:** is incorrect for runs such as `"a12"`.
- **Repeated `hasNext()`:** must not change the current run or compressed index.
- **Run boundary:** the first call after a count reaches zero loads the next encoded character.
- **Exhausted `next()`:** returns one space character on every later call.
- **Single run:** never needs to parse another character after initialization.
- **Large count:** should remain a counter rather than allocate repeated characters.

</details>
