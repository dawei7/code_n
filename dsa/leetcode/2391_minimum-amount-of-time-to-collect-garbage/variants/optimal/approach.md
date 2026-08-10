## General

**Separate unavoidable pickup time from necessary travel**

Every character across all `garbage` strings represents one garbage unit, and picking up each unit takes one minute. All units must be collected, so total pickup time is fixed:

$$
S=\sum_i\lvert\texttt{garbage}[i]\rvert.
$$

The only travel decision is how far each of the three type-specific trucks must go. A truck responsible for type `c` must reach the last house containing `c` and never benefits from traveling farther.

Because only one truck can operate at a time, truck times cannot overlap. The minimum total elapsed time is therefore the sum of all pickup minutes plus the necessary travel minutes of each used truck.

**Count pickups and record last occurrences together**

The first loop adds `len(s)` for each house string to `ans`. This counts every metal, paper, and glass unit exactly once regardless of type.

For every character `c` at house `i`, it assigns:

```python
last[c] = i
```

Later occurrences overwrite earlier ones. After the scan, `last['M']`, `last['P']`, or `last['G']` exists exactly when that type occurs and stores its farthest required house.

The dictionary contains at most three entries. Repeated units of the same type at one house update the same value harmlessly.

**Compute prefix travel time to each house**

`travel[t]` is the time from house `t` to `t+1`. The second loop enumerates it starting with house index one:

```python
for i, t in enumerate(travel, 1):
    ts += t
```

After adding `t`, `ts` is the travel time from house zero through consecutive roads to house `i`. A truck whose last required house is `i` must incur exactly this prefix cost.

The query:

```python
sum(ts for j in last.values() if i == j)
```

adds `ts` once for each garbage type whose final house is `i`. At most three values are checked. If two trucks both end at that house, both must traverse the same roads at different times because trucks cannot operate simultaneously, so adding the prefix twice is correct.

A type found only at house zero has last index zero. The travel loop begins at house one, so it adds no travel for that truck.

**Trace the first example**

There are seven garbage units across `["G", "P", "GP", "GG"]`, so pickup time begins at seven.

Paper's last occurrence is house two. Travel to house two costs `2 + 4 = 6`. Glass's last occurrence is house three, costing `2 + 4 + 3 = 9`. Metal never occurs and needs no truck time.

Total is `7 + 6 + 9 = 22`? Count the units carefully: the strings have lengths `1 + 1 + 2 + 2 = 6`, not seven. Thus, total is `6 + 6 + 9 = 21`. The length-based code avoids manual counting mistakes like this one.

**Why trucks never need to return**

The task only requires collection, and no rule requires returning to house zero. Once a truck reaches its farthest needed house and collects there, its work is complete. Travel cost is therefore a one-way prefix, not doubled.

Similarly, passing through a house with no garbage of that truck's type is unavoidable if a later house needs service, but the truck spends no pickup time there.

**Why the total is minimal**

Every garbage unit imposes one unavoidable pickup minute, giving lower bound $S$. For each type `c`, any valid schedule must bring its truck from house zero to the farthest house containing `c`. The unique ordered route costs the corresponding travel prefix, giving another unavoidable lower bound.

The described plan achieves exactly these bounds: each truck travels only to its last required house, collects every matching unit along the way, and stops. Since truck work cannot overlap, concatenate the three truck schedules in any order. Their times add with no extra transition requirement.

Thus, the algorithm's sum is both necessary and achievable, proving minimality.

**Why a full prefix array is unnecessary**

The code accumulates `ts` once while moving through roads. When it reaches a house that is a final destination, it immediately adds the current prefix to `ans`. Only three destination indices exist, so no array of all prefix times is required.

## Complexity detail

Let $n$ be the number of houses and $S$ the total number of garbage characters. The first loop examines each house and each unit, taking $O(n+S)$ time. The travel loop has $n-1$ iterations and checks at most three dictionary values each, so it takes $O(n)$ time. Total time is $O(n+S)$.

The `last` dictionary has at most three entries, and the remaining variables are scalar. Exact auxiliary space is $O(1)$ beyond the input and returned integer. The manifest's $O(n)$ space is a loose upper bound; this implementation does not build an $n$-length prefix array.

## Alternatives and edge cases

- **Prefix travel array:** Precompute travel time to every house, then add the entries at the three last positions. It is clear but uses $O(n)$ extra space.
- **Separate scan per garbage type:** Find each last occurrence and count pickups independently. With only three types it remains linear but repeats work.
- **Simulate truck movements house by house:** Correct if stopped at each final occurrence, but explicit scheduling is unnecessary because times simply add.
- **Type absent entirely:** It has no `last` entry, so neither pickup nor travel time is added for its truck.
- **Type only at house zero:** Its last index is zero and requires no road travel.
- **Several types end at the same house:** The prefix time is added once per truck because their work cannot overlap.
- **Many units at one house:** Each character contributes one pickup minute, while travel to the house is paid once for that truck.
- **No return trip:** Trucks stop after their last collection, so prefix travel is not doubled.
- **Houses beyond a truck's last type occurrence:** That truck never visits them.
- **Serialized operation rule:** It justifies adding all truck pickup and travel durations rather than taking a maximum across trucks.
