## Function Contract

**Input**

- `Salaries(company_id, employee_id, employee_name, salary)`: one uniquely
  identified row for each employee within a company.

Let $E$ be the number of employee rows and $C$ the number of distinct
companies.

**Return value**

Return one row per input employee with columns `company_id`, `employee_id`,
`employee_name`, and `salary`. Determine the tax bracket from the maximum salary
within the employee's company, apply that company-wide percentage to the
employee's original salary, and round the final after-tax amount to the nearest
integer. Row order is unrestricted.
