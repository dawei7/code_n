## Description

Each row `items[i] = [price_i, weight_i]` describes an item with a total price and weight. An item may be divided in any proportions whose fractions sum to 1; each resulting portion keeps the same fraction of both the original weight and the original price.

Given a positive bag `capacity`, choose whole items or fractional portions whose weights total exactly that capacity. Return the maximum total price obtainable. If all available weight is insufficient to fill the bag exactly, return `-1`. A floating-point result within $10^{-5}$ of the optimum is accepted.
