# Guided Example: Word Frequency

We trace the step-by-step Unix shell stream transformation pipeline and single-pass `awk` associative array evaluation on representative text files:

- **Input File `words.txt`:**
  ```text
  the day is sunny the the
  the sunny is is
  ```
- **Required output:**
  ```text
  the 4
  is 3
  sunny 2
  day 1
  ```

This instance demonstrates Unix pipeline stream processing, breaks down tokenization (`tr -s ' ' '\n'`), adjacent grouping (`sort | uniq -c`), numeric descending ranking (`sort -nr`), and field reordering (`awk '{print $2, $1}'`), and analyzes execution complexity in $O(W \log W)$ time.

---

## 1. Instance & Teaching Goal

Given a text file `words.txt` containing space-delimited lowercase words:
```text
the day is sunny the the
the sunny is is
```
Compute the frequency count of each unique word, and print the result sorted by descending frequency in the format:
$$
\text{<word> <count>}
$$

Analyzing the token counts:
- `"the"`: appears $3$ times on line 1, $1$ time on line 2 $\implies$ total $= 4$.
- `"is"`: appears $1$ time on line 1, $2$ times on line 2 $\implies$ total $= 3$.
- `"sunny"`: appears $1$ time on line 1, $1$ time on line 2 $\implies$ total $= 2$.
- `"day"`: appears $1$ time on line 1, $0$ times on line 2 $\implies$ total $= 1$.
Sorted descending by frequency:
$$
\text{"the 4"} \to \text{"is 3"} \to \text{"sunny 2"} \to \text{"day 1"}
$$

The Unix philosophy solves this by composing modular standard command-line utilities (`tr`, `sort`, `uniq`, `awk`) via anonymous pipes (`|`), where the standard output of each filter feeds the standard input of the next.

---

## 2. Conceptual Foundation & Invariants

### Method A: The 5-Stage Unix Filter Pipeline
```bash
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
```

#### Pipeline Responsibilities:
1. **`tr -s ' ' '\n'` (Word Tokenization):**
   Translates each space into a newline character. The `-s` (squeeze) flag collapses runs of multiple consecutive spaces into a single newline, ensuring no empty blank lines are produced.
2. **`sort` (Lexicographical Pre-sorting):**
   The Unix `uniq` utility only collapses **adjacent** matching lines. Sorting first ensures all occurrences of identical words form contiguous clusters.
3. **`uniq -c` (Prefix Counting):**
   Counts consecutive identical lines and emits rows formatted as: `   <count> <word>`.
4. **`sort -nr` (Numeric Reverse Sort):**
   Sorts lines based on the first whitespace-delimited field numerically (`-n`) in descending/reverse order (`-r`).
5. **`awk '{print $2, $1}'` (Field Projection):**
   Swaps field 1 (`$1` = count) and field 2 (`$2` = word) to output the required `<word> <count>` schema.

### Method B: Single-Pass `awk` Associative Array
```bash
awk '{
    for (i = 1; i <= NF; i++) count[$i]++
} END {
    for (w in count) print w, count[w]
}' words.txt | sort -k2,2nr
```
`awk` splits each line on whitespace into fields `$1 \dots $NF`, accumulating frequencies in a hash map `count`, and sorts the output by column 2 numerically descending.

> **Invariant.** After `sort | uniq -c`, every unique word in `words.txt` appears exactly once with its true total frequency. After `sort -nr`, records are strictly ordered by non-increasing frequency.

---

## 3. Step-by-Step Worked Execution

We trace the data stream stage by stage through the pipeline on `words.txt`:

### Stage 1: Tokenization via `tr -s ' ' '\n'`
Input stream: `"the day is sunny the the\nthe sunny is is\n"`.
- Spaces squeezed and replaced with newlines:
  ```text
  the
  day
  is
  sunny
  the
  the
  the
  sunny
  is
  is
  ```

---

