## General

**Let `awk` perform tokenization and counting together**

The competitive pipeline uses one `awk` program to read `words.txt`. By
default, `awk` splits every input record into fields on runs of whitespace.
`NF` is the number of fields on the current line, and `$i` is field number `i`.

The action loops from 1 through `NF` and executes `a[$i]++`. Associative array
`a` maps each word string to its occurrence count. A previously unseen key has
a numeric value treated as zero, so the post-increment naturally initializes
its first occurrence to one.

Unlike the optimal pipeline's explicit space translation, default `awk` field
splitting also handles tabs and repeated spaces. Blank lines have `NF = 0`, so
the loop performs no updates and no empty word is counted. This makes the
tokenization robust even beyond the Reference's simple lowercase-and-space
domain.

**Delay output until the full file has been read**

The main action counts fields line by line. The `END` action runs once after
all records are consumed. At that point, every occurrence has contributed one
increment to exactly one associative-array key.

`for(k in a) print k,a[k]` emits each distinct word and its final count. The
iteration order of an `awk` associative array is unspecified. That is fine
because a following `sort` establishes the required order.

The variable `k` in this loop is merely an array key and is unrelated to stock
or rotation parameters seen in neighboring problems. Its value is the current
word.

**Sort on the count field**

The `awk` output has two fields: word first, count second. The pipe sends these
records into `sort -k2 -nr`.

`-k2` starts the sort key at field two, `-n` requests numeric comparison, and
`-r` reverses it so larger counts come first. Numeric mode is essential: plain
text order would, for example, place count 10 relative to count 2 according to
characters rather than numeric magnitude.

The Reference guarantees all frequencies are unique, so the primary numeric
key totally determines the order. There is no need to specify a secondary word
key for ties.

**Trace the example**

On the first input line, `awk` increments `the`, `day`, `is`, `sunny`, `the`,
and `the`. On the second, it increments `the`, `sunny`, `is`, and `is`.

The final map contains counts `the: 4`, `is: 3`, `sunny: 2`, and `day: 1`.
The `END` loop may print these in any temporary order. Numeric reverse sorting
then emits exactly:

`the 4`

`is 3`

`sunny 2`

`day 1`

No final reformatting command is needed because `awk` already prints the word
before its count with its default single-space output separator.

**Why the counts are complete and exclusive**

Default field splitting identifies each word occurrence as one field. The
inner loop visits every field exactly once and increments the array entry named
by that field. Thus every occurrence contributes one to its own word and none
to any other word.

After the last line, `a[word]` equals the total number of occurrences of that
word across the entire file. The `END` loop emits each associative-array key
once, so no distinct word is omitted or duplicated. Sorting changes only the
record order, leaving word-count pairs intact.

**Understand the source complexity comment**

The file comments label time as $O(n)$ and space as $O(k)$, where its `k` means
the number of words, likely distinct words. Expected associative-array counting
is linear in the number of tokens. However, the required descending output
passes through `sort`, which sorts the $u$ distinct records and costs
$O(u\log u)$ comparisons in general.

Therefore the entire shell pipeline is not strictly guaranteed linear. The
manifest's $O(n\log n)$ time is a safe upper bound when $u \le n$, while a
tighter decomposition is expected $O(n + u\log u)$. Space is $O(u)$ for the
map plus sorting storage, which is $O(n)$ in the worst case where every word is
distinct.

**Shell and locale details**

The script assumes an `awk` and `sort` implementation supporting these standard
options. It reads the literal relative path `words.txt`, so its working
directory must contain that file.

Default `awk` output separation is one space. Word input contains only lowercase
letters, so no quoting or escape preservation issue arises. Since counts are
unique, locale-dependent secondary text ordering cannot affect the required
result.

## Complexity detail

Let $n$ be the number of word occurrences, $u$ the number of distinct words,
and $c$ the character count. `awk` scans the file in $O(c)$ time with expected
$O(1)$ associative updates per word, using $O(u)$ map space. Sorting the $u$
output records takes $O(u\log u)$ comparison time and up to $O(u)$ working
storage in the in-memory model.

Since $u \le n$, the manifest bounds $O(n\log n)$ time and $O(n)$ space safely
cover the pipeline. External `sort` may spill to temporary files rather than
holding all records in memory, but that changes the storage medium, not the
amount of data processed.

## Alternatives and edge cases

- **Sort and `uniq -c`:** Normalize to one word per line, group identical words, sort counts, and swap fields; more processes but no associative-array logic.
- **Pure `awk` with manual ranking:** Avoid external sort only by implementing a sort in `awk`, which is more code and not asymptotically better.
- **General whitespace:** Default field splitting handles runs of spaces, tabs, and blank lines naturally.
- **Leading or trailing whitespace:** Produces no empty field under default `awk` rules.
- **Empty file:** The map remains empty and the script prints nothing.
- **One word repeated:** The map has one key and sort passes through one record.
- **Unique-frequency guarantee:** Removes the need for a deterministic secondary key.
- **Very large file:** `awk` retains one entry per distinct word; external sort may use disk for its output records.
- **Relative file path:** Run from the directory containing `words.txt` or adjust the path explicitly.
- **Source comment:** Include the final sorting phase when stating end-to-end time complexity.
