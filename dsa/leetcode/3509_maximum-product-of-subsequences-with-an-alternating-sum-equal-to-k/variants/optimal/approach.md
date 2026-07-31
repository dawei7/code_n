## General

Every alternating sum lies between $-S$ and $S$. Encode this entire interval in one integer bitset: bit $x+S$ means that sum $x$ is reachable. Shifting a bitset left by a value adds that value to every represented sum; shifting right subtracts it. Two bitsets distinguish even-length from odd-length subsequences, because the next selected value receives a plus sign after even length and a minus sign after odd length.

For positive answers, group states by their exact product. `products[p]` stores the even- and odd-parity sum bitsets reachable by non-empty, zero-free subsequences with product $p$. When processing a positive value $v$, starting a new subsequence sets sum $v$ at product $v$. Extending an even-length state shifts its sums left by $v$ and makes the length odd; extending an odd-length state shifts right and makes the length even. Both transitions move from product $p$ to $pv$, and products exceeding $L$ are discarded because later positive factors can never reduce them.

Transitions are collected separately before merging them into the persistent states. This represents the choice to skip the current element and prevents one array position from being selected more than once, including when $v=1$ leaves the product unchanged.

Zero needs separate treatment. Discarding an over-limit positive prefix is normally safe, but appending zero can turn any product into zero. Maintain four additional reachability bitsets: even and odd subsequences without a zero, and even and odd subsequences that already contain a zero. These states ignore product magnitude and therefore retain prefixes whose product is too large. Selecting zero moves a zero-free state into the zero-containing group without changing its sum, while still toggling parity.

After all values, inspect the target bit for every stored positive product and take the largest match. If none matches, return zero when a zero-containing state reaches `k`; otherwise return `-1`. Positive products always outrank zero, so this order is correct.

The product states follow directly from the subsequence recurrence: by induction after each input position, they contain exactly every feasible zero-free subsequence classified by product, parity, and alternating sum. The separate reachability recurrence does the same for subsequences containing zero. Together they cover every non-empty subsequence and exclude only positive products already proven unable to return below the limit.

## Complexity detail

Let $P$ be the number of distinct positive products at most $L$ that become reachable, so $P \le L$. Each product owns two bitsets of $2S+1$ bits. Processing one value examines $P$ product states and performs constant many bitset operations. In a bit-operation model this is $O(nPS)$ time and $O(PS)$ space, bounded by $O(nLS)$ time and $O(LS)$ space as recorded in the manifest.

On a machine with word size $w$, each shift or Boolean operation spans $O(\lceil S/w\rceil)$ words, so the packed implementation runs in $O(nP\lceil S/w\rceil)$ word operations and uses $O(P\lceil S/w\rceil)$ words. The four zero-reachability bitsets add only $O(S)$ bits.

The benchmark grows $n$ with varied values while keeping every input legal. It contrasts the packed dynamic program with exhaustive subsequence enumeration, whose $2^n-1$ candidates form the principal slower class.

## Alternatives and edge cases

- **Enumerate all subsequences:** Computing every alternating sum and product is direct but takes exponential time.
- **Keep only the maximum product per sum:** A currently smaller product can accept another factor while a larger one would exceed `limit`, so one product per alternating sum loses necessary states.
- **Apply a modulus:** The contract compares actual products against `limit`; modular arithmetic changes both ordering and feasibility.
- **Discard every over-limit prefix:** This is safe only for zero-free continuations. A later zero can reduce the final product to zero, so separate zero-aware reachability is required.
- **Treat the empty subsequence as sum zero:** The chosen subsequence must be non-empty; target zero alone does not make an empty choice valid.
- **Parity convention:** The first selected element is added, the second subtracted, and each later selection toggles the next sign regardless of skipped input positions.
- **Input order:** Selection is a subsequence, so states process values left to right and never reorder factors.
- **Product one:** Repeated ones create new sum/parity states without changing the product; deferred merging prevents reuse of the same position.
- **Unreachable target:** If $\lvert k\rvert>S$, return `-1` immediately.
