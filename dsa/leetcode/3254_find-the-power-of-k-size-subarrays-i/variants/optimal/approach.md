## General

Let $n$ be the length of \`nums\`.

Every valid window has the same local condition at all $k-1$ internal boundaries: \`nums[j] == nums[j-1] + 1\`. Instead of checking those boundaries again for every overlapping window, maintain \`consecutive_length\`, the length of the longest valid \`+1\` run ending at the current index.

At index zero, or whenever the current value is not exactly one greater than the preceding value, reset the run length to one. Otherwise extend it by one. Once the index is at least \`k - 1\`, one complete length-$k$ window ends there. That window is valid exactly when the current run length is at least $k$.

If valid, the window is strictly ascending, so its maximum is the current and final value. Append that value; otherwise append \`-1\`.

The maintained run length is correct initially. Each new adjacent pair either extends the previous all-\`+1\` suffix or breaks it and leaves only the current element, so induction preserves its meaning. A window ending at the current index has every required boundary precisely when it lies inside a run of length at least $k$. The emitted value therefore matches the power definition for every window.

## Complexity detail

The scan performs constant work per array element, so time complexity is $O(n)$. Apart from the required result list, it stores only the current run length and loop state, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Check every window independently:** Testing all $k-1$ adjacent pairs for each start is correct but takes $O(nk)$ time.
- **Sort each window:** Sorting destroys the required original order and costs more than checking adjacency.
- **Track a sliding maximum:** The maximum alone cannot establish that every value rises by exactly one.
- For $k=1$, every one-element window is valid and its sole element is its power.
- Equal adjacent values break a run.
- A positive jump larger than one is not consecutive and breaks a run.
- Any decrease breaks a run.
- When $k=n$, exactly one power is returned.
- A valid run longer than $k$ makes each overlapping length-$k$ window valid.
- The output excludes partial windows before index \`k - 1\`.
