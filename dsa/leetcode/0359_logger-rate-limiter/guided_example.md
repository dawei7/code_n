# Guided Example: Logger Rate Limiter

We trace the step-by-step next-allowed-timestamp caching (`ts[message] = timestamp + 10`), threshold comparison (`t > timestamp`), state invariance on rate-limited rejections, and sliding 10-second print permission on representative log stream sequences:

- **Input:** Stream of log print requests:
  1. `shouldPrintMessage(1, "foo")` $\implies \text{true}$ (`"foo"` next allowed at $1 + 10 = 11$)
  2. `shouldPrintMessage(2, "bar")` $\implies \text{true}$ (`"bar"` next allowed at $2 + 10 = 12$)
  3. `shouldPrintMessage(3, "foo")` $\implies \text{false}$ (Time $3 < 11$, rate-limited)
  4. `shouldPrintMessage(8, "bar")` $\implies \text{false}$ (Time $8 < 12$, rate-limited)
  5. `shouldPrintMessage(10, "foo")` $\implies \text{false}$ (Time $10 < 11$, rate-limited)
  6. `shouldPrintMessage(11, "foo")` $\implies \text{true}$ (Time $11 \ge 11$, eligible! Next allowed at $11 + 10 = 21$)
- **Required output:** `[true, true, false, false, false, true]`
- **Strict Boundary Equality:** An event at exactly $t = 11$ for a message printed at $t = 1$ is permitted ($11 - 1 = 10 \ge 10$)
- **No Penalty on Rejection:** Suppressed messages do **not** extend the cooldown window; the next allowed timestamp remains anchored to the last successful print

This instance demonstrates token-bucket / rate-limiting systems design, mathematically proves why storing future eligibility thresholds simplifies range arithmetic into $O(1)$ scalar checks, and analyzes constant time and linear message memory bounds.

---

## 1. Instance & Teaching Goal

Design a logger system that receives a stream of incoming messages with strictly non-decreasing integer timestamps.
Each unique message should be printed **at most once every 10 seconds**:
- If message $M$ is printed at timestamp $t$, any subsequent call for $M$ at timestamp $t' < t + 10$ must be rejected (`false`).
- If $t' \ge t + 10$, the message is accepted (`true`), resetting the next eligible window to $t' + 10$.

```text
Message: "foo" printed at t = 1
Next Allowed Timestamp: 1 + 10 = 11

Calls:
t = 3  : "foo" -> 3 < 11   -> REJECT (false)
t = 10 : "foo" -> 10 < 11  -> REJECT (false)
t = 11 : "foo" -> 11 >= 11 -> ACCEPT (true), update next allowed to 11 + 10 = 21!
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Forward-Threshold Dictionary (`ts`)
Instead of storing the last print timestamp and computing `timestamp - last_time >= 10`, we store the **earliest future timestamp at which the message is permitted to print**:
$$
ts[message] = timestamp + 10
$$

### 2. Decision Logic on `shouldPrintMessage(timestamp, message)`:
1. Query stored threshold:
   $$
   t = ts.\text{get}(message, \; 0)
   $$
2. **Rejection Condition:**
   If $t > timestamp$:
   $$
   \text{return } \mathbf{\text{False}}
   $$
   *(Crucial: The dictionary is NOT modified on rejection!)*
3. **Acceptance Condition:**
   If $t \le timestamp$:
   $$
   ts[message] \leftarrow timestamp + 10
   $$
   $$
   \text{return } \mathbf{\text{True}}
   $$

> **Invariant.** For every message, `ts[message]` holds the exact minimum timestamp required for its next emission. Unsuccessful requests never modify this threshold.

---

## 3. Step-by-Step Worked Execution

We trace the operational sequence:

---

### Step 1: `shouldPrintMessage(1, "foo")`
- Query: $t = ts.\text{get}(\text{"foo"}, 0) = 0$.
- Compare: $0 > 1$ is False.
- Decision: **Accept!**
- Update threshold:
  $$
  ts[\text{"foo"}] \leftarrow 1 + 10 = \mathbf{11}
  $$
- Return: **`true`**.

---

### Step 2: `shouldPrintMessage(2, "bar")`
- Query: $t = ts.\text{get}(\text{"bar"}, 0) = 0$.
- Compare: $0 > 2$ is False.
- Decision: **Accept!**
- Update threshold:
  $$
  ts[\text{"bar"}] \leftarrow 2 + 10 = \mathbf{12}
  $$
- Return: **`true`**.

---

### Step 3: `shouldPrintMessage(3, "foo")`
- Query: $t = ts[\text{"foo"}] = 11$.
- Compare:
  $$
  11 > 3 \implies \mathbf{\text{True (Too early!)}}
  $$
- Decision: **Reject!**
- Threshold $ts[\text{"foo"}]$ remains unchanged at $11$.
- Return: **`false`**.

---

### Step 4: `shouldPrintMessage(8, "bar")`
- Query: $t = ts[\text{"bar"}] = 12$.
- Compare:
  $$
  12 > 8 \implies \mathbf{\text{True (Too early!)}}
  $$
- Decision: **Reject!**
- Return: **`false`**.

---

### Step 5: `shouldPrintMessage(10, "foo")`
- Query: $t = ts[\text{"foo"}] = 11$.
- Compare:
  $$
  11 > 10 \implies \mathbf{\text{True (Still within 10-second window!)}}
  $$
- Decision: **Reject!**
- Return: **`false`**.

---

### Step 6: `shouldPrintMessage(11, "foo")`
- Query: $t = ts[\text{"foo"}] = 11$.
- Compare:
  $$
  11 > 11 \implies \mathbf{\text{False (Boundary reached!)}}
  $$
- Decision: **Accept!**
- Update threshold:
  $$
  ts[\text{"foo"}] \leftarrow 11 + 10 = \mathbf{21}
  $$
- Return: **`true`**.

---

## 4. Complete Execution Trace

```text
Stream Trace:
Call 1: (1, "foo")  -> threshold 0 <= 1  -> ts["foo"] = 11 -> True
Call 2: (2, "bar")  -> threshold 0 <= 2  -> ts["bar"] = 12 -> True
Call 3: (3, "foo")  -> threshold 11 > 3  -> Rate-limited   -> False
Call 4: (8, "bar")  -> threshold 12 > 8  -> Rate-limited   -> False
Call 5: (10, "foo") -> threshold 11 > 10 -> Rate-limited   -> False
Call 6: (11, "foo") -> threshold 11 <= 11-> ts["foo"] = 21 -> True

