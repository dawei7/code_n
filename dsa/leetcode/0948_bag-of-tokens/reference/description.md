### 1. Description

You start with an initial **power** of `power`, an initial **score** of `0`, and a bag of tokens given as an integer array `tokens`, where each $\text{tokens}[i]$ denotes the value of token*_i*.

Your goal is to **maximize** the total **score** by strategically playing these tokens. In one move, you can play an **unplayed** token in one of the two ways (but not both for the same token):

- **Face-up**: If your current power is **at least** $\text{tokens}[i]$, you may play token*_i*, losing $\text{tokens}[i]$ power and gaining `1` score.

- **Face-down**: If your current score is **at least** `1`, you may play token*_i*, gaining $\text{tokens}[i]$ power and losing `1` score.

Return *the **maximum** possible score you can achieve after playing **any** number of tokens*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

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
**Input:** tokens = [100], power = 50

**Output:** 0

**Explanation****:** Since your score is `0` initially, you cannot play the token face-down. You also cannot play it face-up since your power (`50`) is less than $\text{tokens}[0]$ (`100`).

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
**Input:** tokens = [200,100], power = 150

**Output:** 1

**Explanation:** Play token*_1* (`100`) face-up, reducing your power to `50` and increasing your score to `1`.

There is no need to play token*_0*, since you cannot play it face-up to add to your score. The maximum score achievable is `1`.

</div>
#### Example 3

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
**Input:** tokens = [100,200,300,400], power = 200

**Output:** 2

**Explanation:** Play the tokens in this order to get a score of `2`:

- Play token*_0* (`100`) face-up, reducing power to `100` and increasing score to `1`.

- Play token*_3* (`400`) face-down, increasing power to `500` and reducing score to `0`.

- Play token*_1* (`200`) face-up, reducing power to `300` and increasing score to `1`.

- Play token*_2* (`300`) face-up, reducing power to `0` and increasing score to `2`.

The maximum score achievable is `2`.

</div>

### 4. Constraints

- $0 \le \text{tokens.length} \le 1000$

- $0 \le \text{tokens}[i], power < 10^{4}$