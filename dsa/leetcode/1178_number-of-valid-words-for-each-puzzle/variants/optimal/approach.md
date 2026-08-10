## General

A word is valid for a puzzle when two set conditions hold: every distinct letter used by the word belongs to the puzzle, and the word uses the puzzle’s first letter. Repeated occurrences do not change either condition. For example, `"aaaa"` and `"a"` use the same set of letters even though their lengths differ. This observation lets the solution replace each string with a compact integer bitmask.

**Encoding a set of letters as bits**

There are 26 possible lowercase letters. Bit zero represents `"a"`, bit one represents `"b"`, and so forth. For a character `c`, the expression

`1 << (ord(c) - ord("a"))`

creates an integer with only that character’s bit set. The code combines character bits using `|=`. Setting the same bit several times has no additional effect, which is exactly what is needed: the mask records presence, not frequency.

During preprocessing, the solution computes a mask for every word and increments `cnt[mask]`. Here `cnt` is a `Counter`, so all words with the same distinct-letter set share one entry. This aggregation is important. When a puzzle accepts that set, the program can add the number of matching words in one lookup rather than checking those words individually. Duplicate input words are still counted separately because every occurrence increments the stored frequency.

The code does not discard word masks containing more than seven distinct letters. Such a mask can never be a submask of a seven-letter puzzle, so it will never be queried and can never create a false match. Filtering those masks could save some memory, but omitting that optimization does not affect correctness.

**Turning a puzzle into a small search space**

Every puzzle contains exactly seven distinct letters. A valid word’s mask must be a subset of the puzzle mask. Instead of comparing the puzzle with every word mask, the solution enumerates the puzzle’s own submasks and looks each one up in the counter.

For a puzzle, the code first builds `mask` in the same way as for a word. It also stores

`i = ord(p[0]) - ord("a")`,

the bit position of the required first letter. The variable `j` starts as the complete puzzle mask. After examining one submask, the statement

`j = (j - 1) & mask`

moves to the next smaller submask. Subtracting one changes the low-order binary pattern, and the bitwise AND removes any bits that do not belong to the original puzzle. Repeating this operation visits every nonempty submask exactly once and eventually reaches zero.

The loop is `while j`, so it stops at the empty submask. That omission is harmless because every valid word must contain the first puzzle letter and therefore cannot have an empty mask. For each visited `j`, `j >> i & 1` tests whether the required bit is present. Only then does the code add `cnt[j]` to the puzzle’s total.

Although a seven-letter set has $2^7=128$ subsets, only half contain a specified letter. The exact code still walks through all 127 nonempty subsets and filters them with the bit test. This is a small fixed amount of work per puzzle. An alternative enumeration could force the first bit and enumerate only the other six letters, but the shipped loop remains easily fast enough.

**Why matching masks is equivalent to matching words**

If a word is valid, every bit in its mask also appears in the puzzle mask. Its mask is therefore one of the enumerated submasks. Because the word contains the puzzle’s first letter, that submask passes the required-bit test, and the word contributes through `cnt[j]`.

In the other direction, a counted counter entry corresponds to a submask of the puzzle, so none of its letters can lie outside the puzzle. The explicit bit test proves that its letter set contains the first puzzle letter. Every word represented by that counter entry therefore satisfies both validity rules. A mask is enumerated only once, so its stored frequency is added exactly once. These two directions show that `x` becomes precisely the number of valid words for the current puzzle.

For a concrete miniature example, suppose the word list contains `"aaaa"` once. Its mask has only the `"a"` bit. For puzzle `"aboveyz"`, the submask enumeration eventually reaches that one-bit mask. Since `"a"` is the puzzle’s required first letter, the test succeeds and the counter contributes one. A word using `"s"` would have a bit absent from this puzzle; its mask is never produced by the submask loop and cannot be counted.

The answer list receives one completed total per puzzle, in the same order as the input puzzles. The counter is constructed once and reused, which is the main advantage for this many-query problem.

## Complexity detail

Let $W$ be the sum of the lengths of all strings in `words`, let $m$ be the number of puzzles, and let each puzzle length be $L=7$.

Constructing all word masks touches every word character once, so it takes $O(W)$ time. Constructing a puzzle mask takes $O(L)$ time. Its submask loop visits $2^L-1$ nonempty masks, doing expected $O(1)$ counter work for each. The total time is

$$
O\left(W+m\left(L+2^L\right)\right).
$$

Because $L$ is fixed at seven, this simplifies to $O(W+m)$. The constant for each puzzle includes 127 submask iterations; hiding it in big-O notation does not mean the work is literally one operation.

Let $u$ be the number of distinct word masks stored in `cnt`. The counter uses $O(u)$ auxiliary space, with $u$ no greater than the number of words and no greater than $2^{26}$. Apart from the counter, the algorithm uses only a few integer variables. The returned list uses $O(m)$ output space. Thus auxiliary space excluding the required output is $O(u)$, and total memory including the answer is $O(u+m)$.

## Alternatives and edge cases

- **Enumerate only the optional six puzzle letters:** Keep the first-letter bit permanently set and enumerate submasks of the other six bits. This performs 64 lookups rather than walking 127 nonempty submasks and filtering, but both approaches have the same asymptotic bound for fixed seven-letter puzzles.
- **Compare every word with every puzzle:** Direct set tests are easy to understand, but up to $10^5$ words and $10^4$ puzzles create as many as $10^9$ pairs before character-checking costs are considered.
- **Trie of distinct sorted letters:** A trie can share prefixes between normalized word sets and search along puzzle letters. It is more elaborate to implement and reason about than the compact mask-frequency table.
- **Repeated letters inside a word:** Repetition sets an already-set bit again. The mask deliberately forgets multiplicity because validity depends only on which letters occur.
- **Duplicate words or different words with the same letter set:** Every occurrence increments the same counter entry. A valid mask contributes the full stored frequency, so no word is lost.
- **Words with more than seven distinct letters:** They cannot fit inside any seven-letter puzzle. The exact preprocessing stores them, but no puzzle submask can equal their masks, so they never contribute.
- **The first puzzle letter is mandatory:** Being a subset is not sufficient. The explicit shifted-bit test prevents a word made only from the other six puzzle letters from being counted.
- **The empty submask:** The `while j` loop does not process zero. No valid word can have an empty letter set or contain the required first letter with a zero mask, so skipping it is correct.
- **Counter lookup for an absent mask:** Python’s `Counter` returns zero for a missing key. The loop can query every submask without separate membership checks.
- **Input order:** Word preprocessing may combine masks freely, but puzzle results are appended one at a time, preserving the exact order requested by the contract.
