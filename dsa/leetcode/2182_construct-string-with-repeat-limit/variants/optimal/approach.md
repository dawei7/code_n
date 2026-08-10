## General

Lexicographic maximization prioritizes the earliest position at which two candidate strings differ. Therefore the algorithm should always place the largest currently legal character as early as possible.

The complication is the repeat limit. After using the largest available letter `repeatLimit` times consecutively, another copy cannot be appended until a different, smaller letter breaks the run. The exact solution counts all letters, processes candidate main letters from `z` down to `a`, and keeps a pointer to the largest available breaker.

**Count the fixed alphabet**

Array `cnt` has 26 entries. Index zero represents `a` and index 25 represents `z`. Scanning `s` increments the matching count through `ord(c) - ord("a")`.

The algorithm does not sort all $n$ characters. The constant-size alphabet already provides their priority order through indices.

**Choose the largest main letter**

The outer loop visits `i` from 25 down to zero. At a given `i`, all letters larger than it have already been used as much as possible or have become impossible to continue.

Inside the loop, `x = min(repeatLimit, cnt[i])` selects the largest legal initial run of that character. The code subtracts those copies and appends `ascii_lowercase[i] * x`.

Using fewer than `repeatLimit` copies while more remain would place a smaller breaker earlier than necessary. The resulting string would be lexicographically smaller at that first breaker position. Thus taking the maximum legal run is optimal.

When `cnt[i]` was already zero, `x` is zero and the code appends an empty string before breaking. This is harmless; joining empty chunks does not change the result.

**Find the best separator**

If copies of letter `i` remain after a full run, another `i` would violate the repeat limit. The construction needs one different letter.

Pointer `j` searches downward for the largest smaller letter with a positive count. Appending exactly one copy is optimal:

- choosing the largest available breaker maximizes the current differing position;
- using more than one breaker would delay the return to the larger letter and make the string lexicographically smaller.

After one breaker, the consecutive run of `i` has ended. The inner loop can append another block of up to `repeatLimit` copies of `i`.

**Keep the breaker strictly below the main letter**

`j` starts at 24 because no letter is smaller than `z` beyond index 24. At the start of each outer iteration, `j = min(i - 1, j)` ensures it is strictly less than the new main index.

The pointer never moves upward. Its search loop skips exhausted letters by decrementing `j`. Since main letters themselves are processed in descending order, no skipped larger breaker later becomes relevant again.

**Stop when no separator exists**

If `j < 0` while copies of `i` remain, there is no smaller character available to break the current run. The leftover copies of `i` cannot be appended legally.

The problem explicitly says not all input characters must be used. Stopping this main letter is therefore correct. At that point all smaller counts have been searched and found zero, so later outer iterations add nothing.

Appending an illegal extra copy would not be allowed, and ending the string is lexicographically better than no valid alternative because there is no different character to extend it.

**Why the greedy prefix is globally largest**

At every output position, the algorithm chooses the largest character that can appear while preserving a valid continuation:

- if the largest remaining letter has not reached its consecutive limit, it is selected;
- if it has reached the limit, the largest different available letter is selected once;
- if no different letter exists, no valid extension exists.

Suppose another valid result first differs from the greedy result at some position. Before that point, both prefixes are identical and have the same remaining multiset and current run. The greedy choice is the largest legal next character, so the alternative cannot place a larger one there. If it places a smaller one, it is lexicographically smaller immediately. Therefore no valid string is lexicographically larger.

For `"cczazcc"` with limit three, the algorithm emits both `z` characters, then three `c` characters. More `c` remain, so it uses `a` as a breaker and returns to `c`, producing `"zzcccac"`.

## Complexity detail

Let $n$ be the input length. Counting characters takes $O(n)$. The algorithm appends at most $n$ characters, possibly grouped into chunks. The breaker pointer decreases across a constant alphabet of 26 letters, and the outer loop has 26 iterations. Total construction and final joining time are $O(n)$.

The count array uses $O(26)=O(1)$ space. The chunk list and returned string together can contain $O(n)$ characters or chunk references, so space is $O(n)$ when output construction is included. Auxiliary state excluding the output is $O(1)$.

The manifest's $O(n)$ time and space match the exact implementation.

## Alternatives and edge cases

- **Max heap:** Repeatedly pop the largest letter and a breaker. This generalizes to large alphabets but adds $O(\log A)$ heap operations for alphabet size $A$.
- **Sort all characters:** Sorting descending costs $O(n\log n)$ and still needs repair logic for repeat-limit violations.
- **Use a smaller breaker than necessary:** The result remains valid but becomes lexicographically smaller at that breaker position.
- **Use several breakers together:** One is enough to reset the run, and extra smaller characters unnecessarily delay a larger letter.
- **All characters identical:** The result contains at most `repeatLimit` copies because no breaker exists.
- **Repeat limit one:** Equal adjacent letters are forbidden, so the algorithm alternates through one-character main runs and breakers.
- **Limit at least every frequency:** No letter needs a breaker for itself, and characters are emitted in descending order.
- **Unused characters allowed:** Leftover copies are correctly abandoned when no separator can make them legal.
- **Empty appended chunks:** A zero count produces `""` in `ans`, which does not affect the joined output.
- **Breaker later becomes main:** The `min(i - 1, j)` update prevents the same letter from being used as its own breaker.
- **Fixed lowercase alphabet:** Array indexing and `ascii_lowercase` are valid because every input character is `a` through `z`.
- **Output length tie:** If one valid string is a prefix of another, the longer is larger; the greedy only stops when no legal extension exists.
- **Input preservation:** Counts are stored separately, and the immutable source string is unchanged.
