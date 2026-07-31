## General

Every permitted value lies between $1$ and $50$, so one integer can act as a fixed-size set. Bit `value` records whether `value` has already appeared. For each array element, compute `bit = 1 << value`. If that bit is absent, set it; if it is already present, this is the value's second occurrence and the value belongs in the answer.

The input guarantee that a value appears at most twice is important. It means the second-occurrence branch runs exactly once for every duplicated value and never runs for a unique value. XORing in the value on that branch therefore combines precisely the required set. Starting the accumulator at zero also gives the required result when no duplicate exists.

## Complexity detail

Let $n$ be the length of `nums`. The scan performs constant work per element, so the time complexity is $O(n)$. The `seen` mask and XOR accumulator occupy a constant number of machine-sized values because the value domain is fixed to $1$ through $50$, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Hash set:** Store encountered values in a set and XOR a value when it is already present. This is also expected $O(n)$ time, but its auxiliary storage grows with the number of distinct values if the fixed bound is ignored.
- **Frequency array:** Count into an array of length $51$, then XOR indices whose count is two. This remains $O(n)$ time and $O(1)$ space under the fixed domain, but requires a second pass over the domain.
- **Repeated counting:** Calling a full-array count for each element is simple and correct, but performs $O(n^2)$ work.
- **No duplicate:** The accumulator is never changed from $0$, which is the specified result.
- **XOR cancellation:** Different duplicated values may XOR to $0$; that does not mean the input lacked duplicates.
