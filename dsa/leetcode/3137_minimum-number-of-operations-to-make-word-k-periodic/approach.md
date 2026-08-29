## General

**View the word as aligned blocks**

Because $k$ divides the word length $n$, the string splits cleanly into

$$
b=\frac nk
$$

non-overlapping blocks of length $k$ beginning at indices $0,k,2k,\ldots,n-k$.

A string is $k$-periodic exactly when all of these aligned blocks are identical. The allowed operation also acts on exactly one aligned block: it replaces one block with the contents of another aligned block. Therefore, the problem becomes:

“Given $b$ block values, how many replacements are needed to make all values equal, when one replacement copies an existing value?”

**Keep the most frequent block**

Suppose a particular block string appears $f$ times. If we choose it as the final repeated block, those $f$ occurrences need no changes. Each of the other $b-f$ blocks can be replaced with a copy of one retained occurrence in one operation. The cost for that choice is $b-f$.

To minimize this quantity, maximize $f$. If `max_frequency` is the largest block count, the answer is

$$
b-\texttt{max\_frequency}.
$$

The exact code computes `b` as `n // k`. Its generator

`word[i : i + k] for i in range(0, n, k)`

produces every aligned block once. `Counter` maps each distinct block string to its frequency, and `max(...values())` obtains the largest frequency. The one-line return applies the formula directly.

**Why one operation per nonmatching block is both enough and necessary**

It is enough because at least one copy of the chosen most frequent block already exists. Keep one such copy unchanged as a source. For each block with a different value, choose its starting index as `i` and the retained source's starting index as `j`. One operation makes that entire destination block correct. Repeating this for all nonmatching blocks creates a periodic word.

It is necessary because an operation changes only one destination block. If the final repeated value is $s$, every original block not already equal to $s$ must be a destination of at least one operation. No single operation can repair two different block positions. Thus at least $b-f_s$ operations are required for final value $s$.

The final block must be a value that exists at some point, because the operation can only copy block contents already present. Even if newly copied occurrences become additional sources, their value traces back to an original block. Checking frequencies of original values therefore covers every possible final periodic string.

Combining the lower bound and construction proves that choosing a maximum-frequency block gives the global optimum.

**Example**

For `word = "leetcodeleet"` and $k=4$, the blocks are:

`"leet"`, `"code"`, `"leet"`.

There are $b=3$ blocks, and `"leet"` has maximum frequency 2. The answer is $3-2=1$: replace `"code"` with a copy of `"leet"`.

For a block list such as `["et","le","co","le","et"]`, the largest frequency is 2. Keeping either `"et"` or `"le"` requires $5-2=3$ replacements. Ties do not affect the minimum count.

**Why individual character differences do not matter**

An operation replaces a whole length-$k$ substring for one fixed cost. A block differing in one character costs one operation, and a block differing in all $k$ characters also costs one. Character-by-character distance is therefore irrelevant. Equality of complete block strings is the correct classification.

The alignment is equally important. Only indices divisible by $k$ may be chosen, so overlapping or shifted occurrences of the same text are not separate legal blocks. The generator uses exactly the allowed starting positions.

## Complexity detail

Let $n=\lvert\texttt{word}\rvert$ and $b=n/k$.

Creating each Python slice of length $k$ costs $O(k)$ time, and the total length of all $b$ slices is $bk=n$. Hashing and counting these strings also processes $O(n)$ total characters in the standard analysis. Taking the maximum scans at most $b$ frequencies. Total expected time is $O(n)$.

The counter can hold up to $b$ distinct block strings. The aggregate character content of those keys is at most $bk=n$, so auxiliary space is $O(n)$ in the worst case. The generator itself is lazy and uses only constant iteration state, but `Counter` retains its distinct string keys.

When many blocks are equal, Python dictionaries may reuse equal key representatives rather than storing every slice as a lasting key, so practical memory can be lower. The worst case of all distinct blocks still has linear total key content.

The returned count is one integer. The input word is not changed.

## Alternatives and edge cases

- **Sort the blocks:** Sorting groups equal block values and reveals the largest run, but costs $O(b\log b)$ string comparisons in addition to slicing.
- **Hash blocks without slicing:** Rolling hashes could count block identities with less copying, but collision handling is needed for exact correctness and the direct string counter already fits the constraints.
- **Compare characters column-wise:** One might try choosing the most common character at each offset, but the operation must copy an entire existing block, so independently chosen columns may form a block that cannot be copied.
- **Try every target block:** Comparing every candidate against every block takes $O(b^2k)$ time. Frequencies compute all candidate costs together.
- **`k = n`:** There is one block, its maximum frequency is one, and the answer is zero.
- **`k = 1`:** Blocks are individual characters, so the answer is string length minus the most frequent character count.
- **Already periodic:** All blocks are equal, maximum frequency is $b$, and no operation is required.
- **All blocks distinct:** Maximum frequency is one, so keep any one block and replace the other $b-1$.
- **Tied maximum frequencies:** Any tied block value leads to the same minimum operation count.
- **Source preservation:** A chosen source occurrence can be left unchanged while all other blocks are overwritten, so copied values never become unavailable.
- **Divisibility guarantee:** Because $k$ divides $n$, every slice has exactly length $k$. Without that guarantee, the final partial block would need separate treatment.
- **Aligned indices only:** The range step of $k$ deliberately ignores identical substrings starting at nonmultiples of $k$, since they cannot define a block operation.
