## General

Each copy of `"balloon"` consumes a fixed collection of letters:

- one `"b"`,
- one `"a"`,
- two `"l"` characters,
- two `"o"` characters,
- and one `"n"`.

Every input character can be used at most once. Therefore, each required letter places an independent upper bound on the number of complete words that can be assembled. The answer is the smallest of those five capacities—the bottleneck resource.

**Count the available characters once**

The solution builds `cnt = Counter(text)`. A `Counter` maps each character to its frequency in the entire input. This scan is sufficient because the problem permits rearranging which occurrences form each word; original positions do not matter.

Characters outside `"balloon"` remain in the counter but never participate in the final minimum. They cannot substitute for a required letter, so ignoring them after counting is correct.

Python’s `Counter` has a useful missing-key behavior: looking up a character that never appeared returns zero rather than raising an error. Consequently, the same code naturally handles a missing required letter. Its zero capacity will make the answer zero.

**Convert raw counts into word capacities**

The letters `"b"`, `"a"`, and `"n"` appear once per target word. If the text contains $x$ copies of one of them, that letter can support $x$ balloons.

The letters `"l"` and `"o"` each appear twice. If there are $x$ available copies, only $\lfloor x/2\rfloor$ complete pairs can be supplied. An unpaired extra letter is unusable.

The exact code transforms those two counter entries in place:

`cnt['o'] >>= 1`

and

`cnt['l'] >>= 1`.

For nonnegative integers, shifting right by one bit is integer division by two. Thus the stored `"o"` and `"l"` values become their whole-word capacities rather than their raw frequencies. This bit operation is compact, but `//= 2` would express the same arithmetic more directly.

**Take the bottleneck over unique required letters**

After the adjustments, the code evaluates

`min(cnt[c] for c in 'balon')`.

The string `"balon"` intentionally contains each distinct letter of `"balloon"` once. The doubled requirements for `"l"` and `"o"` have already been incorporated by halving their counts, so repeating them in the minimum is unnecessary.

Suppose the capacities are three for `"b"`, five for `"a"`, two for paired `"l"`, four for paired `"o"`, and three for `"n"`. At most two balloons can be built because a third would require six `"l"` characters but only enough pairs for two exist. Every other letter can support at least two, so two complete copies are also achievable. The minimum is both an upper bound and a construction count.

For `text = "nlaebolko"`, every single-use letter exists at least once, and both `"l"` and `"o"` exist at least twice. Each normalized capacity is at least one, while some are exactly one, so the answer is one.

For `"leetcode"`, required letters such as `"b"` and `"a"` are absent. Their counter values are zero, so the minimum is zero without any special case.

**Why the minimum is exactly attainable**

Let $r$ be the minimum normalized capacity. Every required character can supply at least the amount needed for $r$ copies of `"balloon"`. Selecting one `"b"`, one `"a"`, two `"l"` characters, two `"o"` characters, and one `"n"` for each of those $r$ copies uses no character more than once. Thus $r$ balloons can be formed.

Now consider any attempt to form $r+1$ copies. The letter whose normalized capacity equals $r$ cannot supply its required multiplicity for $r+1$ complete words. No other character can replace it. Therefore, $r+1$ copies are impossible. The lower and upper bounds meet, proving that the minimum is the maximum feasible count.

The approach never needs to construct the target strings. Counting resource availability is enough because all target copies have the same fixed recipe and there are no positional restrictions.

## Complexity detail

Let $n$ be the length of `text`. Constructing `Counter(text)` visits every character once and takes $O(n)$ time. The two shifts and the minimum over five distinct target letters take $O(1)$ time. Overall time complexity is $O(n)$.

The counter can contain at most 26 keys because the input consists only of lowercase English letters. This alphabet size is fixed, so auxiliary-space complexity is $O(26)=O(1)$. If the alphabet were unbounded, the map would instead use space proportional to the number of distinct input characters.

The result is at most $\lfloor n/7\rfloor$ because `"balloon"` has seven characters. Python integer arithmetic is easily sufficient.

## Alternatives and edge cases

- **Five explicit integer counters:** Increment only `b`, `a`, `l`, `o`, and `n` while scanning. This also gives $O(n)$ time and $O(1)$ space and avoids storing irrelevant letters.
- **General target-frequency division:** Count both the input and an arbitrary target, then minimize `available[c] // required[c]` over target characters. This generalizes the reasoning beyond the fixed word `"balloon"`.
- **Repeatedly remove target letters:** Simulating one constructed word at a time is more cumbersome and can repeat work that the frequency division performs immediately.
- **Missing required letter:** `Counter` returns zero, and the final minimum correctly returns zero.
- **Odd number of `l` or `o` characters:** The extra unpaired occurrence is discarded by floor division through the right shift.
- **Many irrelevant letters:** They increase scan time only linearly and do not influence the bottleneck minimum.
- **Empty construction is allowed:** When no complete target can be made, returning zero is valid; the method never forces a partial word.
- **Why `"balon"` has one `l` and one `o`:** Their multiplicities were already normalized. Taking the same capacity twice would not change the minimum but would obscure the intent.
- **Right shift safety:** Character counts are nonnegative, so `x >> 1` equals $\lfloor x/2\rfloor$. This equivalence would require more care for negative values, which cannot occur here.
- **Each occurrence used once:** Frequency subtraction is implicit in the capacity calculation. Forming $r$ words consumes exactly the required multiples and never exceeds any available count.
