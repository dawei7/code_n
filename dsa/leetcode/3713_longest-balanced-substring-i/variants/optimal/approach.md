## General

Enumerate the left endpoint of the substring. As the right endpoint advances, update a 26-entry frequency array rather than recounting the entire interval. Also track `distinct`, the number of positive frequencies, and `maximum`, the largest frequency currently present.

A substring of length $L$ is balanced exactly when

$$
L=\textit{distinct}\cdot\textit{maximum}.
$$

Every positive character count is at most `maximum`, and their sum is $L$. If their sum reaches `distinct * maximum`, every one of those counts must equal the maximum. Conversely, equal positive counts obviously satisfy the equation. This gives a constant-time balance test after each extension.

Each possible interval is reached once by the two endpoint loops, and the equation recognizes exactly the balanced ones, so the greatest recorded length is the answer. If the unprocessed suffix beginning at `left` is no longer longer than `best`, later left endpoints cannot improve the answer and the outer loop may stop.

## Complexity detail

Let $n=\lvert s\rvert$. There are $O(n^2)$ substrings, and each right-endpoint update and balance test takes $O(1)$ time, so total time is $O(n^2)$. The 26-entry count array uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Recount every substring:** Building a fresh frequency map for all $O(n^2)$ intervals can add another $O(n)$ factor, producing $O(n^3)$ time.
- **Compare all 26 counts directly:** This is also $O(n^2)$ because the alphabet is fixed, but the `length == distinct * maximum` test avoids a 26-entry scan at every endpoint.
- **Single distinct character:** Any substring made from one repeated letter is balanced regardless of its length.
- **All characters distinct:** Every frequency is one, so the complete substring is balanced.
- **Absent letters:** Zero frequencies are excluded; only the `distinct` positive counts participate.
- **Tied longest substrings:** The problem requests only the length, so any number of equally long locations has the same answer.
- **Contiguity:** A balanced subsequence formed by skipping positions is irrelevant; both endpoints describe an uninterrupted slice.
