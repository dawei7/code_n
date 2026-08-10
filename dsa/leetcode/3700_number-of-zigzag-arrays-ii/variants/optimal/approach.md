## General

The linear dynamic program from the smaller version would require one transition per array position. Here, $n$ can be $10^9$, so even an $O(nm)$ algorithm is impossible.

The transition is linear: every new state is a sum of selected old states. A linear transition can be represented by a matrix, and applying it $n-2$ times becomes a matrix power computed with binary exponentiation.

The exact source goes one step further than the editorial's $2m$-state presentation. It uses value-reflection symmetry to store only the states whose final comparison is up. This reduces the transition matrix to $m\times m$.

**Ranks and direction states**

Let:

$$
m=r-l+1.
$$

Represent the allowed values by ranks $0,1,\ldots,m-1$. Translating from actual values to ranks preserves every comparison.

For arrays of length $t$, define:

- $U_t[v]$: number of valid arrays ending at rank $v$ whose final comparison is up;
- $D_t[v]$: number ending at rank $v$ whose final comparison is down.

As in the smaller problem:

$$
U_{t+1}[v]=\sum_{u<v}D_t[u]
$$

and:

$$
D_{t+1}[v]=\sum_{u>v}U_t[u].
$$

The strict inequalities simultaneously prevent equal adjacent values and force comparison directions to alternate.

**Reflecting values exchanges up and down**

Map every rank $x$ to its reflection:

$$
\rho(x)=m-1-x.
$$

Reflection reverses all comparisons. If $a<b$, then $\rho(a)>\rho(b)$. Applying this mapping to every element gives a one-to-one correspondence:

- an up-ending valid array at rank $v$ becomes a down-ending valid array at rank $m-1-v$;
- a down-ending array becomes an up-ending array at the reflected rank.

Therefore:

$$
D_t[u]=U_t[m-1-u].
$$

The complete down vector is just the reversed up vector. It never needs to be stored independently.

This symmetry also means:

$$
\sum_vD_t[v]=\sum_vU_t[v].
$$

Once the final up-state vector is known, the total number of arrays is twice its sum.

**Compressing the transition**

Substitute the reflection identity into the up transition:

$$
U_{t+1}[v]
=
\sum_{u=0}^{v-1}U_t[m-1-u].
$$

As $u$ ranges from zero through $v-1$, reflected index $m-1-u$ ranges over the last $v$ vector positions:

$$
m-v,m-v+1,\ldots,m-1.
$$

Thus:

$$
U_{t+1}[v]
=
\sum_{w=m-v}^{m-1}U_t[w].
$$

Define matrix $T$ so row $v$ has zeros in its first $m-v$ columns and ones in its last $v$ columns. Then:

$$
U_{t+1}=T U_t.
$$

The source constructs exactly this row pattern:

`[0] * (value_count - value) + [1] * value`.

For rank zero, the row is all zeros because no previous rank can be smaller than zero. For the highest rank $m-1$, the row sums every old state except column zero after reflection, matching all possible lower previous ranks.

**Initial state at length two**

For a length-two array ending up at rank $v$, the first rank can be any of:

$$
0,1,\ldots,v-1.
$$

There are $v$ choices. Hence:

`state = list(range(value_count))`

is exactly vector $U_2=[0,1,\ldots,m-1]$.

The desired vector is:

$$
U_n=T^{n-2}U_2.
$$

This explains both the initial state and:

`exponent = n - 2`.

The constraints have `n >= 3`, although the same formulation would leave the length-two state unchanged if the exponent were zero.

**Matrix-vector application**

The helper `apply(matrix, vector)` computes one matrix-vector product. For each matrix row, it takes the dot product with the current state and reduces the result modulo $10^9+7$.

Conceptually:

$$
\textit{result}[i]=\sum_j\textit{matrix}[i][j]\cdot\textit{vector}[j].
$$

The initial transition has only zero-one coefficients, but squared transition matrices contain general modular counts, so ordinary multiplication is necessary.

**Squaring the transition**

The helper `multiply(left, right)` performs standard matrix multiplication. It first forms `right_columns = list(zip(*right))` so every result cell can be computed as a row-column dot product.

