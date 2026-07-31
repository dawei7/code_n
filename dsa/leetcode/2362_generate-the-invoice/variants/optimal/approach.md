## General

**Price and aggregate every invoice once.** Join each purchase to `Products`
by `product_id`, multiply `quantity` by the unit `price`, and group by
`invoice_id`. The resulting total is exactly the sum of all line values on
that invoice.

**Apply both selection rules together.** Order the aggregated invoices by
total descending and `invoice_id` ascending, then retain one row. This chooses
the greatest total and, only among ties, the smallest identifier.

**Return line-level details.** Join the selected identifier back to
`Purchases` and `Products`. Project the purchase's `product_id` and `quantity`
plus `quantity * price` as the output `price`. Every and only line belonging
to the selected invoice is returned.

## Complexity detail

With $P$ product rows and $R$ purchase rows, a conservative sort-based bound
for joining, grouping, and ordering is $O((P+R)\log(P+R))$ time and $O(P+R)$
working space. Hashing and indexes may reduce the physical cost.

## Alternatives and edge cases

- **Window rank:** Rank grouped totals by descending value and ascending ID,
  then select rank one; this is equivalent.
- **Correlated total per invoice:** Recomputing a purchase sum for every
  candidate invoice is correct but can take $O(R^2)$ work.
- **Total ties:** The secondary ascending `invoice_id` ordering is mandatory.
- **Line price:** Output the extended line value, not the product's unit price.
- **Result order:** The selected invoice's detail rows may appear in any order.
