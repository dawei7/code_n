## General

**Track assigned people rather than used hats**

There can be 40 hat labels but at most 10 people. A mask of used hats would have up to $2^{40}$ states, which is far too large. A mask of people who already received hats has only $2^p$ states, where $p$ is the number of people.

The strategy processes hat labels one at a time. For each label, either nobody wears that hat or exactly one person who likes it receives it. Processing a label only once guarantees different people never receive the same hat.

**Reverse the preference mapping**

The input lists hats by person. The DP needs to know who can receive the current hat, so the code builds:

```python
g = defaultdict(list)
for i, h in enumerate(hats):
    for v in h:
        g[v].append(i)
```

`g[v]` is the list of people who prefer hat label `v`. Preferences within one person's list are unique, so the same person is not repeated in one hat list through duplicate input.

**Define the mask**

Bit `k` of mask `j` is one when person `k` has been assigned a hat. The expression:

```python
j >> k & 1
```

shifts person `k`'s bit to the low position and tests whether it is set.

`1 << k` is a mask containing only that person's bit. When the bit is known to be set, `j ^ (1 << k)` clears it and produces the predecessor mask before that person received the current hat.

**Define the table state**

`f[i][j]` is the number of ways to use only hat labels from 1 through `i` so that exactly the people represented by mask `j` have hats.

The largest preferred label is:

```python
m = max(max(h) for h in hats)
```

Hat labels above `m` are preferred by nobody, so processing them could only skip them and would not change the answer. The input guarantees each preference list is nonempty, making the nested maximum defined.

The table has `m + 1` rows and `2^p` masks.

**The empty assignment base case**

```python
f[0][0] = 1
```

With no hat labels processed, there is exactly one way to assign hats to nobody: choose nothing. Every nonzero people mask has zero ways at row zero.

This base state seeds every later sequence of choices.

**Option one: skip the current hat**

For hat label `i` and destination mask `j`:

```python
f[i][j] = f[i - 1][j]
```

copies every assignment that used only earlier hats and leaves current hat `i` unused. Not every available hat must be worn, so this choice is always legal.

**Option two: assign the current hat to one person**

The loop visits every person `k` in `g[i]`. The recurrence is written backward from destination mask `j`. If bit `k` is set in `j`, person `k` could have received current hat `i`:

```python
if j >> k & 1:
    f[i][j] += f[i - 1][j ^ (1 << k)]
```

The predecessor mask has all the same assigned people except `k`. It uses only hats below `i`. Assigning hat `i` to `k` is allowed because membership in `g[i]` means that person prefers it.

No transition assigns hat `i` to two people. Each contribution chooses one `k` and comes from row `i-1`, where hat `i` was not yet available.

**Why destination masks prevent duplicate assignments**

Suppose two different people in `g[i]` have bits set in `j`. The inner loop adds two distinct possibilities: one where the current hat went to the first person and one where it went to the second. Their predecessor masks differ, and their final hat assignments differ, so both should be counted.

An already-assigned person cannot receive a second earlier hat within a predecessor state because each mask records people, and every transition adds exactly one previously absent destination bit relative to its predecessor.

**Trace a two-person example**

For `hats = [[3,5,1],[3,5]]`, the reverse mapping includes:

- Hat 1 liked by person 0.
- Hat 3 liked by people 0 and 1.
- Hat 5 liked by people 0 and 1.

The full mask is binary `11`. Valid final assignments are `(3,5)`, `(5,3)`, `(1,3)`, and `(1,5)`, where tuple positions are people. The DP reaches mask `11` through four distinct sequences of per-hat choices.

**Return the all-people mask**

For $p$ people, the final mask is $2^p-1$, whose low $p$ bits are all one. The last list index is exactly that value, so:

```python
return f[m][-1]
```

returns the count after every relevant hat label has been processed.

Modulo reduction after additions preserves the required remainder. Skip values are already reduced from earlier rows.

**Why the recurrence is correct**

Every assignment using labels through `i` either leaves hat `i` unused or gives it to exactly one person who prefers it. The skip term counts the first disjoint case. For the second, removing the current hat from its unique wearer produces exactly the predecessor state used in the corresponding transition.

Conversely, every transition adds a legal unused current hat to one unassigned preferring person. Thus states count all and only valid partial assignments. The all-bits mask at row `m` counts precisely the ways to give every person a different preferred hat.

## Complexity detail

Let $p$ be the number of people and $m\le40$ the largest relevant hat label. There are $m2^p$ states. For each state, the inner loop can inspect up to $p$ people who prefer the current hat. Time is $O(mp2^p)$, commonly written $O(40p2^p)$ under the fixed hat-label limit.

The exact table has $(m+1)2^p$ entries, so its space is $O(m2^p)$. The manifest advertises $O(2^p)$ space; that requires rolling the hat dimension because row `i` depends only on row `i-1`. The protected source stores every row, so the full-table bound is the accurate one for this implementation.

## Alternatives and edge cases

- **Rolling mask arrays:** Keep only previous and current hat rows to realize $O(2^p)$ DP space.
- **Top-down memoization:** Cache by current hat label and assigned-people mask. It follows the same recurrence and may skip unreachable states.
- **Track used hats per person-first recursion:** This creates a $2^{40}$ hat mask and is infeasible.
- **Hat liked by nobody:** `g[i]` is empty, so the row simply copies all skip counts.
- **Hat liked by many people:** It can contribute one transition per eligible destination person, but only one wearer in any assignment.
- **Person with one preferred hat:** Every successful full-mask path must assign that exact hat to the person.
- **More people than usable distinct hats:** The full mask remains unreachable and the answer is zero.
- **Maximum preferred label below 40:** Hats above `m` cannot help and are safely omitted.
- **All people like the same set:** The DP counts distinct one-to-one assignments, including permutations of hat choices.
- **Modulo arithmetic:** Counts can be huge, so every additive transition is reduced modulo $10^9+7$.
