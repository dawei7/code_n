## Description

In a mystic dungeon, `n` magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.

You have been cursed in such a way that after absorbing energy from magician `i`, you will be instantly transported to magician $(i + k)$. This process will be repeated until you reach the magician where $(i + k)$ does not exist.

In other words, you will choose a starting point and then teleport with `k` jumps until you reach the end of the magicians' sequence, **absorbing all the energy** during the journey.

You are given an array `energy` and an integer `k`. Return the **maximum** possible energy you can gain.

**Note** that when you reach a magician, you *must* take energy from them, whether it is negative or positive energy.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
**Input:**  energy = [5,2,-10,-5,1], k = 3

**Output:** 3

**Explanation:** We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.

</div>
#### Example 2

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
**Input:** energy = [-2,-3,-1], k = 2

**Output:** -1

**Explanation:** We can gain a total energy of -1 by starting from magician 2.

</div>
### Constraints

- $1 \le \text{energy.length} \le 10^{5}$

- $-1000 \le \text{energy}[i] \le 1000$

- $1 \le k \le \text{energy.length} - 1$

​​​​​​