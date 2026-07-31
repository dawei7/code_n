## Constraints

- $1 \le \texttt{orderId} \le 2000$
- Every `orderId` is unique across all orders.
- `orderType` is either `"buy"` or `"sell"`.
- $1 \le \texttt{price} \le 10^9$
- The combined number of calls to `addOrder`, `modifyOrder`, `cancelOrder`, and `getOrdersAtPrice` is at most $2000$.
- Each `orderId` passed to `modifyOrder` or `cancelOrder` is guaranteed to identify an existing active order.
