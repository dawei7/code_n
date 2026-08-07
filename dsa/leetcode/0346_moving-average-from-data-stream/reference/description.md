### 1. Description

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the `MovingAverage` class:

- `MovingAverage(int size)` Initializes the object with the size of the window `size`.

- `double next(int val)` Returns the moving average of the last `size` values of the stream.

### 2. Function Contract

**Inputs**

- `size`: The fixed maximum number of recent values in the window.
- `stream`: For the app adapter, the values supplied to consecutive native `next(val)` calls.

**Return value**

The app adapter returns the sequence of moving averages. Each native `next` call returns only the new average after its value is added.

### 3. Examples

#### Example 1

```
**Input**
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
**Output**
[null, 1.0, 5.5, 4.66667, 6.0]

**Explanation**
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
```

### 4. Constraints

- $1 \le size \le 1000$

- $-10^{5} \le val \le 10^{5}$

- At most $10^{4}$ calls will be made to `next`.