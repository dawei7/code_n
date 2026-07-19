## General
**Merge one ordered product stream per prime**

Every super ugly number after one is an earlier sequence value multiplied by one allowed prime. For each prime `p`, imagine the increasing stream
`p * ugly[0], p * ugly[1], ...`.

Store one pointer into the generated sequence for each prime. Its current product is the first candidate from that stream not yet passed. The next sequence value is the minimum current candidate across all streams.

**Advance every stream tied at the chosen value**

The same number may have several representations, such as `2*3` and `3*2`. After appending the minimum candidate, advance every pointer whose product equals it. Advancing only one would present the same value again on the next iteration and violate strict sequence order.

For primes `[2,3]`, candidates begin at `2,3`. After appending two, the first stream offers four. After appending three, the second offers six. Appending four advances the first stream to six; when six is selected, both tied streams advance, producing the distinct prefix `1,2,3,4,6`.

**The smallest stream head is the next missing number**

Every candidate is an allowed prime times an already generated super ugly number, so every appended value is valid. Conversely, any super ugly number greater than one can remove one of its allowed prime factors, leaving a smaller super ugly number that appears earlier in the sequence. It therefore belongs to at least one product stream.

Each pointer skips exactly the products no greater than the last appended value. Its head is the smallest unseen member of that stream, so the minimum across heads is the smallest super ugly number missing globally. Advancing all equal heads removes duplicates without skipping any larger candidate, proving the sequence by induction.

## Complexity detail
Let `k` be the number of allowed primes. Each of the $n - 1$ generated values scans `k` candidates and may advance tied pointers, giving $O(nk)$ time. The generated sequence uses $O(n)$ space, while pointers and candidates use $O(k)$.

## Alternatives and edge cases
- **Min-heap over product streams:** avoids scanning all `k` heads but must still coordinate duplicate products; it is useful when `k` is large.
- **Test consecutive integers by trial division:** depends on the numeric magnitude of the answer and spends most work rejecting nonmembers.
- One is always the first sequence value. A single prime produces its successive powers.
