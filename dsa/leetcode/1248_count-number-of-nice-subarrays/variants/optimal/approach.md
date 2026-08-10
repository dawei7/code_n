## General

**Replace values by the only property that matters**

A subarray is nice when it contains exactly \(k\) odd values. The actual magnitudes do not matter. `v & 1` is one for an odd positive integer and zero for an even one, so counting odd numbers becomes a prefix-sum problem over zeros and ones.

The variable `t` is the number of odd elements in the prefix processed so far.

**Derive the prefix-count equation**

Let \(P(r)\) be the odd count in the prefix ending just before boundary \(r\), with \(P(0)=0\). A subarray between boundaries \(l\) and \(r\) contains

\[
P(r)-P(l)
\]

odd values. It is nice exactly when

\[
P(r)-P(l)=k,
\]

or

\[
P(l)=P(r)-k.
\]

When the scan reaches a right boundary with current prefix count `t`, every earlier prefix whose count is `t - k` creates one nice subarray ending there.

**Store how often each prefix count has appeared**

`cnt` maps an odd-prefix count to the number of earlier boundaries with that count. It begins as `Counter({0: 1})` because the empty prefix before the first element has zero odd values.

For each `v`:

1. `t += v & 1` updates the current odd count.
2. `ans += cnt[t - k]` adds every valid earlier start boundary.
3. `cnt[t] += 1` records the current boundary for subarrays ending later.

The order of steps matters. The current prefix is queried against earlier prefixes before it is inserted. With the stated \(k\geq1\), inserting first would not match itself anyway, but the established order directly reflects nonempty subarray boundaries.

**Why repeated prefix counts represent different subarrays**

Even values do not change `t`, so the same prefix count may appear at several positions. Those are distinct possible start boundaries.

For example, if there are three even numbers before the first relevant odd, several prefixes share odd count zero. When a later endpoint reaches count \(k\), each zero-count boundary gives a different subarray with exactly \(k\) odds. Storing a frequency rather than a simple set counts all of them.

**Following the first example**

For `nums = [1,1,2,1,1]` and \(k=3\), the prefix odd counts after elements are 1, 2, 2, 3, 4.

At count 3, the needed earlier count is zero. The initialized empty prefix supplies one subarray, `[1,1,2,1]`.

At count 4, the needed count is one. Count one appeared after the first element, supplying `[1,2,1,1]` beginning at the second element.

No other endpoint finds a needed prefix, so the answer is two.

**Why all-even input returns zero for positive \(k\)**

The running count remains zero. Every query asks for `cnt[-k]`, which is zero because no prefix has a negative number of odds. The answer remains zero.


Before each element is processed, `cnt[c]` equals the number of already seen prefix boundaries with exactly \(c\) odd values, `t` is the most recent prefix count, and `ans` counts every nice subarray ending before the current element.

After updating `t`, the equation above proves that exactly `cnt[t-k]` new nice subarrays end at the current position. Adding that number counts each once. Recording the current prefix restores the invariant for the next iteration. At the end, all possible right endpoints have been processed, so `ans` is the total.

**Counter side effects**

Reading a missing key from `Counter` returns zero without raising an error. The expression `cnt[t - k]` may create no explicit entry on read, while `cnt[t] += 1` stores encountered prefix counts. The number of relevant keys is at most \(n+1\).

**Why a naive sliding count is easy to get wrong**

For a fixed right endpoint, leading and trailing even values can create several subarrays with the same \(k\) odds. Merely finding one window would undercount. Prefix frequencies naturally capture all possible starts.

## Complexity detail

Let \(n=\lvert\texttt{nums}\rvert\). The method scans the array once. Each iteration performs expected \(O(1)\) hash-table work, so expected time is \(O(n)\).

The counter can store one key per possible odd prefix count from zero through the number of odd values, at most \(n+1\). Auxiliary space is \(O(n)\) in the worst case. Scalar variables use \(O(1)\).

## Alternatives and edge cases

- **Constant-space sliding window:** Count subarrays with at most \(k\) odds and subtract those with at most \(k-1\). This achieves \(O(n)\) time and \(O(1)\) space.
- **Queue of odd indices:** Track the last \(k\) odd positions and count valid leading even choices. It is linear but uses extra index storage.
- **All values even:** No positive-\(k\) nice subarray exists.
- **Exactly \(k\) odds in the entire array:** Multiple nice subarrays may still exist because even prefixes and suffixes allow different boundaries.
- **Consecutive odd values:** Prefix counts rise at every position and the frequency map still applies directly.
- **Large even gaps:** Repeated prefix counts accumulate, correctly multiplying the number of start choices.
- **Initialization with zero:** Without the empty prefix, subarrays beginning at index zero would be missed.
- **Bitwise parity:** `v & 1` is equivalent to `v % 2` for the positive integers in the contract.
- **Expected hash complexity:** The \(O(n)\) claim assumes ordinary hash-table behavior.
- **Positive \(k\):** The contract excludes zero; counting all-even subarrays for \(k=0\) would require careful current-prefix insertion semantics.
