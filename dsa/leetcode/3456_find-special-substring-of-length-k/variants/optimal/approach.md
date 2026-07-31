## General

The two outside-neighbor conditions mean that a valid substring cannot be cut from the interior of a longer sequence of the same character. It must coincide with an entire maximal equal-character run. The task is therefore exactly to determine whether any such run has length `k`.

Keep the start index of the current run and scan one position beyond the final string character. A run ends when the scan reaches the string boundary or encounters a character different from the run's first character. At that moment, subtract the run start from the current index. Return `True` if the length equals `k`; otherwise begin the next run at the current index. Each run is examined once, and treating the end of the string as a boundary avoids separate final-run logic.

## Complexity detail

Let $n=\lvert s\rvert$. The scan visits every character boundary once, so it takes $O(n)$ time. It stores only the current index and run start, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Checking every length-k window:** Verifying all characters and both boundaries for every possible window is correct but can take $O(nk)$ time.
- **Character frequency counting:** Global frequencies do not describe whether equal characters are consecutive or whether a run has valid boundaries.
- **Longer uniform run:** A run of length greater than `k` contributes no valid substring because any chosen length-`k` portion touches the same character on at least one outside boundary.
- **Whole string:** When all of `s` is one run, the answer is `True` exactly when `k = n`.
- **Required length one:** A single-character run qualifies, but an individual character inside a repeated run does not.
- **First or final run:** A missing neighbor at a string boundary imposes no additional condition.