Every cell is reduced modulo the required modulus. Matrix multiplication composes transitions:

$$
T^aT^b=T^{a+b}.
$$

In particular, squaring changes a one-step transition into a two-step transition, then four steps, eight steps, and so on.

**Binary exponentiation with a vector accumulator**

The exponent is read in binary from its least significant bit.

- If the current bit is one, `state = apply(transition, state)` applies the corresponding power of $T$.
- The exponent is shifted right by one.
- If more bits remain, `transition = multiply(transition, transition)` squares the matrix for the next bit.

This ordering is equivalent to ordinary fast exponentiation. After processing bit position $b$, `transition` represents $T^{2^b}$. Applying only the set-bit powers composes to $T^{n-2}$.

The source skips the final matrix square when the shifted exponent has become zero because that squared matrix would never be used.

Using the vector itself as the accumulator is cheaper than maintaining an identity matrix and multiplying by the starting vector afterward. Matrix-vector application costs $O(m^2)$, whereas another full matrix multiplication would cost $O(m^3)$.

**Recovering both final directions**

After exponentiation, `state` equals $U_n$. Reflection gives a down-ending array for every up-ending array, so the complete count is:

$$
\sum_vU_n[v]+\sum_vD_n[v]
=2\sum_vU_n[v].
$$

The return expression:

`2 * sum(state) % modulus`

implements exactly this identity.

For two available values, `state` at length two is `[0,1]`, and the compressed transition preserves one up-ending array at every later length. Reflection supplies one down-ending array, so the answer is always two: the two forced alternating sequences.

**Why the matrix power counts exactly the valid arrays**

The initial vector counts every length-two up-ending array. One multiplication by $T$ is algebraically identical to the valid DP transition after replacing down states by reflected up states. Therefore, repeated multiplication produces the exact up-ending counts at every length.

Binary exponentiation changes only how these identical linear transitions are grouped; associativity of matrix multiplication makes $T^{n-2}$ equal to applying $T$ one step at a time. Reflection then recovers the omitted down states without loss or duplication.

## Complexity detail

Let $m=r-l+1$.

Constructing the $m\times m$ transition matrix takes $O(m^2)$ time and space.

Each dense matrix multiplication costs $O(m^3)$ time. Binary exponentiation performs $O(\log n)$ matrix squarings. It also performs at most $O(\log n)$ matrix-vector applications at $O(m^2)$ each. The dominant running time is:

$$
O(m^3\log n).
$$

The current transition, its squared replacement, and transposed column representation each require $O(m^2)$ storage. The state vector uses $O(m)$. Peak auxiliary space is $O(m^2)$.

All arithmetic is reduced modulo $10^9+7$, keeping matrix entries bounded.

## Alternatives and edge cases

- **Linear endpoint DP:** The ID 3699 prefix/suffix method uses $O(nm)$ time and $O(m)$ space. It is infeasible when $n$ reaches $10^9$.
- **Full $2m\times2m$ matrix:** Storing both up and down states follows the editorial directly and has the same asymptotic bound, but reflection symmetry allows the exact source to use an $m\times m$ matrix.
- **Recursive matrix power:** Recursion also gives $O(\log n)$ depth, but the iterative bit loop avoids recursion and directly applies set powers to the vector.
- **Two values:** Only the two perfectly alternating arrays are valid, and the compressed state returns two for every legal $n$.
- **Lowest final rank:** Its transition row is all zeros because an up comparison cannot end at the smallest value.
- **Strict comparisons:** The row contains only the last $v$ reflected states; it does not include the boundary column corresponding to equality.
- **Absolute interval location:** Only $m$ matters. Shifting every allowed value leaves all comparison directions unchanged.
- **Modulo during multiplication:** Reducing each dot product is necessary to control extremely large powers and preserves the final remainder.
- **Final factor two:** It is justified by the reflection bijection, not by assuming the two direction counts happen to be numerically similar.
- **Final unused square:** The conditional square after shifting the exponent is an efficiency detail; omitting a matrix that will never be applied does not alter the power.
