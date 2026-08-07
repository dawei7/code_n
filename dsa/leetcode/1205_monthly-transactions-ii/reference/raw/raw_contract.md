## Function Contract

**Input tables**

- `Transactions(id, country, state, amount, trans_date)` supplies each transaction's unique identifier, country, approval state, amount, and date.
- `Chargebacks(trans_id, trans_date)` supplies the referenced transaction identifier and the date of each chargeback.

Let $t$ be the number of transaction rows, $c$ the number of chargeback rows, and $g$ the number of reported month-country groups.

**Return value**

Return one row for every relevant `(month, country)` pair with these columns:

- `month`: the event month in `YYYY-MM` form;
- `country`: the transaction's country;
- `approved_count`: the number of approved transactions in that transaction month and country;
- `approved_amount`: the sum of those approved transaction amounts;
- `chargeback_count`: the number of chargebacks in that chargeback month and country; and
- `chargeback_amount`: the sum of the referenced transaction amounts for those chargebacks.

Use `Transactions.trans_date` for approved metrics and `Chargebacks.trans_date` for chargeback metrics.
