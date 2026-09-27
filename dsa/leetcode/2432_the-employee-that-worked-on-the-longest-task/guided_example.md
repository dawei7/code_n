# Guided Example: The Employee That Worked on the Longest Task

## 1. The Instance and the Two Quantities Being Compared

The company has `n = 8` employees, identified by the integers `0` through `7`. A log entry
`[id, leaveTime]` reports that the employee with that id finished a task at absolute time
`leaveTime`. The task itself is not bracketed by a start time; the statement instead fixes
the schedule globally: the first task begins at time `0`, and every later task begins the
instant the previous one ends.

The instance traced here is

$$
\texttt{logs} = [[7,4],\ [6,5],\ [2,9],\ [5,10]],
$$

whose authored answer is `2`. This instance is chosen because it forces the tie-break to do
real work: the longest duration occurs twice, and the smaller employee id appears in the
*second* of the two tied tasks. A scan that simply keeps the first maximum would return
`7`, and a scan that accumulates work per employee would answer a different question
altogether.

The output is a single employee id, selected by two ranking rules applied in order:

1. largest task duration wins;
2. among tasks of equal duration, the smallest employee id wins.

## 2. Task Durations Are Consecutive Differences of Leave Times

Write the log entries as $\text{id}_i$ and $\text{leaveTime}_i$ for
$i = 0, 1, \dots, m-1$. Because task $i$ starts exactly when task $i-1$ ended, the start
time of task $i$ is simply the leave time of its predecessor, with a virtual predecessor at
time $0$:

$$
\text{start}_i = \begin{cases} 0 & i = 0 \\ \text{leaveTime}_{i-1} & i > 0 \end{cases}
\qquad\text{and}\qquad
\text{duration}_i = \text{leaveTime}_i - \text{start}_i .
$$

The constraints guarantee that the leave times are strictly increasing, so every difference
is at least $1$ and no task has zero or negative length. That guarantee is what makes `0` a
safe initial value for the running maximum: the first real duration always exceeds it.

| Task $i$ | `id` | `leaveTime` | Start time | Duration | Running maximum before | Running maximum after |
|---|---|---|---|---|---|---|
| 0 | 7 | 4 | 0 | 4 | 0 (sentinel) | 4 |
| 1 | 6 | 5 | 4 | 1 | 4 | 4 |
| 2 | 2 | 9 | 5 | 4 | 4 | 4 |
| 3 | 5 | 10 | 9 | 1 | 4 | 4 |

The table already shows the tie: task $0$ and task $2$ both last $4$ units. The durations of
tasks $1$ and $3$ are $1$ each, so they cannot compete.

## 3. Step-by-Step Trace of the Scan

The scan keeps three pieces of state: the leave time of the previous task, the best duration
found so far, and the employee id that owns it. Each log entry is processed once.

| Step | Log entry | Duration computed | Comparison against the current best | Best duration after | Best id after |
|---|---|---|---|---|---|
| 0 | — | — | initialize previous leave time to $0$, best duration to $0$ | 0 | — |
| 1 | `[7, 4]` | $4 - 0 = 4$ | $4 > 0$, so the first task becomes the incumbent | 4 | 7 |
| 2 | `[6, 5]` | $5 - 4 = 1$ | $1 < 4$, strictly worse, no change | 4 | 7 |
| 3 | `[2, 9]` | $9 - 5 = 4$ | $4 = 4$ is a tie and $2 < 7$, so the smaller id replaces the incumbent | 4 | 2 |
| 4 | `[5, 10]` | $10 - 9 = 1$ | $1 < 4$, strictly worse, no change | 4 | 2 |
| 5 | end of input | — | return the incumbent id | 4 | 2 |

The decisive step is step 3. The duration ties the existing maximum, so the comparison
cannot be a plain "is it larger" test: the incumbent must be replaced precisely when the
new employee id is smaller. Step 4 confirms that the scan cannot stop early — the last entry
is examined and rejected on its merits, never because the best answer was assumed final.

## 4. State Before and After Each Entry

The same trace is easier to audit when each row shows the complete state, including the
running previous leave time that must be restored after each subtraction.

| Entry processed | `prevLeave` before | `bestDuration` | `bestId` | Action taken | `prevLeave` after |
|---|---|---|---|---|---|
| none (start) | 0 | 0 | undefined | initialise | 0 |
| `[7, 4]` | 0 | 0 | undefined | set best to $(4, 7)$ | 4 |
| `[6, 5]` | 4 | 4 | 7 | none | 5 |
| `[2, 9]` | 5 | 4 | 7 | replace best with $(4, 2)$ because $2 < 7$ | 9 |
| `[5, 10]` | 9 | 4 | 2 | none | 10 |
| result | — | 4 | **2** | return `bestId` | — |

One arithmetic detail deserves care. Once a duration has been computed by subtracting the
previous leave time, the running variable no longer holds an absolute leave time; it holds a
duration. Adding the duration back to it restores the current absolute leave time, which is
what the next iteration needs. Assigning the observed leave time directly would be clearer,
and the two are numerically identical:

$$
\texttt{prevLeave}_{\text{old}} + \bigl(\text{leaveTime}_i - \texttt{prevLeave}_{\text{old}}\bigr)
= \text{leaveTime}_i .
$$

Mishandling this restoration is the classic failure mode here: the durations computed after
it would become differences of differences and silently shrink.

## 5. The Tie-Break Rule in Both Directions

A tie-break only needs to replace the incumbent when the newcomer is *better*, and a smaller
id is better. The direction matters, so the table exercises it both ways.

