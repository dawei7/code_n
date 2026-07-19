## General
**Only three positions can identify the answer.** A contiguous block occupying more than one quarter of an array must cover at least one of the indices $\lfloor n/4 \rfloor$, $\lfloor n/2 \rfloor$, or $\lfloor 3n/4 \rfloor$. Otherwise the block would fit entirely within one of the four gaps separated by those positions and could not contain more than $n/4$ elements.

Take the values at those three indices as the only candidates. For each candidate, use binary search to find its first and first-after-last positions. Their difference is its exact frequency. Return the candidate when four times that frequency exceeds $n$. The guaranteed special value covers a sampled quartile position and passes this test; no other candidate can pass because the problem promises exactly one over-quarter value.

## Complexity detail
There are at most three candidates. Two binary searches per candidate take $O(\log n)$ time, while candidate storage and boundary indices use $O(1)$ auxiliary space. No scan or frequency table proportional to $n$ is required.

## Alternatives and edge cases
- **Linear run count:** Scan adjacent equal values and track each run's length. This is simple and uses $O(1)$ space, but takes $O(n)$ time.
- **Frequency map:** Counting every value also takes $O(n)$ time and $O(n)$ space, ignoring the useful sorted order.
- **Single element:** The sole value necessarily occupies more than one quarter and may appear at all sampled indices.
- **Strict threshold:** A count equal to exactly one quarter is insufficient; the test must use $4c > n$.
- **Duplicate candidates:** Several sampled positions may contain the same value; rechecking it changes only a constant factor.
