## General

**Enumerate subarrays by their starting index**

A subarray is determined by a start `i` and an end `j` with `i \le j`. The outer loop selects every possible start from zero through `n - 1`. For a fixed start, the inner loop advances `j` from `i` to the end of the array. It therefore visits

`nums[i:i + 1]`, `nums[i:i + 2]`, and so on,

without skipping any non-empty subarray beginning at `i`.

The loops distinguish occurrences by their indices, but the requested count distinguishes subarrays by their value sequences. Two equal sequences found at different locations must count once. The set `s` is responsible for that deduplication.

**Stop extending as soon as divisibility exceeds the limit**

The variable `cnt` records how many elements in the current subarray are divisible by `p`. Python evaluates `nums[j] % p == 0` to a Boolean, and Booleans behave as integers in addition: true contributes one and false contributes zero. Thus,

`cnt += nums[j] % p == 0`

updates the count for the newly appended element in constant time.

If `cnt > k`, the loop breaks before hashing or inserting that subarray. This early termination is valid because extending a subarray can never reduce its count of divisible elements. Every longer subarray with the same start would still have more than `k` such elements, so none of them could be eligible.

When `cnt \le k`, the current subarray satisfies the restriction and receives a content signature.

**Build a rolling signature as the end moves**

Copying an entire subarray into a tuple at each `(i, j)` pair would require work proportional to its length. Instead, the code maintains two polynomial rolling hashes. Both start at zero for each new start index. When value `nums[j]` is appended, they update as

$$
h_1 \leftarrow (h_1 \cdot 131 + \texttt{nums}[j]) \bmod (10^9 + 7)
$$

and

$$
h_2 \leftarrow (h_2 \cdot 13331 + \texttt{nums}[j]) \bmod (10^9 + 9).
$$

Multiplying the old hash by a base shifts the existing sequence to higher polynomial positions, and adding the new value places that value at the end. Order matters: sequences containing the same values in a different order generally produce different hashes. The modular reduction keeps each hash within a fixed numerical range, allowing every extension to take constant arithmetic time.

The hashes are reset when `i` changes because the next outer-loop iteration begins a different family of subarrays.

**Use two hashes rather than one**

A modular hash compresses many possible sequences into a finite set of integers, so different sequences can theoretically share a hash. Computing the sequence under two different bases and two different prime moduli makes an accidental collision in both components vastly less likely than a collision in one component.

The expression `h1 << 32 | h2` packs the pair into one Python integer. Both residues are below roughly one billion, which is less than `2^{32}`. Shifting `h1` left by 32 bits reserves the low 32 bits for `h2`, and bitwise OR fills those low bits. Consequently, two different residue pairs cannot collide merely because of packing: the packed integer uniquely recovers its high `h1` and low `h2` components.

This packing guarantee is separate from the rolling-hash guarantee. Distinct sequences can still, in theory, have the same pair of modular residues. The implementation treats equal hash pairs as equal subarrays, relying on double hashing to make that event negligibly unlikely for the stated input size.

**Why adding signatures to a set counts distinct values**

For every eligible indexed subarray, the code calls `s.add(...)` with its packed double-hash signature. A Python set retains one copy of an equal integer. Repeated occurrences of the same value sequence follow the same recurrence from zero, so they obtain the same two residues and the same packed signature; the set counts them once.

Assuming no double-hash collision, different value sequences have different stored signatures. Under that standard rolling-hash assumption, there is a one-to-one correspondence between entries in `s` and distinct eligible subarray sequences. Therefore, `len(s)` is the requested count.

**A trace of the eligibility boundary**

Consider `nums = [2, 3, 3, 2, 2]`, `k = 2`, and `p = 2`. For start zero, the count becomes one after the first value. Extending through indices one and two leaves it at one. Adding index three raises it to two, so `[2, 3, 3, 2]` is still hashed and inserted. Adding index four raises it to three, so the loop breaks and the length-five subarray is not inserted.

The next start begins with fresh hashes and `cnt = 0`. If it produces `[3]` or `[2]` that was already produced from another index, its signature is already in `s` and the set size does not grow. This is exactly the difference between counting distinct sequences and counting all indexed occurrences.

**Why every eligible distinct subarray is considered**

