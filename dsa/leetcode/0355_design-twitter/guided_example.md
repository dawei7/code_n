# Guided Example: Design Twitter

We trace the step-by-step social graph relationship modeling (`user_following`), chronological logical timestamping (`self.time`), self-inclusive feed generation (`users = set(following) | {userId}`), and heap-based top-10 most recent tweet retrieval (`heapq.nlargest`) on representative Twitter action sequences:

- **Input:** Sequence of operations:
  1. `postTweet(1, 5)` (User 1 posts tweet 5)
  2. `getNewsFeed(1)` $\implies [5]$ (User 1 sees own tweet 5)
  3. `follow(1, 2)` (User 1 follows User 2)
  4. `postTweet(2, 6)` (User 2 posts tweet 6)
  5. `getNewsFeed(1)` $\implies [6, 5]$ (User 1 sees tweet 6 then tweet 5)
  6. `unfollow(1, 2)` (User 1 unfollows User 2)
  7. `getNewsFeed(1)` $\implies [5]$ (Tweet 6 is removed from feed)
- **Required output:** `[[5], [6, 5], [5]]`
- **Self-Feed Invariant:** A user always sees their own tweets regardless of whether they follow themselves
- **News Feed Capacity Limit:** The feed yields at most the 10 most recent tweets even if followed accounts have posted hundreds of tweets

This instance demonstrates object-oriented system design with inverted indexing and fan-out-on-read querying, mathematically proves why timestamp-keyed heaps preserve global chronological order across distributed user tweet streams, and analyzes time and space bounds.

---

## 1. Instance & Teaching Goal

Implement a simplified Twitter service supporting 4 core operations:
1. `postTweet(userId, tweetId)`: User posts a tweet.
2. `getNewsFeed(userId)`: Retrieve the 10 most recent tweet IDs in the user's feed (posted by followed users or by the user themself), ordered from newest to oldest.
3. `follow(followerId, followeeId)`: Follow an account.
4. `unfollow(followerId, followeeId)`: Unfollow an account.

```text
Timeline of Events:
t = 1: User 1 posts Tweet 5.
       NewsFeed(User 1): [5]

t = 2: User 1 follows User 2.
t = 3: User 2 posts Tweet 6.
       NewsFeed(User 1): [6, 5]  <-- Tweet 6 (t=3) is newer than Tweet 5 (t=1)!

t = 4: User 1 unfollows User 2.
       NewsFeed(User 1): [5]     <-- Tweet 6 filtered out!
```

---

## 2. Conceptual Foundation & Invariants

### 1. Data Store Entities
- `user_tweets`: `defaultdict(list)` mapping `userId` to an append-only list of posted tweet IDs.
- `user_following`: `defaultdict(set)` mapping `followerId` to the set of `followeeId`s they follow.
- `tweets`: `defaultdict(int)` mapping each `tweetId` to its global logical timestamp `self.time`.
- `time`: A monotonic integer incremented on each `postTweet` call.

### 2. Operational Semantics:
- **`postTweet(userId, tweetId)`:**
  $$
  time \leftarrow time + 1
  $$
  $$
  user\_tweets[userId].\text{append}(tweetId), \quad tweets[tweetId] = time
  $$
- **`follow(followerId, followeeId)`:**
  $$
  user\_following[followerId].\text{add}(followeeId)
  $$
- **`unfollow(followerId, followeeId)`:**
  Remove `followeeId` from `user_following[followerId]` if present.
- **`getNewsFeed(userId)`:**
  1. Build candidate authors set:
     $$
     users = set(user\_following[userId]) \cup \{userId\}
     $$
  2. For each author $u \in users$, take their up to 10 most recent tweets:
     $$
     recent\_tweets = [user\_tweets[u][::-1][:10] \text{ for } u \in users]
     $$
  3. Extract top 10 chronologically newest using max-heap:
     $$
     \text{nlargest}(10, \; \text{flatten}(recent\_tweets), \; \text{key} = \lambda t: tweets[t])
     $$

> **Invariant.** Global timestamp `self.time` increases strictly monotonically, establishing an absolute, collision-free total order over all tweets across all users.

---

## 3. Step-by-Step Worked Execution

We trace the operational sequence:

---

### Step 1: `postTweet(1, 5)`
- Increment time: $time \leftarrow 0 + 1 = \mathbf{1}$.
- Record tweet:
  $$
  user\_tweets[1] = [5]
  $$
  $$
  tweets[5] = 1
  $$

---

### Step 2: `getNewsFeed(1)`
- Author set: $users = set(\emptyset) \cup \{1\} = \{1\}$.
- Candidates: User 1's tweets $\implies [5]$.
- `nlargest(10, [5])` returns $\mathbf{[5]}$.

---

### Step 3: `follow(1, 2)`
- Update social graph:
  $$
  user\_following[1].\text{add}(2) \implies user\_following[1] = \{2\}
  $$

