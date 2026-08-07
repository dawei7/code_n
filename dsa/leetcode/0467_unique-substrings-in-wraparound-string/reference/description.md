### 1. Description

We define the string `base` to be the infinite wraparound string of `"abcdefghijklmnopqrstuvwxyz"`, so `base` will look like this:

- `"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...."`.

Given a string `s`, return *the number of **unique non-empty substrings** of *`s`* are present in *`base`.

### 2. Function Contract

**Inputs**

- `p`: The lowercase input string called `s` in the source statement.

**Return value**

- Return the number of distinct nonempty contiguous substrings of `p` that appear in the infinite wraparound string `base`.

Equal substring text is counted once even if it occurs at multiple positions in `p`.

### 3. Examples

#### Example 1

- **Input:** `s = "a"`
- **Output:** `1`
- **Explanation:** Only the substring "a" of s is in base.
#### Example 2

- **Input:** `s = "cac"`
- **Output:** `2`
- **Explanation:** There are two substrings ("a", "c") of s in base.
#### Example 3

- **Input:** `s = "zab"`
- **Output:** `6`
- **Explanation:** There are six substrings ("z", "a", "b", "za", "ab", and "zab") of s in base.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of lowercase English letters.