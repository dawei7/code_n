### 1. Description

We have an integer array `arr`, where all the integers in `arr` are equal except for one integer which is **larger** than the rest of the integers. You will not be given direct access to the array, instead, you will have an **API** `ArrayReader` which have the following functions:

- `int compareSub(int l, int r, int x, int y)`: where $0 \le l, r, x, y < \text{ArrayReader.length}()$, $l \le r and$ $x \le y$. The function compares the sum of sub-array `arr[l..r]` with the sum of the sub-array `arr[x..y]` and returns:

		<li>**1** if $\text{arr}[l]+arr[l+1]+...+\text{arr}[r] > \text{arr}[x]+arr[x+1]+...+\text{arr}[y]$.

- **0** if $\text{arr}[l]+arr[l+1]+...+\text{arr}[r] = \text{arr}[x]+arr[x+1]+...+\text{arr}[y]$.

- **-1** if $\text{arr}[l]+arr[l+1]+...+\text{arr}[r] < \text{arr}[x]+arr[x+1]+...+\text{arr}[y]$.

	</li>
- `int length()`: Returns the size of the array.

You are allowed to call `compareSub()` **20 times** at most. You can assume both functions work in `O(1)` time.

Return *the index of the array `arr` which has the largest integer*.

### 2. Function Contract

**Inputs**

- `reader`: A read-only `ArrayReader` for an array of length $N$, where $2 \leq N \leq 5 \cdot 10^5$.
- Every hidden value is an integer; exactly one value is strictly larger than all other identical values.
- `reader.length()` returns $N$ in $O(1)$ time.
- `reader.compareSub(l, r, x, y)` compares two valid inclusive subarray sums in $O(1)$ time: returns 1 if `sum(l..r) > sum(x..y)`, 0 if equal, and -1 if `sum(l..r) < sum(x..y)`.

**Return value**

Return the zero-based index of the unique larger value while making at most 20 calls to `compareSub`.

### 3. Examples

#### Example 1

- **Input:** `arr = [7,7,7,7,10,7,7,7]`
- **Output:** `4`
- **Explanation:** The following calls to the API
reader.compareSub(0, 0, 1, 1) // returns 0 this is a query comparing the sub-array (0, 0) with the sub array (1, 1), (i.e. compares arr[0] with arr[1]).
Thus we know that arr[0] and arr[1] doesn't contain the largest element.
reader.compareSub(2, 2, 3, 3) // returns 0, we can exclude arr[2] and arr[3].
reader.compareSub(4, 4, 5, 5) // returns 1, thus for sure arr[4] is the largest element in the array.
Notice that we made only 3 calls, so the answer is valid.
#### Example 2

- **Input:** `nums = [6,6,12]`
- **Output:** `2`

### 4. Constraints

- $2 \le \text{arr.length} \le 5 * 10^{5}$

- $1 \le \text{arr}[i] \le 100$

- All elements of `arr` are equal except for one element which is larger than all other elements.

**Follow up:**

- What if there are two numbers in `arr` that are bigger than all other numbers?

- What if there is one number that is bigger than other numbers and one number that is smaller than other numbers?