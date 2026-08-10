## General

Testing every pair would be quadratic. The exact solution instead compresses each number to the part of `k` that it can supply: `gcd(value, k)`.

Two values form a divisible product exactly when the product of their gcd classes is divisible by `k`. Since gcd classes are divisors of `k`, there are usually far fewer classes than values.

**Reduce each value to a gcd class**

For current `value`, the code computes

`current_gcd = gcd(value, k)`.

This gcd contains every prime factor of `k` that the value can contribute, capped at the exponent needed by `k`. Factors of `value` that do not divide `k` are irrelevant to divisibility by `k` and can be discarded.

For example, with `k = 12`, values whose gcds with 12 are four and three have a product of gcd classes twelve, so any such pair's value product is divisible by twelve.

**Why gcd products are a complete compatibility test**

Consider one prime $p$ whose exponent in $k$ is $e$. If its exponents in values $a$ and $b$ are $u$ and $v$, then $ab$ supplies enough of $p$ exactly when $u+v\ge e$.

The gcds with $k$ retain exponents $\min(u,e)$ and $\min(v,e)$. Their sum reaches at least $e$ exactly when $u+v$ does. Repeating this reasoning for every prime factor of $k$ proves

$$
k\mid ab
\quad\Longleftrightarrow\quad
k\mid\gcd(a,k)\gcd(b,k).
$$

Therefore no necessary divisibility information is lost by replacing full values with gcd classes.

**Count compatible earlier classes**

`gcd_counts` stores how many previously scanned values belong to each gcd class. For the current class, the generator examines every stored `previous_gcd` and includes its `count` when

`(current_gcd * previous_gcd) % k == 0`.

The sum is the number of earlier array positions that can pair with the current position. Adding that number to `answer` counts all newly completed valid pairs at once.

Only after counting does the code increment `gcd_counts[current_gcd]`. Thus the current element cannot pair with itself, and every counted partner has a smaller index.

**Why every index pair is counted once**

Take a valid pair `(i, j)` with `i < j`. When the scan reaches `j`, the class of `nums[i]` is already in `gcd_counts`. The gcd compatibility equivalence makes the modulus test succeed, so that earlier occurrence contributes one through its class count.

Before iteration `j`, the pair could not be counted because its later endpoint had not been processed. Afterward, it is never counted again as the same pair because future iterations have different later endpoints. Invalid products fail the compatibility test and contribute nothing.

Aggregating equal classes does not merge away multiplicity. If a class has count five, all five earlier indices are separate valid partners whenever that class is compatible, and the generator adds five.

**Understand the number of possible classes**

Every `gcd(value, k)` is a positive divisor of `k`. Let $D=\tau(k)$ be the number of divisors. The counter can contain at most $D$ keys, no matter how large $n$ is.

Divisors occur in pairs around $\sqrt{k}$, giving the simple bound $D=O(\sqrt{k})$. The scan of counter items is therefore much smaller than scanning all earlier elements when $k$ has relatively few divisors.

For `k = 1`, every gcd is one and every class pair is compatible. The algorithm then adds the number of earlier elements at each step and returns all $\binom n2$ index pairs.

**Why the online order is useful**

Maintaining only previous elements automatically enforces `i < j`. A frequency table over the entire array would require careful combination formulas and special handling for pairs within the same class. The online version uses one uniform compatibility sum and then inserts the current class.

It also avoids storing the original values. Once a value's gcd is counted, its remaining numeric details are irrelevant to all future decisions.

## Complexity detail

Let $n$ be the array length and $D=\tau(k)$ be the number of positive divisors of `k`. Computing one gcd takes $O(\log k)$ time, and scanning the current counter takes at most $O(D)$. Total time is

$$
O\left(n(\log k+D)\right).
$$

Using $D=O(\sqrt{k})$, this is commonly written as $O(n\sqrt{k})$, matching the manifest.

The counter stores at most $D$ classes, so auxiliary space is $O(D)$, bounded by $O(\sqrt{k})$. The generator itself is consumed immediately by `sum` and does not build a separate list.

## Alternatives and edge cases

- **Enumerate all pairs:** It is simple but costs $O(n^2)$, which is too large for $n=10^5$.
- **Precompute compatible divisor lists:** Enumerate divisors of `k` and store which class pairs work. This can reduce repeated modulus checks at the cost of setup and extra tables.
- **Count all classes first:** Combine compatible class frequencies with careful handling of identical classes. It is valid but easier to double-count than the online scan.
- **Value divisible by `k`:** Its gcd class is `k`, which is compatible with every previous class, so it pairs with every earlier value.
- **`k = 1`:** Every product is divisible by one, and the answer is $\binom n2$.
- **No compatible classes:** The generator sum is zero and the current value adds no pairs.
- **Repeated equal values:** Equality is irrelevant; only product divisibility matters, and each occurrence is retained in its class count.
- **Current element inserted afterward:** This prevents self-pairing and enforces the index order.
- **Prime `k`:** Gcd classes are only one and `k`; a pair works exactly when at least one value is divisible by `k`.
- **Composite prime powers:** The gcd retains partial exponents, allowing two values to combine their factors.
- **Factors outside `k`:** They are discarded by gcd because they cannot help satisfy divisibility by `k`.
- **Large answer:** Up to $\binom n2$ pairs may qualify; Python integers avoid overflow.
- **Input preservation:** The array is only scanned, while all state lives in the counter.
- **Counter iteration safety:** The counter is updated only after the generator sum finishes, so its size does not change during iteration.
