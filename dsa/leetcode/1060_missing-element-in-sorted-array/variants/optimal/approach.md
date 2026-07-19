## General
**Count omissions at an index:** If no values were missing, the value at index `i` would be `nums[0] + i`. Therefore define

$$
M(i)=\texttt{nums[i]}-\texttt{nums[0]}-i,
$$

the number of missing integers strictly between the first element and `nums[i]`. Because `nums` is ascending with unique elements, $M(i)$ is non-decreasing.

**Handle the suffix beyond the array:** Compute `M(n - 1)`. If it is smaller than `k`, every internal gap is exhausted. The remaining `k - M(n - 1)` missing values continue consecutively after `nums[-1]`, so add that remainder to the last value.

**Locate the containing gap:** Otherwise, binary-search for the first index `right` satisfying $M(\texttt{right}) \ge k$. The requested value lies after `nums[right - 1]`. Exactly $M(\texttt{right}-1)$ missing numbers precede or end at that earlier position, so advance by `k - M(right - 1)` from `nums[right - 1]`.

The monotonic count makes the binary-search boundary well-defined. At that boundary, fewer than `k` omissions occur before the left endpoint but at least `k` occur before the right endpoint, placing the requested missing integer in exactly that gap. The final offset counts only the omissions still needed.

## Complexity detail
Each value of $M(i)$ is computed in constant time. Binary search performs $O(\log N)$ such evaluations and uses only index variables, giving $O(\log N)$ time and $O(1)$ auxiliary space. The suffix case is also constant time.

## Alternatives and edge cases
- **Linear gap scan:** Subtract each gap's missing count until locating the answer. It uses $O(1)$ space but takes $O(N)$ time in the worst case.
- **Hash-set enumeration:** Increment integers and test membership, but time depends on `k` and can be enormous when the answer lies far beyond the array.
- **Single-element array:** No internal gap exists, so the answer is `nums[0] + k`.
- **Consecutive array:** Since $M(n-1)=0$, every requested missing number lies after the last element.
- **Answer at a gap boundary:** Searching for the first count at least `k` correctly returns the last missing value immediately before that array element.
- **Large `k`:** Arithmetic suffix handling avoids iterating up to the requested missing position.
