## General

A word is uncommon only when its total behavior across both sentences is “appears exactly once.” If a word appears once in one sentence and never in the other, its combined count is one. Every other situation produces a different combined count:

- repeated in its own sentence gives at least two;
- present in both sentences gives at least two;
- absent from both sentences means it never becomes a candidate.

Therefore the two-sentence definition can be reduced to one frequency table over all words from both sentences.

**Split each sentence into words.** The contract guarantees lowercase words separated by single spaces, with no leading or trailing spaces. Calling `s1.split()` and `s2.split()` produces the word sequences directly. Python's default `split()` would also tolerate repeated whitespace, but the valid input does not require that extra behavior.

**Count each sentence, then combine.** `Counter(s1.split())` maps each word in the first sentence to its number of occurrences. The same is done for the second sentence. Adding two Counter objects adds counts for matching keys and retains words seen in either input:

```text
cnt = Counter(s1.split()) + Counter(s2.split())
```

If `apple` appears twice in the first sentence and zero times in the second, its combined count is two. If `this` appears once in each, its combined count is also two. If `sweet` appears once only in the first, its combined count is one. Only the last situation satisfies the definition.

The list comprehension iterates through `cnt.items()` and keeps exactly entries with `v == 1`. The problem accepts any answer order, so no sorting is necessary.

**Why combined count one is equivalent to uncommon.** Let $c_1(w)$ and $c_2(w)$ be the occurrence counts of word $w$ in the two sentences. Counts are nonnegative integers. The combined condition

$$
c_1(w)+c_2(w)=1
$$

has only two possible solutions: $(1,0)$ or $(0,1)$. Those are precisely “once in one sentence and absent from the other.” Conversely, every uncommon word has one of those count pairs and therefore has combined count one. This proves both directions of the equivalence.

**Why a set alone is insufficient.** A set can reveal whether a word appears in a sentence but not whether it appears more than once there. In `s1 = "apple apple"` and `s2 = "banana"`, set difference would wrongly consider `apple` unique to the first sentence. Its frequency is two, so it is not uncommon. The Counter retains exactly the multiplicity needed to reject it.

**Example trace.** For `"this apple is sweet"` and `"this apple is sour"`, combined counts are:

```text
this: 2
apple: 2
is: 2
sweet: 1
sour: 1
```

Filtering count one returns `sweet` and `sour`. Their relative order is an implementation detail and is not part of correctness.

The method is optimal in the basic sense that every character or word must be inspected to know whether a repetition exists. It builds one compact record per distinct word and performs no pairwise comparisons.

## Complexity detail

Let $L$ be the total number of characters in `s1` and `s2`, including spaces. Splitting, hashing words, combining counters, and filtering together process total text proportional to $L$ under expected hash-table behavior.

- **Time complexity:** $O(L)$ expected.
- **Space complexity:** $O(L)$ in the worst case for split word strings, counters, and the output when most words are distinct.

If measured by total word count $W$ and distinct word count $U$, counting is $O(W)$ expected and the frequency table is $O(U)$, while stored word text remains bounded by $L$.

## Alternatives and edge cases

- **One Counter over concatenated word lists:** `Counter(s1.split() + s2.split())` expresses the same combined-count idea. It creates an additional concatenated list, while Counter addition keeps the two stages explicit.
- **Manual dictionary:** Increment a normal mapping for every word from both splits. This has the same asymptotic behavior and avoids relying on Counter addition syntax.
- **Set symmetric difference:** It ignores repeated occurrences within one sentence and can report words that are not uncommon.
- **Compare every word with every other word:** This is unnecessarily quadratic; frequency counting summarizes all comparisons.
- **Word occurs once in each sentence:** Combined count is two, so it is correctly excluded.
- **Word repeats only in one sentence:** Combined count exceeds one, so it is excluded even though absent from the other sentence.
- **Every word is shared:** No count equals one, and the result is empty.
- **Every word is globally unique:** Every word is returned.
- **One-word sentences:** Equal words produce no answer; different words produce both words.
- **Any output order:** The comprehension follows Counter iteration order in current Python, but correctness must not depend on that order.
- **Lowercase-only contract:** Word comparison is case-sensitive, but uppercase forms never occur in valid input.
- **Single-space guarantee:** `split()` produces no empty words. It would also safely ignore extra whitespace in a broader input.
- **Output multiplicity:** Each uncommon word appears exactly once globally, so it appears once in the returned list.
