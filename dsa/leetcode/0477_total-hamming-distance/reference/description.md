### 1. Description

The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.

Given an integer array `nums`, return *the sum of **Hamming distances** between all the pairs of the integers in* `nums`.

### 2. Function Contract

**Inputs**

- `nums`: the nonempty array of nonnegative integers

**Return value**

- Return the sum, over every unordered pair of distinct array positions, of the number of binary bit positions where
  the two values differ.

Equal values at different positions still form a pair, although their mutual contribution is zero.

### 3. Examples

#### Example 1

- **Input:** `nums = [4,14,2]`
- **Output:** `6`
- **Explanation:** In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

#### Example 2

- **Input:** `nums = [4,14,4]`
- **Output:** `4`

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $0 \le \text{nums}[i] \le 10^{9}$

- The answer for the given input will fit in a **32-bit** integer.
