### 1. Description

Given an initial array `arr`, every day you produce a new array using the array of the previous day.

On the `i`-th day, you do the following operations on the array of day `i-1` to produce the array of day `i`:

- If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.

- If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.

- The first and last elements never change.

After some days, the array does not change. Return that final array.

### 2. Function Contract

**Inputs**

- `arr`: The initial array of $n$ integers.

Each daily update must compare only values from the previous day. In particular, a change at position `i` cannot affect the decision for $i + 1$ until the following day. Comparisons are strict, so equality with either neighbor prevents that peak-or-valley update.

Let $C$ be the total number of individual increments and decrements performed before stabilization.

**Return value**

Return the stable array reached when a complete simultaneous day produces no changes. Positions `0` and $n - 1$ must equal their original values.

### 3. Examples

#### Example 1

- **Input:** `arr = [6,2,3,4]`
- **Output:** `[6,3,3,4]`
- **Explanation:** On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
No more operations can be done to this array.

#### Example 2

- **Input:** `arr = [1,6,3,4,3,5]`
- **Output:** `[1,4,4,4,4,5]`
- **Explanation:** On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
No more operations can be done to this array.

### 4. Constraints

- $3 \le \text{arr.length} \le 100$

- $1 \le \text{arr}[i] \le 100$
