## General

**Recognize four standalone solutions**

The competitive file contains four commands: two awk forms, one sed form, and
one tail/head pipeline. They are alternative ways to select line ten. They are
not supposed to run as successive stages.

If the file is executed unchanged, every command reads `file.txt` independently
and each prints the tenth line when it exists. The result is therefore four
copies of that line, violating the one-line output contract. A correct submitted
script must keep exactly one alternative.

**First awk form: explicit action**

`awk '{if(NR==10) print $0}' file.txt` executes its action for every input
record. `NR` is the current one-based record number. When it equals 10, the
action prints `$0`, which is the complete current line. On every other record,
the condition is false and the action emits nothing.

This form is beginner-friendly because both condition and output are visible,
though the outer braces and `if` are more verbose than awk requires.

**Second awk form: pattern plus default action**

`awk 'NR == 10' file.txt` treats `NR == 10` as a pattern. When the pattern is
true, awk performs its default action, `{ print $0 }`. When false, it performs
nothing.

The second form is logically identical to the first. It is shorter because awk
already defines printing the current record as the default behavior for a true
pattern. Both forms continue scanning the file after record ten unless an
explicit `exit` is added.

**Sed form: suppress and explicitly print**

`sed -n 10p file.txt` disables sed's default printing with `-n`. Address `10`
selects exactly record ten, and command `p` prints it. If `-n` were absent, all
records would print automatically and the tenth would print an extra time.

Like the awk commands, this concise form normally consumes later input even
though no later record can satisfy the address.

**Tail/head form: discard a prefix, then take one**

`tail -n+10 file.txt` means to begin output at line ten and continue through the
end. Its output is piped to `head -1`, which keeps only the first received line.
That first tail record is the original file's tenth line.

The syntax `-n+10` is accepted by GNU-style tail; the spaced spelling
`tail -n +10` is clearer and portability can vary across implementations. The
pipeline launches two processes. `head` exits after one record, and on a long
file the upstream `tail` may receive a closed pipe after that point rather than
delivering its remaining output.

**Trace existing and missing line cases**

When a tenth line exists, each individual alternative selects exactly that
record and preserves its text. When fewer than ten lines exist, neither awk
condition becomes true, the sed address never matches, and tail produces no
line for head. Each individual command therefore prints nothing.

When all four stored commands run, the missing-line case still prints nothing,
which can conceal the composition defect. The duplication appears only on
files that actually contain a tenth line—the main case the task is designed to
test.

**Why each individual method is exact**

The two awk commands and sed use the input record counter directly, so their
sole possible printed record is number ten. If that record exists, consecutive
record numbering ensures it is reached and printed once.

The pipeline removes the first nine records by choosing a stream beginning at
ten, then selects the first remaining record. That coordinate transformation
also identifies exactly original line ten. None of the commands interprets the
line's content, so arbitrary text on that line is retained.

**Preserve order and text without sorting**

This task selects one position, so sorting would be incorrect and unnecessary.
All four methods scan in file order. `$0`, sed's pattern space, and tail's output
represent the original record; no word splitting or field reconstruction is
used.

An empty tenth record still exists. The tools represent it as a blank output
line rather than as no record, assuming ordinary text-file newline semantics.

**Choose based on clarity and portability**

The short sed command is the canonical stored optimal choice. `awk 'NR == 10'`
is equally concise and widely understood. Adding an early exit can avoid a full
scan: `awk 'NR == 10 { print; exit }'`.

The tail/head pipeline states “from ten, take one” naturally but creates an
extra process and depends more visibly on command-option conventions. These are
tradeoffs among alternatives, not reasons to combine their outputs.

## Complexity detail

Let $n$ be the line count and $c$ the character count. Each awk or sed command
as written can read the whole file, taking $O(c)$ time or $O(n)$ under bounded
line length. The tail/head pipeline may stop useful downstream work after line
ten, though implementation and pipe buffering affect how much upstream input
is read.

The unchanged file performs up to four scans, which is still $O(n)$
asymptotically because four is constant, but it multiplies I/O and produces the
wrong repeated output. Every individual method uses streaming $O(1)$ auxiliary
space in the line-count model.

## Alternatives and edge cases

- **Keep one alternative:** Required to avoid printing line ten four times.
- **Early-exit awk:** Print when `NR == 10` and immediately `exit`, reading at most ten records.
- **Early-exit sed:** Use an addressed block that prints and quits on line ten.
- **Portable tail spelling:** Prefer `tail -n +10 | head -n 1` where supported, but it still uses two processes.
- **Fewer than ten lines:** Every standalone alternative correctly emits nothing.
- **Exactly ten lines:** The selected command prints the last line once.
- **More than ten lines:** Direct selectors print only ten but may continue scanning.
- **Empty tenth line:** Output is one blank line, not no output.
- **Missing `file.txt`:** All commands report an input error; executing all four can repeat diagnostics too.
- **Very long file:** An explicit quit after the answer materially reduces I/O.
