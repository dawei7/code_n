## General

Different written email strings may deliver to the same normalized address. The solution transforms every input email into its delivery-equivalent canonical form, inserts that form into a set, and returns the number of unique canonical strings.

**Separate local and domain names.** Each valid email contains exactly one `@`, so

```text
local, domain = email.split("@")
```

produces the two components.

Normalization rules apply only to `local`. The domain must be preserved exactly, including its periods. This distinction is crucial because `leetcode.com` and `lee.tcode.com` are different domains.

**Scan the local name from left to right.**

- A period `.` is ignored with `continue`.
- The first plus `+` ends meaningful local input, so the loop `break`s.
- Any lowercase letter is appended to temporary list `t`.

After the first plus, all remaining local characters—including letters, dots, and later plus signs—are ignored. Breaking immediately implements that rule directly.

Joining `t` removes all periods that appeared before the plus while preserving letter order.

**Reattach the unchanged domain.** The normalized address is

```text
"".join(t) + "@" + domain
```

The explicit `@` prevents ambiguity between the normalized local and domain strings.

**Why this canonicalization is exact.** The forwarding rules say that local periods have no effect and the first plus discards the rest of the local name. Therefore any two emails that normalize to the same local letters and the same domain deliver to the same place.

Conversely, if canonical forms differ, either the effective local letters differ or domains differ. Neither difference is erased by the forwarding rules, so the emails do not deliver to the same address.

Thus equality of normalized strings is necessary and sufficient for delivery equivalence.

**Set counts recipients, not messages.** Every email still causes one message to be sent, but the task asks how many different addresses receive mail. Inserting canonical strings into `s` collapses all duplicate recipients. `len(s)` is the required count.

For `test.email+alex@leetcode.com`, the local scan keeps `testemail`, ignores the dot, and stops at plus. Its canonical address is `testemail@leetcode.com`.

For `testemail+david@lee.tcode.com`, the normalized local is the same but the domain remains `lee.tcode.com`. Because domain periods are not removed, this is a different recipient.

Consider the full local scan for `m.y+name`. The list begins empty. Character `m` is appended, the dot is skipped, and `y` is appended. At plus, scanning stops, so `name` is never examined. Joining produces `my`. This is equivalent to first taking the substring before plus and then deleting its periods.

**Canonicalization is idempotent.** If a normalized address is passed through the same process again, its local name contains neither periods nor a plus suffix, and its domain is unchanged. The result stays identical. This is a useful property of a canonical form: every equivalence class maps to one stable representative.

The order of meaningful local letters is preserved. Period removal closes gaps but never reorders letters, and plus truncation keeps an initial prefix. Therefore `a.b` normalizes to `ab`, while `b.a` normalizes to `ba`; they remain different recipients.

**Order of local rules.** Dots after the first plus are irrelevant because the scan has already stopped. Dots before the plus are skipped. A plus never becomes part of the output local name.

The contract guarantees local and domain names are nonempty and local does not start with plus, so normalized local output remains meaningful for valid inputs.
During the local scan, `t` contains exactly the meaningful letters from the processed prefix: all periods removed and no characters after a plus. Encountering a letter, dot, or first plus preserves this definition through append, skip, or termination. The joined form is therefore the exact effective local name.

After insertion, the set invariant is that `s` contains exactly one canonical representative for every recipient encountered so far. Normalizing the next email either adds a genuinely new recipient or leaves cardinality unchanged for an existing one. Induction over the list proves the final set size is the number of different receiving addresses.

## Complexity detail

Let $S$ be the total number of characters across all input emails. Splitting, scanning, joining, hashing, and set insertion together take expected time proportional to processed text.

- **Time complexity:** $O(S)$ expected.
- **Space complexity:** $O(S)$ in the worst case for canonical strings stored in the set and temporary normalized local data.

The temporary list for one email is bounded by that email's length.

## Alternatives and edge cases

- **Regular expressions:** They can remove dots and plus suffixes but add complexity and must still avoid altering domains.
- **Normalize the full email string:** Incorrect because dots and plus signs in the domain do not use local-name rules.
- **Split local on plus first, then remove dots:** This is an equivalent concise formulation.
- **No dots or plus:** Canonical form equals the original email.
- **Several local dots:** All are removed, including adjacent dots allowed by the simplified contract.
- **Several plus signs:** Only the first matters because everything after it is ignored.
- **Dot after plus:** It is ignored as part of the entire discarded suffix.
- **Same local, different domain:** These are distinct recipients.
- **Different written locals, same normalized letters:** They collapse when domains match.
- **Duplicate identical emails:** The set counts one recipient.
- **Domain periods:** They remain exactly where written.
- **Exactly one `@`:** Makes two-variable split safe.
- **Any input order:** Set cardinality is independent of message order.
- **Local plus near the end:** Even a one-character suffix after plus is fully discarded.
- **Periods only in the domain:** They are preserved, so domains remain distinguishable.
- **Canonical set strings:** Including `@` makes the local/domain boundary explicit.
