### 1. Description

You are given an array of transactions `transactions` where $\text{transactions}[i] = [\text{from}_{i}, \text{to}_{i}, \text{amount}_{i}]$ indicates that the person with $ID = \text{from}_{i}$ gave $\text{amount}_{i}$$to the person with$ID = \text{to}_{i}$.

Return *the minimum number of transactions required to settle the debt*.

### 2. Function Contract

**Inputs**

- `transactions`: A list of entries $[\text{from}_{i}, \text{to}_{i}, \text{amount}_{i}]$, each describing one completed transfer between two distinct people.

Let $n$ be the number of input transactions, $p$ the number of distinct person identifiers in those transactions, and $k$ the number of people whose net balance is nonzero after all transactions are combined.

**Return value**

- Return the smallest number of additional transactions that can make every person's net balance zero.

Person identifiers label accounts; they need not form a contiguous range.

### 3. Examples

#### Example 1

- **Input:** $transactions = [[0,1,10],[2,0,5]]$
- **Output:** `2`
- **Explanation:**
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
#### Example 2

- **Input:** $transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]$
- **Output:** `1`
- **Explanation:**
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.

### 4. Constraints

- $1 \le \text{transactions.length} \le 8$

- $\text{transactions}[i].length = 3$

- $0 \le \text{from}_{i}, \text{to}_{i} < 12$

- $\text{from}_{i} \neq \text{to}_{i}$

- $1 \le \text{amount}_{i} \le 100$