| Logs | Durations | Tied ids | Decision path | Output |
|---|---|---|---|---|
| `[[7,4],[6,5],[2,9],[5,10]]` | 4, 1, 4, 1 | 7 and 2 | incumbent 7, then 2 arrives later and is smaller, so it replaces | `2` |
| `[[0,10],[1,20]]` | 10, 10 | 0 and 1 | incumbent 0, then 1 arrives later and is larger, so it does not replace | `0` |
| `[[1,2],[0,4],[2,6]]` | 2, 2, 2 | 1, 0, 2 | incumbent 1, then 0 replaces it, then 2 fails the tie test | `0` |
| `[[4,9],[2,10],[1,12]]` | 9, 1, 2 | none | first duration is the unique maximum and is never challenged | `4` |

Reversing the comparison — replacing only on a strictly larger duration — would leave the
first tied id in place in all three tie rows. That is correct for the second row and wrong
for the first and third, which is exactly why the tie condition must be tested separately
from the duration condition.

## 6. Why a Single Left-to-Right Pass Is Correct

**Invariant.** After processing the first $t$ log entries, `bestDuration` equals the maximum
duration among tasks $0$ through $t-1$, and `bestId` equals the smallest employee id among
the tasks that attain that maximum.

**Initialisation.** Before any entry is processed the set of considered tasks is empty, so
the sentinel `bestDuration = 0` is a lower bound that any positive duration beats. Because
the leave times are strictly increasing, the first duration is at least $1$, so the first
comparison always installs a real incumbent.

**Inductive step.** Let $d$ be the duration of task $t$ and let $u$ be its employee id.
Exactly one of three cases holds.

- If $d > \text{bestDuration}$, then no earlier task reached $d$, so $t$ is the unique
  longest task among the first $t+1$ and the new pair is $(d, u)$.
- If $d = \text{bestDuration}$, the maximum is unchanged and the smallest id among the
  tied tasks becomes $\min(\text{bestId}, u)$, which is precisely the replacement condition.
- If $d < \text{bestDuration}$, the maximum and its owner are unchanged.

In each case the invariant is preserved, so after all $m$ entries `bestId` is the smallest id
among the longest tasks — the requested answer.

**Completeness.** Every task is examined exactly once, so no longer task can be missed and no
tie can be overlooked. In particular the scan cannot terminate early: a later task may have
a larger duration, and among equal durations a later task may carry a smaller id.

**Sufficiency of the state.** The answer depends only on the pair (duration, id) of each
task, compared lexicographically as (larger duration, smaller id). The previous leave time
is needed only to compute the next duration, and the employee parameter `n` is never used by
the scan, because every id appearing in a log is guaranteed to be valid.

## 7. Boundary and Degenerate Instances

| Situation | Input | Behaviour | Output |
|---|---|---|---|
| A single log entry | `n = 4`, `logs = [[3,5]]` | the one task starts at time $0$, so its duration is $5$, and its employee is returned regardless of id | `3` |
| First task is the longest | `n = 5`, `logs = [[4,9],[2,10],[1,12]]` | durations $9, 1, 2$; the incumbent is never challenged | `4` |
| Smaller id arrives in a later tied task | `n = 8`, `logs = [[7,4],[6,5],[2,9],[5,10]]` | tie at duration $4$; replacement by the smaller id | `2` |
| Smaller id already first | `n = 2`, `logs = [[0,10],[1,20]]` | tie at duration $10$; the equal id test fails, so the incumbent stands | `0` |
| Three-way tie | `n = 3`, `logs = [[1,2],[0,4],[2,6]]` | all durations $2$; the running minimum id wins | `0` |
| The same employee appears twice | `n = 4`, `logs = [[1,2],[3,7],[1,11]]` | durations $2, 5, 4$ are compared independently; no per-employee total is formed | `3` |
| `n` smaller than the id range suggests | `n = 1` with four log entries | the scan never consults `n`; ids come from the logs and are guaranteed valid | `1` |

The repeated-employee row is the most tempting trap. Summing all work by an employee answers
"who worked the most in total", but the question here is "who owns the single longest task",
and the two can disagree. Employee $1$ appears twice in that row yet loses to employee $3$,
whose single task of length $5$ is longer than either of employee $1$'s tasks.

## 8. Alternative Methods and Their Costs

| Alternative | Idea | Trade-off |
|---|---|---|
| Build a duration list, then sort | Materialise (duration, id) pairs and sort by descending duration then ascending id | $O(m \log m)$ time and $O(m)$ extra space to solve a problem that a single pass decides |
| Two passes over the logs | First pass finds the maximum duration, second pass finds the smallest id attaining it | $O(m)$ time but two traversals, and either stored durations or recomputation is required |
| Accumulate time per employee | Add each duration to a per-employee total, then take the largest total | Answers a different question; an employee with several short tasks would beat the owner of the longest task |
| Stop early once a large duration is seen | Terminate as soon as some threshold is exceeded | No valid threshold exists, because the maximum is unknown until the last log is read |
| Sort the logs by leave time first | Reorder the entries before scanning | Unnecessary: the constraints already guarantee strictly increasing leave times |

## 9. Complexity Derivation

Let $m = \texttt{logs.length}$ be the number of logged tasks.

**Time.** Each log entry is read once and performs exactly one subtraction, one arithmetic
restoration of the running leave time, and a bounded number of comparisons for the duration
and tie conditions. That is $O(1)$ work per entry, so the total is

$$
O(m).
$$

The employee count $n$ does not appear in the bound at all, because the scan never iterates
over employee ids; only the ids that actually appear in the logs are examined. Since the
strictly increasing leave times must be read in full, the bound is tight.

**Auxiliary space.** The method stores only the previous leave time, the best duration, and
the best employee id. No array, map, or recursion is used, so auxiliary space is

$$
O(1)
$$

beyond the input. The returned id is a single integer, so the output space is constant as
well. Any method that instead materialised the durations would need $\Theta(m)$ space for no
benefit in time.