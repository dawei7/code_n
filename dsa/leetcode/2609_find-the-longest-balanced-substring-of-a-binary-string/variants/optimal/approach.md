## General

Every nonempty balanced substring has the form $0^k1^k$ for some positive $k$. It can only cross a boundary between a maximal run of zeroes and the immediately following maximal run of ones. If those two run lengths are $z$ and $o$, the best substring using that boundary takes the last $\min(z,o)$ zeroes and the first $\min(z,o)$ ones, for length $2\min(z,o)$.

Scan `s` while storing the size of the current zero-run and the one-run that follows it. A zero seen after at least one one begins a new candidate pair, so both counters are reset before the new zero is counted. A one extends the current one-run; at that moment, $2\min(z,o)$ is the best balanced length available at this boundary and can update the global maximum.

This considers every relevant zero-to-one boundary. For each boundary it records the largest possible balanced substring crossing it, and every nonempty balanced substring crosses exactly such a boundary. The largest recorded value is therefore the required answer. If there is no suitable boundary, the maximum remains zero, representing the permitted empty substring.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. Each character is processed once, so the time complexity is $O(n)$. The scan keeps only three integer counters, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all substrings:** Checking every interval directly is correct for the small public limit, but it performs avoidable repeated work and has superlinear time complexity.
- **Store all run lengths:** Run-length encoding also exposes adjacent zero/one pairs and works in $O(n)$ time, but storing the runs uses $O(n)$ space when the counters can be maintained online.
- **Unequal adjacent runs:** Only the shorter run limits the balanced substring; extra zeroes are discarded from the left or extra ones from the right.
- **All one character:** A string containing only zeroes or only ones has no nonempty balanced substring, so the result is zero.
- **Reset after ones:** A zero following a one cannot reuse the earlier zero-run, because that would place a zero after a one inside the candidate substring.
