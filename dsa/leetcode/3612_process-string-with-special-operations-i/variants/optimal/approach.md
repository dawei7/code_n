## General

The exact source directly simulates the evolving result with a Python list of characters. After each input character, `result` contains the literal current string in normal left-to-right order. No compressed representation, deque, or logical reversal flag is used.

This is simple and correct under the small input limit, but it differs materially from the manifest, which describes constant-time logical reversals and `O(n+L)` processing.

**Why a character list is used**

Python strings are immutable, so repeatedly removing or appending characters to a string would create new string objects. A list supports:

- amortized constant-time append at the end;
- constant-time pop from the end;
- in-place reversal;
- bulk extension for duplication.

After all operations, `"".join(result)` creates the requested string once.

**Processing lowercase letters**

The first branch is:

`if c.isalpha(): result.append(c)`.

The statement guarantees that ordinary characters are lowercase English letters and that the only nonletters are `*`, `#`, and `%`. Within this input domain, `isalpha` identifies exactly the append operations.

As a general Python predicate, `isalpha` accepts alphabetic Unicode characters and uppercase letters too. The source relies on the problem's restricted alphabet rather than enforcing lowercase ASCII explicitly.

**Processing `*`**

The second branch is:

`elif c == "*" and result: result.pop()`.

If the current result is nonempty, `pop()` removes its final character. If it is empty, the combined condition is false. The following branches do not match `*`, so the operation becomes a no-op, exactly as required.

Because the list always stores the actual current orientation, “last character” means the physical last list entry even after earlier reversals.

**Processing `#`**

`result.extend(result)` appends the list's current sequence to itself. For an original current value `[a, b]`, the result becomes `[a, b, a, b]`.

The operation must duplicate the entire current value once, not repeatedly consume newly appended elements forever. Python's list extension handles self-extension with those duplication semantics.

Its running time and additional list capacity are proportional to the current result length. If the result is empty, extending it by itself changes nothing.

**Processing `%`**

`result.reverse()` reverses all current list entries in place. For `[a, a, b]` it produces `[b, a, a]`.

The call uses constant auxiliary workspace at the algorithmic level, but it performs swaps across the whole list and therefore costs linear time in the current result length. Reversing an empty or one-character list is harmless.

**Following `"a#b%*"`**

The invariant can be observed after every character:

- `a` appends one letter, giving `["a"]`;
- `#` self-extends it, giving `["a", "a"]`;
- `b` appends at the end, giving `["a", "a", "b"]`;
- `%` reverses the physical list, giving `["b", "a", "a"]`;
- `*` pops its last entry, giving `["b", "a"]`.

Joining produces `"ba"`.

**Why branch order is safe**

The source checks `isalpha` before comparing the three special symbols. None of `*`, `#`, or `%` is alphabetic, so each reaches its correct later branch. Under the promised alphabet, there is no character that ambiguously represents both a letter and a special operation.

The branches are mutually exclusive. Exactly one rule is applied to every lowercase letter or special character, except that an empty-result `*` intentionally applies no state change.

**Invariant and correctness**

Before processing any input, the empty list represents the required empty result.

Assume the list exactly represents the result after some prefix of `s`. For the next character:

- appending a letter adds it at the end;
- popping removes the last character when one exists;
- extending the list by itself appends an exact copy;
- reversing changes the order exactly as `%` requires.

Each branch transforms the list into precisely the result defined for the longer prefix. By induction, after the complete input, `result` contains the correct final character sequence. Joining changes representation from a list to a string without changing order or content.

**Growth can be exponential**

Each `#` can double the current length. If the input begins with one letter followed by many `#` characters, lengths progress as 1, 2, 4, 8, and so on. With input length at most 20, the largest construction occurs with one letter followed by 19 duplications, producing `2^19` characters.

The small constraint makes direct materialization feasible. It would not be suitable for a large-input variant where only a character at an index or a truncated prefix was requested.

**Difference from the manifest**

The manifest says the solution stores characters in a deque with a logical orientation flag so reversals are constant-time. The exact source stores one list and calls `reverse()`, which is linear in the current result length.

It also claims `O(n+L)` time. That can be false if `L` means final output length: repeated reversals rescan the same large list, and a large intermediate result can later be reduced by stars. The implementation's cost depends on all intermediate lengths, not just the final one.

## Complexity detail

Let `n` be the input length, `\ell_i` the result length immediately before operation `i`, and `L` the final result length.

Letters and successful stars take amortized `O(1)` time. A `#` costs `O(\ell_i)` because it appends that many characters. A `%` also costs `O(\ell_i)` because it reverses the list. Joining costs `O(L)`. A precise output-sensitive expression is:

$$
O\left(n+L+\sum_{i:\ s_i\in\{\#,\%\}}\ell_i\right).
$$

In terms of `n` alone, the current result can grow exponentially through duplication. Even accounting for repeated reversals, the worst-case total is `O(2^n)`, matching the local editorial's broad worst-case bound rather than the manifest's claimed linear-output strategy.

Let `P` be the maximum result length reached during processing. The list uses `O(P)` space, and the final joined string uses `O(L)` output space. In the worst case, `P = O(2^n)`. In-place reversal uses no second full list, but self-extension may temporarily require implementation-level copying/capacity growth proportional to the duplicated content.

## Alternatives and edge cases

- **Deque with orientation flag:** Appends, removals, and reversals can use opposite deque ends depending on orientation. Duplication still has to materialize copied output, but repeated `%` operations become constant-time.
- **Rope or expression tree:** Represent duplication and reversal lazily for much larger inputs, then materialize only once; this is unnecessary under `n <= 20`.
- **Immutable string simulation:** It is concise, but repeated concatenation, slicing, and reversal allocate new strings and can add copying overhead.
- **Empty result and `*`:** The guarded pop makes the operation a no-op instead of raising `IndexError`.
- **Empty result and `#`:** Duplicating empty remains empty.
- **Empty result and `%`:** Reversing empty remains empty.
- **One-character reversal:** It leaves the character unchanged.
- **Consecutive stars:** They remove available suffix characters one at a time, then become no-ops.
- **Consecutive duplications:** They double the current length on each occurrence and cause exponential growth.
- **Consecutive reversals:** Two reversals restore the same content but the exact source still scans the full list twice.
- **Reverse followed by star:** Because the list is physically reversed, `pop` removes what was originally the first character.
- **Letters after reversal:** They append to the end of the currently reversed sequence, as required by literal simulation.
- **Only special characters:** The result may remain empty throughout.
- **Maximum expansion:** One initial letter followed by 19 `#` symbols produces `2^19` characters under the length-20 constraint.
- **Broader Unicode input:** `isalpha` would accept letters outside lowercase English, but the stated input guarantee excludes them.
- **Manifest mismatch:** The source has no deque or orientation flag; its reverse operation is linear, and its time is not generally `O(n+L_{\text{final}})`.
- **Input preservation:** The string `s` is immutable; all mutations affect only the local result list.
