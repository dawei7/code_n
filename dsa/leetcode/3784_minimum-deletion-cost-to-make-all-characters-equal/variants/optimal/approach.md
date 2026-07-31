## General

Any valid nonempty result contains copies of one chosen character, say `x`. Once `x` is chosen, every position holding a different character must be deleted. Conversely, deleting an occurrence of `x` cannot improve validity, and because every cost is positive, doing so would only increase the total. Thus the optimal result for `x` keeps every occurrence of `x` and deletes everything else.

View the decision in terms of saved cost. Deleting all positions would cost `sum(cost)`. Keeping character `x` saves the sum of the costs attached to all occurrences of `x`. Therefore the cheapest valid deletion plan is obtained by maximizing this saved amount over the 26 lowercase letters.

During one scan, accumulate the total cost and a 26-entry array of saved costs by character. Subtract the largest character total from the overall total. At least one entry is positive because `s` is nonempty, so the chosen result always retains at least one character.

## Complexity detail

Let $N=\lvert s\rvert$. The scan performs constant work for each index, taking $O(N)$ time. The 26-entry lowercase-letter array has fixed size, so the auxiliary space is $O(1)$. The result may exceed 32-bit range because as many as $N-1$ costs of $10^9$ may be deleted.

## Alternatives and edge cases

- **Hash map by character:** Aggregate retained costs in a dictionary instead of a 26-entry array. This remains $O(N)$ time and uses at most 26 entries.
- **Evaluate every position:** Treat each index's character as a separate candidate and rescan the entire string to price its deletions. This is correct but repeats candidates and can take $O(N^2)$ time.
- **Already equal:** All cost belongs to one character, so subtracting that full amount returns `0`.
- **Singleton:** The only character must remain, again producing cost `0`.
- **Repeated chosen character:** All occurrences of the chosen letter should remain; deleting a matching occurrence is unnecessary and strictly more expensive.
- **Tied totals:** If several characters have the same maximum retained cost, any one yields the same minimum deletion cost.
- **Large total:** Use an integer type capable of representing sums above $2^{31}-1$.
