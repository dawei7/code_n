## General

**Represent one transformation as a linear map.** Only character frequencies matter for final length. Let a row vector `cnt` contain counts of `a` through `z`. A transformation sends each source letter $i$ to the next `nums[i]` alphabet letters, wrapping modulo 26.

The source constructs matrix `matrix` so `matrix[i][d] = 1` when one occurrence of source letter $i$ produces one occurrence of destination $d$. For each offset $j=1,\ldots,\texttt{nums}[i]$, destination is `(i + j) % 26`.

Because `nums[i] <= 25`, destinations in one row are distinct; a zero/one entry correctly represents each produced character once.

With this row-oriented convention, one transformation is

$$
\text{nextCounts}=\text{counts}\cdot T.
$$

Entry $d$ of the product sums `counts[i] * T[i][d]` over all sources, exactly aggregating every new occurrence.

**Raise the transition to the number of rounds.** Applying the same fixed transformation $t$ times gives

$$
\text{finalCounts}=\text{initialCounts}\cdot T^t.
$$

Since $t$ can be $10^9$, multiplying once per transformation is too slow. `matpow` uses exponentiation by squaring. It starts with the identity matrix, representing zero transformations. When the current binary bit of `power` is one, it multiplies the result by the current matrix power. It squares that matrix each iteration and halves the exponent.

After $O(\log t)$ iterations, `factor` is $T^t$.

**Matrix multiplication details.** `matmul(a,b)` creates an $n\times q$ result for compatible $n\times p$ and $p\times q$ inputs. It loops through $i,k,j$ and accumulates `a[i][k] * b[k][j]`. Skipping the innermost loop when `a[i][k]` is zero improves early sparse multiplications without changing the dense worst-case bound.

Every accumulation is reduced modulo $10^9+7$. Matrix powers and the final vector product therefore remain bounded while preserving the requested final residue.

**Apply the powered matrix to the input.** The initial string is counted into a 26-entry list. Wrapping it in `[cnt]` makes a $1\times26$ row matrix. Multiplying by `factor` returns a one-row final frequency vector. Summing that row yields the transformed length.
The transition-matrix construction records exactly every one-round source-to-destination production. Matrix multiplication composes these linear contributions: entry $(i,d)$ of $T^r$ counts how many destination-$d$ characters one source-$i$ character produces after $r$ rounds. Exponentiation returns the exact $t$-round composition, initial vector multiplication scales by source frequencies, and the final sum counts all resulting characters.

**Orientation matters.** The local editorial displays column-vector notation, where matrix indices are transposed relative to this source. Both are valid. Here the matrix stores source in rows and destination in columns because the frequency vector multiplies on the left. Copying the editorial's matrix orientation without changing multiplication order would produce wrong transitions.

The source assumes standard typing names but otherwise implements its own matrix operations. It never materializes the transformed string.

## Complexity detail

Let alphabet size be $A=26$ and input length $n$. Counting the string costs $O(n)$. Matrix construction costs $O(A^2)$ at most. Exponentiation performs $O(\log t)$ matrix multiplications, each $O(A^3)$ worst-case. The final $1\times A$ vector product costs $O(A^2)$. Total time is $O(n+A^3\log t)$.

At any moment, a constant number of $A\times A$ matrices are stored, plus result matrices allocated during multiplication. Peak auxiliary space is $O(A^2)$. With fixed $A=26$, this is constant relative to $n$ and $t$.

## Alternatives and edge cases

- **Simulate $t$ frequency rounds:** It costs $O(tA^2)$ or $O(tA)$ with direct transitions, which is impossible for $t=10^9$.
- **Materialize strings:** Their length can grow exponentially and cannot be stored.
- **Column-vector convention:** It works if transition entries and multiplication order are transposed consistently.
- **`t = 0`:** Although constraints start at one, identity initialization would correctly return the original length.
- **`nums[i] = 1`:** Source letter produces only its immediate successor.
- **`nums[i] = 25`:** It produces every letter except itself exactly once.
- **Alphabet wrap:** Modulo 26 maps positions beyond `z` back through `a`.
- **All initial characters equal:** Vector multiplication scales the corresponding transition row by their count.
- **Modular arithmetic:** Reduction during every multiplication prevents unbounded integer growth.
- **Sparse first matrix:** The zero skip helps initially, but squared powers may become dense, so worst-case cubic multiplication remains appropriate.
- **Identity matrix:** It is the neutral transformation and is essential for binary exponentiation.
- **Final length only:** Summing frequencies avoids any need to preserve character order.
- **Fixed alphabet:** The apparently cubic factor is only $26^3$ per exponent bit, making the approach practical.
- **Distinct destinations:** Because each `nums[i]` is at most 25, the consecutive wrapped offsets never visit the same destination twice in one transformation row; Boolean matrix entries are therefore sufficient.
- **Row-vector application:** Wrapping `cnt` inside another list is what gives it matrix shape $1\times26$ for the generic multiplication helper.
- **Power one:** Binary exponentiation multiplies identity by the original transition and returns exactly one transformation, providing a useful boundary check on orientation.
