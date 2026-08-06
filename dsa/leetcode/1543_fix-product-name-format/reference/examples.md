## Examples

**Example 1**

- **Input:** Six sales spelling `LCPhone` and `LCKeyChain` with different letter cases, plus one `Matryoshka` sale.
- **Output:**
  | product_name | sale_date | total |
  | --- | --- | --- |
  | lckeychain | 2000-02 | 2 |
  | lcphone | 2000-01 | 2 |
  | lcphone | 2000-02 | 1 |
  | matryoshka | 2000-03 | 1 |
- **Explanation:** Case variants share a normalized name, while January and February remain separate groups.

**Example 2**

- **Input:** `("  Widget  ", "2000-05-04")` and `("widget", "2000-05-20")`
- **Output:**
  | product_name | sale_date | total |
  | --- | --- | --- |
  | widget | 2000-05 | 2 |
- **Explanation:** Trimming and lowercasing make both rows part of one group.

**Example 3**

- **Input:** One sale each for `"Beta"` in January and `"alpha"` in December.
- **Output:**
  | product_name | sale_date | total |
  | --- | --- | --- |
  | alpha | 2000-12 | 1 |
  | beta | 2000-01 | 1 |
- **Explanation:** Product-name ordering takes precedence over chronological ordering between products.
