## General

**Validity depends on nesting order, not only on counts**

For one bracket type, a counter can track how many opening brackets remain unmatched. With three types, separate counters still cannot represent nesting. For example, `([)]` has balanced counts for both round and square brackets, but it is invalid: after reading `([`, the round closer `)` attempts to close `(` while the more recent `[` is still open.

The rule is therefore last opened, first closed. That is precisely the behavior of a stack. Opening brackets are pushed in left-to-right order, and a closing bracket must match the opening bracket currently at the top.

**Store the three complete legal pairs**

The implementation creates

```python
d = {'()', '[]', '{}'}
```

Each set member is a complete valid adjacent pair: opener first and closer second. Later, the source forms `stk.pop() + c`; membership in `d` tests both bracket type and order in one operation. A set provides expected $O(1)$ membership testing, and its size is fixed at three.

The string `'({['` is used only as an opening-bracket membership collection. Under the contract, every input character is one of the six bracket characters, so any character not in that string is necessarily one of `')'`, `'}'`, or `']'`. A broader text-validation API would need an explicit policy for non-bracket characters, but this problem does not.

**Maintain exactly the unmatched opening brackets**

The essential invariant is:

> After processing a prefix of `s`, `stk` contains exactly the opening brackets in that prefix that have not yet been closed, in their original order. Its final element is the opening bracket that must be closed next.

The stack is initially empty, which correctly describes the empty prefix. When `c` is an opener, `stk.append(c)` adds a newly unmatched opening bracket. It must appear at the top because any brackets opened earlier surround this new bracket and cannot close until the inner one does.

When `c` is a closer, validity requires two facts: an unmatched opener must exist, and the most recent one must have the same type. The branch

```python
elif not stk or stk.pop() + c not in d:
    return False
```

checks both.

**Why the short-circuit expression is safe**

Python evaluates `or` from left to right and stops as soon as one operand is true. If `stk` is empty, `not stk` is true, so `stk.pop()` is never evaluated. The method returns `False` for an unmatched closer instead of raising an exception.

If the stack is non-empty, the first operand is false and Python evaluates the second. `stk.pop()` removes the most recent unmatched opener, concatenates it with `c`, and tests the resulting two-character string. A matching pair such as `'[' + ']'` belongs to `d`; a crossing or mismatched pair such as `'[' + ')'` does not.

The pop happens before the set test, including on a mismatch. That mutation is harmless because the function immediately returns `False`; no later state needs to be preserved. On a match, removing the opener correctly records that the pair is now closed, so the invariant holds for the longer prefix.

**Reject impossible prefixes immediately**

A closing bracket with an empty stack can never be repaired by characters that appear later: its required opener would need to occur earlier. Likewise, if a closer mismatches the top opener, a later closer cannot change the fact that the current order is already crossed. Returning `False` at the first such event is therefore both safe and useful.

This prefix reasoning explains why `([)]` fails at its third character. After `(` and `[`, the stack is `['(', '[']`. Reading `)` pops `[`, forms `'[)'`, and rejects it. The algorithm does not search deeper for `(` because closing it through an unclosed `[` would violate correct nesting.

**An empty final stack is the last requirement**

Reaching the end without a bad closer proves that every processed closer had the correct preceding opener. It does not prove that every opener received a closer. The return statement

```python
return not stk
```

is `True` only if no unmatched opening brackets remain. Thus strings such as `"(("` are rejected even though they never contain an incorrectly typed closer.

**Trace valid nesting with `"([])"`**

The stack evolves as follows:

| Character | Action | Stack afterward |
|---|---|---|
| `(` | push opener | `['(']` |
| `[` | push opener | `['(', '[']` |
| `]` | pop `[`, accept `[]` | `['(']` |
| `)` | pop `(`, accept `()` | `[]` |

The final stack is empty, so the string is valid. By contrast, `"()[]{}"` demonstrates adjacent rather than nested pairs: each opener is pushed and immediately removed by its closer. Both shapes obey the same invariant.

**Why the result is correct**

If the function returns `False` inside the loop, the current closer either has no earlier unmatched opener or does not match the latest one. Either condition directly violates the definition, so rejection is correct. If the function returns `False` at the end, some opener remains unmatched, also violating the definition.

If it returns `True`, every closer encountered a matching top opener, so all pairs have the correct type and close in reverse opening order. The empty stack additionally proves every opener was closed. These are exactly the required validity conditions, establishing both directions of correctness.

## Complexity detail

Let $n$ be `len(s)`.

- **Time complexity: $O(n)$.** The loop reads each character once. Every character causes at most one constant-time set/string membership check and one stack push or pop. The concatenated pair always has length two, so constructing and hashing it is constant work. Each opener is pushed once and can be popped at most once.
- **Space complexity: $O(n)$.** In the worst case, such as a string consisting entirely of opening brackets, the stack holds all $n$ characters. The three-entry set and other variables require $O(1)$ space. For a well-balanced string the peak stack size equals its maximum nesting depth, which can still be proportional to $n$.

The algorithm may terminate before scanning all characters on invalid input, but $O(n)$ remains the worst-case bound.

## Alternatives and edge cases

- **Closer-to-opener dictionary:** Map each closer to its expected opener, then compare it with the popped top. This avoids constructing a two-character pair and is equally $O(n)$ time and space.
- **Repeated string replacement:** Repeatedly remove `()`, `[]`, and `{}` until nothing changes. It mirrors eliminating innermost pairs but can repeatedly rescan and rebuild the string, leading to $O(n^2)$ time.
- **One or three counters:** Counts can detect surplus brackets but cannot detect crossing order, so `([)]` defeats this approach.
- **Recursive parsing:** A grammar-based parser can validate nesting, but it adds recursion overhead and may use $O(n)$ call-stack depth without improving the bound.
- **Single character:** Any legal one-character input is either an unmatched opener or closer, so the result is `False`.
- **Starts with a closer:** `not stk` short-circuits immediately and safely rejects it.
- **Ends with an opener:** The scan finishes, but `not stk` is false because the opener remains.
- **Adjacent pairs:** Strings such as `"()[]{}"` repeatedly empty the stack and are valid.
- **Deep nesting:** Strings such as `"{[()]}"` exercise last-in-first-out order and are valid when closing types reverse the opening sequence.
- **Correct counts but wrong order:** `"([)]"` is rejected at the first mismatched closer; balanced totals do not override nesting.
- **Non-bracket characters:** The contract excludes them. In this exact source they would enter the closer branch and be rejected, but that behavior is not intended as a general-purpose filtering policy.
- **Non-empty input guarantee:** The stated input is non-empty. If called with `""`, the exact code would return `True`, which is mathematically consistent with an empty balanced sequence but outside the supplied domain.
