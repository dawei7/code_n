## General

**Separate the two roles with aliases.** Read `Elements` twice: alias one occurrence as `metal` and the other as `nonmetal`. Restrict the first alias to rows whose `type` is `Metal`, and the second to rows whose `type` is `Nonmetal`.

**Generate every compatible combination.** Cross join the filtered roles. Each resulting row selects exactly one metal and one nonmetal, so it represents a valid bond. Conversely, any valid bond consists of one row from each filtered category and therefore appears once in this Cartesian product.

Project `metal.symbol` as `metal` and `nonmetal.symbol` as `nonmetal`. The `electrons` values explain the categories but do not impose an equality or balancing condition in the requested pairing rule.

## Complexity detail

Let $r$ be the number of input rows and $b$ the number of returned pairs. Classifying the input rows and producing the Cartesian result takes $O(r+b)$ time. The result itself contains $b$ rows and occupies $O(b)$ space; an engine may stream those rows, but the output still has that size.

## Alternatives and edge cases

- **Inner self join with category predicates:** Writing the same aliases with `JOIN ... ON` is equivalent, although `CROSS JOIN` states the all-combinations requirement directly.
- **Match equal electron counts:** This wrongly removes valid pairs because the contract depends only on the two categories.
- **Include Noble elements:** Noble rows belong to neither role and must never appear in the result.
- **Missing category:** If there are no metals or no nonmetals, one side of the Cartesian product is empty and the result has no rows.
- **Several elements per category:** Every metal pairs with every nonmetal; choosing only one counterpart per element is incomplete.
- **Output order:** The contract permits any order, so no `ORDER BY` clause is required.
