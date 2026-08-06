## Function Contract

**Inputs**

- `Countries`: the country lookup table described above.
- `Weather`: the dated weather-observation table described above.

Let $C$ be the number of rows in `Countries`, $W$ the number of rows in `Weather`, and $K$ the number of countries having at least one observation from `2019-11-01` through `2019-11-30`, inclusive.

**Return value**

Return a table with these columns:

- `country_name`: the name belonging to a qualifying country identifier.
- `weather_type`: exactly `Cold`, `Warm`, or `Hot`, according to that country's November 2019 average.

Return exactly one row for each of the $K$ qualifying countries. A country without a November 2019 observation contributes no row. Result order is unrestricted.
