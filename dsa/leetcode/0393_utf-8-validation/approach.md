## General

**Read the array as a stream of characters, not one character**

The input may encode several UTF-8 characters back to back. A one-byte character can be followed by a three-byte character, which can be followed by another one-byte character. The validator must partition the complete sequence into legal character patterns and must finish exactly at a character boundary.

The exact solution is a small state machine. Its variable `cnt` is the number of continuation bytes still required for the current multi-byte character.

- `cnt == 0` means the next byte must begin a new character;
- `cnt > 0` means the next byte must have prefix `10`, after which the requirement decreases by one.

No decoded Unicode value needs to be constructed. The task, as defined here, asks only whether byte prefixes fit the specified one-through-four-byte structure.

**Recognizing a continuation byte**

When `cnt > 0`, the byte must have form `10xxxxxx`. Shifting an eight-bit value right by six removes the lower six payload bits and leaves only the two most significant bits. Therefore

```text
v >> 6 == 0b10
```

is exactly the continuation-byte test.

If it fails, the current character is incomplete or malformed, and the method returns `False` immediately. If it passes, `cnt -= 1` records that one required continuation byte has been consumed.

While continuation bytes are expected, the code does not reinterpret a byte beginning with `0`, `110`, `1110`, or `11110` as a new character. A multi-byte character must receive all of its continuation bytes first; character boundaries cannot overlap.

**Recognizing a one-byte character**

When `cnt == 0`, the code checks possible leading-byte patterns from shortest to longest.

The condition `v >> 7 == 0` examines the most significant bit. It is true exactly for `0xxxxxxx`, the required shape of a one-byte character. No continuation bytes follow, so `cnt` remains zero and the next array element starts another character.

For example, decimal `1` is binary `00000001`. Shifting it right seven positions yields zero, so it is accepted as a complete one-byte character.

**Recognizing multi-byte leading bytes**

For a two-byte character, the leader must be `110xxxxx`. Shifting right by five leaves the top three bits, so the test is

```text
v >> 5 == 0b110
```

One additional byte is required, so `cnt = 1`.

For a three-byte leader `1110xxxx`, shifting right four positions exposes `1110`. The solution sets `cnt = 2` because two continuation bytes must follow.

For a four-byte leader `11110xxx`, shifting right three positions exposes `11110`. The solution sets `cnt = 3`.

These counts exclude the leader itself. The current iteration has already consumed that byte; `cnt` records only what remains.

**Why the checks use different shift amounts**

Each legal leader is identified by a fixed prefix ending in zero:

| Character length | Leader shape | Shift | Exposed prefix | Required continuations |
|---:|---|---:|---|---:|
| `1` | `0xxxxxxx` | `7` | `0` | `0` |
| `2` | `110xxxxx` | `5` | `110` | `1` |
| `3` | `1110xxxx` | `4` | `1110` | `2` |
| `4` | `11110xxx` | `3` | `11110` | `3` |

Right shifting discards exactly the variable payload bits denoted by `x`. Equality then verifies every fixed prefix bit at once.

The `elif` chain matters because only a new-character state should classify leaders. Each legal eight-bit byte matches at most one listed leader shape. A byte beginning `10` is a continuation marker and matches none of the leader tests when `cnt == 0`, so it is correctly rejected as a stray continuation.

**Rejecting forbidden leaders**

If a new-character byte matches none of the four legal patterns, the method returns `False`.

This rejects:

- `10xxxxxx` at character boundaries, because a continuation cannot begin a character;
- `11111xxx` and longer runs of leading ones, because the stated UTF-8 characters may contain at most four bytes;
- `11111111`, which likewise describes no legal leader.

For example, decimal `250` begins `11111010`. It suggests five leading bytes by its run of ones, but five-byte characters are forbidden. It fails every leader comparison and is rejected immediately even if four apparently valid continuation bytes follow.

**Tracing a valid sequence**

For `data = [197, 130, 1]`:

