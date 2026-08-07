### 1. Description

You have a list `arr` of all integers in the range `[1, n]` sorted in a strictly increasing order. Apply the following algorithm on `arr`:

- Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

- Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.

- Keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Given the integer `n`, return *the last number that remains in* `arr`.

### 2. Function Contract

**Inputs**

- `n`: The positive inclusive upper bound of the initial sequence.

**Return value**

Return the sole integer left after alternating left-to-right and right-to-left elimination passes.

### 3. Examples

#### Example 1

- **Input:** $n = 9$
- **Output:** `6`
- **Explanation:**
arr = [<u>1</u>, 2, <u>3</u>, 4, <u>5</u>, 6, <u>7</u>, 8, <u>9</u>]
arr = [2, <u>4</u>, 6, <u>8</u>]
arr = [<u>2</u>, 6]
arr = [6]
#### Example 2

- **Input:** $n = 1$
- **Output:** `1`

### 4. Constraints

- $1 \le n \le 10^{9}$