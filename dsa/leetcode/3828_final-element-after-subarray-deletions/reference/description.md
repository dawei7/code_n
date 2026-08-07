## Description

You are given an integer array `nums`.

Two players, Alice and Bob, play a game in turns, with Alice playing first.

- In each turn, the current player chooses any **subarray** `nums[l..r]` such that $r - l + 1 < m$, where `m` is the **current length** of the array.

- The selected **subarray is removed**, and the remaining elements are **concatenated** to form the new array.

- The game continues until **only one** element remains.

Alice aims to **maximize** the final element, while Bob aims to **minimize** it. Assuming both play optimally, return the value of the final remaining element.
### Function Contract

**Inputs**

- `nums`: The integer array on which Alice and Bob play the deletion game.

Let $N = \lvert\texttt{nums}\rvert$ be the initial array length.

Every move acts on the current array: it removes one nonempty, proper, contiguous subarray. Elements outside that block keep their relative order when they are joined together. Alice moves first, and both players choose optimally for their opposing objectives.

**Return value**

Return the value of the sole remaining element when Alice maximizes the outcome and Bob minimizes it.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,5,2]

**Output:** 2

**Explanation:**

One valid optimal strategy:

- Alice removes `[1]`, array becomes `[5, 2]`.

- Bob removes `[5]`, array becomes `[2]`​​​​​​​. Thus, the answer is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,7]

**Output:** 7

**Explanation:**

Alice removes `[3]`, leaving the array `[7]`. Since Bob cannot play a turn now, the answer is 7.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$