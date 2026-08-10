## General

**End removals leave one contiguous middle substring**

Any sequence of taking characters from the left and right removes a prefix and a suffix. Everything not taken lies between them as one contiguous middle window.

Instead of minimizing how many characters are taken, maximize how many can safely remain in that middle window. If the longest removable-from-consideration middle has length `mx`, then the number taken is

`len(s)-mx`.

This complement view converts many choices of left and right removals into a standard longest-valid-window problem.

**What makes a middle window valid**

`cnt` initially stores the total count of each character in `s`. During the sliding-window scan, it is repurposed to represent counts outside the current middle window.

When right endpoint `i` includes character `c` in the window, the code performs `cnt[c]-=1`. That character is now left behind rather than taken.

The window is valid exactly when the outside portion still contains at least `k` copies of `a`, `b`, and `c`. Those outside characters can be taken from the two ends because they form the prefix and suffix complementary to the window.

**Reject globally impossible input first**

Before forming a window, the algorithm checks whether any total character count is below `k`. If so, even taking the whole string cannot obtain enough of that character, and `-1` is unavoidable.

This check also establishes the invariant that the empty middle window is valid before scanning begins.

**Expand right and shrink only when necessary**

`j` is the left endpoint of the current middle window. For every new character `c=s[i]`, its outside count decreases.

At the end of the previous iteration, every outside count was at least `k`. Including the new right character changes only `cnt[c]`, so only that character can newly violate the requirement. This is why the loop condition checks `cnt[c]<k` rather than scanning all three counts repeatedly.

While deficient, the code removes `s[j]` from the middle window, returning it to the taken outside portion:

`cnt[s[j]] += 1`.

It then increments `j`. Shrinking continues until `cnt[c]` returns to at least `k`. Counts of other characters only increase while shrinking and therefore remain valid.

**Why this produces the longest valid window ending at `i`**

The right endpoint is fixed during the inner loop. `j` advances only as much as required to restore validity. Any smaller left endpoint would include additional characters and still leave too few copies of `c` outside. The resulting `j` is therefore the earliest valid start and gives the longest valid window ending at `i`.

Taking the maximum of `i-j+1` across all endpoints finds the globally longest middle substring that can remain.

**Translate the window back into actual moves**

For final window `s[j..i]`, take the prefix of length `j` from the left and the suffix after `i` from the right. Their total length is

$$
j+(n-i-1)=n-(i-j+1).
$$

The maintained outside counts prove those taken characters include at least `k` of each letter. Thus every valid window yields a feasible sequence of exactly its complement length.

Conversely, every feasible removal sequence leaves some contiguous middle window whose outside counts meet the requirement. The algorithm considers that window's right endpoint and retains a window at least as long. Therefore, no removal sequence can use fewer than `n-mx` characters.

The feasible construction and lower bound establish optimality.

**Trace the state conceptually**

For `s="aabaaaacaabc"` and `k=2`, total counts are sufficient. As the right endpoint grows, `cnt` describes what would still be taken if the current window were left behind. Whenever too many copies of the new character have moved into the middle, `j` advances and restores copies to the outside.

The longest valid middle has length four, so $12-4=8$ characters must be taken, matching the sample.

**The `k=0` boundary**

No characters are required. The feasibility check passes, the inner shrink loop never runs, and the window expands to the entire string. `mx=n` and the returned number is zero.

## Complexity detail

Let $n=\lvert s\rvert$. Building the initial counter costs $O(n)$. The right pointer visits every character once. The left pointer only moves forward and advances at most $n$ times total, so the nested-looking scan is $O(n)$.

The counter has at most the three fixed keys `a`, `b`, and `c`. All other state is scalar, so auxiliary space is $O(1)$.

The input string is read without modification.

## Alternatives and edge cases

- **Enumerate prefix/suffix splits:** Testing all splits with maintained counts can also be linear but is usually more awkward.
- **Binary search the number taken:** A feasibility check is possible, but sliding window solves the complement directly.
- **Globally insufficient character:** Return `-1` before scanning windows.
- **`k=0`:** Leave the whole string and take zero minutes.
- **Empty middle window:** It represents taking the entire string and is always available after the feasibility check.
- **Only the new character can become deficient:** Previous validity makes the focused shrink condition safe.
- **Repeated shrink steps:** Each moves `j` permanently, keeping total work linear.
- **Take from both ends:** The complement of any contiguous window is exactly a prefix plus suffix.
- **At least `k`:** Extra outside copies are allowed and need not be removed from consideration.
- **Maximum middle:** Minimizing removals is exactly maximizing what remains.
