## General
**Count distinguishable outcomes for one pig**

There are `rounds = minutesToTest // minutesToDie` complete opportunities to observe a death. A pig can die after any one of those rounds or remain alive through the test, giving `rounds + 1` distinguishable final states.

**Combine pigs as independent state digits**

With `p` pigs, the vector of their final states has `(rounds + 1) ** p` possibilities. Label each bucket with a different base-`rounds + 1` code and let pig `q` drink from a bucket in the round encoded by digit `q`; the observed state vector identifies that code. Thus this capacity is achievable, not merely an upper bound.

**Find the smallest sufficient exponent**

Start with capacity one and multiply by the per-pig state count until capacity reaches `buckets`. The number of multiplications is the smallest `p` satisfying `states ** p >= buckets`. Using integer multiplication avoids floating-point rounding near exact powers.

**Why fewer pigs cannot work**

Any experiment ultimately observes only one of the possible final state vectors. With fewer pigs than the computed exponent, there are fewer vectors than buckets, so two poisoned-bucket scenarios must produce the same observation and cannot always be distinguished.

## Complexity detail
Capacity grows by a factor of at least two per pig, so the loop runs $O(\log buckets)$ times. It stores only the state count, capacity, and pig count, using $O(1)$ space.

## Alternatives and edge cases
- **Logarithm and ceiling:** directly computes the exponent but can round an exact power incorrectly in floating-point arithmetic.
- **Dynamic-programming capacity table:** generalizes to related testing variants but stores states unnecessary for this formula.
- **Explicitly generate outcome vectors:** demonstrates the coding construction but creates `Theta(buckets)` signatures instead of counting them.
- **One bucket:** needs no experiment and therefore zero pigs.
- **Only one testing round:** each pig has two states, so the answer is the smallest `p` with `2 ** p >= buckets`.
- **Unused partial interval:** only complete `minutesToDie` intervals produce an observable additional death state.
- **Exact capacity:** when `states ** p = buckets`, exactly `p` pigs suffice; do not add one more.
