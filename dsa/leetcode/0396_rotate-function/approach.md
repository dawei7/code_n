## General

**Avoid rescoring every rotation from scratch**

There are $n$ rotations, and directly computing each score touches all $n$ elements. That would take $O(n^2)$ time. Consecutive rotations are closely related, however: one value moves from the final position to the first, while every other value shifts one position to the right. Their weighted sums can therefore be updated with one formula.

The exact solution first computes two quantities from the original array:

$$
F(0)=\sum_{j=0}^{n-1}j\cdot\texttt{nums}[j]
$$

and

$$
S=\sum_{j=0}^{n-1}\texttt{nums}[j].
$$

It stores the current rotation score in `f`, the fixed total sum in `s`, and the best score seen in `ans`.

**Understand one clockwise rotation**

Moving from rotation $k-1$ to rotation $k$ takes the last value of the current arrangement and moves it to index zero.

Call that moved value $x$. Its coefficient changes from $n-1$ to zero, reducing the score by $(n-1)x$.

Every other value moves one index to the right. Each of their coefficients increases by one, so together they add the sum of all values except $x$, which is $S-x$.

The net change is therefore

$$
(S-x)-(n-1)x=S-nx.
$$

This yields the recurrence

$$
F(k)=F(k-1)+S-nx.
$$

Instead of multiplying every rotated element by its new index, the algorithm performs one addition and one multiplication.

**Which original value moves on rotation `i`**

For the first clockwise rotation, the original last element `nums[n - 1]` moves to the front. For the second rotation, the original element `nums[n - 2]` is the last element of the current arrangement and moves next. In general, transition $i$ moves

$$
x=\texttt{nums}[n-i].
$$

The exact loop runs `i` from `1` through `n - 1` and updates

```text
f = f + s - n * nums[n - i]
```

After that assignment, `f` equals $F(i)$. The method compares it with `ans`, so every rotation score is considered exactly once.

**Deriving the formula algebraically**

The initial score is

$$
F(0)=0a_0+1a_1+2a_2+\cdots+(n-1)a_{n-1}.
$$

After one clockwise rotation,

$$
F(1)=0a_{n-1}+1a_0+2a_1+\cdots+(n-1)a_{n-2}.
$$

Subtracting $F(0)$ from $F(1)$ gives one extra copy of $a_0$ through $a_{n-2}$ and removes $(n-1)$ copies of $a_{n-1}$:

$$
F(1)-F(0)
=
(a_0+\cdots+a_{n-2})-(n-1)a_{n-1}
=S-na_{n-1}.
$$

Exactly the same coefficient change occurs at every transition, with a different value $x$ moving from the end to the front. This is why one fixed total sum supports all rotations.

**Tracing `nums = [4, 3, 2, 6]`**

The length is `n = 4`, and total sum is

$$
S=4+3+2+6=15.
$$

The initial score is

$$
F(0)=0\cdot4+1\cdot3+2\cdot2+3\cdot6=25.
$$

The successive updates are:

| Rotation | Value moved to front | Recurrence | Score |
|---:|---:|---|---:|
| `0` | — | directly computed | `25` |
| `1` | `nums[3] = 6` | `25 + 15 - 4 * 6` | `16` |
| `2` | `nums[2] = 2` | `16 + 15 - 4 * 2` | `23` |
| `3` | `nums[1] = 3` | `23 + 15 - 4 * 3` | `26` |

The maximum is `26`, so that value is returned. The original `nums[0]` would move to the front on a fourth rotation, but that returns to the original arrangement. There are only `n` distinct rotations, so the loop stops after `n - 1` transitions.

**Why `ans` starts at `F(0)` rather than zero**

Array values may be negative, so every rotation score may also be negative. Initializing the maximum to zero could then return a value that no rotation achieves. Setting `ans = f` makes the first real rotation the baseline. Each later real score is compared against it.

**The loop invariant**

At the beginning of loop iteration `i`, `f` equals $F(i-1)$, `s` equals the sum of every array value, and `ans` is the maximum of $F(0)$ through $F(i-1)$.

The update uses exactly the original value that moves from the final position to the front, so the recurrence makes `f = F(i)`. Updating `ans` extends the maximum through $F(i)$. The invariant therefore holds for the next iteration.

After the loop, all scores $F(0)$ through $F(n-1)$ have been included. `ans` is exactly their maximum.

## Complexity detail

Computing $F(0)$ with the generator expression visits all $n$ elements. Computing `sum(nums)` visits them again. The rotation loop performs $n-1$ constant-time updates. These three linear passes give total time $O(n)$.

Only `f`, `n`, `s`, `ans`, and the loop index are stored. The generator used by `sum` produces one product at a time instead of materializing a list, so auxiliary space is $O(1)$. The input array is not modified and no rotated copies are created.

The statement guarantees that the answer fits in a 32-bit integer. Python also represents intermediate sums without fixed-width overflow. In another language, it is prudent to calculate products and totals in a sufficiently wide integer type even if the final answer is bounded.

## Alternatives and edge cases

- **Construct every rotated array:** Rotating and rescoring each arrangement costs $O(n^2)$ time and may allocate $O(n)$ temporary space. The recurrence captures the same coefficient changes directly.

- **Rescore without constructing rotations:** Modular indexing avoids copies but still performs $n$ weighted additions for each of $n$ rotations, so time remains quadratic.

- **Prefix-sum derivation:** One can derive rotation scores through prefix sums, but the total-sum recurrence is simpler and uses less state.

- **One-element array:** `F(0) = 0 * nums[0] = 0`. The rotation loop is empty, and the exact method returns zero.

- **All values equal:** Every rotation has the same score because rotation changes no value placement relative to unequal values. The recurrence’s `S - n*x` becomes zero at each step.

- **All scores negative:** Initializing `ans` from the actual first score ensures the greatest negative score is returned rather than an invalid zero.

- **Negative array values:** The algebra uses ordinary addition and multiplication and does not assume nonnegative values.

- **Repeated values:** The formula depends on the moved occurrence’s value, not uniqueness. Equal values require no special handling.

- **Clockwise direction:** The index `nums[n - i]` follows the element moved from the end to the front. A counterclockwise rotation would have a different recurrence and moved index.

- **Exactly `n` rotations:** Rotation zero plus `n - 1` updates covers every distinct configuration. The next update would repeat rotation zero.

- **Output-size independence:** Unlike algorithms that construct rotations, memory does not grow with the number of scores considered because only the current score and maximum are retained.
