### 1. Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the $$i^{\text{th}}$$ line are `(i, 0)` and $(i, \text{height}[i])$.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

### 2. Function Contract

**Inputs**

- `height`: The non-negative line heights in index order.

Let $n = \lvert\texttt{height}\rvert$.

**Return value**

Return the maximum container area formed by two lines and the x-axis.

### 3. Notice

that you may not slant the container.

### 4. Examples

#### Example 1

![](images/question_11.jpg)

- **Input:** $height = [1,8,6,2,5,4,8,3,7]$
- **Output:** `49`
- **Explanation:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

#### Example 2

- **Input:** $height = [1,1]$
- **Output:** `1`

### 5. Constraints

- $n = \text{height.length}$

- $2 \le n \le 10^{5}$

- $0 \le \text{height}[i] \le 10^{4}$
