### 1. Description

There are `n` persons on a social media website. You are given an integer array `ages` where $\text{ages}[i]$ is the age of the $i^{\text{th}}$ person.

A Person `x` will not send a friend request to a person `y` ($x \neq y$) if any of the following conditions is true:

- $\text{age}[y] \le 0.5 * \text{age}[x] + 7$

- $\text{age}[y] > \text{age}[x]$

- $\text{age}[y] > 100 \&\& \text{age}[x] < 100$

Otherwise, `x` will send a friend request to `y`.

Note that if `x` sends a request to `y`, `y` will not necessarily send a request to `x`. Also, a person will not send a friend request to themself.

Return *the total number of friend requests made*.

### 2. Function Contract

**Inputs**

- `ages`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $ages = [16,16]$
- **Output:** `2`
- **Explanation:** 2 people friend request each other.

#### Example 2

- **Input:** $ages = [16,17,18]$
- **Output:** `2`
- **Explanation:** Friend requests are made 17 -> 16, 18 -> 17.

#### Example 3

- **Input:** $ages = [20,30,100,110,120]$
- **Output:** `3`
- **Explanation:** Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

### 4. Constraints

- $n = \text{ages.length}$

- $1 \le n \le 2 * 10^{4}$

- $1 \le \text{ages}[i] \le 120$
