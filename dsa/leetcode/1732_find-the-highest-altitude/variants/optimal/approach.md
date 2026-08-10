## General

**Altitude is a running sum of gains**

The biker begins at altitude zero. After the first road segment, the altitude is `gain[0]`. After two segments, it is `gain[0] + gain[1]`. In general, the altitude at point $r$ is the prefix sum of the first $r$ gains.

Because $n$ gains connect $n+1$ points, the complete altitude sequence is

$$
0,\quad
\texttt{gain}[0],\quad
\texttt{gain}[0]+\texttt{gain}[1],\quad\ldots
$$

The requested answer is the maximum value in exactly this sequence.

**Generate prefix sums lazily**

`accumulate(gain, initial=0)` produces an iterator. It first yields the supplied initial value zero, then successively adds each gain and yields the new running total.

Including `initial=0` is essential. The starting point is a real point on the journey and can be the highest altitude, especially when every later prefix sum is negative.

Without the initial value, `accumulate(gain)` would begin after the first movement and could incorrectly miss altitude zero.

**Let max consume the altitude stream**

`max(...)` reads every yielded altitude and retains the greatest. The exact source composes the two operations:

`return max(accumulate(gain, initial=0))`.

No list of all altitudes is created. The prefix sums exist one at a time as the iterator advances.

**Trace the first example**

For `gain = [-5,1,5,0,-7]`, accumulation yields:

- zero at the start,
- negative five after the first segment,
- negative four,
- one,
- one again,
- negative six.

The maximum is one.

The repeated altitude one is not a problem; the question asks for the value, not how many points reach it or which point appears first.

**Trace the all-below-start pattern**

For `[-4,-3,-2,-1,4,3,2]`, every nonempty prefix sum remains negative. Because the iterator begins with zero, `max` returns zero.

An implementation that initialized the maximum to the first gain would incorrectly return a negative altitude even though the biker started higher.

**Why gains can be negative or zero**

A negative gain decreases the running altitude, a positive gain increases it, and zero preserves it. Ordinary integer addition models all three cases.

The algorithm does not assume the running total is monotonic. `max` compares every prefix independently, so a later recovery after a descent is handled naturally.

**Why the method is correct**

Let $A_r$ be the altitude at point $r$. The starting condition gives $A_0=0$. For each segment $i$,

$$
A_{i+1}=A_i+\texttt{gain}[i].
$$

The iterator begins with $A_0$. If its latest yielded value is $A_i$, adding the next gain yields $A_{i+1}$. By induction, it yields every point altitude in order and no other values.

`max` over that exact set is, by definition, the highest altitude reached. Therefore the returned value is correct.

**Why one expression remains readable when its roles are understood**

Although the implementation is one line, it contains two conceptually distinct stages:

- `accumulate` reconstructs point altitudes from changes.
- `max` performs the requested extremum selection.

Recognizing these stages prevents the common mistake of treating `gain` values themselves as altitudes. A large positive individual gain is not necessarily the highest point if it begins from a deeply negative current altitude.

**No final altitude special case is needed**

The last running sum is yielded after the final gain, so the destination point participates in `max` exactly like every intermediate point.

Likewise, the first point participates through `initial=0`. The iterator's endpoints line up with all $n+1$ physical points.

## Complexity detail

Let $n$ be `len(gain)`. `accumulate` processes every gain once, and `max` consumes each of the $n+1$ yielded altitudes once. Total time is $O(n)$.

The iterator stores only its current total, while `max` stores only the current greatest value. Auxiliary space is $O(1)$, matching the manifest. The input list is not modified.

Python integers avoid overflow for the bounded total altitude. Iterator construction itself is constant-space.

## Alternatives and edge cases

- **Explicit loop:** Track `current += gain[i]` and `best = max(best,current)`. It has identical $O(n)$ time and $O(1)$ space and may be easier to debug.
- **Build a prefix-sum list:** It makes every altitude inspectable but uses $O(n)$ extra space unnecessarily.
- **Take max of gain values:** This is incorrect because gains are changes, not absolute altitudes.
- **All negative gains:** The starting altitude zero remains the answer.
- **All positive gains:** The final prefix sum is the maximum.
- **Zero gains:** They repeat the current altitude and cause no special behavior.
- **Highest point occurs multiple times:** `max` returns its value once, as required.
- **Highest at start:** `initial=0` preserves it.
- **Highest at destination:** The final accumulated sum is included.
- **Single gain:** The answer is the larger of zero and that gain.
- **Input preservation:** Lazy accumulation reads `gain` without changing it.
- **Iterator behavior:** It is consumed once by `max`; no second traversal is needed.
- **Prefix meaning:** After consuming gain `i`, the accumulated value is the altitude at point `i + 1`, so the iterator covers every visited point exactly once.
