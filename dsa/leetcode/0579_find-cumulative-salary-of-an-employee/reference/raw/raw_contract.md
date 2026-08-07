## Function Contract

**Input**

`Employee(id, month, salary)` contains the monthly salary records. Let $R$ be the total number of rows.

**Return value**

Return `Id`, `Month`, and `Salary`, where `Salary` is the sum of the current recorded month and the two immediately preceding calendar months for that employee. Exclude each employee's greatest recorded month, then order by `Id` ascending and `Month` descending.
