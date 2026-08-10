## General

**Turn each possible value of `k` into a direct candidate**

By definition, `word` is `k`-repeating when the string `word * k` occurs as one contiguous substring of `sequence`. The source tests that definition directly. It does not build a dynamic-programming table or a specialized string matcher; it constructs repeated candidates and uses Python’s substring-membership operation.

A candidate containing `k` copies has length `k * len(word)`. It cannot fit inside `sequence` if that length exceeds `len(sequence)`. Therefore the largest value worth testing is

`len(sequence) // len(word)`.

Integer division gives the maximum number of full word-length blocks that could physically fit. This is only a length upper bound, not a claim that the candidate actually occurs.

**Search from the largest candidate downward**

The range

`range(len(sequence) // len(word), -1, -1)`

starts at the upper bound, decreases by one, and includes zero. Python ranges exclude their stop endpoint, so using `-1` as the stop is what allows `k = 0` to be tested.

For each `k`, `word * k` constructs exactly `k` consecutive copies of `word`. The expression `candidate in sequence` asks whether those copies occur contiguously anywhere in `sequence`. Subsequence matching would not be enough; the membership operation correctly enforces the substring requirement.

The first successful candidate is returned immediately. Because values are visited in strictly descending order, every larger feasible-by-length value has already failed. The first match is therefore the maximum repeating value.

**Why the zero case guarantees a return**

If `word` does not occur even once, every positive `k` fails. At `k = 0`, Python defines `word * 0` as the empty string. The empty string is considered a substring of every string, so `'' in sequence` is true and the method returns zero.

This matches the problem’s explicit rule that the maximum value is zero when `word` is not a substring. It also means the function needs no separate return statement after the loop under the stated nonempty-input constraints.

**A trace**

For `sequence = "ababc"` and `word = "ab"`, the length upper bound is `5 // 2 = 2`. The first candidate is `"ab" * 2 = "abab"`, which occurs starting at index zero, so the function immediately returns two.

For `word = "ba"`, candidate `"baba"` fails. The next candidate `"ba"` occurs starting at index one, so the method returns one. It never needs to test zero because a larger answer has already been found.

For `word = "ac"`, `"acac"` and `"ac"` both fail. The empty candidate at zero succeeds, producing the required answer zero.

**Why the answer is correct**

Any valid `k` must be no larger than the initial floor-division bound, because otherwise its repeated string is longer than `sequence` and cannot be a substring. Thus the loop’s candidate set contains every possible answer.

At iteration `k`, the membership test is true exactly when `word` repeated `k` times is a substring, which is exactly the definition of `k`-repeating. Since candidates are tested from largest to smallest, returning the first true one returns the greatest valid `k`. If no positive candidate works, the included zero candidate returns zero. These cases cover every input.

**What this implementation does not reuse**

Candidates for neighboring values overlap heavily: `word * (k - 1)` is a prefix of `word * k`. Nevertheless, the source constructs each candidate anew and performs a new substring search. That simplicity is reasonable for the maximum sequence length of 100, but it matters when describing complexity. The manifest’s linear bound would require a different matching or dynamic-programming implementation.

## Complexity detail

Let `N = len(sequence)`, `M = len(word)`, and `K = floor(N / M)`. The loop performs at most `K + 1` iterations. Constructing `word * k` costs $O(kM)$ time and space for that iteration.

If substring membership is modeled with a linear-time string-search implementation, each check costs $O(N + kM)$. Summed over all candidates, the total is

$$
O\left(KN + M\sum_{k=0}^{K}k\right)
= O(KN + MK^2).
$$

Since `K = floor(N/M)`, this is $O(N^2/M)$ in the usual simplification, and $O(N^2)$ when `M` can be one. A naive substring comparison can have a still larger worst case, up to $O(N\cdot kM)$ per candidate on adversarial text. Python’s exact internal search algorithm is an implementation detail, so the safe point is that this repeated-search source is not generally $O(N+M)$.

Only one repeated candidate needs to exist at a time, and its length is at most `N`, so peak auxiliary space is $O(N)$. The loop index is constant space.

## Alternatives and edge cases

- **Dynamic programming by ending position:** Track how many consecutive copies of `word` end at each usable boundary. This can reuse matches and avoid constructing every repeated candidate.
- **Build upward until failure:** Repeatedly append one `word` and test membership. It is correct because if `word * k` fails, every larger repetition also fails, but it discovers the answer from the other direction.
- **KMP or another linear matcher:** Matching `word` structure against `sequence` and counting adjacent occurrences can achieve a genuinely linear-style bound, but requires careful alignment so copies are contiguous.
- **`word` longer than `sequence`:** The upper bound is zero, so the loop immediately returns zero.
- **Exact full-length repetition:** If `N` is divisible by `M` and the whole sequence equals the maximum candidate, the first test succeeds.
- **Overlapping occurrences:** The problem asks for one contiguous repeated block. Membership naturally allows that block to start anywhere; separate occurrences elsewhere do not combine.
- **Partial copy at an end:** A partial occurrence does not count because `word * k` contains only complete copies.
- **Single-character word:** The answer is the length of the longest contiguous run of that character, and the exact source discovers it by descending candidate tests.
- **Guaranteed nonempty `word`:** Division by `len(word)` is safe. An empty word would make the mathematical definition and division invalid, but the constraints exclude it.
- **Zero candidate:** Its success is intentional and implements the specified fallback, not an accidental Python trick.
