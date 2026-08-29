## General

Today's span extends backward through consecutive prices less than or equal to today's price and stops immediately before the first greater price. A monotonic stack can skip whole already-summarized blocks instead of comparing today with every prior day individually.

Each stack entry is a pair `(price, span)`. Its span tells how many consecutive days ending at that stored day were less than or equal to that stored price and have already been compressed into the entry.

The stack's prices are strictly decreasing from bottom to top. When a new price arrives:

1. Start `cnt = 1` for today itself.
2. While the top stored price is less than or equal to today's price, pop it and add its entire stored span to `cnt`.
3. Push `(price, cnt)` and return `cnt`.

**Why a popped block can be absorbed completely.** Suppose top entry is `(p, span)` and $p\le\text{price}$. The entry represents a consecutive block ending at price $p$ in which every included daily price is at most $p$. By transitivity, every price in that block is also at most today's price. The entire block belongs to today's span, so adding its stored size is correct.

After popping one block, the next stack entry represents the immediately preceding unresolved block. The loop repeats while its boundary price is also no greater than today.

**Why the first greater price stops the span.** When the loop ends with a nonempty stack, its top price is strictly greater than today's price. That day cannot be included, and the span must stop there. Entries below it are even earlier and cannot be reached without crossing this blocking day, regardless of their values.

**Why equality is popped.** The definition includes prices less than or equal to today's price. Therefore a top price equal to today belongs to the span and must be absorbed. Using a strict `<` comparison would undercount repeated equal prices.

**Stack invariant.** After processing a call, stored prices decrease strictly from bottom to top. Before pushing, all top entries with price at most the new price have been removed. If an entry remains, its price is greater than the new price. Thus appending the new entry preserves the invariant.

Each entry's stored span is also correct: it begins with today and adds exactly the consecutive compressed blocks that are not blocked by a greater price.

For prices `100,80,60,70,60,75,85`:

- 60 has span 1.
- When 70 arrives, it pops 60 and has span 2.
- The next 60 has span 1.
- When 75 arrives, it pops that 60 and the compressed 70-block of size 2, giving $1+1+2=4$.
- When 85 arrives, it absorbs the 75-block of size 4 and the earlier 80-block of size 1, giving 6. Price 100 remains as the blocker.

The compression is lossless for future queries because only a block's boundary maximum and size matter when deciding whether a later price can absorb it.

**Why online processing is possible.** Each call uses only the stack summary of previous calls. It never needs future prices and returns immediately, satisfying the online interface.

## Complexity detail

Let $q$ be the number of `next` calls. A single call can pop $O(q)$ entries in the worst case, such as a large price after a long decreasing sequence. However, every entry is pushed once and popped at most once over the full operation history.

- **Total time across $q$ calls:** $O(q)$.
- **Amortized time per call:** $O(1)$.
- **Worst-case time for one call:** $O(q)$.
- **Space complexity:** $O(q)$ in the worst case for a strictly decreasing price sequence.

The manifest's $O(q)$ time describes the full sequence of operations, not a worst-case bound for each individual call.

## Alternatives and edge cases

- **Scan stored prices backward per call:** This is simple but can cost $O(q^2)$ total on increasing sequences.
- **Store all prices with a previous-greater index:** It can also answer spans, but the monotonic stack is the direct compressed representation.
- **Segment tree:** Supports more general historical queries but is unnecessary for this one-sided online span and has logarithmic operation cost.
- **First price:** No stack entry exists, so its span is one.
- **Strictly increasing prices:** Each new call pops all remaining entries, and spans grow by one each day. Total work remains linear because popped entries never return.
- **Strictly decreasing prices:** Nothing is popped, every span is one, and stack space grows to $q$.
- **Equal prices:** They are popped and combined because equality is allowed in the span.
- **One very large price:** It may absorb many compressed blocks in one call.
- **Greater blocker:** Once encountered, it stops the consecutive span even if still earlier prices are small.
- **No explicit day indices:** The stored block sizes contain exactly the distance information needed for the result.
- **Positive price bounds:** Comparisons are ordinary integer comparisons; magnitude does not change the method.
- **Amortized versus worst case:** Claiming every call literally executes constant work is inaccurate; constant time is an amortized guarantee.
