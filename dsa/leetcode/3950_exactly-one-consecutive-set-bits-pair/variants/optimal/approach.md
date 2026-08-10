## General

An adjacent set-bit pair occurs whenever two neighboring binary positions both contain one. The source reads the bits from least significant to most significant, remembers the preceding bit, and records whether one `11` pair has already been found.

It returns false immediately if a second pair appears.

**Read one bit at a time**

The expression

`cur = n & 1`

extracts the least significant bit:

- an odd `n` has `cur = 1`;
- an even `n` has `cur = 0`.

After inspecting that bit, the source executes

`n = n >> 1`.

Right shift discards the bit just processed and moves the next binary position into the least significant place. Repeating these two operations visits every bit exactly once from right to left.

The parameter `n` is only a local integer binding. Shrinking it does not mutate caller-owned data because Python integers are immutable.

**Remember the neighboring bit**

`pre` stores the bit processed during the preceding loop iteration. Since traversal moves through consecutive bit positions, `pre` and `cur` always represent one adjacent pair in the original binary representation.

Before the first real bit, `pre` is initialized to zero. This behaves like an implicit leading zero below the least significant position and cannot create a false `11` match.

The chained comparison

`pre == cur == 1`

is true exactly when both neighboring bits are one.

**Distinguish one pair from two pairs**

`vis` means that an adjacent `11` pair has already been encountered.

When a pair is found:

- if `vis` is false, the source sets it to true and continues;
- if `vis` is already true, this is a second pair and the source returns false immediately.

After every iteration, `pre = cur` prepares the next adjacent comparison.

When all set bits have shifted out and `n` becomes zero, the loop ends. Returning `vis` distinguishes the two remaining cases:

- false means no adjacent pair ever appeared;
- true means exactly one appeared, because a second would already have returned false.

**Overlapping pairs are counted separately**

The binary substring `111` contains two adjacent pairs: the first and second bits, and the second and third bits. They overlap at the middle bit but are still distinct neighboring positions.

The source handles this correctly. After recognizing the first two ones, it leaves `pre = 1`. The next `cur = 1` forms another pair, sees `vis == True`, and returns false.

This is why searching for one run of consecutive ones would not be enough. A run of length two contributes one pair, while a run of length three contributes two.

Separated runs also count independently. A representation such as `11011` contains one pair near each end, so the second discovery causes false.

**A small trace**

For `n = 6`, binary `110`, traversal sees bits $0,1,1$:

- comparing initial zero with bit zero finds no pair;
- comparing zero with one finds no pair;
- comparing one with one finds the first pair and sets `vis`.

The loop ends and returns true.

For `n = 5`, binary `101`, the visited bits are $1,0,1$. Neither adjacent comparison has two ones, so `vis` remains false.

**Why every adjacent pair is considered**

If the original bit at position $i$ is $b_i$, then after $i$ shifts `cur` equals $b_i$ and `pre` equals $b_{i-1}$ for $i>0$. Therefore the iteration tests exactly the pair $(b_{i-1},b_i)$.

Every neighboring position from zero up to the most significant bit is reached once. No nonadjacent bits are compared, and no adjacent pair is skipped. The state logic then accepts exactly one successful comparison.

**The manifest describes a different implementation**

The manifest summary says the source uses a shifted-AND mask and tests whether that mask has one set bit. A compact version could form `pairs = n & (n >> 1)`; each set bit in `pairs` marks one `11` occurrence.

The exact `solution.py` does not use that method. It contains the iterative `pre`/`cur` scan described here.

## Complexity detail

Let $L$ be the number of bits in `n`, with $L=1$ for the representation of zero. For positive input, the loop runs once per significant bit, so time is $O(L)=O(\log(n+1))$. It may terminate earlier after finding a second pair.

The source uses only `pre`, `cur`, `vis`, and the shrinking integer, so additional space is $O(1)$.

The manifest reports $O(1)$ time. Under the fixed constraint $n\le10^5$, at most 17 significant bits are scanned, so the operation count is bounded by a problem-constant. For variable-size integers, however, the exact source's natural asymptotic time is $O(\log(n+1))$, unlike the constant-number-of-bitwise-operations mask approach named by the manifest.

## Alternatives and edge cases

- **Shift-and-AND mask:** `pairs = n & (n >> 1)` marks all adjacent `11` pairs. Testing `pairs != 0 and pairs & (pairs - 1) == 0` checks whether exactly one marked position exists. This is the manifest's summarized algorithm, not the source.
- **Convert to a binary string:** Count occurrences of `"11"` with overlapping positions. A naive non-overlapping substring count can mishandle `"111"`, and string allocation is unnecessary.
- **Count runs of ones:** A run of length $r$ contributes $r-1$ adjacent pairs, not merely one run. The source's pairwise scan avoids that confusion.
- **`n = 0`:** The loop is skipped and `vis` is false, correctly reporting no pair.
- **One set bit:** No neighboring set bit exists, so the result is false.
- **Exactly two consecutive ones:** They create one pair and return true if no other pair occurs.
- **Three consecutive ones:** They create two overlapping pairs and return false.
- **Two separated `11` runs:** The first sets `vis` and the second triggers the early false return.
- **Leading zeroes:** Standard binary representation omits them, and adding leading zeroes would never create a new `11` pair anyway.
- **Trailing zero bits:** They are processed normally and separate any later set bit from the previous one.
- **Early exit:** Once two pairs exist, unprocessed higher bits cannot restore validity, so returning immediately is safe.
- **Local right shifts:** Rebinding `n` has no external side effect.
