## Description

The `Terms` table stores the nonzero terms of a one-variable polynomial. Each
row gives a unique integer `power` from $0$ through $100$ and a nonzero integer
`factor`.

Build one equation string whose left-hand side contains every table row in
descending power order and whose right-hand side is zero. Every term begins
with `+` or `-`, followed by the factor's absolute value. A power greater than
one appends `X^power`; power one appends only `X`; and power zero appends no
variable text. Finish the complete left-hand side with `=0`.
