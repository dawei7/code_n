## General

**Track one character independently.** Choose a pivot occurrence of character $c$ that has another $c$ on both sides. The operation deletes exactly two occurrences of $c$ and leaves the pivot itself. It never changes the count of any other character.

Therefore each letter's frequency can be minimized independently, and the final minimum length is the sum of the minimum surviving counts for all letters that appear.

**Every operation preserves frequency parity.** If a letter currently appears $q$ times, an operation on that letter changes its count to $q-2$. Subtracting two does not change whether $q$ is odd or even. A positive odd frequency can never become zero or two; a positive even frequency can never become one.

This gives lower bounds:

- a positive odd count must leave at least one occurrence;
- a positive even count must leave at least two occurrences, because zero would require applying an operation when only two remained, which is impossible.

**Those lower bounds are achievable.** Whenever a letter has at least three occurrences, order those occurrences by position and choose any non-end occurrence as the pivot. It has a same-letter occurrence to its left and right; the closest such occurrences exist and are deleted. The frequency decreases by exactly two.

Repeat while the count is at least three. An odd count reaches one, and an even positive count reaches two. Interleaved other characters do not prevent this argument because “closest” refers to matching occurrences, and unrelated symbols may remain between them.

So a character with frequency $q>0$ contributes:

$$
\begin{cases}
1,&q\text{ odd},\\
2,&q\text{ even}.
\end{cases}
$$

**Implement the formula directly.** `cnt = Counter(s)` records every positive character frequency. The generator visits only present characters and yields

`1 if x & 1 else 2`.

`x & 1` extracts the low bit: it is one for odd $x$ and zero for even $x$. Summing these contributions returns the minimum final length without simulating deletions or tracking changing indices.

Absent letters do not appear in `cnt.values()` and correctly contribute zero. This matters because the even-frequency formula of two applies only to positive even counts, not to frequency zero.

**Why operations for different letters do not conflict.** Deleting occurrences changes absolute indices, but it does not change the left-to-right order among surviving occurrences of any other letter. If another letter has at least three copies before a deletion, it still has the same number afterward and still has an internal pivot. Frequency reductions can be scheduled letter by letter, so summing independent minima is achievable globally.

**Trace the first example by counts.** In `"abaacbcbb"`, frequencies are $a=3$, $b=4$, and $c=2$. The odd count for $a$ reduces to one. Each positive even count reduces to two. The minimum total length is $1+2+2=5$, matching the example without needing to reproduce one particular deletion order.

For `"aa"`, frequency two is already the minimum positive even terminal count. No occurrence has matching copies on both sides, so the result remains two.

**Why sequence content is unnecessary for the returned number.** Exact deletion choices affect which particular occurrences survive and the final character order, but the problem asks only for minimum length. Counts and parity completely determine that scalar answer.

## Complexity detail

Let $n$ be string length. `Counter(s)` scans all characters once in $O(n)$ expected time. The result loop visits at most 26 frequencies because the alphabet is lowercase English, so it is $O(1)$ relative to $n$. Total time is $O(n)$.

The counter has at most 26 keys, a fixed bound, so auxiliary space is $O(1)$ under the stated alphabet. In a generalized alphabet of size $\sigma$, space would be $O(\sigma)$.

The source does not mutate `s` and allocates no output string, since only an integer length is returned.

## Alternatives and edge cases

- **Fixed 26-element frequency array:** It avoids hashing and has the same $O(n)$ time and $O(1)$ space.
- **Presence and parity bitmasks:** One mask records which letters occur and another toggles frequency parity. Each present odd bit contributes one and present even bit contributes two.
- **Simulate deletions in a mutable string:** It repeatedly searches matching neighbors and shifts content, doing far more work than the frequency invariant requires.
- **Frequency one:** No operation is possible, and one occurrence remains.
- **Frequency two:** Neither occurrence has matching copies on both sides, so both remain.
- **Frequency three:** Choose the middle occurrence and delete the two outer ones, leaving one.
- **Frequency four:** One operation reduces it to two, where processing stops.
- **Odd positive frequency:** Repeated subtraction by two reaches exactly one.
- **Even positive frequency:** Repeated subtraction by two reaches exactly two.
- **Zero frequency:** It contributes zero, not two; iterating only counter values handles this.
- **Interleaved letters:** They do not change per-letter occurrence order or frequency feasibility.
- **Closest-occurrence wording:** Any internal same-letter pivot's immediate matching predecessor and successor are precisely the required closest occurrences.
- **Final string not unique:** Different valid deletion orders can leave different occurrences, but their minimum length is identical.
