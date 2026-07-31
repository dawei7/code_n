## General

**Interpret each response after the mutation.** Suppose the hidden state before a query is $s$ and the query is $x$. The API counts positions where $s$ and $x$ agree, then changes the state to `s XOR x`. A position is zero in this new state exactly when the two old bits agreed. Therefore, although the count is calculated before the update, the returned value is precisely the number of zero bits in the new hidden state.

**Establish a zero-count baseline.** Begin with `commonBits(0)`. Comparing the current state with the all-zero query counts its zero bits, and XOR by zero leaves the state unchanged. Save this response as the number of zeros before any bit is toggled.

**Toggle one previously untouched position.** For every bit position $i$ from $0$ through $29$, call the API with the singleton mask `1 << i`. All earlier singleton queries targeted different positions, so position $i$ still has its initial value immediately before this call. The query toggles only that position.

If the initial bit was one, the toggle changes it to zero and the returned zero count rises by one. If the initial bit was zero, the toggle changes it to one and the count falls by one. Comparing the new response with the zero count saved after the preceding query therefore determines the initial value of bit $i$. Record the bit when the count rises, then retain the new count as the baseline for the next position.

After position $i$ is processed, the answer agrees with the initial $n$ in every position from $0$ through $i$. Each later query touches a different, still-original position, so it cannot invalidate any recorded bit. Once all 30 positions have been examined, every possible bit of the initial number has been recovered and the assembled answer equals that original value.

## Complexity detail

The problem fixes the number width at 30 bits. The algorithm makes exactly 31 API calls: one zero query and 30 singleton queries. Each call and each update uses constant work, and only the running zero count and answer are stored. Under this fixed-width contract, time and auxiliary space are both $O(1)$. For a generalized $B$-bit interface, the method would require $B+1$ calls, $O(B)$ time, and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Restore after every singleton query:** Querying each singleton mask twice returns the hidden state to its initial value, allowing every first response to be compared with one fixed baseline. This is correct but uses 61 calls instead of tracking the changing zero count across 31 calls.
- **Query all one bits:** An all-ones query reveals only the number of set bits and complements the hidden state; it does not identify which positions were initially set.
- **Enumerate candidate numbers:** Trying the entire 30-bit domain ignores the direct one-bit information available from controlled XOR mutations and is unnecessary.
- **Initial value zero:** The baseline is 30, and every singleton toggle lowers the zero count, so no answer bit is set.
- **Initial value $2^{30}-1$:** Every singleton toggle raises the zero count, so all 30 answer bits are set.
- **Highest bit:** Position 29 must be queried; stopping at position 28 loses the most significant legal bit.
- **Mutation accounting:** Each singleton position is toggled exactly once. Comparing every response only with the original baseline would be wrong unless prior toggles were explicitly reverted.
- **Query range:** Zero and every mask from `1 << 0` through `1 << 29` lie within the API's reliable interval.
