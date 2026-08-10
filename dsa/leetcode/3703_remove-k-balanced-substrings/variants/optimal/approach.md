## General

The removable pattern is:

$$
\underbrace{((\cdots(}_{k\text{ opening parentheses}}
\underbrace{))\cdots)}_{k\text{ closing parentheses}}.
$$

Removing one occurrence may join characters that were previously separated and create another occurrence. Repeatedly searching and rebuilding the complete string would be expensive.

The exact source reduces the string online. Its stack stores a run-length encoding of the already processed, fully reduced prefix. Each stack entry is:

`[character, count]`.

Adjacent entries always have different characters.

**Adding one character to the run stack**

For each character `c`:

- if the top run has the same character, increment that run's count;
- otherwise, append a new run `[c, 1]`.

For example, prefix `"((())"` is represented by runs such as:

`[['(', 3], [')', 2]]`

before any applicable reduction.

Run lengths are the relevant information because a removable substring requires $k$ consecutive openings immediately followed by $k$ consecutive closings. Individual positions inside one run do not need separate stack entries.

**When a new pattern can appear**

Before processing the current character, the stack represents a prefix with no removable pattern. Appending one character cannot create a new occurrence entirely inside the old prefix. Any newly created pattern must end at the newly appended character.

The pattern ends with a closing parenthesis, so the source checks only when:

`c == ")"`.

At that moment, a removable suffix exists exactly when:

- the top run is a closing run of length exactly $k$; and
- the preceding run is an opening run with at least $k$ characters.

The stack alternates characters, so once the top is `')'`, the preceding run—if it exists—is necessarily `'('`. The condition:

`len(stk) > 1 and stk[-1][1] == k and stk[-2][1] >= k`

therefore recognizes the entire pattern without comparing characters one by one.

**Why the closing count is tested for equality**

If an opening run has at least $k$ characters, the pattern is removed at the exact moment the following closing run reaches length $k$. That closing run never grows to $k+1$ while it remains removable.

If a closing run does grow beyond $k$, it means that when it first reached $k$, the preceding opening run did not contain enough openings or did not exist. Continuing to append closings cannot increase that preceding opening count, so the same run cannot later become a valid pattern boundary.

Thus `== k` is the correct online trigger; `>= k` is unnecessary and could obscure the immediate-removal invariant.

**Removing the suffix in run form**

When a pattern is found, the top closing run has exactly $k$ characters, so the source removes the whole entry:

`stk.pop()`.

The preceding opening run may contain more than $k$ characters. Subtract:

`stk[-1][1] -= k`.

If its count becomes zero, remove that run as well. If openings remain, they stay as the final run of the reduced prefix.

No output string is rebuilt during this step. A removal changes only the final one or two run entries.

**Why one removal check per input character is enough**

The removed pattern is a suffix of the processed prefix. After deleting it:

- if some openings remain in its opening run, the reduced prefix ends with `'('`, so no pattern ending in `')'` can exist;
- if that opening run disappears, an older run may be exposed, but it belongs to a prefix that was already fully reduced before the removed openings were read.

Therefore, the removal cannot reveal another previously unchecked removable suffix immediately. A later input character may create a new pattern across the joined boundary, and the ordinary next iteration will detect it.

The example `s = "(())"` with `k = 1` illustrates this. Reading the first closing parenthesis removes the innermost `"()"`, leaving one opening run. Reading the final closing parenthesis then creates and removes the second `"()"`.

**Processed-prefix invariant**

After every iteration, expanding the stack entries yields the result of fully reducing the processed prefix, and that expanded string contains no $k$-balanced substring.

The invariant begins with the empty stack. Appending a character preserves all old reductions. The only possible new pattern is the suffix ending at that character, and the condition removes it when present. The preceding argument shows the resulting stack needs no immediate second reduction.

Consequently, after the final character, the stack represents the fixed point requested by the problem.

**Reconstructing the final string**

The expression:

`"".join(c * v for c, v in stk)`

expands each run back into repeated characters and concatenates the runs in order. Removed characters no longer appear in the stack, while every unreduced character retains its original relative order.

If every character is removed, `stk` is empty and joining the empty generator returns the empty string.

## Complexity detail

Let $n$ be `len(s)`.

Each input character is processed once. It either increments one run or creates one new run. Each run pushed onto the stack can be popped at most once. All stack updates therefore total $O(n)$ time.

Reconstructing the answer repeats exactly the remaining characters and takes $O(n)$ time in the worst case. Overall time is $O(n)$.

The stack can contain $O(n)$ alternating runs, and the returned string can also contain $O(n)$ characters. Auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Repeated global replacement:** Searching for the pattern and rebuilding the string after each round can take $O(n^2)$ time because many characters may be copied repeatedly.
- **Character stack with suffix comparison:** Storing every character and checking the last $2k$ positions after each push can cost $O(nk)$. Run lengths make the suffix test constant time.
- **Regular-expression replacement:** Repeated regex passes still require fixed-point iteration and repeated whole-string scans.
- **`k = 1`:** The pattern is `"()"`, and the run stack behaves like online adjacent-pair cancellation.
- **Opening run longer than `k`:** Only its final $k$ openings are removed; the earlier openings remain in the same run.
- **Closing run longer than `k`:** It could grow that large only when no sufficient opening run preceded it at the trigger moment, so it is not a missed removable suffix.
- **Nested removals:** Immediate suffix reduction lets newly adjacent future characters remove patterns created by earlier removals.
- **No removable pattern:** The stack expands to the original string unchanged.
- **Complete removal:** All runs are popped, and joining produces `""`.
- **Run entry reaches zero:** It must be popped so no zero-length entry interferes with future adjacency.
