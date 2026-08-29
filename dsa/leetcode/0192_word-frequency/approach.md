## General

**View the shell pipeline as staged data transformations**

The script turns a text file into one word per record, sorts equal words
together, counts adjacent equal records, sorts those counts from largest to
smallest, and finally rearranges each line into the requested `word count`
format. Each command has one small responsibility, and the pipe operator sends
one command's standard output into the next command's standard input.

The complete pipeline reads the fixed file `words.txt`; it does not consume
function parameters or caller-provided standard input. Its final command writes
to standard output, matching the Reference contract.

**Normalize spaces into line boundaries**

`cat words.txt` streams the file contents. `tr -s ' ' '\n'` translates every
space into a newline. The `-s` option squeezes repeated translated characters,
so a run of several spaces becomes one newline rather than several empty
records.

Existing newline characters pass through unchanged. Under the Reference's
restricted content—lowercase word characters, spaces, and the physical line
boundaries of the file—every word consequently occupies its own line. This is
the representation the following Unix tools expect.

The initial `cat` is not necessary; `tr -s ' ' '\n' < words.txt` could read the
file directly. It is nevertheless logically correct and makes the left-to-right
pipeline visually explicit.

**Sort words so equal values become adjacent**

The first `sort` orders the one-word lines lexicographically. Its purpose is not
the final display order. It prepares the stream for `uniq`, which only combines
equal lines that are next to one another.

Without this sort, occurrences of `the` separated by other words would form
different runs and `uniq -c` would report several partial counts. Sorting turns
all occurrences of each word into one contiguous block.

**Count each contiguous block**

`uniq -c` emits one line for each distinct word, prefixed by the number of lines
in that word's block. Its conceptual output for the example is similar to:

`1 day`

`3 is`

`2 sunny`

`4 the`

Leading alignment spaces added by `uniq -c` do not matter because later `sort`
and `awk` split fields on whitespace.

**Sort by frequency rather than by word**

The second command `sort -nr` interprets the beginning of each line as a number
and orders numerically in reverse, or descending, order. Because the count is
currently field one, the largest count appears first.

The Reference guarantees every word has a unique frequency, so no tie-breaking
rule is needed. If ties were possible, `sort -nr` could use the remaining text
as an implementation-dependent or locale-sensitive secondary comparison, and
the problem would need to say whether that mattered.

**Reformat the two fields**

After counting, each line is `count word`, but the required output is
`word count`. The final `awk` action prints `$2` followed by `$1`. Default
output-field separation inserts one space, giving the exact requested shape.

For the example, the sorted count records become `4 the`, `3 is`, `2 sunny`,
and `1 day`; `awk` transforms them into `the 4`, `is 3`, `sunny 2`, and
`day 1`.

**Why every reported count is exact**

After translation, there is one stream record per word occurrence. The first
sort neither adds nor removes records; it only makes all equal words contiguous.
`uniq -c` replaces each maximal equal block with its word and the exact block
length. Since every occurrence of that word lies in the same block, that length
is its complete file frequency.

The remaining commands only reorder records and swap displayed fields. They do
not change any count. Therefore every distinct word appears exactly once with
its correct frequency, and the numeric reverse sort establishes descending
frequency order.

**Whitespace assumptions deserve precision**

The Reference says words are separated by one or more whitespace characters,
but also restricts file characters to lowercase letters and spaces; physical
newlines separate the example's lines. This exact `tr` invocation translates
ordinary spaces and naturally retains newlines, so it handles the stated data.
It does not translate tabs or carriage returns as generic whitespace.

Leading or trailing spaces can also create a leading or trailing newline. Runs
of translated spaces are squeezed, but a boundary newline can still represent
an empty record for downstream `sort` and `uniq`. If arbitrary boundary
whitespace had to be accepted, an `awk` field scan or a broader normalization
step would be safer. The stored pipeline relies on the conventional problem
input not producing meaningful empty tokens.

## Complexity detail

Let $n$ be the number of word occurrences and $c$ the total number of input
characters. Translation and final formatting are linear in their streams. The
first sort processes $n$ word records in $O(n\log n)$ comparison time, and the
second sorts at most $u$ distinct-word records in $O(u\log u)$, where
$u \le n$. This matches the manifest's $O(n\log n)$ dominant bound, with word
comparison costs depending on word lengths and locale.

Sorting tools may use memory and temporary files proportional to the data.
`uniq` itself needs only the current run, but the whole pipeline has $O(n)$
working-storage scale under the manifest model.

## Alternatives and edge cases

- **Single `awk` counter:** Scan all fields into an associative array, print counts, then sort by the second field; this is the competitive variant and handles general field whitespace better.
- **Direct input redirection:** Replace `cat words.txt | tr ...` with `tr ... < words.txt` to avoid an unnecessary process.
- **`grep -o` tokenization:** Extract lowercase runs explicitly, but behavior and options vary across environments.
- **Repeated spaces:** `tr -s` collapses them into one delimiter.
- **Line breaks:** Existing newlines already separate records and need no translation.
- **Tabs or carriage returns:** Not translated by the exact command; use `awk` or a complete whitespace class if the domain expands.
- **Leading or trailing spaces:** May expose empty-record behavior; filter empty lines for a generalized script.
- **One distinct word:** `uniq -c` emits one record and both sorts remain harmless.
- **Unique-frequency guarantee:** Makes unspecified tie ordering irrelevant.
- **Locale:** Can affect lexical comparison cost/order in the preparatory sort but not grouping equality for identical lowercase words.
