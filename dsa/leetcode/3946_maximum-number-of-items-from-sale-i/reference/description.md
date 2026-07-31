## Description

An item catalog is given as `items`, where row `items[i] = [factor_i, price_i]` describes the factor and purchase price of indexed type $i$. Any nonnegative number of copies of every type may be bought, provided the combined purchase cost does not exceed `budget`.

Buying at least one copy of type $i$ activates that type exactly once. Its activation awards one free copy of every indexed type $j$ satisfying both $j\ne i$ and `factor_j % factor_i == 0`. Buying more copies of the already activated type still adds those purchased copies to the total, but it does not repeat type $i$'s free-copy reward.

Different activated types award their rewards independently. Consequently, the same indexed target type may be received free more than once when several purchased types have factors that divide its factor.

Return the greatest total number of copies obtainable, counting every purchased and free copy, while the amount spent on purchases remains at most `budget`.