Take any eligible subarray `nums[a:b + 1]`. The outer loop eventually chooses `i = a`. Before the inner loop reaches `j = b`, the divisible count cannot have exceeded `k`: counts only grow, and the complete chosen subarray has at most `k` divisible elements. Therefore, the early break cannot occur before `b`. The recurrence consequently builds and inserts the signature for this subarray.

Every inserted signature also comes from a non-empty contiguous range whose counted divisible elements do not exceed `k`, because insertion occurs only after adding one real element and only on the non-breaking branch. Thus, the enumeration neither misses an eligible indexed range nor includes an ineligible one. The set then collapses ranges with equal contents.

**What the exact solution actually uses**

The branch summary describes a value trie, but the executable Optimal source does not construct trie nodes. It uses the two rolling hashes and a set of packed hash pairs shown above. Both designs can achieve quadratic time and space, but their correctness guarantees and stored data differ. This explanation follows the code that runs: its deduplication is probabilistic because modular fingerprints are not mathematically collision-free.

## Complexity detail

Let `n` be the length of `nums`. Ignoring early breaks, the nested loops visit

$$
\sum_{i=0}^{n-1}(n-i) = \frac{n(n+1)}{2}
$$

subarrays. Each visit performs a divisibility test, a few fixed-size modular arithmetic operations, and an expected `O(1)` Python set insertion. The expected running time is therefore `O(n^2)`. Early termination can reduce practical work when divisible elements are frequent and `k` is small, but it does not improve the worst-case bound.

At most one signature is stored for every indexed subarray, so the set contains at most `n(n+1)/2` integers. Its worst-case auxiliary space is `O(n^2)`. The loop counters and rolling-hash state use `O(1)` additional space. Because the packed hashes remain bounded to about 62 bits, their representation does not grow with subarray length.

The expected-time qualifier comes from hash-table operations. The probabilistic-correctness qualifier comes from the polynomial fingerprints: double collisions are extremely unlikely but theoretically possible.

## Alternatives and edge cases

- **Value trie:** Insert every eligible subarray as a path whose edges are array values, and count newly created nodes. This gives deterministic `O(n^2)` time and space and avoids rolling-hash collisions, but it is not the data structure used by the exact solution.
- **Store tuples of subarray values:** A set of tuples is collision-safe because Python resolves hash collisions with equality, but constructing or comparing length-proportional tuples across all ranges can push total work toward `O(n^3)`.
- **Single rolling hash:** It uses a smaller signature but has a substantially higher accidental-collision risk than the two independent residues.
- **Suffix structures:** Suffix arrays, suffix automata, or tries can deduplicate sequence content, but incorporating the at-most-`k` eligibility boundary adds complexity unnecessary for `n \le 200`.
- **Count every eligible occurrence:** Merely incrementing an answer in the nested loops is wrong when the same value sequence appears at several locations; distinctness is about contents, not index ranges.
- **Sliding window only:** A two-pointer window can count ranges meeting a monotone restriction, but it does not by itself deduplicate equal subarray values.
- **No divisible elements in a range:** `cnt` remains unchanged, and every extension from that start stays eligible until the array ends.
- **Every element divisible by `p`:** For each start, at most `k` elements are inserted before the next extension breaks.
- **`k = n`:** No subarray can contain more than `n` divisible elements, so all indexed subarrays are eligible; the set still removes content duplicates.
- **Repeated values:** Equal subarrays at different positions deliberately map to one signature and one set entry.
- **Different lengths:** The rolling recurrence normally distinguishes them, and the pair of hashes serves as the full signature; unlike an explicit representation, length is not stored separately, so theoretical modular collisions remain possible.
- **Break placement:** The code checks `cnt > k` before updating the hashes. The first invalid range and all longer ranges for that start are intentionally absent.
- **Boolean arithmetic:** In Python, true adds one and false adds zero, making the compact count update exact.
- **Packing the residues:** Since `h2 < 2^{32}`, its bits never overlap the shifted `h1` field. Packing itself creates no ambiguity between hash pairs.
- **Hash collision:** Two unequal sequences sharing both residues would be undercounted. Double hashing makes this extraordinarily unlikely but cannot offer a formal zero-collision guarantee.
- **Non-empty requirement:** Each signature is inserted only after the inner loop appends `nums[j]`, so the empty subarray is never counted.
- **Single-element input:** The only length-one subarray is inserted if its divisible count is at most `k`, which holds because `k \ge 1`.
- **Input preservation:** Values are read and hashed; `nums` is never modified.
