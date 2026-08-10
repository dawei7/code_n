## General

**Replay events in the only order that makes status meaningful.** Mentions depend on whether a user is online at a message timestamp, so input order cannot be trusted. The source sorts `events` by

`(int(e[1]), e[0][2])`.

The first key is numeric time. The second key is a compact tie-breaker: character index two is `"F"` for `"OFFLINE"` and `"S"` for `"MESSAGE"`. Since `"F" < "S"`, offline events precede messages at the same timestamp, satisfying the rule that status changes happen first.

The sort mutates the input `events` list. All later processing is chronological.

**Represent offline status by a return time.** `online_t[user]` is the earliest timestamp at which that user is online again. Every entry begins at zero, so all users are online at every allowed positive timestamp.

For an offline event at time `cur`, the source sets

`online_t[user] = cur + 60`.

At a later time, `online_t[user] <= cur` means the automatic return has occurred and the user is online. A user is offline while the stored time is strictly greater than the message time. The input guarantee that offline events name currently online users means no overlapping offline interval needs to be combined.

**Handle the four event/token forms.** The source first identifies offline events through `etype[0] == "O"`.

For a message whose text begins with `"A"`, the token is `"ALL"`. Every user receives one mention regardless of status. Instead of looping over all users immediately, the source increments scalar `lazy`. After all events, it adds this global number to every answer entry. This converts any number of ALL messages from repeated user scans into one final scan.

For a token beginning with `"H"`, the token is `"HERE"`. The source scans `online_t` and increments `ans[i]` exactly when the user's return time is at most `cur`. HERE cannot be accumulated globally because its recipient set changes over time.

Otherwise, the message contains explicit tokens such as `"id1 id0 id1"`. Splitting on whitespace preserves duplicates. For each token `a`, `a[2:]` removes the `"id"` prefix, and the parsed user receives one increment. Explicit mentions count even when the user is offline.

For example, an offline user with return time $71$ is included in HERE at timestamp $71$ because the comparison is `<=`. This implements automatic return before same-time messages.

**Why lazy ALL mentions are safe.** An ALL mention always contributes exactly one to every user and is independent of event order, online state, and later offline intervals. Addition is commutative, so postponing all those identical contributions until the end cannot change any result. Explicit and HERE counts continue to accumulate directly in `ans`.
Immediately before each processed event, every `online_t` entry describes the user's current status at that timestamp. Same-time offline events were sorted first, and automatic return is recognized by comparison rather than by a separate event. Each message branch implements its token's recipient definition, including repeated explicit IDs. Thus direct counts are exact; adding the deferred ALL count completes every user's total.

The source's sort tie-breaker relies on the exact two event names. It is clever but less self-documenting than `e[0] == "MESSAGE"`; under the contract, both produce the required order.

## Complexity detail

Let $E$ be the number of events, $U$ the number of users, $H$ the number of HERE messages, and $M$ the total number of explicit ID tokens. Sorting costs $O(E\log E)$. Playback costs $O(E+HU+M)$, and the final lazy addition costs $O(U)$. Total time is $O(E\log E+HU+M+U)$.

The answer and return-time arrays use $O(U)$ space. Python sorting can use $O(E)$ temporary space. Split token lists require space proportional to one message at a time, bounded by its token count. Total peak auxiliary space is $O(E+U+M_{\max})$, commonly summarized as $O(E+U)$ under the given per-message bound.

## Alternatives and edge cases

- **Apply ALL immediately:** It is correct but costs $O(U)$ per ALL message. The lazy scalar reduces all such work to one final pass.
- **Explicit online/offline Boolean:** It would require scheduling return events or checking timestamps separately. A next-online time represents both states compactly.
- **Wrong same-time order:** Processing a message before OFFLINE at the same timestamp would incorrectly include that user in HERE.
- **Automatic return time:** A user is online at exactly `offline_time + 60`, so the comparison must be `<=`.
- **Duplicate explicit IDs:** Splitting and incrementing every token counts duplicates separately as required.
- **Offline explicit mention:** The explicit-ID branch never checks `online_t`, correctly counting offline users.
- **ALL while offline:** Deferred ALL mentions still reach every user because status is irrelevant.
- **Initially online:** Zero return times make every user pass HERE at positive timestamps until an offline event changes the entry.
- **Input mutation:** `events.sort` reorders the caller's event list.
- **Tie-break key:** `e[0][2]` works only because the guaranteed names place `"F"` before `"S"`; an explicit Boolean is clearer for maintenance.
