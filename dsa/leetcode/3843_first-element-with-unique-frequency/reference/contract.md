## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers, kept in its original order.

For each distinct value $x$ in `nums`, define its frequency as

$$
F(x)=\left\lvert\left\{i\mid\texttt{nums}[i]=x\right\}\right\rvert.
$$

Also let $M(f)$ be the number of distinct values whose frequency equals $f$. Thus, the frequency of $x$ is unique exactly when $M(F(x))=1$.

**Return value**

Return `nums[i]` for the smallest index $i$ satisfying $M(F(\texttt{nums}[i]))=1$. Return `-1` if no index satisfies that condition.
