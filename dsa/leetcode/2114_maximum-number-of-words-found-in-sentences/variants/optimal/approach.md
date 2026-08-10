## General

**Use the sentence-format guarantee**

Every sentence is nonempty, has no leading or trailing spaces, and separates consecutive words with exactly one space.

Under these guarantees, a sentence with $w$ words contains exactly $w-1$ spaces. Therefore,

$$
\text{word count}=1+\text{space count}.
$$

The source evaluates `s.count(' ')` for every sentence, takes the maximum space count, and adds one:

`1 + max(s.count(' ') for s in sentences)`.

This avoids splitting sentences into word lists because only the count is needed.

**Why the formula works**

Consider a sentence with words

`word1 word2 word3`.

There are three words and two separators. Each separator marks exactly one boundary between neighboring words. With no leading or trailing spaces, there are no separators that fail to represent a boundary. With single spacing, each boundary contributes exactly one space.

The first word accounts for the added one; every later word is preceded by one of the counted spaces.

A one-word sentence contains zero spaces, and the formula returns one.

**Find the maximum without storing all counts**

The expression inside `max` is a generator. It computes one sentence's space count at a time rather than constructing a separate list of all counts.

`max` retains only the greatest count seen. Adding one after the maximum is equivalent to adding one to every individual count first because the same constant shifts all candidates equally:

$$
1+\max(c_i)=\max(1+c_i).
$$

The input guarantee `sentences.length >= 1` ensures `max` always receives at least one value and needs no default.

**Trace both examples**

For the first example, space counts are 4, 3, and 5. Their maximum is 5, and adding one returns 6 words.

For `["please wait", "continue to fight", "continue to win"]`, counts are 1, 2, and 2. The maximum is 2, so the result is 3. Multiple sentences may tie; the task requests only the maximum count, not which sentence attains it.

**Why scanning characters is necessary**

In the absence of stored word metadata, the algorithm must inspect sentence contents to distinguish how many separators they contain. `str.count` performs this scan internally.

The compact one-line source still has time proportional to total characters; it is not constant time merely because it contains one expression.

**Why the result is correct**

For each sentence, the format guarantees establish a one-to-one relationship between spaces and boundaries after the first word. Its computed `space count + 1` is therefore its exact word count.

The generator covers every sentence, and `max` selects the largest exact count. The returned integer is precisely the maximum number of words in any input sentence.

No sentence or character is modified.

**Dependence on the input contract**

If multiple spaces were allowed between words, counting spaces would overcount. If leading or trailing spaces were allowed, those spaces would not introduce new words. The solution is correct because the reference explicitly rules out all of those formats.

This is a good example of using a strong input guarantee to replace general parsing with a simpler statistic.

**Why adding one after `max` is safe**

The source does not explicitly calculate each sentence's word count before comparing them. It compares space counts and adds one only once at the end.

This preserves ordering because every sentence receives the same constant adjustment. If sentence A has more spaces than sentence B, it also has more words; if their space counts tie, their word counts tie. Therefore, the sentence with maximum separators is exactly a sentence with maximum words.

**What `s.count(' ')` returns**

The method counts non-overlapping occurrences of the one-character string `' '`. Since a single character cannot overlap itself in a meaningful multi-character pattern, this is simply the number of space characters.

It does not modify the sentence or create a token array. The implementation can scan characters internally and maintain one integer count.

## Complexity detail

Let

$$
S=\sum_{s\in\texttt{sentences}}\lvert s\rvert.
$$

Each `count` call scans its sentence, so total time is $O(S)$.

The generator, current count, and running maximum use constant auxiliary space. `str.count` does not build a list of matches, so auxiliary space is $O(1)$.

The input strings and returned integer are not counted as extra working storage.

## Alternatives and edge cases

- **`len(s.split())`:** Correct under the contract and more general about whitespace, but allocates a list of word substrings for each sentence.
- **Manual character loop:** It can count spaces with the same time and constant space, but `str.count` expresses the operation directly.
- **One-word sentence:** Zero spaces plus one gives one word.
- **Multiple sentences tie:** Only the maximum count is returned, so no tie-breaking is needed.
- **Nonempty sentence array:** Guarantees `max` is safe without a default.
- **No leading or trailing spaces:** Essential to the separator formula.
- **Exactly one separator:** Essential because repeated spaces would be overcounted.
- **Lowercase-only content:** Letter identity is irrelevant; only separator positions matter.
- **Very short sentences:** A length-one sentence still contains one word.
- **Generator laziness:** Individual counts are not retained after `max` processes them.
- **Compact code versus work:** The implementation still scans all $S$ characters.
- **Input preservation:** Sentences remain unchanged.
- **Add after maximum:** A uniform plus one commutes with taking the maximum, so no per-sentence word-count list is needed.
- **Tie preservation:** Equal separator counts imply equal word counts under the format contract.
