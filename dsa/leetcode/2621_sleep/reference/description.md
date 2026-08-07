### 1. Description

Given a positive integer `millis`, write an asynchronous function that sleeps for `millis` milliseconds. It can resolve any value.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

that *minor* deviation from `millis` in the actual sleep duration is acceptable.

### 4. Examples

#### Example 1

- **Input:** $millis = 100$
- **Output:** `100`
- **Explanation:** It should return a promise that resolves after 100ms.
let t = Date.now();
sleep(100).then(() => {
console.log(Date.now() - t); // 100
});
#### Example 2

- **Input:** $millis = 200$
- **Output:** `200`
- **Explanation:** It should return a promise that resolves after 200ms.

### 5. Constraints

- $1 \le millis \le 1000$