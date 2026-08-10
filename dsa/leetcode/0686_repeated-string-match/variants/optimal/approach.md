## General

The task is to repeat `a` the smallest number of times so that `b` occurs as one contiguous substring. The occurrence may begin near the end of one copy of `a`, continue through several complete copies, and end inside a later copy. Therefore, checking whether every character of `b` appears somewhere in `a` is not enough; their cyclic order and adjacency must match.

Let

$$
m=\lvert a\rvert
$$

and

$$
n=\lvert b\rvert.
$$

Both strings are nonempty.

**The unavoidable lower bound on the repeat count**

A string made from `r` copies of `a` has length `r m`. It cannot contain `b` unless its total length is at least `n`. Thus any answer must satisfy

$$
r m \ge n.
$$

The smallest integer that satisfies this condition is

$$
q=\left\lceil\frac{n}{m}\right\rceil.
$$

The code stores this lower bound in `ans`. It also constructs `t = [a] * ans`, a list containing `ans` references to `a`. Joining that list produces the repeated candidate string.

Starting at this lower bound matters for minimality. Every smaller repeat count is too short even before character content is considered, so there is no reason to test it.

**Why only one extra copy is theoretically necessary**

The infinitely repeated string

`aaaa...`

is periodic with period `m`. If `b` occurs anywhere in it, an equivalent starting alignment occurs at some offset from `0` through `m - 1` within a copy of `a`. There are only `m` distinct alignments modulo the period.

The lower-bound string of `q` copies already has length at least `n`. It can contain every occurrence that starts at offset zero and ends early enough. An occurrence beginning at a positive offset may extend beyond its right boundary. Adding one more full copy supplies `m` additional characters, enough for any start offset smaller than `m`:

$$
\text{offset}+n \le (m-1)+n \le (q+1)m.
$$

Therefore, if `b` is a substring of any number of repetitions, it must already be a substring of either `a` repeated `q` times or `a` repeated `q+1` times.

The exact code loops three times, so it checks repeat counts `q`, `q+1`, and `q+2`. The third check is redundant under the proof above, but harmless. It cannot produce a nonminimal answer: if `b` could first appear at `q+2`, periodicity says it would already have appeared by `q+1`. In a correct substring implementation, the third attempt can only repeat the conclusion that no occurrence exists.

**What happens in each loop iteration**

At the start of an iteration, `t` contains exactly `ans` copies of `a`.

The expression `''.join(t)` materializes the current repeated string. The membership test

`b in ''.join(t)`

asks whether `b` occurs contiguously anywhere in it.

If the answer is true, the method immediately returns `ans`. Because the tested counts increase one at a time from the length lower bound, this is the minimum possible repeat count.

If the membership test fails, `ans` is increased and one more copy of `a` is appended to `t`. The next iteration tests the next repeat count. After all three attempts fail, the method returns `-1`.

The final increment and append after the third failed test are never examined. They do not affect the return value; they are simply a consequence of placing the update at the bottom of every loop iteration.

**A boundary-crossing example**

Take `a = "abcd"` and `b = "cdabcdab"`. Here `m = 4` and `n = 8`, so `q = 2`.

- Two repetitions produce `"abcdabcd"`. It is long enough, but the desired occurrence starting at the first `c` would need two more characters beyond the end.
- Three repetitions produce `"abcdabcdabcd"`.
- Starting at index `2` gives `"cdabcdab"`, so the method returns `3`.

This example shows why “candidate length is at least `b`'s length” is necessary but not sufficient. Alignment can require one extra copy.

**Why impossible cases are rejected**

Suppose `b` contains a character that never occurs in `a`. No repetition can introduce that character, so every membership test fails.

More subtly, all characters may be present but in an incompatible periodic order. For example, repetition preserves the same cycle of characters forever. Testing a string long enough to cover every starting offset verifies all possible alignments. Once both `q` and `q+1` fail, additional copies add no new alignment pattern, so returning `-1` is correct.

**Why the returned count is minimal**

There are three parts to the argument:

1. Counts below `q` are impossible because their strings are shorter than `b`.
2. The code tests candidate counts in increasing order beginning with `q`.
3. Any occurrence that exists at all must appear by `q+1` because start positions repeat modulo `m`.

Therefore, the first successful membership test is the minimum count, and failure through `q+1` proves impossibility. The exact extra `q+2` check does not change that conclusion.

## Complexity detail

Let `m = len(a)` and `n = len(b)`. The largest relevant repeated string has length at most `n + 2m`, which is `O(m+n)`. The exact loop performs only three iterations, a constant independent of input sizes.

Each `join` copies the characters of the current candidate, so all joining work across the three attempts is `O(m+n)`.

The cost of `b in candidate` depends on the substring-search guarantee supplied by the language runtime. Under the standard linear-time substring-search model used by the intended bound, the three membership tests total `O(m+n)` time. If one instead assumes a naive comparison at every possible start, a conservative language-independent worst case is

$$
O((m+n)n).
$$

The algorithm's high-level work is linear apart from that built-in search primitive; it does not implement its own KMP or rolling hash.

The joined candidate requires `O(m+n)` temporary character storage. The list `t` holds `O(q)` references, where `q = \lceil n/m\rceil`, and the strings `a` and `b` are inputs rather than auxiliary copies. Thus the dominant auxiliary-space bound is

$$
O(m+n).
$$

Only one joined candidate is needed by the membership expression at a time.

## Alternatives and edge cases

- **KMP over a virtual repeated string:** Build the prefix table for `b` and scan characters of repeated `a` by modular indexing. This gives an explicit deterministic `O(m+n)` search guarantee and avoids materializing every candidate, but its prefix-function logic is longer.

- **Rabin–Karp rolling hash:** Rolling hashes can test all periodic alignments efficiently. A direct character verification is needed after a hash match to eliminate collision risk.

- **Only two attempts:** Testing `q` and `q+1` is sufficient by periodicity. The exact three-iteration loop performs one unnecessary final test without changing correctness.

- **`b` shorter than `a`:** Then `q = 1`. The answer may be `1` if `b` lies inside `a`, `2` if it crosses the boundary between copies, or `-1`.

- **Equal strings:** With `a == b`, the first candidate succeeds and returns `1`.

- **One-character `a`:** Repetition can form only a run of that character. The returned count is `len(b)` if every character of `b` matches; otherwise it is `-1`.

- **Missing character:** If any character in `b` is absent from `a`, no repetition works. The membership tests discover this without a separate set check.

- **Compatible letters in the wrong cyclic order:** Having the same character set is insufficient. Substring matching verifies exact order and multiplicity.

- **Nonempty-input guarantee:** The division `n / m` is safe because `a` cannot be empty. A generalized version allowing empty `a` would need a special case.

- **Use of `ceil`:** Python's `ceil(n / m)` returns an integer here. The bounded lengths make floating-point rounding harmless, though integer arithmetic `(n + m - 1) // m` would avoid floating point entirely.

- **Repeated construction:** `''.join(t)` is required because `t` is a list. Checking `b in t` would search list elements, not substrings of the concatenation.

- **Return after a successful larger count:** Since smaller counts have already been tested or ruled out by length, immediate return never violates minimality.
