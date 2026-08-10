## General

**Keep the fully reduced result of the processed prefix**

The stack `stk` represents what remains after performing all possible adjacent-equal removals on the part of `s` processed so far.

When a new character `c` arrives, it is appended conceptually at the right end of that reduced prefix. The only pair it can immediately form is with the current last surviving character, `stk[-1]`. No earlier position can be adjacent to `c` while that top character remains between them.

This leads to two cases:

- If the stack is nonempty and its top equals `c`, the adjacent equal pair is removed by popping the top and not storing `c`.
- Otherwise, no removal involving `c` is currently possible, so `c` is pushed.

The stack is both working memory and the eventual output character sequence.

**Why checking only the top is sufficient**

Before processing `c`, the stack has no adjacent duplicate pair by the invariant. Appending `c` changes adjacency only at one boundary: between the old stack top and `c`.

If those characters differ, every old adjacency remains valid and the new boundary is also valid. Pushing preserves a fully reduced stack.

If they match, removing both restores the stack to exactly its earlier state before that top was pushed. That remaining stack was already fully reduced, so no additional immediate pair exists inside it.

Thus one top comparison completely handles the new character. There is no need to scan backward after each update.

**How chain reactions appear naturally**

Consider `"abbaca"`.

- Read `a` and push it: `[a]`.
- Read the first `b` and push: `[a,b]`.
- Read the second `b`. It matches the top, so pop: `[a]`.
- Read the next `a`. The earlier `bb` removal has made this `a` adjacent to the surviving first `a`. It matches the top, so pop: `[]`.
- Read `c` and push, then read `a` and push.

Joining the final stack gives `"ca"`.

The second cancellation is not found by repeatedly rescanning a modified string. It emerges when the later `a` is processed against the current reduced prefix.

**Trace `"azxxzy"`**

Push `a`, `z`, and the first `x`. The second `x` pops the first.

The next input character `z` now meets the earlier surviving `z` at the top and pops it. Finally, `y` is pushed after `a`.

The result is `"ay"`. This demonstrates that duplicate pairs can be separated in the original input and become adjacent only after an inner pair disappears.

**The prefix invariant**

After processing the first `i` characters, the stack spells the unique fully reduced result for `s[0:i]`.

The invariant holds initially because the empty prefix reduces to the empty stack.

For the next character, any valid first reaction involving it must occur with the final survivor of the reduced prefix. The top comparison performs that reaction when possible; otherwise, it appends the character. The resulting stack has no adjacent equal pair and is exactly the reduction of the longer prefix.

Induction proves the invariant after all characters. The source guarantees the final reduced string is unique, so the stack's valid complete reduction is the requested answer regardless of which duplicate pair a manual process might remove first.

**Why removing a matching top is correct even if other choices existed earlier**

The stack has already resolved all duplicate choices inside the prefix. Equal adjacent characters at its end and the new character form a legal pair. Removing them cannot skip a better outcome because the operation has no score or optimization objective; it simply continues until no pair remains, and the final result is unique.

The algorithm therefore commits immediately without backtracking.

**Why a Python list is a good stack**

`append` adds a character at the right end in amortized constant time. `pop()` removes the rightmost character in constant time. Accessing `stk[-1]` reads the top.

A list also works efficiently with `''.join(stk)`. Repeatedly concatenating immutable strings during the scan could copy the growing output many times and lead to quadratic behavior.

**Why the empty-stack condition comes first**

The expression `if stk and stk[-1] == c` uses short-circuit evaluation. When `stk` is empty, Python does not evaluate `stk[-1]`, avoiding an invalid index access.

An empty stack means there is no previous surviving character, so the current character must be pushed.

**Why each input character has one lifetime**

Every character is examined once. It is either discarded immediately while popping a matching earlier character or appended once. An appended character can later be popped at most once by a matching future character.

This bounded lifetime is what makes the method linear even though removals can cause long conceptual chain reactions.


The algorithm never leaves an adjacent equal pair in the processed representation: a new equal boundary is removed immediately, and old boundaries were already reduced.

It also performs only legal removals between characters that have become adjacent after earlier removals. At the end, the stack is a reachable string with no adjacent duplicates. By the uniqueness guarantee, joining it returns exactly the final required string.

## Complexity detail

Let `N = len(s)`. Each character is processed once, pushed at most once, and popped at most once. All stack operations are constant time, so the scan takes `O(N)` time.

Joining the remaining characters takes `O(N)` in the worst case. Total time remains `O(N)`, matching the manifest.

If no duplicates occur, the stack stores all `N` characters. It therefore uses `O(N)` auxiliary construction space, and the returned immutable string also uses up to `O(N)` space. This matches the manifest.

## Alternatives and edge cases

- **Repeated string replacement:** Remove `aa` through `zz` until the length stops changing. It is simple but repeatedly scans and allocates strings, leading to quadratic worst-case work.
- **Repeated full rescans:** Find one adjacent pair, remove it, and restart. Each removal can shift or rebuild most of the string, again becoming quadratic.
- **Use a mutable character array with a write pointer:** Treat the array prefix as a stack and overwrite positions in place. This implements the same invariant and can reduce object overhead.
- **Recursive removal:** Recursion complicates newly formed boundaries and risks deep call stacks; the explicit stack captures them directly.
- **One character:** The stack receives it and returns it unchanged.
- **Two equal characters:** The second pops the first, producing the empty string.
- **Two different characters:** Both remain in order.
- **All equal characters:** Pairs cancel successively; an even count leaves empty, while an odd count leaves one character.
- **No duplicates anywhere:** Every character is pushed, and the original string is returned.
- **Nested chain reaction:** Patterns such as `abbaca` are handled because later characters compare against the already reduced prefix.
- **Empty final result:** `''.join([])` returns `""` without a special case.
- **Lowercase alphabet:** The stack algorithm actually works for any comparable characters, but the source restricts input to lowercase English letters.
- **Removal order:** Different manual orders lead to the same final answer by the source guarantee; the stack realizes one deterministic left-to-right order.
