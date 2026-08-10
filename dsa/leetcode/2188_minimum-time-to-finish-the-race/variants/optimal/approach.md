## General

The key decision is not which tire to use on each isolated lap. It is how to divide the race into consecutive stints. Within one stint, a single fresh tire is used for several laps without changing; between stints, the driver pays `changeTime` and starts with a fresh tire of any type.

The exact solution first finds the cheapest possible tire-only time for every useful stint length. It then uses dynamic programming to combine those stints into exactly `numLaps` laps.

**Compute one tire's successive lap times**

For tire `[f, r]`, its first lap takes `f`. Each next consecutive lap multiplies the previous lap time by `r`.

The variables have these meanings:

- `i` is the current stint length being recorded;
- `t` is the time of the next lap on this worn tire;
- `s` is the cumulative time for all laps in the stint so far.

After adding `t` to `s`, `cost[i]` is updated with the smaller total among all tire types capable of an `i`-lap stint.

Thus `cost[j]` eventually means the minimum lap-driving time for completing exactly `j` consecutive laps on one fresh tire, excluding any change time before the stint.

**Stop extending a tire once changing dominates**

The precomputation continues while `t <= changeTime + f`.

If the next worn-tire lap takes more than `changeTime + f`, it is strictly faster to change tires and take a fresh first lap of this same tire type. Because `r >= 2`, all still later worn laps are even slower. No optimal plan needs a single-tire stint that includes that dominated lap.

Using this tire's own `f` makes the cutoff safe even without comparing against other tire types. A globally fastest fresh tire could only make changing more attractive.

**Why an array of length 18 is enough**

The slowest possible useful growth occurs with `f = 1` and `r = 2`. Also, `changeTime + f <= 100001` in that case. Successive lap time at stint position $i$ is at least $2^{i-1}$.

The seventeenth such lap is $2^{16}=65536$, which may still be useful, while the eighteenth is $2^{17}=131072$, already above 100001. Larger `f` or `r` reaches the cutoff sooner.

Therefore no useful stint exceeds 17 laps, and indices one through 17 fit in `cost = [inf] * 18`.

**Define the race dynamic program**

Let `f[i]` be the minimum total time to finish exactly `i` laps after accounting for tire changes between selected stints.

For a final stint of length `j`, the earlier `i - j` laps cost `f[i - j]`, the stint's driving time is `cost[j]`, and starting this new stint normally requires `changeTime`.

The code first minimizes `f[i - j] + cost[j]` over useful `j`, then adds `changeTime` once after the inner loop. This is algebraically the same as adding the change cost to every transition.

**Cancel the nonexistent change before the first stint**

The race begins with any tire for free; there is no change delay before lap one. Yet the uniform transition adds `changeTime` before every stint, including the first.

Initialization `f[0] = -changeTime` cancels that first addition:

$$
-\texttt{changeTime}+\texttt{cost[j]}+\texttt{changeTime}
=\texttt{cost[j]}.
$$

Every later transition starts from a positive-lap state and retains its added change time, exactly matching a real tire replacement between stints.

This negative sentinel is bookkeeping, not a claim that finishing zero laps takes negative physical time.

**Why combining cheapest stints is sufficient**

Any valid race plan can be partitioned at every tire change. Each resulting block is a consecutive stint on one tire. Replacing that stint's tire choice with `cost[length]` cannot increase the time.

Conversely, every finite `cost[j]` came from a real tire type and represents a feasible `j`-lap stint. Combining such entries with change delays constructs a valid race.

For each total lap count, the DP tries every possible length of the final useful stint. Therefore it considers the final split point of every optimal race and stores the minimum exact total.

For the four-lap first example, the best two-lap stint on tire `[2,3]` costs eight. Two such stints plus one change cost $8+5+8=21$.

## Complexity detail

Let $T$ be the number of tire types, $N$ be `numLaps`, and $L=17$ be the maximum useful stint length.

Each tire is extended for at most $L$ laps, so precomputation takes $O(TL)$ time. The DP tries at most $L$ final stint lengths for each of $N$ lap totals, taking $O(NL)$. Total time is $O(TL+NL)$.

The `cost` array uses $O(L)$ space and the full DP array uses $O(N)$, for $O(N+L)$ auxiliary space. The manifest bounds match the exact source.

## Alternatives and edge cases

- **Memoized recursion by remaining laps:** Choose a next stint length recursively and cache remaining-lap states. It has equivalent transitions but adds call-stack overhead.
- **Precompute without the dominance cutoff:** Extending every tire through all `numLaps` can cost $O(TN)$ and creates huge geometric lap times unnecessarily.
- **Greedy cheapest current lap:** A locally cheap worn lap may lead to a poor future stint structure; DP is needed to price change boundaries globally.
- **One lap:** `f[0] = -changeTime` cancels the added change, so the answer is the smallest first-lap time.
- **Change to the same tire type:** This is allowed and is exactly what justifies comparing a worn lap with `changeTime + f`.
- **Unlimited tire supply:** Every DP stint may start with a fresh copy independently.
- **Unused long costs:** Entries left at infinity cannot win a transition.
- **Exactly 17 useful laps:** Array index 17 is available; the loop never reaches an out-of-range useful index 18 under the constraints.
- **Large repeat factor:** The dominance cutoff arrives after very few laps.
- **Change delay paid between stints:** It is added once per transition and canceled only for the first.
- **No change after the race:** The DP adds change time before a new stint, never after the final lap.
- **Modulo not needed:** The answer is a minimum time, and Python integers hold the values exactly.
- **Input preservation:** Tire pairs and scalar inputs are only read.
