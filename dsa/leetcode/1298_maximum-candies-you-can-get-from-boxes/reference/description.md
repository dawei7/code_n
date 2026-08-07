### 1. Description

You have `n` boxes labeled from `0` to $n - 1$. You are given four arrays: `status`, `candies`, `keys`, and `containedBoxes` where:

- $\text{status}[i]$ is `1` if the $$i^{\text{th}}$$ box is open and `0` if the $$i^{\text{th}}$$ box is closed,

- $\text{candies}[i]$ is the number of candies in the $$i^{\text{th}}$$ box,

- $\text{keys}[i]$ is a list of the labels of the boxes you can open after opening the $$i^{\text{th}}$$ box.

- $\text{containedBoxes}[i]$ is a list of the boxes you found inside the $$i^{\text{th}}$$ box.

You are given an integer array `initialBoxes` that contains the labels of the boxes you initially have. You can take all the candies in **any open box** and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return *the maximum number of candies you can get following the rules above*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]$
- **Output:** `16`
- **Explanation:** You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
Box 1 is closed and you do not have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
Total number of candies collected = 7 + 4 + 5 = 16 candy.
#### Example 2

- **Input:** $status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]$
- **Output:** `6`
- **Explanation:** You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys.
The total number of candies will be 6.

### 4. Constraints

- $n = \text{status.length} = \text{candies.length} = \text{keys.length} = \text{containedBoxes.length}$

- $1 \le n \le 1000$

- $\text{status}[i]$ is either `0` or `1`.

- $1 \le \text{candies}[i] \le 1000$

- $0 \le \text{keys}[i].length \le n$

- $0 \le \text{keys}[i][j] < n$

- All values of $\text{keys}[i]$ are **unique**.

- $0 \le \text{containedBoxes}[i].length \le n$

- $0 \le \text{containedBoxes}[i][j] < n$

- All values of $\text{containedBoxes}[i]$ are unique.

- Each box is contained in one box at most.

- $0 \le \text{initialBoxes.length} \le n$

- $0 \le \text{initialBoxes}[i] < n$