## General

**Every starting point belongs to one fixed jump chain**

Starting at index $j$ forces the path

$$
j,\ j+k,\ j+2k,\ldots
$$

until the next jump leaves the array. There are no choices after the starting index. The energy earned is the sum of that complete forced suffix of one residue class modulo $k$.

Indices with the same remainder modulo $k$ form one chain. Its last index must be among

$$
n-k,\ n-k+1,\ldots,n-1,
$$

because adding $k$ to any of these leaves the array. Conversely, every jump chain has exactly one terminal index in this range.

That is why the outer loop uses `range(n - k, n)`: it chooses each chain's endpoint exactly once.

**Walk each chain backward**

For one terminal index `i`, the inner loop visits

$$
i,\ i-k,\ i-2k,\ldots
$$

and maintains running sum `s`.

After first adding `energy[i]`, `s` is the energy obtained by starting at terminal index $i$. After moving back to $i-k$ and adding that value, `s` is the energy obtained by starting at $i-k$, because the forced forward path visits $i-k$ and then $i$. Continuing backward produces the total for every possible starting point in that chain.

The method updates `ans` after every addition, so it compares the energy totals of all legal starts. No explicit suffix-DP array is needed because each total is consumed immediately while walking its chain.

**Why every index is visited exactly once**

Every array index has one residue modulo $k$ and therefore lies in exactly one chain. Repeatedly adding $k$ from that index eventually reaches that chain's unique endpoint in the last $k$ positions. The outer loop selects that endpoint, and the backward inner loop reaches the index.

Different endpoints represent different residues and their backward sequences cannot overlap. Therefore, although the code has nested loops, the total number of inner iterations across all outer iterations is $n$, not $nk$.

**Negative values must remain in the sum**

The journey cannot stop early. If a chosen starting point's path goes through a negative-energy magician, that value must be included.

The running sum always represents the complete suffix from the current backward index through the terminal endpoint. It never resets just because the sum becomes negative, so it respects this rule. This is not Kadane's maximum-subarray problem, where one may discard a harmful prefix.

Initializing `ans = -inf` is equally important. If every legal journey has negative total, the answer must be the least negative one rather than zero. For `[-2,-3,-1]` with $k=2$, the chains produce starts totaling $-1$, $-3$, and $-3$; the maximum is $-1$.

**Example**

For `energy = [5,2,-10,-5,1]` and $k=3$, the terminal indices are 2, 3, and 4.

- Chain ending at 2 visits 2 backward and yields total $-10$.
- Chain ending at 3 visits 3 then 0, yielding starts with totals $-5$ and $5+(-5)=0$.
- Chain ending at 4 visits 4 then 1, yielding totals 1 and $2+1=3$.

The maximum over all starts is 3.


For each chain endpoint, after processing backward index $j$, `s` equals $\sum_{r\ge0,\ j+rk<n}\texttt{energy}[j+rk]$, exactly the forced journey total from $j$. This follows by induction: the endpoint total starts correctly, and moving back by $k$ adds the one new first magician.

Every possible start belongs to exactly one enumerated chain, so `ans` sees every legal total. It stores their maximum and is therefore the requested result.

## Complexity detail

Let $n$ be the length of `energy`.

The $k$ backward chains partition all $n$ indices. Each index is added once and causes one maximum comparison, so total time is $O(n)$.

The exact code uses only `ans`, `n`, endpoint `i`, current index `j`, and running sum `s`. Auxiliary space is $O(1)$.

This differs from the manifest's $O(k)$ space and “retaining suffix total for each residue class” summary. That description fits a different scan using a $k$-entry array. The exact reverse-chain implementation needs no such array and realizes the editorial's $O(1)$ space.

The output is one integer, and the input list is unchanged.

## Alternatives and edge cases

- **Right-to-left DP array:** Store `best[i] = energy[i] + best[i+k]` and take the maximum. It is direct but uses $O(n)$ storage unless values are written into the input.
- **Residue-sum array:** Scan right to left and retain one running suffix total per residue modulo $k$. This uses $O(k)$ space and matches the manifest summary.
- **Enumerate forward from every start:** It repeatedly visits shared suffixes and can take $O(n^2/k)$ time.
- **Kadane-style reset:** Incorrect because a journey cannot stop before leaving the array and cannot skip negative energy.
- **All negative energies:** `-inf` initialization ensures the best required journey is returned instead of zero.
- **k close to n:** Most chains contain one element, and one chain may contain two; the partition argument still holds.
- **Positive and negative mix:** Every intermediate value is included in its chain suffix exactly once.
- **Terminal start:** Starting in the last $k$ positions visits only that magician, and those one-element totals are checked first.
- **Earlier start:** Its sum extends an already computed later-start total by one energy value.
- **No overflow:** Python integers safely hold sums up to the constraint range.
- **At least one legal path:** The array is nonempty and `k < n`, so the endpoint range is nonempty.
- **Input preservation:** The algorithm does not turn `energy` into a DP array.