### Stage 2: Lexicographical Pre-Sort (`sort`)
Orders the 10 tokens alphabetically:
```text
day
is
is
is
sunny
sunny
the
the
the
the
```
*(Notice: identical words are now grouped into contiguous adjacent blocks)*.

---

### Stage 3: Deduplication and Counting (`uniq -c`)
Collapses contiguous blocks into counts:
- `day` (1 line) $\implies$ `1 day`
- `is` (3 lines) $\implies$ `3 is`
- `sunny` (2 lines) $\implies$ `2 sunny`
- `the` (4 lines) $\implies$ `4 the`

Stream state:
```text
1 day
3 is
2 sunny
4 the
```

---

### Stage 4: Frequency Ordering (`sort -nr`)
Sorts numerically on field 1 descending:
- $4 > 3 > 2 > 1$.

Stream state:
```text
4 the
3 is
2 sunny
1 day
```

---

### Stage 5: Field Swap (`awk '{print $2, $1}'`)
Swaps the count (field 1) and word (field 2):
```text
the 4
is 3
sunny 2
day 1
```

Emitted to standard output!

---

## 4. Complete Execution Trace

```text
File words.txt:
"the day is sunny the the \n the sunny is is"

Stage 1: tr -s ' ' '\n'  -> 10 one-word lines
Stage 2: sort            -> "day", "is" (x3), "sunny" (x2), "the" (x4)
Stage 3: uniq -c         -> 1 day, 3 is, 2 sunny, 4 the
Stage 4: sort -nr        -> 4 the, 3 is, 2 sunny, 1 day
Stage 5: awk '{print $2, $1}' ->
the 4
is 3
sunny 2
day 1
```

| Pipeline Stage | Command Invoked | Primary Transformation | Stream Snapshot (Top 2 Records) |
|:---:|:---|:---|:---|
| 0 | `cat words.txt` | Raw file ingestion | `"the day is sunny..."` |
| 1 | `tr -s ' ' '\n'` | Tokenize into 1 word per line | `"the\nday\nis..."` |
| 2 | `sort` | Alphabetical adjacency clustering | `"day\nis\nis\nis..."` |
| 3 | `uniq -c` | Count adjacent matching lines | `"1 day\n3 is..."` |
| 4 | `sort -nr` | Rank descending by numerical count | `"4 the\n3 is..."` |
| **5** | **`awk '{print $2, $1}'`** | **Format `<word> <count>`** | **`"the 4\nis 3..."` (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** `tr -s ' ' '\n'` handles irregular spaces by squeezing consecutive delimiters. Because `sort` guarantees that all identical words are adjacent, `uniq -c` correctly computes the total global frequency of each word. Sorting with `-nr` places the highest frequency first, and `awk` flips the columns to match the output contract.

**Completeness.** Every character in `words.txt` is consumed. No tokens are lost, and all unique words appear in the output.

---

## 6. Traps This Instance Exposes

- **Calling `uniq -c` Without Pre-Sorting:** In Unix, `uniq` only detects *adjacent* duplicates. If `the` appears on line 1 and line 2, calling `uniq -c` without `sort` emits multiple partial counts (e.g. `3 the` and `1 the`) instead of `4 the`.
- **Multiple Spaces Between Words:** If text contains `"the   day"`, standard `tr ' ' '\n'` creates empty lines. Adding `-s` (squeeze) collapses consecutive spaces into a single newline.
- **Output Column Ordering:** `uniq -c` outputs `<count> <word>` with leading spaces. LeetCode requires `<word> <count>`. Reversing columns via `awk '{print $2, $1}'` is mandatory.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(W \log W)$, where $W$ is the total number of words in `words.txt`. Tokenization takes $O(C)$ where $C$ is character count. Sorting words takes $O(W \log W)$, counting takes $O(W)$, and sorting distinct frequencies takes $O(U \log U)$ where $U \le W$ is unique words.
- **Auxiliary Space Complexity:** $O(W)$ pipe buffer and sorting memory.
