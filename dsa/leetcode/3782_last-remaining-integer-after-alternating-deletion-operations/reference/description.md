### 1. Description

You are given an integer `n`.

We write the integers from 1 to `n` in a sequence from left to right. Then, **alternately** apply the following two operations until only one integer remains, starting with operation 1:

- **Operation 1**: Starting from the left, delete every second number.

- **Operation 2**: Starting from the right, delete every second number.

Return the last remaining integer.

### 2. Function Contract

**Inputs**

- `n`: The positive upper endpoint of the initial integer sequence.

The initial sequence is `[1, 2, ..., n]`. A sweep keeps the first number visited from its starting side, deletes the next one, and continues alternating keep/delete decisions across the entire current sequence. The sweep direction changes after every operation, beginning from the left.

**Return value**

Return the sole integer left after all alternating deletion operations finish.

### 3. Examples

#### Example 1

- **Input:** n = 8

- **Output:** 3

- **Explanation:** 

- Write `[1, 2, 3, 4, 5, 6, 7, 8]` in a sequence.

- Starting from the left, we delete every second number: `[1, <u>**2**</u>, 3, <u>**4**</u>, 5, <u>**6**</u>, 7, <u>**8**</u>]`. The remaining integers are `[1, 3, 5, 7]`.

- Starting from the right, we delete every second number: `[<u>**1**</u>, 3, <u>**5**</u>, 7]`. The remaining integers are `[3, 7]`.

- Starting from the left, we delete every second number: `[3, <u>**7**</u>]`. The remaining integer is `[3]`.

#### Example 2

- **Input:** n = 5

- **Output:** 1

- **Explanation:** 

- Write `[1, 2, 3, 4, 5]` in a sequence.

- Starting from the left, we delete every second number: `[1, <u>**2**</u>, 3, <u>**4**</u>, 5]`. The remaining integers are `[1, 3, 5]`.

- Starting from the right, we delete every second number: `[1, <u>**3**</u>, 5]`. The remaining integers are `[1, 5]`.

- Starting from the left, we delete every second number: `[1, <u>**5**</u>]`. The remaining integer is `[1]`.

#### Example 3

- **Input:** n = 1

- **Output:** 1

- **Explanation:** 

- Write `[1]` in a sequence.

- The last remaining integer is 1.

### 4. Constraints

- $1 \le n \le 10^{15}$