Result Stream: [true, true, false, false, false, true]
```

| Step | Timestamp | Message | Next Allowed Threshold $t$ | $t > \text{timestamp}$? | Action Taken | Updated Threshold in `ts` | Output Emitted |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| 1 | 1 | `"foo"` | 0 (Default) | No | Accept, set $+10$ | `ts["foo"] = 11` | **`true`** |
| 2 | 2 | `"bar"` | 0 (Default) | No | Accept, set $+10$ | `ts["bar"] = 12` | **`true`** |
| 3 | 3 | `"foo"` | 11 | Yes ($11 > 3$) | Reject | Unchanged ($11$) | **`false`** |
| 4 | 8 | `"bar"` | 12 | Yes ($12 > 8$) | Reject | Unchanged ($12$) | **`false`** |
| 5 | 10 | `"foo"` | 11 | Yes ($11 > 10$) | Reject | Unchanged ($11$) | **`false`** |
| **6** | **11** | **`"foo"`** | **11** | **No ($11 \le 11$)** | **Accept, set $+10$** | **`ts["foo"] = 21`** | **`true`** |

---

## 5. Algorithmic Correctness

**Soundness.** A message is accepted if and only if $timestamp \ge t_{prev} + 10$. Precomputing $t = t_{prev} + 10$ and testing $t > timestamp$ guarantees that any event arriving within 9 seconds of the prior print is rejected, while an event arriving at or after 10 seconds is accepted.

**Completeness.** Each message's rate-limiting status is completely independent of other messages, preventing cross-message interference. Using default value $0$ for unseen keys guarantees that any first occurrence is accepted without special-case branching.

---

## 6. Traps This Instance Exposes

- **Updating Threshold on Rejection:** If `ts[message] = timestamp + 10` were updated on rejected requests, repeated failed requests would continually postpone future print permissions indefinitely (starvation).
- **Strict Inequality vs Non-Strict Inequality:** A message printed at $t = 1$ is permitted to print again at exactly $t = 11$ ($11 - 1 = 10 \ge 10$). Testing $t > timestamp$ correctly permits equality ($11 > 11$ is False $\implies$ prints).
- **Unbounded Memory Growth:** In continuous production systems, storing all historical message keys in a hash map without eviction can cause unbounded memory growth. Sliding window deques or TTL caches can clean up messages inactive for over 10 seconds.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ per `shouldPrintMessage` call. Hash table lookup and insertion take $O(1)$ average time.
- **Auxiliary Space Complexity:** $O(M)$, where $M$ is the number of distinct message strings received across the entire lifetime of the logger.
