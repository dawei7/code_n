## General

**Think about what remains outside the replaced window**

Let \(n\) be the string length and \(q=n/4\). A balanced result needs exactly \(q\) copies of each of `Q`, `W`, `E`, and `R`.

Suppose a window is selected for replacement. Characters outside that window cannot be changed. Therefore, the window is usable exactly when no outside character count exceeds \(q\). If an outside count were already too large, replacing only the window could not remove the excess.

Conversely, if every outside count is at most \(q\), the replacement can supply each character’s deficit. The outside contains \(n-L\) characters for a window of length \(L\), so the sum of the four deficits is

\[
4q-(n-L)=L.
\]

Exactly \(L\) replacement positions are available, so all deficits can be filled. Thus “every outside count is at most \(q\)” is both necessary and sufficient.

This converts the problem into finding the shortest window whose removal leaves acceptable outside counts.

**The counter changes meaning as the window grows**

`cnt = Counter(s)` initially counts the entire string. The early check returns zero if all stored counts are at most \(q\). Since the four total counts sum to \(n=4q\), none can be below \(q\) unless another is above it; therefore, this condition means the string is already exactly balanced.

During the main loop, `cnt` represents characters outside the current window. The right boundary is `i`. Before testing, `cnt[c] -= 1` removes `s[i]` from the outside and places it inside the candidate replacement window `s[j:i+1]`.

The condition

`all(v <= n // 4 for v in cnt.values())`

then asks whether every outside count is within its allowed quota. A character absent from the `Counter` has count zero and is automatically safe; checking stored values is sufficient because the input alphabet has only four possibilities.

**Shrink every feasible window from the left**

When the outside is valid, the current window can be replaced successfully. The code records its length `i - j + 1` and then tries to make it shorter:

- `cnt[s[j]] += 1` moves the leftmost window character back outside;
- `j += 1` advances the left boundary.

The while loop continues while the outside remains valid. The moment adding a left character back makes some outside count exceed \(q\), further shrinking would not restore validity, because outside counts only increase as `j` advances. The algorithm then waits for the outer loop to expand the right boundary and remove more characters from outside.

**Why two pointers find the minimum**

For each right boundary `i`, the while loop examines all feasible left-boundary contractions until reaching the first infeasible one. Therefore, it finds the shortest feasible window ending at that `i`. Taking the minimum over every right boundary yields the global shortest window.

Neither pointer ever moves backward. The right pointer visits each character once. The left pointer crosses each character at most once across all while-loop executions, which is why nested syntax still gives linear total movement.

**Following `"QQQW"`**

Here \(n=4\) and \(q=1\). Whole-string counts are three `Q` and one `W`, so two excess `Q` characters must be inside the replacement window.

As the right boundary passes the first `Q`, the outside still has two `Q` characters and is invalid. After it passes the second `Q`, outside counts are `Q:1` and `W:1`, all within quota. The window `"QQ"` has length two and can be replaced by `"ER"`.

Trying to move the left boundary returns one `Q` outside, raising its count to two and breaking feasibility. Thus two is the minimum for that ending point and, ultimately, for the string.

**Why the early return is correct**

If the original outside, meaning the whole string when no window is selected, already has every count at most \(q\), total-count equality forces every character count to equal \(q\). No replacement is needed, and zero is the smallest possible length.


A window is feasible exactly when the counter of characters outside it has no value above \(q\). The outer update and left-shrink update maintain that counter exactly. For each right endpoint, the while loop records every feasible shrinking step and stops only when no shorter window with that endpoint can be feasible. Since all endpoints are processed, `ans` becomes the minimum feasible length. By the feasibility equivalence, this is exactly the minimum replaceable substring length.

## Complexity detail

Let \(n=\lvert\texttt{s}\rvert\). Building the counter takes \(O(n)\). The right pointer moves \(n\) times and the left pointer at most \(n\) times. Each `all` call examines at most four counter values, a constant, so total time is \(O(n)\).

The counter contains at most four keys, and all other variables are scalars. Auxiliary space is \(O(1)\), independent of \(n\). The input string is not modified and no substrings are created by the algorithm.

## Alternatives and edge cases

- **Binary search on window length:** Test whether any window of a chosen length covers all excess counts. It works but costs \(O(n\log n)\), while the sliding window obtains the minimum directly in \(O(n)\).
- **Track only excess counts:** Compute how many copies above \(q\) each character has and find the shortest window covering those excesses. This is equivalent but requires a second vocabulary of counts.
- **Already balanced string:** The early condition returns zero before entering the sliding window.
- **One-character replacement:** A string such as `"QQWE"` needs one excess `Q` replaced by `R`; the window contracts to length one.
- **All one character:** A large window must contain enough excess copies to leave at most \(q\) outside.
- **Missing character key:** `Counter` may omit a letter not present in `s`. Its outside count is zero, which already satisfies the quota.
- **Window replacement contents:** The algorithm returns only length. Deficit counts determine a valid replacement, but constructing it is unnecessary.
- **Length divisible by four:** The quota \(n/4\) is integral by contract. Without this guarantee, the definition of balanced would need reconsideration.
- **Positive window length during the loop:** `j <= i` prevents shrinking past an empty window. The only valid zero-length case is handled by the early return.
- **Fixed alphabet:** Treating `all(cnt.values())` as constant time relies on the four-character alphabet.
