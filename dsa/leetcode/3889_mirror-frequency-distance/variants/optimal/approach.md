## General

The answer depends only on how many times each character occurs. The positions of those characters in the string do not matter. This immediately suggests separating the work into two stages:

1. count all characters; and
2. compare the two counts belonging to each mirror pair.

The source implements exactly that idea with a `Counter` and a small visited set.

**The mirror mapping is two independent reversals**

Letters and digits belong to different character sets. A letter is mirrored within the 26 lowercase letters, while a digit is mirrored within the ten decimal digits.

For a lowercase letter `c`, its zero-based alphabet position is

$$
p=\operatorname{ord}(c)-\operatorname{ord}(\texttt{'a'}).
$$

Reversing positions $0$ through $25$ changes $p$ into $25-p$. The source reconstructs the corresponding character as

$$
\operatorname{chr}\!\left(
\operatorname{ord}(\texttt{'a'})+25-p
\right).
$$

Thus `a` maps to `z`, `b` maps to `y`, and `m` maps to `n`. Applying the formula twice returns to the original letter.

For a digit, the same reversal is simpler. After converting `c` to its integer value $d$, its mirror is $9-d$, converted back to a string. Consequently `0` pairs with `9`, `1` with `8`, and `4` with `5`.

Both domains have even size, so no valid character is its own mirror. The 36 possible characters form exactly 18 disjoint unordered pairs: 13 letter pairs and 5 digit pairs.

**Why frequency counting is sufficient**

For one pair $\{c,m\}$, the required contribution is

$$
\left|\operatorname{freq}(c)-\operatorname{freq}(m)\right|.
$$

No index, adjacency, or ordering information appears in this expression. Once `freq = Counter(s)` has been built, every needed value is available in constant time.

The source iterates over `freq.items()` rather than over all 36 allowed characters. That is enough because a pair for which neither character appears contributes $|0-0|=0$. If exactly one member appears, that present member is encountered and `freq[m]` evaluates to zero. Python's `Counter` returns zero for a missing key, which is precisely the frequency required by the definition.

**How one unordered pair is counted once**

The subtle part is avoiding both orientations. If `b` and `y` both occur, iterating over distinct characters eventually sees both `b` and `y`, but the pair's absolute difference must be added only once.

The set `vis` records the character that represented each pair when that pair was first processed. Suppose `c` is the first encountered member:

1. The source computes its mirror `m`.
2. Because the pair has not yet been handled, `m` is not in `vis`.
3. The source adds `c` to `vis` and adds $|\texttt{freq[c]}-\texttt{freq[m]}|$ to `ans`.
4. If `m` also occurs, its later iteration computes mirror `c`.
5. Now `c in vis` is true, so that reverse orientation is skipped.

At first glance, adding only `c` rather than both `c` and `m` may look incomplete. It is nevertheless sufficient. The later member tests whether its mirror—the earlier member—is present in the set. If the mirror character never appears in the string, no later iteration exists and no duplicate can occur.

This also shows that the result does not depend on which member happens to be encountered first. Reversing the representative changes

$$
|\operatorname{freq}(c)-\operatorname{freq}(m)|
$$

into

$$
|\operatorname{freq}(m)-\operatorname{freq}(c)|,
$$

which is identical.

**A complete trace**

For `s = "ab1z9"`, the nonzero frequencies are one each for `a`, `b`, `1`, `z`, and `9`.

- When `a` is encountered, its mirror is `z`. Their counts are both one, so the contribution is zero, and `a` enters `vis`.
- For `b`, the mirror `y` is absent. `Counter` supplies frequency zero, so the contribution is one, and `b` enters `vis`.
- For `1`, mirror `8` is absent, giving another one.
- When `z` is encountered, its mirror `a` is already in `vis`, so the already-counted pair is skipped.
- For `9`, mirror `0` is absent, giving the final one.

The sum is $0+1+1+1=3$.

**Why all required pairs are covered**

Take any unordered mirror pair that has at least one member in `s`. Among its members that occur, one is encountered first. The skip condition cannot discard that first member because its opposite member has not previously represented the pair. Therefore the contribution is added. If the second member is later encountered, the first member is in `vis`, so the duplicate is discarded. Each relevant pair contributes exactly once, and irrelevant all-zero pairs contribute nothing. Summing those pair contributions produces the required answer.

The implementation uses `c.isalpha()` to distinguish the two formulas. Under the stated input contract, every character is either a lowercase English letter or a digit, so this test selects the correct domain.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Constructing `Counter(s)` reads all $n$ characters, so it costs $O(n)$ time.

There are only 36 possible distinct input characters. The second loop therefore runs at most 36 iterations. Each iteration performs constant-time arithmetic, character conversion, dictionary access, and set access. Its time is $O(36)$, conventionally written $O(1)$ with respect to $n$.

The total running time is

$$
O(n).
$$

The frequency counter holds at most 36 keys, and `vis` also holds at most one representative per encountered pair. Their sizes are bounded by the fixed alphabet rather than by the string length. The auxiliary space is consequently

$$
O(1)
$$

with respect to $n$. If the alphabet were not fixed, the more general statement would be $O(\sigma)$ space for $\sigma$ distinct allowed characters.

The returned value is a single integer. Python integers do not overflow, and the answer is at most $n$: every absolute pair imbalance can be charged to occurrences in that pair, and the 18 pairs partition the character domain.

The checked-in source refers to `Counter` without importing it in this file. Its algorithmic bounds assume the execution harness supplies that standard-library name, as the surrounding solution environment is expected to do.

## Alternatives and edge cases

- **Iterate over 18 predetermined pairs:** A fixed table such as `(a,z)` through `(m,n)` and `(0,9)` through `(4,5)` removes the need for `vis`. It has the same $O(n)$ time and $O(1)$ space, but the source instead derives mirrors arithmetically.
- **Iterate over all 36 characters:** Comparing a character only when it is the lexicographically smaller member of its pair also prevents duplication. This remains constant work after frequency counting.
- **Mirror absent from the string:** Its frequency is zero, so a present character with count $v$ contributes $|v-0|=v$. `Counter` provides that zero without a special branch.
- **Both mirror counts equal:** The pair is still processed, but its contribution is zero, as with `b` and `y` in `"byby"`.
- **Only one distinct character:** The answer equals the string length because the character's mirror has frequency zero.
- **Pairs absent on both sides:** They need not be visited because their contribution is zero; this is why looping only through `freq.items()` is complete.
- **No self-mirror case:** Lowercase letters and digits both have even-sized domains, so the formulas never map a valid character to itself.
- **Letter and digit boundaries stay separate:** `a` cannot mirror a digit, and `0` cannot mirror a letter. The source chooses one formula before computing the opposite character.
- **Input contract matters for `isalpha`:** Other Unicode alphabetic characters would pass `isalpha()` but would not fit the lowercase-English arithmetic. The stated constraints exclude them.
- **Missing imports:** Standalone execution needs `Counter` from `collections`. This is an integration requirement, not a change to the counting logic.
