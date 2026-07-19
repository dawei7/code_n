## General
**Reject impossible window lengths.** If `k > n`, no requested substring fits. Because `s` uses only 26 lowercase letters, `k > 26` also makes an all-distinct window impossible. Either condition yields zero immediately.

**Maintain one exact-length window.** Store the frequency of each character in the current window. As `right` advances, add `s[right]`. Once more than `k` characters are present, remove `s[right - k]`, deleting its frequency entry when the count reaches zero. Each character enters and leaves the window once.

**Use the number of distinct keys.** When the window length is `k`, it has no repetition exactly when its frequency map contains `k` keys. Increment the answer for every such position. This counts overlapping windows independently, including repeated window text at different starts.

After each update, the frequency map describes exactly the last at most `k` characters ending at `right`. A full window is valid precisely when its `k` positions also contribute `k` distinct characters. Therefore every valid start is counted once when its right endpoint arrives, and no invalid window is counted.

## Complexity detail
The scan performs constant expected hash-table work when each of the $n$ characters enters and leaves the window, for $O(n)$ time. At most $min(k,26)$ lowercase-letter keys are stored, giving $O(\min(k,26))$ auxiliary space.

## Alternatives and edge cases
- **Build a set for every window:** This is simple but repeats up to $k$ character inspections per start, taking $O(nk)$ time.
- **Fixed 26-entry array:** It replaces hashing with indexed counts and uses $O(1)$ space under the lowercase alphabet contract.
- **`k > n`:** No complete window exists, so the result is zero.
- **`k > 26`:** The pigeonhole principle guarantees a repeated lowercase letter in every window.
- **`k = 1`:** Every one-character substring is valid, including repeated letters at different indices.
- **Overlapping valid windows:** Each start position is counted separately even when windows share most characters.
