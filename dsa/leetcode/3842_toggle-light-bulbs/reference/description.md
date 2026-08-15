### 1. Description

You are given an array `bulbs` of integers between 1 and 100.

There are 100 light bulbs numbered from 1 to 100. All of them are switched off initially.

For each element $\text{bulbs}[i]$ in the array `bulbs`:

- If the $\text{bulbs}[i]^th$ light bulb is currently off, switch it on.

- Otherwise, switch it off.

Return the list of integers denoting the light bulbs that are on in the end, **sorted** in **ascending** order. If no bulb is on, return an empty list.

### 2. Function Contract

**Inputs**

- `bulbs`: The sequence of bulb numbers to toggle, in operation order.

For each bulb number $b\in\{1,\ldots,100\}$, define its occurrence count

$C(b)=\left\lvert\left\{i\mid\texttt{bulbs}[i]=b\right\}\right\rvert.$

All bulbs begin off, and each occurrence reverses exactly one bulb's state. Consequently, bulb $b$ is on at the end exactly when $C(b)$ is odd.

**Return value**

Return every $b$ with odd $C(b)$ in ascending numeric order. If no such bulb exists, return `[]`.

### 3. Examples

#### Example 1

- **Input:** bulbs = [10,30,20,10]

- **Output:** [20,30]

- **Explanation:** 

- The $\text{bulbs}[0] = 10^th$ light bulb is currently off. We switch it on.

- The $\text{bulbs}[1] = 30^th$ light bulb is currently off. We switch it on.

- The $\text{bulbs}[2] = 20^th$ light bulb is currently off. We switch it on.

- The $\text{bulbs}[3] = 10^th$ light bulb is currently on. We switch it off.

- In the end, the 20^th and the 30^th light bulbs are on.

#### Example 2

- **Input:** bulbs = [100,100]

- **Output:** []

- **Explanation:** 

- The $\text{bulbs}[0] = 100^th$ light bulb is currently off. We switch it on.

- The $\text{bulbs}[1] = 100^th$ light bulb is currently on. We switch it off.

- In the end, no light bulb is on.

### 4. Constraints

- $1 \le \text{bulbs.length} \le 100$

- $1 \le \text{bulbs}[i] \le 100$
