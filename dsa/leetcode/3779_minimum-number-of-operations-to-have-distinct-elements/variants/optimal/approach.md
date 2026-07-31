## General

The only arrays that can remain are suffixes beginning at indices `0`, `3`, `6`, and so on. Scan from right to left while recording the values in the suffix. Until a duplicate is encountered, the scanned suffix is distinct and would be a valid stopping state.

Suppose the first right-to-left duplicate is found at index `i`. Every suffix beginning at or before `i` contains that occurrence and its already-seen copy, so none is valid. The suffix beginning just after `i` is distinct by construction. We therefore need to remove at least `i + 1` elements, and the fixed operation removes them in groups of three. The exact answer is

$$
\left\lceil\frac{i+1}{3}\right\rceil
=\left\lfloor\frac{i}{3}\right\rfloor+1.
$$

If the reverse scan reaches the start without a duplicate, the original array already satisfies the stopping condition and the answer is zero.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Each element is inspected at most once, giving $O(N)$ expected time with a hash set and $O(N)$ auxiliary space in the worst case.

## Alternatives and edge cases

- **Frequency countdown:** Count all values once, then remove at most three elements per operation while tracking how many frequencies exceed one. This is also expected $O(N)$ time, but carries more state than the reverse suffix scan.
- **Repeated distinctness checks:** Rebuilding a set after every three-element removal is correct but can take $O(N^2)$ total time.
- **Initially distinct:** No operation is allowed or needed once the stopping condition already holds, so return `0`.
- **Fewer than three elements:** If such an array contains a duplicate, its first operation removes the entire array.
- **Duplicate across a removed boundary:** Only the surviving suffix matters after an operation; a removed copy cannot keep a later value duplicated.
- **Final one-element suffix:** A single remaining value is distinct and stops the process without another operation.
