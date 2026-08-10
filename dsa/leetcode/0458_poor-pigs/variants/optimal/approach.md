## General

The key is not to think of a pig as providing only a yes-or-no result. When several complete test rounds fit into the available time, a pig has several distinguishable outcomes: it can die after the first round, die after the second round, and so on, or survive every round. Each pig therefore behaves like one digit in a number system whose base is the number of possible outcomes.

**Count complete testing rounds**

A death is observable only after waiting `minutesToDie` minutes. The number of complete waiting periods that fit into the total testing time is

$$
r=\left\lfloor\frac{\texttt{minutesToTest}}{\texttt{minutesToDie}}\right\rfloor.
$$

Partial leftover time cannot reveal another death and creates no additional outcome. A pig has `r` possible death rounds plus one survival outcome, so the exact solution computes

$$
\texttt{base}=r+1.
$$

For example, with `minutesToDie = 15` and `minutesToTest = 30`, two full rounds fit. One pig can be observed in three distinct states: dies by minute 15, dies between minute 15 and minute 30 after the second feeding, or remains alive at minute 30.

**Combine independent pig outcomes**

If one pig has `base` possible final states, two pigs have `base * base` distinguishable state pairs. With `p` pigs, the complete observation is a vector of `p` states, giving

$$
\texttt{base}^{p}
$$

possible outcome vectors.

Each bucket can be assigned a different vector. View the bucket number as a `p`-digit number in base `base`. For a particular pig, that bucket's digit tells in which testing round the pig should drink from it; one reserved digit means that pig never drinks from that bucket. During each round, a live pig can simultaneously drink from every bucket assigned that round's digit, which the rules allow.

Because exactly one bucket is poisonous, each pig's death round or survival state reveals the corresponding digit of that poisoned bucket's code. Reading all pigs' states recovers the complete code and therefore identifies the unique bucket.

The schedule remains feasible even if a pig dies early and cannot drink in later rounds. Its early death already fixes its digit. The later buckets assigned to that pig cannot be poisonous, and surviving pigs continue to reveal their own digits.

**Turn capacity into the minimum-pig condition**

To distinguish all `buckets` possibilities, the number of available outcome vectors must satisfy

$$
\texttt{base}^{p}\ge\texttt{buckets}.
$$

The required answer is the smallest nonnegative integer `p` satisfying this inequality.

The exact solution finds it without floating-point logarithms. `p` stores the current number of distinguishable buckets, initially `1`, because with zero pigs there is one possible observation: the empty outcome vector. `res` stores how many pigs have been included.

While `p < buckets`, multiply `p` by `base` and increment `res`. Each iteration adds one independent pig and one more base-`base` digit. The first time `p` reaches or exceeds `buckets`, `res` is sufficient.

**Why the first sufficient count is minimal**

Before the final loop iteration, `p` represented `base^(res - 1)` and was strictly smaller than `buckets`. Therefore `res - 1` pigs cannot create enough distinct observations to identify every bucket; by the pigeonhole principle, at least two buckets would share an outcome and could not be distinguished.

After the multiplication, `p = base^res` is at least `buckets`, so distinct codes can be assigned to every bucket. Thus `res` pigs are sufficient while every smaller count is insufficient. The returned number is exactly minimal.

**Trace the examples**

With four buckets and one 15-minute round, `base = 15 // 15 + 1 = 2`. Start with `p = 1`, `res = 0`. One pig raises capacity to `2`; that is still below four. A second pig raises capacity to `4`, so the loop stops and returns two. The four joint states are both survive, only the first dies, only the second dies, and both die.

With four buckets and two rounds, `base = 30 // 15 + 1 = 3`. One pig distinguishes three buckets, which is not enough. Two pigs distinguish nine possible codes, so the answer is still two. The extra five codes simply go unused.

If `buckets = 1`, the initial capacity `p = 1` already covers the sole possibility. No experiment is necessary, so the loop returns zero pigs.

## Complexity detail

Let $B$ be `buckets` and let $q=\lfloor\texttt{minutesToTest}/\texttt{minutesToDie}\rfloor+1$ be the per-pig base. After `t` iterations, `p = q^t`. The loop therefore runs

$$
\left\lceil\log_q B\right\rceil
$$

times. Its time complexity is $O(\log B)$ when expressed only in terms of the number of buckets, matching the manifest. More precisely it is $O(\log_q B)$, and the constraints guarantee $q\ge2$ because at least one complete death interval fits.

Only `base`, `res`, and `p` are stored, so auxiliary space is $O(1)$. Under the bounded input, their magnitudes are small. The iterative method also avoids floating-point rounding near exact powers.

## Alternatives and edge cases

- **Logarithm formula:** Compute $\lceil\log(B)/\log(q)\rceil$. It is mathematically direct and constant-time under a machine model, but floating-point rounding can produce an off-by-one result at exact powers unless handled carefully.
- **One pig per bucket:** Testing buckets independently wastes the fact that pigs may drink mixtures and that joint outcomes encode many possibilities.
- **Binary-only reasoning:** Treating every pig as merely alive or dead ignores distinct death rounds. With `r` rounds, each pig has `r + 1` states, not two.
- **One bucket:** Zero pigs are enough because there is no uncertainty; the initial `p = 1` handles this naturally.
- **Exactly one round:** `base = 2`, reducing the formula to the familiar number of binary outcome bits needed for the buckets.
- **Unused leftover minutes:** A remainder smaller than `minutesToDie` cannot complete another observable round and must be ignored by floor division.
- **Capacity larger than bucket count:** Outcome vectors need not all be used. The first power at least as large as the bucket count is sufficient.
- **Exactly one poisonous bucket:** The coding argument relies on a single bucket determining each pig's state. Multiple poisoned buckets would combine signals and require a different design.
- **Simultaneous feeding:** A pig can sample any number of buckets in a round, and a bucket can be sampled by several pigs; those permissions make digit-code assignments possible.
