## General

**Remember which opening bracket must close next**

Balanced totals are insufficient when several bracket types can nest. In `([)]`, the counts eventually balance, but `)` arrives while `[` is the most recently opened, still-unclosed bracket. Correct nesting demands that closures occur in the reverse order of openings.

A stack records exactly that order. The earliest unmatched opener remains near the bottom, and the most recent unmatched opener is on top. Each closer needs to agree with that top entry; searching for a matching opener deeper in the stack would incorrectly permit crossing pairs.

**Map every opener to its only legal closer**

The competitive source defines

```python
lookup = {"(": ")", "{": "}", "[": "]"}
```

Dictionary keys identify opening brackets, while each value is the closing bracket that must eventually match that opener. Consequently, `parenthese in lookup` answers whether the current character opens a new nested region. The spelling of the loop variable does not affect the algorithm; it holds one character of `s` at a time.

The contract states that `s` contains only the six bracket characters. Therefore a character that is not a dictionary key is guaranteed to be a closer. The implementation intentionally relies on that closed input alphabet.

**The stack describes the unfinished part of the prefix**

After any processed prefix, the algorithm maintains this invariant:

> `stack` lists every opening bracket in the prefix that has not been matched yet, from oldest to newest; `stack[-1]` is the only opener the next closing bracket is allowed to close.

The empty stack satisfies the invariant before scanning anything. On an opener, `stack.append(parenthese)` adds a new innermost unmatched bracket, so it correctly becomes the top. On a closer, the code must remove exactly the top opener and verify that its dictionary value equals the current closer.

**Understand the compound rejection condition**

The closer branch is

```python
elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
    return False
```

There are two invalid situations.

First, if `len(stack) == 0`, no unmatched opening bracket exists. A closer cannot be matched by a future opener because ordering requires its opener to be earlier. Python's `or` short-circuit behavior prevents `stack.pop()` from running in this case, so an early closer returns `False` without causing an empty-stack error.

Second, if the stack is not empty, the expression pops its most recent opener, looks up that opener's expected closer, and compares it with `parenthese`. A difference means the types do not match in the required nesting order. The popped state does not need restoration because the method returns immediately.

On equality, the branch condition is false and the scan continues. Popping the opener is exactly the state transition required by a successfully completed pair, so the invariant remains true.

**Why early rejection cannot discard a future valid outcome**

Once a prefix contains an unmatched closer, appending more characters cannot insert an opener before it. Once a prefix closes the wrong top type, later characters cannot reorder that already-read closer around the unfinished inner region. Validity is therefore prefix-sensitive: either violation is permanent. The immediate `return False` is logically final, not just a performance shortcut.

For `"(]"`, the first character pushes `(`. The second character is not a key, so the code pops `(`, obtains the expected `)`, and compares it with `]`. The mismatch rejects the string. For `"([)]"`, the closer `)` instead pops `[`, and `lookup['[']` is `]`, again exposing the crossing structure immediately.

**Require every opening bracket to be consumed**

If the scan finishes without rejection, every closer had a matching opener. There may nevertheless be unmatched openers left, as in `"(()"`. The final line

```python
return len(stack) == 0
```

returns `True` only when the unfinished-opening list is empty. This supplies the other half of matching: not only does every closer have a correct opener, but every opener has a closer.

**Trace both nested and adjacent pairs**

For `"([])"`, processing `(` then `[` creates `['(', '[']`. Reading `]` pops `[`, whose expected closer is indeed `]`; reading `)` then pops `(`. The empty final stack proves complete matching.

For `"()[]{}"`, the stack repeatedly changes from empty to a one-element list and back to empty. Nesting depth is only one, but all three types are handled by the same dictionary rule. The algorithm does not require pairs to be nested; it accepts any sequence whose individual nested regions are well formed.

**Why the return value exactly matches the definition**

Suppose the function returns `True`. Every closer passed the comparison with the most recent unmatched opener, proving correct type and last-in-first-out order. The stack is empty at the end, proving no opener remains. Thus all three validity conditions hold.

Suppose the input is valid. It can never reach the empty-stack rejection because every closer has an earlier unmatched opener. It can never reach the type-mismatch rejection because correct nesting requires that opener to be the top one and of the corresponding type. Every opener is eventually popped, so the final stack is empty and the function returns `True`. This establishes that no valid input is rejected and no invalid input is accepted.

## Complexity detail

Let $n$ be the number of characters in `s`.

- **Time complexity: $O(n)$.** The source scans characters once. Dictionary membership and lookup, stack append, and stack pop are constant expected-time operations here; the dictionary has exactly three fixed entries. Each character is pushed at most once and popped at most once.
- **Space complexity: $O(n)$.** An input containing only opening brackets leaves all $n$ of them in `stack`. The dictionary occupies constant space. More precisely, the peak stack length is the greatest number of simultaneously unmatched openers, or the maximum nesting depth, which can be $n$ for an invalid all-opening input and proportional to $n$ for a deeply nested valid input.

An invalid string may return early in less than $n$ work, but worst-case valid strings and invalid strings detected at the end require the full linear scan.

## Alternatives and edge cases

- **Set of complete pairs:** The optimal variant pops an opener, concatenates it with the closer, and checks membership in `{'()', '[]', '{}'}`. It expresses the same rule with a different constant-size lookup.
- **Closer-to-opener map:** Mapping `')'` to `'('` and so forth lets the closer select its required top directly. It has the same complexity and may make closer detection more explicit.
- **Counters per type:** They lose relative nesting information and can incorrectly accept crossing arrangements such as `"([)]"`.
- **Repeated pair removal:** Continuously deleting `()`, `[]`, and `{}` eventually recognizes valid strings but may rebuild and rescan the string quadratically.
- **Starts with `)`, `]`, or `}`:** The empty-stack operand is true, so short-circuit evaluation safely rejects the string.
- **Only opening brackets:** Every character is pushed; the non-empty final stack causes rejection.
- **Only closing brackets:** Rejection occurs on the first character.
- **One bracket pair:** A matching pair pushes then pops and returns `True`; a mixed pair fails the dictionary comparison.
- **Duplicate bracket types:** Repetition is normal. `"((()))"` is valid because each closer consumes the current top `(`.
- **Adjacent valid regions:** `"{}[()]"` is valid even though the first pair finishes before the later nested region begins.
- **Legal length up to $10^4$:** The iterative stack avoids recursion-depth concerns and comfortably maintains linear work.
- **Empty string outside the contract:** The exact source returns `True` because no mismatch occurs and the stack remains empty.
- **Unexpected characters outside the contract:** Any non-key character enters the closer branch and normally fails comparison. The method is specified for bracket-only strings, not for ignoring arbitrary text.
