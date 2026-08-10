## General

**Maintain one exact-length window**

Every candidate is a contiguous window of exactly `k` characters. Neighboring candidates overlap in all but one position, so rebuilding a set for every substring repeats almost all work. A sliding window keeps frequency information and updates only the character that enters and the character that leaves.

`Counter(s[:k])` initializes frequencies for the first window. If `k <= len(s)`, this slice contains exactly the first $k$ characters. If `k` is larger than the string, the slice contains the whole shorter string, which is handled naturally.

**Use the number of Counter keys as the distinct count**

The Counter keeps only characters with positive frequency because the algorithm removes a key when its count becomes zero. Therefore, `len(cnt)` is exactly the number of distinct characters in the current window.

A complete window contains $k$ positions. Its characters are pairwise distinct exactly when it has $k$ distinct keys, so `len(cnt) == k` is a complete validity test. Converting the Boolean to an integer contributes one for a valid window and zero otherwise.

The first window is counted through `ans = int(len(cnt) == k)`. When `k > len(s)`, the slice has fewer than $k$ positions, so it cannot have $k$ distinct characters. The initial contribution is zero, and the later loop has no iterations.

**Slide by one character**

For each `i` from `k` through the final string index, `s[i]` enters the window and `s[i-k]` leaves it. The code increments the entering frequency and decrements the outgoing frequency.

If the outgoing count becomes zero, `pop` removes that key. This removal is essential: leaving a zero-count key in the Counter would make `len(cnt)` larger than the number of characters actually present and could create false positives.

Adding before removing is safe even when the entering and outgoing characters are equal. Their two updates cancel, correctly reflecting that the window still contains the same number of occurrences of that character.

After both updates, the Counter describes exactly `s[i-k+1:i+1]`. The same key-count test adds the new window’s contribution. Overlapping occurrences are counted separately because each ending index causes its own test.

**Why every candidate is counted correctly**

Initially, frequencies match the first candidate. Each iteration deletes precisely the old left endpoint and adds precisely the new right endpoint, so by induction the Counter matches the current window. Positive-key cleanup makes its size equal the distinct-character count. A $k$-position window has no repetition exactly when that size is $k$. The loop tests the first window and then every later start once, proving the final count.

Notice that the algorithm never needs to remember the substrings themselves. Two windows with identical text are still encountered at different loop positions and contribute independently. Conversely, frequency counts retain exactly the information relevant to repetition, so discarding character order inside the current window cannot change the validity decision.

## Complexity detail

Let $n$ be the string length. Initializing from a slice costs $O(\min(n,k))$. The loop performs at most $n-k$ iterations, each with expected constant-time Counter operations. Total time is $O(n)$.

The string contains only 26 lowercase English letters. The Counter can hold no more than 26 keys and no more than $k$ positive keys for a $k$-length window, giving $O(\min(k,26))$ auxiliary space. Python slicing creates up to $O(\min(n,k))$ temporary characters during initialization; a strictly no-slice implementation could build the Counter by index, while the package’s stated data-structure bound focuses on maintained frequencies.

## Alternatives and edge cases

- **Set per substring:** Construct `set(s[start:start+k])` for every start. It is simple but costs $O(nk)$ time in the worst case due to repeated slicing and scanning.
- **Fixed array of 26 counts:** Map each lowercase letter to an integer slot. This avoids hashing and has constant 26-entry storage, while requiring a separate distinct counter.
- **Last-seen positions:** Maintain the longest suffix with unique characters and count it whenever its length is at least `k`. This also runs in $O(n)$ and avoids explicit frequency decrements.
- **`k > len(s)`:** No complete candidate exists. The initial distinct count is below `k` and the loop is empty, so zero is returned.
- **`k > 26`:** No lowercase window can contain more than 26 distinct characters, so every test is false.
- **`k == 1`:** Every one-character substring is distinct, so the answer is `len(s)`.
- **Repeated text at different starts:** Each window position is counted independently, as required.
- **Entering character equals leaving character:** Increment then decrement preserves its correct frequency and does not disturb the key.
- **Frequency drops to zero:** Removing the key is required so Counter length remains the current distinct count.
- **All characters identical:** Only windows of length one qualify; every longer window has one distinct key.
- **Window equal to whole string:** The initial test is the only candidate and returns one exactly when all characters are distinct.
