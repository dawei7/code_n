## General

**Merge the character stream with the insertion-index stream**

The indices in `spaces` are strictly increasing. The string indices are also visited in increasing order by `enumerate(s)`. Two monotonic streams can therefore be merged in one pass.

`j` points to the next unused insertion index. At string index `i`:

- if `j < len(spaces)` and `i == spaces[j]`, append a space and increment `j`;
- append the current character `c`.

Appending the space first implements “insert before the character at that index.”

Strictly increasing insertion indices guarantee at most one space belongs before each character, so one `if` is sufficient rather than a loop.

**Why original indices remain valid**

The algorithm compares `spaces` against `i` from the original string, not against positions in the growing output.

Inserted spaces would shift later output positions, but they do not shift the original indices supplied by the problem. Keeping a separate output buffer and enumerating the unchanged input avoids all index-adjustment mistakes.

For `s = "EnjoyYourCoffee"` and `spaces = [5, 9]`, `i = 5` still refers to `"Y"` and `i = 9` still refers to `"C"`, regardless of the first space already appended to `ans`.

**Build pieces in a list, then join once**

Python strings are immutable. Repeatedly adding to a result string may copy the accumulated prefix many times.

The source appends individual characters and spaces to `ans`, then performs `''.join(ans)` once. The final join allocates the result of length `len(s) + len(spaces)` and copies each collected piece into it.

This makes construction linear in the output size.

**Trace a boundary insertion**

If `spaces[0] == 0`, the first loop iteration sees `i == 0`, appends `' '`, and then appends `s[0]`. The output correctly begins with a space.

The constraints do not provide insertion index `len(s)`, so there is never a requested space after the final character. Every supplied index is encountered during enumeration.

**Why the algorithm is correct**

Before processing original index `i`, `ans` contains exactly the modified output for characters before `i`, and `j` identifies the first not-yet-inserted space index.

If `i == spaces[j]`, the contract requires a space immediately before `s[i]`; the code appends it and consumes that instruction. If they are unequal, strict ordering means no space belongs at `i`. The character is then appended in either case.

This invariant holds for every character. Since every valid insertion index occurs exactly once and in increasing order, all requested spaces are inserted at the correct original positions, no extra spaces are added, and character order is preserved.

The source does not modify either input.

**Trace several insertions without shifted-index arithmetic**

For `s = "abcde"` and `spaces = [1, 3]`:

- index 0 does not match the next instruction, so append `"a"`;
- index 1 matches, so append a space and then `"b"`;
- index 2 appends `"c"` normally;
- index 3 matches the second instruction, so append a space and then `"d"`;
- index 4 appends `"e"`.

The result is `"a bc de"`. Notice that the second instruction remains 3, not 4, even though one output space already exists. This is the central advantage of scanning original characters and writing to a separate destination.

**Why every insertion instruction is consumed**

All `spaces` values lie between 0 and `len(s) - 1` and are strictly increasing. The character loop visits every integer in exactly that range. Therefore, whenever `j` points to an instruction, the loop must eventually reach the matching `i` unless all instructions have already been consumed.

There can be no stale instruction smaller than `i`: it would have matched and incremented `j` at its own iteration. This justifies checking equality rather than using a more defensive `i >= spaces[j]` condition.

## Complexity detail

Let $n=\lvert s\rvert$ and $m=\lvert\texttt{spaces}\rvert$.

The loop visits $n$ characters, while `j` advances at most $m$ times. Joining creates an output of length $n+m$. Total time is $O(n+m)$.

The list and returned string contain $n+m$ characters or pieces, so construction space is $O(n+m)$. The pointer variables use constant space.

The output itself necessarily has length $n+m$, so linear result storage is unavoidable.

## Alternatives and edge cases

- **Repeated string slicing and concatenation:** Inserting one space at a time shifts later positions and can repeatedly copy large strings, leading to quadratic behavior.
- **Build whole string segments:** Appending `s[previous:index]` and a space for each insertion is also linear and may use fewer list elements. The character-wise merge is direct.
- **Use a set of insertion indices:** Membership checks work, but ignore the useful sorted guarantee and require extra $O(m)$ storage.
- **Space before index zero:** The space is appended before the first character correctly.
- **Many consecutive indices:** Each original character receives its own preceding space, producing alternating spaces and characters.
- **Insertion before the last character:** It is encountered normally during the final loop iteration.
- **No insertion after the string:** Such an index is outside the valid domain.
- **Strictly increasing indices:** No duplicate-space handling is needed.
- **Uppercase and lowercase characters:** They are copied unchanged.
- **Original-index semantics:** Inserted output characters never affect `i`.
- **Input preservation:** Neither `s` nor `spaces` is changed.
- **Join once:** Avoids repeated immutable-string copying.
- **Every character retained:** The unconditional `ans.append(c)` ensures insertion never replaces or drops the character at that index.
- **Instruction pointer exhausted:** The bounds test stops reading `spaces[j]` after the final instruction while remaining characters continue normally.
