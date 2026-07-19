## General
**Treat each maximal equal-digit run independently**

A value-equal substring cannot cross a boundary between different digits.
Therefore every maximal run of one digit must be partitioned entirely into
pieces of length two and three. Scan the string once to obtain each run length.

**Use the remainder modulo three**

A run whose length is divisible by three can use only length-three pieces. A
run with remainder two can use one length-two piece and fill the rest with
length-three pieces. A run with remainder one cannot participate in a valid
global decomposition: replacing threes with twos would require either two
length-two pieces, as for length four, or leave the same conflict after
removing threes.

Consequently every run must have remainder zero or two, and exactly one run
must have remainder two. That one run supplies the unique length-two piece;
all other characters are covered by length-three pieces. These conditions are
both necessary and sufficient, so the scan can reject remainder one
immediately and count remainder-two runs.

## Complexity detail
Each of the $N$ characters belongs to exactly one maximal run and is visited
once, giving $O(N)$ time. The scan stores only indices and the number of runs
that require a length-two piece, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Dynamic programming over prefix lengths:** Track whether each prefix can
  be covered with zero or one length-two piece. This is correct and linear but
  stores more state than the run-remainder characterization needs.
- **Rescan the full run from every position:** Recovering equal-run boundaries
  independently for each character is correct, but a long uniform string
  causes $O(N^2)$ repeated work.
- A string of length two is valid because its only piece is the required
  length-two substring.
- A string made solely of length-three groups is invalid because the
  length-two piece must exist exactly once.
- Two separate runs with remainder two are invalid because they require two
  length-two pieces.
- A run of length five is valid on its own because it splits into lengths
  three and two.
- Runs of different digits are never allowed to share a piece.
