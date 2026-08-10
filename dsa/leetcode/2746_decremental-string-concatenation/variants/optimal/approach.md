## General

**Only the two endpoint characters affect the next join**

The current constructed string may become very long, but joining the next word can delete at most one boundary character.

If the next word is appended on the right, deletion depends only on the current last character and the word's first character. If the word is prepended on the left, deletion depends only on the word's last character and the current first character.

The entire interior content is irrelevant to every future length decision. This permits a compact state containing only endpoints and the next word index.

**State meaning**

`dfs(i, a, b)` returns the minimum additional length contributed by words from index `i` onward when the current constructed string begins with character `a` and ends with character `b`.

The length already accumulated is deliberately omitted. Every future option adds the same next word length minus a possible one-character overlap, so the recursion can return only the future contribution.

When `i` reaches `len(words)`, no word remains and the additional length is zero.

**Option one: append the next word**

Let `s = words[i]`. Appending produces `join(current, s)`.

The new first character remains `a`, and the new last character is `s[-1]`. If `b == s[0]`, the join deletes one of those equal boundary characters.

The exact code computes:

`x = dfs(i + 1, a, s[-1]) - int(s[0] == b)`.

Later, `len(s)` is added outside the minimum. Thus this branch contributes the full word length minus one exactly when the append boundary overlaps.

**Option two: prepend the next word**

Prepending produces `join(s, current)`.

The new first character becomes `s[0]`, and the current last character `b` remains. A deletion occurs when `s[-1] == a`.

The code computes:

`y = dfs(i + 1, s[0], b) - int(s[-1] == a)`.

Again, subtracting the Boolean accounts for the single deleted boundary character.

**Choose the better orientation**

Both choices must include all characters of `s` except a possible one-character overlap. Therefore the recurrence returns:

`len(s) + min(x, y)`.

This does not greedily choose the orientation with an immediate overlap. An orientation that saves nothing now may create better endpoint characters for many later words. Recursion compares the complete future cost of both choices.

**Initialize from the first word**

The process is required to begin with `words[0]`. Its length is unavoidable, and its endpoints are known.

The function returns:

`len(words[0]) + dfs(1, words[0][0], words[0][-1])`.

No join is performed for the first word, so no overlap subtraction belongs in this initial term.

**Trace words equal to aa, ab, bc**

Start with `"aa"`, length two, endpoints `a,a`.

Appending `"ab"` matches current last `a` with new first `a`, adding only one character and giving conceptual result `"aab"` with endpoints `a,b`.

Appending `"bc"` then matches `b` with `b`, adding one more character and producing length four. The recursion evaluates this path and all prepend alternatives, finding four as the minimum.

**Why interior strings never need construction**

Endpoint updates are exact under both operations. Deleting one of two equal boundary characters does not change the outside first and last characters except in one-character corner cases; the formulas still work because a word's first and last may be the same, and the concatenated current string is never empty.

Future overlap depends only on these updated endpoints. Thus two different constructed strings with equal `i,a,b` have identical sets of future length outcomes and can share a cached answer.

**Memoization**

`@cache` stores each `(i,a,b)` result. Without it, two branches per word would create up to $2^{n-1}$ orientation sequences.

There are only 26 possible first characters and 26 possible last characters. For each index, the endpoint dimension is fixed-size relative to input length.


At state `(i,a,b)`, every legal continuation must either append or prepend `words[i]`. The two recurrence branches compute the exact word length, exact one-character overlap, resulting endpoints, and optimal remaining continuation for those exhaustive choices. The base case is exact when no words remain. By induction backward over `i`, every cached state returns its minimum possible added length, and the initialized state returns the global minimum.

## Complexity detail

There are at most $n\cdot26^2=O(n)$ states under the fixed lowercase alphabet. Each state performs constant-time endpoint comparisons and two cache lookups, while obtaining `len` and endpoint characters is constant time. Total time is $O(n)$.

The memo cache can retain $O(n\cdot26^2)=O(n)$ results, and the recursion stack can reach depth $O(n)$. The exact auxiliary space is therefore $O(n)$.

The manifest's $O(1)$ space describes an iterative endpoint table that keeps only one layer. It does not describe this recursive cached source, whose cache grows with the number of words.

## Alternatives and edge cases

- **Iterative 26-by-26 DP:** Retain only current endpoint costs and achieve $O(n)$ time with $O(1)$ space under the fixed alphabet.
- **Construct every candidate string:** Exponential in orientation choices and wastes memory on irrelevant interiors.
- **Immediate-overlap greedy:** Can choose endpoints that cause worse future joins and is not generally optimal.
- **Single word:** The recursion starts at index one, immediately returns zero, and the answer is its length.
- **One-character word:** Its first and last endpoints are the same; both formulas remain valid.
- **Both orientations overlap:** Compare their future endpoint effects even though immediate savings tie.
- **Neither orientation overlaps:** The whole word length is added, but endpoint choice still matters.
- **Boolean subtraction:** Python converts true to one and false to zero.
- **No empty current string:** Every state begins from `words[0]`, so endpoints always exist.
- **Manifest mismatch:** Memoization and recursion require $O(n)$ rather than $O(1)$ space.
