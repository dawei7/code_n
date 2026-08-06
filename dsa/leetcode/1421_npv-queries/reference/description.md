## Description

`NPV` stores net present values for some inventory-and-year pairs, while `Queries` lists the pairs whose values must be reported. A requested pair may have no stored row. In that case, its reported net present value is `0`; the missing lookup must not cause the query row itself to disappear.

For every row in `Queries`, return its `id`, `year`, and matching `npv`, using `0` when that exact composite key is absent from `NPV`. Result rows may appear in any order.
