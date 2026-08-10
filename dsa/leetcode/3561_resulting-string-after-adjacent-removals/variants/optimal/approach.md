## General

The operation must always remove the **leftmost** adjacent consecutive pair, and a removal can expose a new adjacent pair. Repeatedly deleting from a Python string would require shifting or rebuilding characters many times. The solution instead uses a stack that represents the fully reduced result of the prefix processed so far.

For each new character, only one new adjacent pair can possibly appear: the stack’s last character next to the incoming character. If that pair is consecutive in the circular alphabet, both are removed by popping the stack. Otherwise the incoming character is appended.

**Recognizing consecutive letters**

Lowercase English letters have consecutive character codes. For ordinary neighbors such as `'a'` and `'b'` or `'m'` and `'n'`, the absolute code difference is one.

The alphabet is circular, so `'a'` and `'z'` are also consecutive. Their code difference is 25. Therefore

`abs(ord(c) - ord(stk[-1])) in (1, 25)`

recognizes every removable pair in either order:

- difference `1` covers ordinary alphabet neighbors;
- difference `25` covers the wraparound pair `a/z`;
- the absolute value makes order irrelevant.

Equal letters have difference zero and are not removed.

**The stack invariant**

After processing the first `t` input characters, `stk` equals the string produced by repeatedly applying the required leftmost-removal rule to exactly that prefix until no removable adjacent pair remains.

This invariant gives both correctness and efficiency.

Initially the processed prefix is empty and the empty stack is its reduced result.

Now assume the invariant holds before reading character `c`. The stack contains no removable adjacent pair; if it did, the prefix would not be fully reduced. Appending `c` cannot change adjacency between any earlier stack characters. The only newly created adjacent pair is `(stk[-1], c)`, provided the stack is nonempty.

- If that pair is not consecutive, no removal is possible anywhere, so appending `c` gives the fully reduced new prefix.
- If it is consecutive, that boundary pair is the only possible removable pair and hence is necessarily the leftmost one. Popping `stk[-1]` while discarding `c` performs exactly that required removal.

After a pop, no second removal is immediately necessary. The character now at the top of the stack has no new character to its right: the incoming `c` was removed together with the old top. The remaining stack is a prefix of the previously reduced stack, so it still contains no removable internal pair.

Thus the invariant holds after every character. At the end, the stack is exactly the mandated final string.

**Why this respects “leftmost,” not merely some removal order**

It is important not to assume that arbitrary removal orders always produce the same result. The proof above ties the stack to the stated leftmost process.

Before a new input character is considered, every removable pair wholly inside the earlier prefix has already been handled. When the new character creates a removable boundary pair, there is no earlier removable pair remaining to its left. The boundary pair is therefore the precise pair the rule would choose next.

The left-to-right stream effectively pauses after each input character until the available prefix is reduced. That is why the stack result matches the specified deterministic sequence of operations.

**How chain reactions appear naturally**

A removal can make characters that were separated in the original string relevant to later input.

For `s = "adcb"`:

- `a` is pushed.
- `d` is not consecutive with `a`, so it is pushed.
- `c` is consecutive with the top `d`, so `d` and `c` are removed, leaving `a`.
- `b` is now compared with the exposed `a`. They are consecutive, so both are removed.

The stack becomes empty, matching the repeated-removal result. No indices need to be shifted and no scan needs to restart.

**Why each input character is handled once**

Every character is pushed at most once. A pushed character can later be popped at most once. The algorithm never moves backward over the input and never restores a removed character.

The final `"".join(stk)` converts the surviving characters into the required string. Joining once at the end avoids the quadratic behavior that repeated immutable-string concatenation can cause.

**Circular behavior example**

For `s = "zadb"`, `z` is first pushed. When `a` arrives, the absolute code difference is 25, so the circular pair `za` is removed. The remaining `d` and `b` differ by two and survive, producing `"db"`.

This demonstrates why checking only code difference one would be incomplete.

## Complexity detail

Let `n` be the length of `s`. Each character causes constant-time stack work. Across the entire run there are at most `n` pushes and at most `n/2` pops, so the scan takes `O(n)` time.

Joining the surviving stack takes `O(r)` time for result length `r \le n`. Total time remains `O(n)`.

In the worst case no pair is removable, so the stack stores all `n` characters. Auxiliary space is `O(n)`. The joined result itself also has up to `n` characters; whether output storage is counted or not does not change the asymptotic bound.

## Alternatives and edge cases

- **Repeatedly scan and delete from the string:** This directly follows the statement but can require `O(n)` work per deletion due to searching and rebuilding, leading to `O(n^2)` time.
- **Linked list plus a moving pointer:** A linked structure can delete adjacent nodes cheaply, but finding and revisiting the correct leftmost candidate requires more bookkeeping. The stack is the natural representation for a left-to-right cancellation rule.
- **Use modular alphabet indices:** Mapping letters to `0` through `25` and checking whether their circular distance is one is equivalent. The source’s code differences `1` and `25` are simpler for lowercase ASCII-compatible ordering.
- **Ignore the circular pair:** Checking only absolute difference one would fail on `"az"` and `"za"`, both of which must disappear.
- **Empty stack:** The condition begins with `stk and ...`, so the source never reads `stk[-1]` when no survivor exists.
- **One-character input:** The character is pushed and returned because no adjacent pair exists.
- **Two removable characters:** They produce an empty stack and therefore the empty string.
- **Equal adjacent letters:** Their code difference is zero, so they remain; equal letters are not consecutive under the rule.
- **Complete cancellation:** `join` of an empty list is `""`, so no special return branch is needed.
- **No cancellation:** Every character remains in original order because the stack only appends, and the output equals `s`.
- **New adjacency after a removal:** The exposed stack top is compared with the next input character when it arrives, exactly as in the `"adcb"` trace.
- **Order sensitivity:** The invariant proves this stack simulates the required leftmost sequence; it is not relying on an unstated freedom to choose arbitrary removable pairs.
- **Lowercase constraint:** The `ord` difference test depends on the promised lowercase English alphabet. Other alphabets or case combinations would require a different successor relation.
