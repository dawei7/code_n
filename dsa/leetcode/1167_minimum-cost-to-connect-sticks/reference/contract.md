## Function Contract

**Inputs**

- `sticks`: An array of $n$ positive integer stick lengths.

Each connection removes two current lengths, adds their sum to the cost, and inserts that sum as the replacement stick. The operation is repeated until the collection contains one stick.

**Return value**

- The minimum possible integer sum of all connection costs. A one-stick input requires no connection and therefore returns `0`.
