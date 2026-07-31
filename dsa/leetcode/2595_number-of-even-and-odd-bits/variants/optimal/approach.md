## General

**Read the binary digits from right to left.** The least significant bit is exactly index zero. The expression `n & 1` reads that bit, and `n >>= 1` removes it so that the next bit becomes the new least significant bit.

Maintain two counters and a current index. Add the extracted bit to counter `index & 1`: index parity zero selects the even counter and parity one selects the odd counter. Increment the index after every shift.

Each loop iteration records the original bit at exactly one index before discarding it. Consequently, every set bit contributes once to the counter matching its original index parity, and unset bits contribute zero. When `n` becomes zero, no represented bits remain and the two counters are the requested result.

## Complexity detail

A positive integer `n` has $\lfloor\log_2 n\rfloor + 1$ represented bits. Processing each bit once takes $O(\log n)$ time. The two-element output and scalar loop state use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Binary string:** Converting `n` to a string and counting characters at alternating reversed positions is also $O(\log n)$, but allocates $O(\log n)$ additional space.
- **Alternating bit masks:** Counting set bits in fixed masks for even and odd positions is concise when the integer width is known, but the masks are tied to that width.
- **Lowest legal value:** For `n = 1`, only index zero is set, so the result is `[1,0]`.
- **Leading zeros:** They are not part of the binary representation and do not need processing; stopping when `n` reaches zero handles this naturally.
