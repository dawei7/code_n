## General

The procedure is deterministic: extend the current segment until its complete string has never been emitted before, then emit it and restart.

The source stores emitted segments in a hash set `vis`, their order in `ans`, and the currently growing string in `t`.

**Processing one character**

Each character is appended to `t`. If the resulting candidate already belongs to `vis`, it cannot be emitted yet, so the next input character will extend it.

If it is absent:

- add it to `vis`;
- append it to `ans`;
- reset `t` to empty.

This is exactly the stated “first unseen extension” rule.

**Why every emitted segment is unique**

A segment is appended only after `t not in vis`. It is inserted into the set at the same moment, so no later segment with identical contents can pass the test again.

The set stores content rather than positions, matching uniqueness by segment string.

**Why the choice is forced**

At a new segment start, every shorter candidate encountered before emission was already seen. Emitting one would violate uniqueness. The first unseen candidate is therefore the earliest legal endpoint.

The source neither searches ahead nor optimizes segment count; it directly simulates the required construction.

**Unfinished suffix**

It is possible to reach the end while `t` is still a previously seen string. In that case the source does not append it.

For `"aaaa"`:

- emit `"a"`;
- extend the next start from seen `"a"` to unseen `"aa"` and emit it;
- the final character forms `"a"` again, but no next character exists to make it unique.

The returned result is `["a","aa"]`, exactly as the reference example shows. The output segments therefore need not cover a final suffix that never becomes new; “partition” here follows the explicitly defined procedure rather than the usual requirement that every character appear in a returned part.

**The exact source is not a trie**

The manifest summary claims a prefix-closed trie processes every character once without rebuilding candidates. No trie exists in the executable source.

`t += c` creates a new immutable Python string, copying the previous candidate. Hashing a newly created candidate for set lookup can also inspect its characters.

For a growing segment of length `L`, repeated concatenation and hashing can cost:

$$
1+2+\cdots+L=O(L^2).
$$

Across the input, a safe worst-case upper bound is `O(n^2)`, not a guaranteed `O(n)`. The problem’s particular uniqueness structure may keep candidates shorter in many inputs, but the source should not be credited with trie behavior it does not implement.

**Space behavior**

Every emitted segment is stored in both set and answer references. Their character contents collectively cover at most the consumed emitted portions, bounded by `O(n)`. The current candidate is also at most `n`.

Temporary strings created during concatenation are released, so peak live auxiliary/result storage is `O(n)`.

**Example trace**

For `"abbccccd"`, `a` and `b` emit immediately. The next `b` is seen, so adding `c` creates unseen `bc`. Later `c` emits once, the next `c` waits, and a second `c` creates unseen `cc`. Finally `d` emits.

The set membership invariant explains every boundary without any backtracking.

## Complexity detail

The scan has `n` iterations, but Python immutable-string construction and hashing make the safe exact-source time bound `O(n^2)` in the worst case.

The set, answer list, emitted strings, and current candidate use `O(n)` live space. This agrees with the manifest space bound but not its claimed linear-time trie mechanism.

## Alternatives and edge cases

- **Trie of emitted segments:** Traversing existing prefixes character by character can avoid rebuilding and rehashing candidates, realizing the manifest’s intended `O(n)` behavior with `O(n)` nodes.
- **String builder plus hash:** Rolling hashes can reduce repeated membership cost but require collision handling and a way to materialize emitted strings.
- **All characters initially different:** Every one-character candidate is unseen and emits immediately.
- **Repeated one character:** Segment lengths grow as needed to find unseen strings; a final seen suffix may remain omitted.
- **Empty current segment after emission:** The next character starts a completely new candidate.
- **Seen prefix, unseen extension:** Only the complete candidate is tested; extending a seen string can create a new segment.
- **Duplicate prevention:** Both set insertion and answer append occur atomically in the same branch.
- **Lowercase constraint:** It does not change set logic but bounds trie branching for an alternative.
- **One-character input:** Its candidate is unseen, so it is returned.
- **Unfinished seen suffix:** It is deliberately not appended, as confirmed by the second example.
- **No delimiter or slicing:** Boundaries are represented by resetting `t` rather than storing indices.
- **Input preservation:** Strings are immutable and `s` is never changed.
- **Manifest mismatch:** The source’s set contains full strings, not prefix nodes, and `t += c` rebuilds candidate content.
- **Expected hashing:** Set operations are expected constant-time after a hash exists, but every newly constructed `t` still needs its content hash computed.
