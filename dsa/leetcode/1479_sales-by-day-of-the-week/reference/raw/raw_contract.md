## Function Contract

**Inputs**

- `Orders(order_id, customer_id, order_date, item_id, quantity)`: dated item
  order quantities;
- `Items(item_id, item_name, item_category)`: item identities and categories.

Let $I$ be the number of item rows, $O$ the number of order rows, and $C$ the
number of distinct categories.

**Return value**

Return columns `Category`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`,
`Friday`, `Saturday`, and `Sunday`. Each weekday value is the total `quantity`
ordered for every item in that category on that weekday, using zero when no
matching units were ordered. Sort the rows by `Category` ascending.
