## Description

There are `n` types of units indexed from `0` to `n - 1`. You are given a 2D integer array `conversions` of length `n - 1`, where `conversions[i] = [sourceUnit_i, targetUnit_i, conversionFactor_i]`. This indicates that a single unit of type `sourceUnit_i` is equivalent to `conversionFactor_i` units of type `targetUnit_i`.

Return an array `baseUnitConversion` of length `n`, where `baseUnitConversion[i]` is the number of units of type `i` equivalent to a single unit of type 0. Since the answer may be large, return each `baseUnitConversion[i]` **modulo** `10^9 + 7`.
