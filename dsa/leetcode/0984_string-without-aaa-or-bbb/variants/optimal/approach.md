## General

**Build safe blocks instead of choosing one character at a time**

The output must use exactly `a` copies of `'a'` and exactly `b` copies of `'b'`, while never containing three equal consecutive characters. The protected solution handles both requirements by repeatedly appending a short block whose composition reflects which character is more plentiful.

While both counts are positive, there are three cases:

- if `a > b`, append `"aab"` and consume two `a` characters and one `b` character;
- if `a < b`, append `"bba"` and consume one `a` character and two `b` characters;
- if `a == b`, append `"ab"` and consume one of each.

Each individual block is already safe: no block contains `"aaa"` or `"bbb"`. More importantly, the blocks spend the more abundant character faster. This steadily reduces an imbalance instead of allowing the majority character to accumulate into a dangerous run.

**Why the larger count receives two positions**

Suppose more `a` characters remain than `b` characters. If the construction alternated one-for-one forever, all `b` characters could be exhausted while too many `a` characters remained. Appending `"aab"` uses the scarce `b` as a separator between groups of at most two `a` characters. The difference `a - b` falls by one:

`(a - 2) - (b - 1) = (a - b) - 1`.

The symmetric `"bba"` case raises `a - b` by one when it is negative, again moving the difference toward zero. When counts are equal, `"ab"` preserves equality.

This is the core greedy idea: use two of the majority character when possible, but immediately follow them with the minority character that prevents a third copy.

**The subtractions are always legal**

The `while a and b` condition guarantees both counts are at least one. If `a > b` and `b >= 1`, then `a` must be at least two, so subtracting two from `a` is safe. Similarly, `a < b` guarantees `b >= 2`. In the equal case, both are positive and subtracting one from each is safe.

No count can become negative. Every appended block contains exactly the characters reflected by its accompanying subtraction, so the remaining counters always equal the number of unused characters.

**Why safe blocks remain safe when joined**

Checking blocks separately is not enough in general because a forbidden substring could cross a block boundary. The way the imbalance changes prevents that here.

After appending `"aab"`, the current text ends in one `b`. The new difference cannot jump from positive to negative: if `a - b >= 1` before the block, then the new difference is at least zero. Therefore, the next block cannot be `"bba"` because `b` cannot suddenly be the larger remaining count. It is either another `"aab"` or, after equality is reached, `"ab"`. Both begin with `a`, so the boundary is `"ba"`, never `"bbb"`.

The symmetric argument applies after `"bba"`. That block ends in `a`, and the difference cannot jump from negative to positive, so the next block begins with `b` rather than `"aa"`.

Once the counts are equal, appending `"ab"` leaves them equal. Repeating this case produces `"abab..."`, whose boundaries are also safe. Thus neither the interior of a block nor the boundary between consecutive blocks can create three equal characters.

**Finish the one remaining character type**

The loop stops when at least one counter reaches zero. If `a` remains, the code appends `'a' * a`; if `b` remains, it appends `'b' * b`.

The problem guarantees that a valid answer exists. For any valid arrangement, copies of one character must fit into the gaps around the other character in groups of at most two. Hence the necessary feasibility bounds are

`a <= 2(b + 1)` and `b <= 2(a + 1)`.

The block process spends the majority count in groups of two separated by the minority. Under these guaranteed-feasible inputs, when the minority is finally exhausted, at most two copies of the majority remain. The preceding majority block ends with the now-exhausted minority character, so appending one or two remaining copies is safe. For example, `a = 6` and `b = 2` becomes `"aab" + "aab" + "aa"`.

Both final `if` statements are written independently, but at most one can append a nonempty suffix because the loop stops only after one or both counts become zero.

**Trace an imbalanced input**

For `a = 4` and `b = 1`:

- `a > b`, so append `"aab"` and change the counts to `a = 2`, `b = 0`.
- The loop ends because no `b` remains.
- Append the remaining `"aa"`.

The result is `"aabaa"`. It has four copies of `a`, one copy of `b`, and its two groups of `a` have length two rather than three.

For `a = 1` and `b = 2`, the first block is `"bba"` and both counters become zero. That is one of several valid answers; the contract permits any valid one.

**Why the final counts and forbidden-substring rules both hold**

Maintain two facts after every iteration: the concatenated blocks are safe, and the counters exactly describe unused characters. They hold before the first iteration. The selected block uses available characters, the corresponding subtraction preserves the counter fact, and the boundary analysis above preserves safety.

At termination, the guaranteed-feasible remainder has length at most two and is appended after the opposite character or to an empty result. This remains safe. All counters then reach zero, meaning the output used exactly the requested multiplicities. Therefore, the joined string satisfies every requirement.

**Why the list of blocks is used**

Python strings are immutable. Repeatedly extending one large string can copy the already-built prefix many times. Appending small strings to `ans` is efficient, and `''.join(ans)` allocates the final result once from all blocks.

## Complexity detail

Let `L = a + b` denote the requested output length using the original input counts. Every loop iteration consumes at least two and at most three characters, and the final suffix consumes the rest. Across the whole method, exactly `L` characters are created. Constructing the blocks and joining them takes `O(L)` time.

The returned string itself requires `O(L)` space. The list stores `O(L)` total character content across its blocks and at most `O(L)` block references, so total construction space is `O(L)`. Excluding the required output and its block representation, the counters and other working variables use `O(1)` space.

Any correct method must spend `Omega(L)` time merely to produce an `L`-character answer, so the linear running time is asymptotically optimal.

## Alternatives and edge cases

- **Character-by-character greedy:** Append the more frequent remaining character unless it would match the previous two characters. This is also linear and more directly checks the forbidden pattern, but it performs a decision for every character instead of using safe blocks.
- **Pure alternation:** Alternating `"ab"` works only when counts are close. It can leave too many copies of the majority character at the end.
- **Backtracking over all strings:** It can search for a valid arrangement but explores many equivalent prefixes even though the feasibility guarantee makes a deterministic greedy construction sufficient.
- **Always append two of the majority:** The minority must be inserted as a separator. Appending majority pairs without the trailing opposite character could create a triple where blocks meet.
- **One count initially zero:** The loop is skipped and the only character is repeated. The existence guarantee implies its count is at most two; otherwise no legal string could exist.
- **Both counts zero:** Both final conditions are false, and joining the empty block list correctly returns the empty string of length zero.
- **Equal counts:** Repeated `"ab"` blocks consume both counts together and can never form a triple.
- **Difference of one:** The larger side may first use a three-character block, after which the remainder becomes equal and alternates safely.
- **Maximum counts:** The construction depends only on counts, not on recursion or search, so inputs up to one hundred are handled with the same linear work.
- **Any valid answer accepted:** The method does not try to produce lexicographically smallest output because the contract does not require a unique ordering.