- `197` is `11000101`. With `cnt == 0`, `197 >> 5` equals `0b110`, so it begins a two-byte character and sets `cnt = 1`.
- `130` is `10000010`. Since a continuation is required, `130 >> 6` equals `0b10`; it is accepted and `cnt` becomes zero.
- `1` is `00000001`. It has leading bit zero and forms a complete one-byte character.

The scan ends with `cnt == 0`, so both characters are complete and the method returns `True`.

For `data = [235, 140, 4]`, `235` begins `1110`, setting `cnt = 2`. Byte `140` begins `10`, reducing the count to one. Byte `4` begins `00`, not `10`, while a continuation is still required. The method returns `False` at that byte.

**Why the end-state check is essential**

Every byte inspected so far can have a legal local prefix while the sequence is still incomplete. For example, `[0b11100000, 0b10000000]` contains a valid three-byte leader and one valid continuation, but it is missing the second continuation.

The final statement `return cnt == 0` accepts only when the scan ends between characters. A positive count at the end means the final character was truncated.

**The state invariant and correctness**

Before each byte, all earlier bytes have been partitioned into complete valid characters plus, when `cnt > 0`, one valid leader and its already-seen continuation prefix. The value `cnt` is exactly how many more `10xxxxxx` bytes that unfinished character requires.

When `cnt > 0`, accepting only `10` preserves that partial character and reduces the exact remainder. When `cnt == 0`, accepting only one of the four legal leaders starts a character with the correct continuation count. Every rejected byte violates the only pattern allowed in its state.

Therefore no invalid local structure can pass. If the scan ends with zero remaining bytes, every input byte belongs to exactly one complete legal pattern. If it ends positive, the last pattern is incomplete. This proves the returned Boolean matches the stated encoding rules.

## Complexity detail

Let $n$ be the number of integers in `data`.

The for-loop processes every byte at most once. Each iteration performs a constant number of shifts, integer comparisons, and assignments. Total time is $O(n)$.

Only the integer state `cnt` and loop variable are used, so auxiliary space is $O(1)$. No binary strings, decoded characters, or stack are allocated.

The constraints already restrict every value to `0` through `255`, so each integer is exactly one byte. The reference note about using the least significant eight bits is automatically satisfied. If larger integers were actually allowed, the implementation would need to mask with `v & 0xFF` before applying these exact comparisons.

## Alternatives and edge cases

- **Binary-string conversion:** Format each byte as eight bits and inspect textual prefixes. This can be easier to visualize but allocates temporary strings and performs unnecessary conversion. Bit shifts express the same fixed-prefix tests directly.

- **Leading-one count:** Starting from mask `10000000`, count consecutive leading one bits, reject one or more than four, then validate the required continuations. This is equivalent; the exact solution enumerates the only four legal leaders explicitly.

- **Regular expression over a bit string:** A regex can describe the patterns after conversion, but constructing the full bit string costs extra memory and obscures the simple streaming state.

- **One-byte-only sequence:** Every byte beginning with zero leaves `cnt` at zero, so any number of such characters is accepted.

- **Stray continuation byte:** A top-level `10xxxxxx` matches no leader branch and is rejected.

- **Leader at the final array position:** A two-, three-, or four-byte leader leaves positive `cnt`; the final check rejects the truncated character.

- **Too few continuations:** The sequence ends with positive `cnt` and returns `False`.

- **Too many continuations:** After the required number, `cnt` becomes zero. An additional `10xxxxxx` is then treated as a new leader, matches none, and is rejected.

- **A leader where continuation is expected:** The `cnt > 0` branch tests only the top bits `10`; it rejects even an otherwise valid standalone leader because the current character has not finished.

- **Five-byte prefix:** Any leader beginning `111110` is invalid under the one-to-four-byte rule and reaches the final `else`.

- **Structural versus full modern Unicode validity:** The exact solution implements the bit-pattern rules stated by this problem. It does not additionally reject overlong encodings, surrogate code points, or values above the modern Unicode maximum when their byte prefixes fit the table. Those semantic checks are outside the supplied contract.

- **Input value width:** With the guaranteed range `0..255`, right shifts expose the intended leading bits. Without that guarantee, high bits would affect equality unless values were first masked to eight bits.
