## General

**A potion follows a fixed no-wait timeline once its start is chosen.** For potion mana $x$, wizard $i$ needs `skill[i] * x` time. If the potion starts at time $T$, it reaches wizard $i$ after all earlier wizards finish:

$$
T+x\sum_{h=0}^{i-1}\texttt{skill}[h].
$$

The immediate-transfer rule means this arrival time must also be the exact time wizard $i$ starts. The only freedom is choosing $T$ late enough that no wizard is still busy with the previous potion.

Potions must be brewed in order, so it is sufficient to compare the current potion against the immediately preceding one on each wizard. Earlier potions already finish no later than that previous potion.

**Interpret the array `f` between potion iterations.** Before processing a new mana value, `f[i]` is the time at which wizard $i$ finishes the previous potion in the synchronized no-wait schedule built so far. Initially every entry is zero, meaning all wizards are free before the first potion.

The first potion can start at time zero. The same recurrence used for later potions naturally constructs its cumulative completion times.

**Run a forward pass that finds the earliest possible final completion.** Variable `tot` is the tentative completion time of the current potion at the previous wizard. At wizard $i$, two conditions must hold before processing:

- the potion must have arrived, represented by `tot`; and
- the wizard must have finished the preceding potion, represented by `f[i]`.

The tentative recurrence is

`tot = max(tot, f[i]) + skill[i] * x`.

This is the usual flow-shop recurrence. It temporarily permits the current potion to wait between wizards when `f[i] > tot`. That seems to violate the problem, but the pass is being used to discover the earliest feasible finishing time, not as the final internal schedule.

An equivalent start-time derivation makes the result clearer. Let

$$
P_i=\sum_{h=0}^{i-1}\texttt{skill}[h].
$$

To avoid overlap at wizard $i$, current start $T$ must satisfy

$$
T+xP_i\ge f[i].
$$

Therefore,

$$
T\ge f[i]-xP_i
$$

for every wizard. The earliest valid start is the maximum of these lower bounds. The forward `max` recurrence computes exactly the final completion produced by that start, even though its intermediate tentative times may contain waiting.

**Reconstruct a truly synchronized schedule backward.** After the forward pass, `tot` is the earliest achievable completion time at the last wizard. The source sets `f[-1] = tot`. It then walks backward:

`f[i] = f[i + 1] - skill[i + 1] * x`.

Wizard $i+1$ spends exactly `skill[i+1] * x` time on the potion. Subtracting that duration from its completion time gives its start time, which must equal wizard $i$'s completion time under immediate transfer. Thus the backward pass removes all tentative gaps and stores exact completion times for the current potion at every wizard.

These reconstructed times still respect all previous-potion constraints because `tot` was chosen from the maximum of every wizard's required start lower bound. Shifting the potion into a continuous chain ending at `tot` places its work on each wizard no earlier than that wizard's old `f[i]`.

For `skill = [1,1,1]` and equal mana one, the first potion completes at times $1,2,3$. The second potion's earliest synchronized start is one, so its completions become $2,3,4$. The third starts at two and finishes at five. The pipeline overlaps across different wizards while never making one potion wait.

**Why greedy earliest placement is globally optimal.** Once prior potions are fixed, delaying the current potion beyond its earliest feasible start cannot help this potion and can only make every wizard finish it later. Those later finish times are the availability constraints for all future potions. Therefore, an optimal schedule always places the current potion as early as possible. Applying this argument in potion order proves the repeated forward/backward update minimizes the final completion time.

**Why the final answer is `f[-1]`.** After each iteration, `f` stores synchronized completion times for that potion. After the last mana value, its last entry is when the final wizard finishes the final potion, which is exactly the total brewing time from start time zero.

The local assignment `max = lambda ...` shadows Python's built-in name but implements the same two-value maximum needed by the recurrence.

## Complexity detail

Let $n$ be the number of wizards and $m$ the number of potions. Each potion performs one forward pass over $n$ wizards and one backward pass over $n-1$ boundaries. Total time is $O(nm)$.

Array `f` stores one completion time per wizard. All other state is scalar, so auxiliary space is $O(n)$. These bounds match the manifest.

Completion times may be much larger than a single `skill * mana` product because they accumulate across wizards and potions. Python integers avoid overflow; a fixed-width implementation should use 64-bit arithmetic.

The two passes are both necessary in this realization: the forward pass discovers the binding no-overlap constraint, and the backward pass restores the no-wait invariant.

## Alternatives and edge cases

- **Standard flow-shop DP only:** Keeping the forward tentative completion times would permit a potion to wait between wizards, violating immediate transfer.
- **Binary-search each potion's start:** Feasibility is monotone, but the maximum start constraint is derived directly in one pass.
- **Build a full \(n\times m\) table:** It is unnecessary because only the previous potion's wizard completion times are needed.
- **Start every potion when wizard zero is free:** A later wizard may still be occupied, so all wizard constraints must influence the start.
- **Delay an already feasible potion:** This cannot improve future availability and therefore cannot be part of a minimum makespan schedule.
- **One wizard:** Each potion simply follows the previous one, and forward/backward passes reduce to cumulative work.
- **One potion:** It starts at zero and its result is the sum of all wizard processing times for that mana.
- **Equal skills and mana:** The schedule forms a regular pipeline with adjacent potion starts one wizard-duration apart.
- **Large bottleneck wizard:** Its availability becomes the maximum constraint that shifts the entire next potion later.
- **Immediate transfer:** Backward subtraction makes each wizard's completion exactly the next wizard's start.
- **Positive durations:** No processing interval has zero or negative length, preserving scheduling order.
- **Name shadowing:** The local `max` lambda behaves correctly for two arguments but should not be confused with a different optimization.
