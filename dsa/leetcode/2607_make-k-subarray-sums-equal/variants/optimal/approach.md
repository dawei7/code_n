## General

**Compare neighboring circular windows**

Let $W_i$ be the sum of the length-$k$ circular subarray starting at index $i$. Moving the window one step removes `arr[i]` and adds `arr[(i+k) % n]`:

$$
W_{i+1}=W_i-\texttt{arr[i]}+\texttt{arr[(i+k)\%n]}.
$$

All window sums are equal exactly when $W_{i+1}=W_i$ for every $i$. Rearranging the equation gives

$$
\texttt{arr[i]}=\texttt{arr[(i+k)\%n]}
$$

for every index.

Thus the task is not directly about sums anymore. Indices connected by repeated jumps of $k$ modulo $n$ must all end with the same value.

**Jump edges form gcd cycles**

Starting at index $i$, repeatedly add $k$ modulo $n$:

$$
i,\ i+k,\ i+2k,\ldots\pmod n.
$$

The sequence returns to its start after $n/\gcd(n,k)$ distinct positions. There are exactly

$$
g=\gcd(n,k)
$$

disjoint cycles.

Indices lie in the same cycle exactly when they have the same remainder modulo $g$. This is why the code groups values with slice `arr[i:n:g]` for each `i` from zero through $g-1$.

Although stepping by $g$ is not literally the same traversal order as repeatedly stepping by $k$, it selects exactly the same set of indices. Writing $n=gn'$ and $k=gk'$ gives $\gcd(n',k')=1$. The multiples of $k'$ modulo $n'$ visit every residue once, so the jump cycle from remainder $i$ contains every index `i + q*g` and no index with another remainder. The slice is therefore a convenient way to collect a cycle without simulating its modular order.

**Why equal cycle values are sufficient**

If every cycle is constant, then `arr[i] == arr[(i+k)%n]` for all $i$ because a jump by $k$ stays in the same cycle. The neighboring-window recurrence then gives `W[i+1] = W[i]` around the entire circle, so all window sums are equal.

The earlier derivation also proves necessity. Therefore cycles can be optimized independently.

**Minimize changes within one cycle**

Suppose a cycle contains values $x_1,\ldots,x_c$ and they must all become common value $v$. The number of unit operations is

$$
\sum_{j=1}^c|x_j-v|.
$$

This absolute-deviation sum is minimized by any median of the values.

After sorting cycle list `t`, the code selects

`t[len(t) >> 1]`,

the middle element at index $\lfloor c/2\rfloor$. For even $c$, this is the upper median; every value between the two central elements minimizes the sum, so choosing the upper one is valid.

**Why the median is optimal**

Imagine moving candidate $v$ from left to right. Each cycle value below $v$ contributes a slope of $+1$ to total cost, while each value above contributes $-1$. Before the median, more values lie to the right, so increasing $v$ decreases cost. After the median, more lie to the left, so increasing $v$ increases cost.

The balance point is a median.

Equivalently, pair smallest and largest values. For any common $v$ between them,

$$
|small-v|+|large-v|=large-small,
$$

the minimum possible pair contribution. Medians lie inside every relevant central interval.

**Sum independent cycle costs**

Operations on one index affect only its value and only its own equality cycle. There is no requirement that different cycles share a common value.

The code sorts each cycle, sums absolute distances to its median, and adds that cost to `ans`. Since constraints and costs separate, independently minimal cycle choices produce the global minimum.

**Trace the first example**

For `arr = [1,4,1,3]` and $k=2$, $g=\gcd(4,2)=2$.

- Cycle zero contains indices zero and two with values `[1,1]`, cost zero.
- Cycle one contains indices one and three with values `[4,3]`. Choosing median four costs one, as does choosing three.

Changing one value produces alternating `[1,3,1,3]` or `[1,4,1,4]`, and every length-two circular sum is equal. Minimum cost is one.

**Special cycle structures**

When $k=n$, $g=n$ and every cycle has one element. Every length-$n$ circular window already contains the whole array, so answer zero.

When $\gcd(n,k)=1$, all indices form one cycle and every array value must become equal. The global median minimizes the cost.

## Complexity detail

Let $n$ be the array length. The $g$ slices collectively copy $n$ values. Sorting cycle sizes $c_1,\ldots,c_g$ costs $\sum O(c_i\log c_i)\le O(n\log n)$. Distance summation is $O(n)$.

Temporary cycle lists and sorting workspace use at most $O(n)$ total-scale space, matching the manifest. The original `arr` is not modified.

## Alternatives and edge cases

- **Solve window equations directly:** Subtracting neighboring equations immediately yields the same cycle equalities; building a large linear system is unnecessary.
- **Use the mean:** Mean minimizes squared error, not absolute unit-change cost. Median is required.
- **One global median:** This overconstrains different gcd cycles, which may choose independent values.
- **`k = n`:** Every index is its own cycle and no operations are needed.
- **Coprime `n` and `k`:** One cycle forces all values equal.
- **Even cycle length:** Any value between the two central values is optimal; the code uses the upper median.
- **Duplicate values:** Sorting and absolute deviations handle them naturally.
- **Circular wraparound:** The modulo jump is captured by gcd residue cycles.
- **Input preservation:** Slices are sorted copies, leaving `arr` unchanged.
