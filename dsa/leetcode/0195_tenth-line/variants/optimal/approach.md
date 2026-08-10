## General

**Address one record and suppress everything else**

`sed` processes a text file as a sequence of records, normally one line per
record. The script gives it the fixed input path `file.txt`, so no arguments or
standard-input data are required from the caller.

The command combines two features: `-n` turns off automatic printing, and
`10p` says to print the record with line address 10. Together they make line ten
the only possible output.

**Understand sed's default behavior first**

Without `-n`, sed normally prints every input line after applying commands. A
bare `sed '10p' file.txt` would therefore print all lines once and line ten a
second time. That is not a filter for the tenth line.

The `-n` option suppresses this automatic output globally. Once suppression is
active, a line appears only if an explicit command prints it. This option is
therefore not a cosmetic flag; it is essential to the correctness of `10p`.

**Use a numeric address**

In sed syntax, the number before a command is an address selecting an input
record. Address `10` matches exactly the tenth record encountered. Command `p`
prints the current pattern space, which initially contains that entire original
line.

For records 1 through 9, the address does not match, so `p` is not executed and
automatic printing is already disabled. At record 10, `p` executes once. For
records 11 and later, the address again does not match and nothing is printed.

**Trace the example**

As sed reads `Line 1` through `Line 9`, each record is silently discarded after
its processing cycle. When `Line 10` becomes the pattern space, numeric address
10 matches and `p` writes `Line 10` to standard output.

The command does not parse the text `Line 10`; it relies only on record position.
A tenth line containing spaces, punctuation, or an empty string is still the
tenth record and is selected by the same address.

**Why files shorter than ten lines produce nothing**

If input ends after at most nine records, sed never encounters a record whose
number is 10. The explicit print command never runs, and `-n` prevents all
default output. The result is empty standard output, which matches the Function
Contract's “when that line exists” condition.

No error or placeholder is necessary. The absence of line ten is represented
by the absence of output.

**Why exactly the requested line is printed**

Soundness follows from the numeric address: the only explicit output action is
guarded by record number 10, so any printed record must be line ten.

Completeness follows because sed numbers records consecutively as it reads
them. If a tenth record exists, its address matches `10`, and `p` prints it.
There is only one tenth record, so it prints once. Earlier or later content
cannot change that positional decision.

**Preserve line contents**

The script has no substitution or transformation command. `p` writes the
pattern space as read, followed by sed's normal output newline. It does not
split the line into words, trim its leading characters, or reconstruct it from
fields.

The Reference calls the input a text file, so line-oriented sed semantics are
appropriate. As with most Unix text tools, details of a final missing newline
or CRLF carriage returns can be toolchain-dependent, but the line's visible
content is otherwise preserved.

**The exact command scans beyond the answer**

After printing line ten, ordinary sed continues reading later records even
though none can match address 10. This keeps the implementation extremely
short but means runtime depends on the complete file length rather than only
the first ten lines.

A variant such as `sed -n '10{p;q;}' file.txt` can print and quit immediately at
line ten. That reduces work on very long files while preserving the same output.
For a file shorter than ten lines, it still reaches end of file and prints
nothing.

**Working-directory requirement**

The relative filename is literal. The command succeeds only when its working
directory contains `file.txt` or the path is adjusted. Failure to open the file
is an environment error, not the “fewer than ten lines” case.

## Complexity detail

Let $n$ be the number of lines and $c$ the number of characters. The exact sed
command reads the entire file, so time is $O(c)$, commonly summarized as $O(n)$
when line size is treated as bounded. Although only one line is emitted, later
lines are still consumed.

Sed stores the current pattern space rather than all prior lines. Under a
bounded-line model, auxiliary space is $O(1)$. More precisely, it is
proportional to the longest current line, not to the number of lines.

## Alternatives and edge cases

- **Early-quit sed:** `sed -n '10{p;q;}'` stops immediately after printing, reducing long-file I/O.
- **Awk address:** `awk 'NR == 10' file.txt` uses the default print action for the tenth record.
- **Explicit awk action:** `awk 'NR == 10 { print $0 }'` states the output directly.
- **Tail and head:** Start output at line ten and take one line; readable but uses two processes and may rely on option dialect.
- **Fewer than ten lines:** Print nothing.
- **Exactly ten lines:** Print the final line once.
- **More than ten lines:** Print line ten only; the exact command still scans the rest.
- **Empty tenth line:** It is still printed as an output newline.
- **Long line:** Streaming memory depends on that line's size even though it is constant in the line-count model.
- **Missing file:** Produces a tool error rather than an empty valid result.
