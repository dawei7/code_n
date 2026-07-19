## General
**Turn each relevant fact into an event.** Select approved transaction rows as events keyed by the month of `Transactions.trans_date` and by `country`. Each contributes `1` and `amount` to the approved fields and zeros to the chargeback fields. Declined transactions do not create approved events.

**Attach chargebacks to their transaction attributes.** Join each `Chargebacks.trans_id` to `Transactions.id` to recover the transaction's `country` and `amount`. Key this event by the month of `Chargebacks.trans_date`, not the original transaction date, and contribute only to the chargeback fields. This join works identically for approved and declined original transactions.

**Aggregate the unified stream.** Combine the two event sets with `UNION ALL`, then group by `month` and `country` and sum all four numeric contributions. Every event has at least one nonzero count, so only groups with approved or chargeback activity are created; declined-only groups with no chargeback never enter the stream. A deterministic `ORDER BY` is useful for local fixtures even though the platform permits any row order.

## Complexity detail
With an indexed or hash lookup from each of the $c$ chargebacks to its transaction, the event construction processes $t+c$ rows. Hash aggregation adds constant expected work per event, for $O(t+c)$ logical time. The aggregation stores one fixed record for each of the $g$ reported keys, requiring $O(g)$ auxiliary space. Physical database plans may choose sorting or different join strategies.

## Alternatives and edge cases
- **Correlated aggregates per month-country key:** Recomputing each of the four metrics for every key is correct but can take $O(g(t+c))$ time.
- **Redundant cross-product aggregation:** Repeating every event once per transaction and dividing the resulting sums by the transaction count preserves the metrics but creates quadratically many intermediate rows.
- **Full outer join of monthly summaries:** Separately aggregating approved transactions and chargebacks and then full-joining the summaries works on engines that support it, but requires careful key coalescing and zero filling.
- **Use the original date for chargebacks:** This incorrectly attributes a later chargeback to the transaction month rather than the chargeback month.
- **Declined transaction with a chargeback:** It adds zero approved activity and still contributes its amount to chargeback metrics.
- **Declined-only month:** Without a chargeback, it produces no output row because all four requested values are zero.
- **Chargeback-only month:** It must appear with approved count and amount equal to zero.
- **Multiple countries:** Equal calendar months remain separate when their countries differ.
- **Any output order:** Ordering is not part of the platform contract, though the app-local query sorts the keys for stable verification.
