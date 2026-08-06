## Function Contract

**Input**

`Employee(id, company, salary)` contains one row per employee. Let $E$ be the total number of rows in `Employee`.

**Return value**

Return a table with columns `id`, `company`, and `salary`. For each company, include the single central row when its employee count is odd and the two central rows when its employee count is even, using ascending `(salary, id)` order to determine position.
