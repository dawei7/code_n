## Description

An item catalog is represented by `items`, where `items[i] = [factor_i, price_i]` gives the factor and purchase price of indexed type $i$. Every type has unlimited stock. You may purchase any nonnegative number of copies as long as their combined cost does not exceed `budget`.

Purchased copies can also produce free copies. Each purchased copy of source type $i$ may award at most one copy of a different indexed target type $j$. Such a match is allowed only when $i\ne j$ and `factor_j % factor_i == 0`.

Every ordered source-target pair `(i, j)` may be used at most once, even if many copies of source type $i$ are purchased. Thus one source type can award at most one free copy of each eligible target, and additional purchases of that source stop producing rewards after all its eligible targets have been matched. Different source types remain independent: several sources may each award a free copy of the same target type.

Return the largest total number of copies obtainable, counting both purchased and free copies, while spending at most `budget` on purchases.
