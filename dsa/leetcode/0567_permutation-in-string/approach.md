## General

A substring is a permutation of `s1` exactly when it has the same length and the same frequency of every lowercase letter. The solution maintains frequency differences for a sliding window of length `m = len(s1)`.

Counter `cnt` starts with the required counts from `s1`. As characters enter the window, their counts are subtracted. As characters leave, their counts are restored.

Interpret `cnt[c]` as:

$$
\text{required copies of }c-\text{copies currently in the window}.
$$

A positive value means the window still lacks that character. Zero means it has exactly the required count. A negative value means it contains extras.

Variable `need` begins as `len(cnt)`, the number of distinct required characters not yet exactly satisfied.

**Add the new right-edge character.** At index `i`, incoming `c` executes `cnt[c] -= 1`.

If that update makes `cnt[c] == 0`, this character's required frequency has just become satisfied, so `need` decreases by one.

Counter automatically creates zero entries for characters absent from `s1`. Subtracting such a character makes its balance negative; it never falsely reduces `need`.

**Remove the character beyond window length.** If `i >= m`, the window would now contain `m + 1` characters. Its oldest character is `s2[i - m]`.

The code adds one back to that character's balance. If the result becomes one, the balance was zero before removal, so an exactly satisfied required count has become deficient. `need` increases.

If a negative balance rises to zero, no deficiency is introduced, so `need` correctly remains unchanged.

After this removal, the active window ends at `i` and has length exactly `m`. During the initial prefix when `i < m`, it contains all characters seen so far.

**Why `need == 0` proves a permutation.** Zero need means no required character has a positive shortage. At a full window of length `m`, the sum of required counts equals the sum of window counts. Therefore there cannot be an unbalanced extra character without a corresponding shortage elsewhere. All balances must be zero, so the multisets match.

Before the window reaches length `m`, it cannot satisfy all `m` required copies, so `need` cannot legitimately become zero.

For `s1 = "ab"` and `s2 = "eidbaooo"`, the fixed windows eventually reach `"ba"`. Subtracting `b` and `a` makes both required balances zero, `need` becomes zero, and the method returns true.

In `"eidboaoo"`, no two-character window has one `a` and one `b` simultaneously, so at least one distinct requirement remains deficient throughout.

**Why only the current window influences the state.** Every incoming character is subtracted once. Exactly `m` positions later, it is restored once. Thus `cnt` always describes the current suffix window and no older character remains.

**Why overlapping windows are handled efficiently.** Moving one step changes only the entering and leaving characters. Rebuilding a full 26-letter frequency table per start would repeat almost all work.

The method returns at the first matching window because only existence is requested. If the scan ends, every possible length-`m` substring has been examined and false is correct.

Consider `s1 = "aab"` and a current window `"aba"`. Initial balances are `a: 2, b: 1`. Reading the first `a` leaves one copy missing; reading `b` satisfies `b`; reading the second `a` satisfies `a`. `need` reaches zero only after exact multiplicities are present. A window `"abb"` instead drives `b` negative while `a` remains positive, so `need` cannot reach zero.

The invariant after each removal is: for every character, `cnt` equals target frequency minus frequency in the current window, and `need` equals the number of target characters with a positive balance. Incoming transitions reduce `need` precisely when a positive balance reaches zero. Outgoing transitions increase it precisely when zero becomes positive. Negative balances may move toward or away from zero without changing shortage status.

This explains why the algorithm does not need to count how many entries are negative. At full window length, total balance over the alphabet is zero. If no entry is positive, none can be negative either; otherwise the totals would not cancel. Hence tracking positive shortages is enough.

## Complexity detail

Let $m=\lvert s1\rvert$ and $n=\lvert s2\rvert$. Building the initial Counter costs $O(m)$ and scanning `s2` costs $O(n)$ expected time, for $O(m+n)$ total.

The alphabet is fixed to 26 lowercase letters. Counter therefore contains at most a constant number of meaningful keys, giving $O(1)$ space under the source constraints, matching the manifest.

Although Counter may receive keys from `s2` that were absent from `s1`, there are still at most 26 possible lowercase keys, so this does not weaken the constant-space claim.

## Alternatives and edge cases

- **Sort every window:** Comparing sorted strings costs at least $O(m\log m)$ per window.
- **Recount every window:** It takes $O(mn)$ time instead of updating two characters.
- **Use two 26-entry arrays:** Directly compare or track matching positions; it has the same asymptotic bounds.
- **`s1` longer than `s2`:** No full window forms and the method returns false.
- **Repeated required letters:** Counter values track exact multiplicity.
- **Extra window character:** Its negative balance forces some required shortage in a full-length window.
- **Character enters and leaves:** Update order temporarily creates length `m+1`, then restores the exact window before testing.
- **Match at the first window:** `need` reaches zero and returns immediately.
- **Overlapping matches:** Existence allows returning the first.
- **Lowercase guarantee:** Constant alphabet justifies $O(1)$ frequency storage.
