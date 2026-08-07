## Function Contract

**Inputs**

- `cost1`: The price of one type-1-only item.
- `cost2`: The price of one type-2-only item.
- `costBoth`: The price of one item contributing to both requirements.
- `need1`: The minimum required contribution toward type 1.
- `need2`: The minimum required contribution toward type 2.

Contributions may exceed either requirement; exact equality is not required. Any nonnegative number of each item type may be purchased.

**Return value**

Return the least total purchase cost whose contributions meet or exceed both required amounts.
