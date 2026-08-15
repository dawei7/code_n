### 1. Description

You are given a string `initialCurrency`, and you start with `1.0` of `initialCurrency`.

You are also given four arrays with currency pairs (strings) and rates (real numbers):

- $\text{pairs1}[i] = [\text{startCurrency}_{i}, \text{targetCurrency}_{i}]$ denotes that you can convert from $\text{startCurrency}_{i}$ to $\text{targetCurrency}_{i}$ at a rate of $\text{rates1}[i]$ on **day 1**.

- $\text{pairs2}[i] = [\text{startCurrency}_{i}, \text{targetCurrency}_{i}]$ denotes that you can convert from $\text{startCurrency}_{i}$ to $\text{targetCurrency}_{i}$ at a rate of $\text{rates2}[i]$ on **day 2**.

- Also, each `targetCurrency` can be converted back to its corresponding `startCurrency` at a rate of $1 / rate$.

You can perform **any** number of conversions, **including zero**, using `rates1` on day 1, **followed** by any number of additional conversions, **including zero**, using `rates2` on day 2.

Return the **maximum** amount of `initialCurrency` you can have after performing any number of conversions on both days **in order**.

### 2. Function Contract

**Inputs**

- `initialCurrency`: Input parameter (`str`).
- `pairs1`: Input parameter (`List[List[str]]`).
- `rates1`: Input parameter (`List[float]`).
- `pairs2`: Input parameter (`List[List[str]]`).
- `rates2`: Input parameter (`List[float]`).

**Return value**

- Returns `float`.

### 3. Note

Conversion rates are valid, and there will be no contradictions in the rates for either day. The rates for the days are independent of each other.

### 4. Examples

#### Example 1

- **Input:** initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0]

- **Output:** 720.00000

- **Explanation:** To get the maximum amount of **EUR**, starting with 1.0 **EUR**:

- On Day 1:

		- Convert **EUR **to **USD** to get 2.0 **USD**.

- Convert **USD** to **JPY** to get 6.0 **JPY**.

- On Day 2:

		- Convert **JPY** to **USD** to get 24.0 **USD**.

- Convert **USD** to **CHF** to get 120.0 **CHF**.

- Finally, convert **CHF** to **EUR** to get 720.0 **EUR**.

#### Example 2

- **Input:** initialCurrency = "NGN", pairs1 = [["NGN","EUR"]], rates1 = [9.0], pairs2 = [["NGN","EUR"]], rates2 = [6.0]

- **Output:** 1.50000

- **Explanation:** Converting **NGN** to **EUR** on day 1 and **EUR** to **NGN** using the inverse rate on day 2 gives the maximum amount.

#### Example 3

- **Input:** initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0]

- **Output:** 1.00000

- **Explanation:** In this example, there is no need to make any conversions on either day.

### 5. Constraints

- $1 \le \text{initialCurrency.length} \le 3$

- `initialCurrency` consists only of uppercase English letters.

- $1 \le n = \text{pairs1.length} \le 10$

- $1 \le m = \text{pairs2.length} \le 10$

- $\text{pairs1}[i] = [\text{startCurrency}_{i}, \text{targetCurrency}_{i}]$<!-- notionvc: c31b5bb8-4df6-4987-9bcd-6dff8a5f7cd4 -->

- $\text{pairs2}[i] = [\text{startCurrency}_{i}, \text{targetCurrency}_{i}]$<!--{C}%3C!%2D%2D%20notionvc%3A%20c31b5bb8-4df6-4987-9bcd-6dff8a5f7cd4%20%2D%2D%3E-->

- $1 \le \text{startCurrency}_{i}.length, \text{targetCurrency}_{i}.length \le 3$

- $\text{startCurrency}_{i}$ and $\text{targetCurrency}_{i}$ consist only of uppercase English letters.

- $\text{rates1.length} = n$

- $\text{rates2.length} = m$

- $1.0 \le \text{rates1}[i], \text{rates2}[i] \le 10.0$

- The input is generated such that there are no contradictions or cycles in the conversion graphs for either day.

- The input is generated such that the output is **at most** $5 * 10^{10}$.