---

### Step 4: `postTweet(2, 6)`
- Increment time: $time \leftarrow 1 + 1 = \mathbf{2}$.
- Record tweet:
  $$
  user\_tweets[2] = [6]
  $$
  $$
  tweets[6] = 2
  $$

---

### Step 5: `getNewsFeed(1)`
- Author set: $users = \{2\} \cup \{1\} = \{1, 2\}$.
- Collect recent tweets:
  - User 1: $[5]$ (Timestamp 1)
  - User 2: $[6]$ (Timestamp 2)
- Candidate pool: $[5, 6]$.
- Rank by timestamp:
  - Tweet 6 has $time = 2$
  - Tweet 5 has $time = 1$
- `nlargest(10, [5, 6])` yields $\mathbf{[6, 5]}$.

---

### Step 6: `unfollow(1, 2)`
- Remove 2 from following set:
  $$
  user\_following[1].\text{remove}(2) \implies user\_following[1] = \emptyset
  $$

---

### Step 7: `getNewsFeed(1)`
- Author set: $users = \emptyset \cup \{1\} = \{1\}$.
- Candidate pool: $[5]$.
- `nlargest(10, [5])` yields $\mathbf{[5]}$.

---

## 4. Complete Execution Trace

```text
Action 1: postTweet(1, 5) -> time=1, user_tweets[1]=[5], tweets[5]=1
Action 2: getNewsFeed(1)  -> users={1}, candidates=[5]            -> returns [5]
Action 3: follow(1, 2)    -> user_following[1]={2}
Action 4: postTweet(2, 6) -> time=2, user_tweets[2]=[6], tweets[6]=2
Action 5: getNewsFeed(1)  -> users={1, 2}, candidates=[5, 6]      -> returns [6, 5]
Action 6: unfollow(1, 2)  -> user_following[1]={}
Action 7: getNewsFeed(1)  -> users={1}, candidates=[5]            -> returns [5]
```

| Step | Operation | Mutated Internal State | Active Feed Authors for User 1 | Tweet Candidate Pool | Ordered Output Emitted |
|:---:|:---:|:---|:---:|:---:|:---:|
| 1 | `postTweet(1, 5)` | $time=1, tweets[5]=1$ | - | - | None |
| **2** | **`getNewsFeed(1)`** | - | $\{1\}$ | `[5]` | **`[5]`** |
| 3 | `follow(1, 2)` | $following[1]=\{2\}$ | - | - | None |
| 4 | `postTweet(2, 6)` | $time=2, tweets[6]=2$ | - | - | None |
| **5** | **`getNewsFeed(1)`** | - | $\{1, 2\}$ | `[5, 6]` | **`[6, 5]`** |
| 6 | `unfollow(1, 2)` | $following[1]=\emptyset$ | - | - | None |
| **7** | **`getNewsFeed(1)`** | - | $\{1\}$ | `[5]` | **`[5]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Tweets are tagged with unique increasing integer timestamps upon creation. When `getNewsFeed` is invoked, `users.add(userId)` guarantees the user's own tweets are considered. Slicing the last 10 elements of each followed user's tweet history bounds the candidate pool to at most $10 \times |users|$ items. The heap selection `nlargest` returns the 10 globally newest tweets in descending timestamp order.

**Completeness.** Since each user's tweet list is append-only, the newest tweets are always at the end. Any tweet outside the newest 10 of a specific user could never beat that same user's 10 newer tweets, ensuring no top-10 candidate across the network is prematurely discarded.

---

## 6. Traps This Instance Exposes

- **Self-Follow / Self-Unfollow Guard:** If a user follows themselves or calls `unfollow(userId, userId)`, removing `userId` from `user_following` could accidentally hide their own tweets. Explicitly adding `users.add(userId)` at feed generation time guarantees self-visibility regardless of follow set manipulation.
- **Unfollow When Not Following:** Calling `unfollow` for a user not currently followed must be a no-op; checking `if followeeId in following:` prevents KeyError exceptions.
- **Feed Fan-Out Memory Overhead:** Storing a precomputed timeline for each user (fan-out on write) consumes excessive memory for accounts with millions of followers. Fan-out on read with a k-way heap merge keeps storage minimal.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `postTweet`: $O(1)$ constant time list append and dictionary insert.
  - `follow` / `unfollow`: $O(1)$ constant time hash set addition / removal.
  - `getNewsFeed`: $O(F \log K)$, where $F$ is the number of followed users ($F = |users|$) and $K = 10$. Merging up to $10 \cdot F$ candidate tweets with `nlargest(10, ...)` takes $O(F \log 10) = O(F)$ time.
- **Auxiliary Space Complexity:** $O(U + T)$, where $U$ is the number of users and follow relationships, and $T$ is the total number of posted tweets.
