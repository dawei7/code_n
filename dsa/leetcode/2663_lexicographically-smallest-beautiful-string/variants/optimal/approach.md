## General

**Beautiful means avoiding equality one or two positions back**

A palindrome of length two has equal adjacent characters: `aa`.

A palindrome of length three has equal first and last characters: `aba`.

Every palindrome of length at least four contains a smaller palindrome of length two or three at its center. Therefore, a string contains no palindrome of length at least two exactly when each character differs from:

- the immediately preceding character;
- the character two positions earlier.

The solution only needs these two local checks while constructing a candidate.

**Find the rightmost position that can be increased**

To obtain the smallest lexicographically larger string, preserve the longest possible prefix of `s`.

The code scans position `i` from right to left. At one position, it tries letters strictly larger than the current `cs[i]`, starting with the next letter.

If a valid increase is possible far to the right, it changes a less significant lexicographic position and is smaller than every candidate whose first change occurs farther left.

This is analogous to carrying in a numeral system, except some digits are forbidden by the palindrome rule.

**Try larger letters in increasing order**

Current zero-based alphabet index is:

`p = ord(cs[i]) - ord('a') + 1`.

Starting at `p` means the first tried character is exactly one greater than the current one. Loop ends before `k`, so only the first $k$ lowercase letters are used.

For candidate `c`, the code rejects it when it equals `cs[i-1]` or `cs[i-2]`, when those positions exist.

The unchanged prefix was already beautiful, so these are the only new palindromes that can end at position $i$.

**Greedily rebuild the suffix**

Once position $i$ is increased validly, every later position can be made as small as possible because lexicographic superiority is already established at $i$.

For each suffix index `l`, the code tries alphabet letters from `a` upward and selects the first that differs from the previous one and previous two characters.

This produces the lexicographically smallest valid character at each suffix position given the already-fixed prefix.

Because $k\ge4$, at most two distinct letters are forbidden, so at least two legal alphabet choices remain. The inner loop always finds one.

**Why local greedy suffix choices are globally minimal**

At suffix position $l$, all earlier characters are fixed. The only restrictions on `cs[l]` come from positions $l-1$ and $l-2$.

Choosing the smallest legal character cannot make the current prefix worse, and future feasibility is guaranteed by the alphabet size. Any candidate choosing a larger character at the first suffix difference would be lexicographically larger.

Induction over suffix positions proves the greedy rebuild is the smallest beautiful suffix compatible with the increased prefix.

**Return the first complete candidate**

The scan order is:

1. rightmost possible change position first;
2. smallest valid larger letter at that position;
3. smallest valid suffix.

These three nested priorities exactly match lexicographic order. Therefore, the first constructed full string is the answer and the method returns immediately.

**Why moving left is correct when a position cannot increase**

If no larger allowed character at position $i$ avoids conflict with its two prefix predecessors, then no beautiful larger string can preserve prefix through $i-1$ and make its first difference at $i$.

The algorithm moves to $i-1$, permitting an earlier, more significant increase. Suffix contents no longer matter because they will be rebuilt after a successful carry.

The code does not mutate `cs[i]` while merely rejecting candidates, so the original prefix context remains intact during this search.

**Trace `"abcz"`**

With $k=26$, the last character `z` cannot be increased.

At index two, current `c` can increase to `d`. It differs from previous `b` and the character two back `a`, so it is valid.

The suffix at index three is filled with the smallest character differing from `d` and `b`, which is `a`.

Result is `"abda"`.

**Why empty string can be necessary**

If every position fails to admit a valid larger letter while preserving its earlier prefix, then there is no legal lexicographic carry.

Every length-$n$ string larger than `s` must have some first differing position with a larger character. The loop has exhausted all such possibilities, so returning `""` is correct.


The local condition is equivalent to full palindrome avoidance. For each possible first-difference position from right to left, the solution tests larger letters in order.

Upon a valid choice, greedy suffix construction returns the smallest beautiful completion. Any untested candidate either changes a more significant earlier position or uses a larger letter/suffix at the same first difference, so it is lexicographically larger.

If all trials fail, no larger beautiful string exists.

## Complexity detail

There are $n$ positions and at most $k$ candidate letters tested at each during carry search. Suffix construction also tests at most $k$ letters per suffix position once. Total time is $O(nk)$.

Converting `s` to character list and joining the result use $O(n)$ space. Other state is constant.

## Alternatives and edge cases

- **Generate strings in lexicographic order:** Exponential and unnecessary.
- **Backtracking from scratch:** Ignores that the input is already beautiful and that only the next lexicographic string is needed.
- **Check every substring for palindromes:** Local distance-one and distance-two checks are sufficient.
- **Increase last position:** Preferred whenever a legal larger character exists.
- **Character already at alphabet limit:** Carry moves left.
- **Two forbidden predecessors equal:** At most one distinct letter is excluded, making completion even easier.
- **Length one:** Only alphabet bound matters; return next letter or empty.
- **No successor:** Exhausted carry search returns empty string.
- **`k >= 4`:** Guarantees greedy suffix completion after excluding at most two letters.
- **Input preservation:** The original string is immutable; changes occur in list `cs`.
