## Description

The `CoffeeShop` table records drink orders with a unique integer `id` and a nullable text column `drink`. Its rows have a presented input order that is independent of the numeric identifier. The first row is guaranteed to name a drink, but later rows may contain `NULL`.

Return every input row in exactly that same order. Keep each non-null drink unchanged, and replace each null drink with the closest non-null drink appearing earlier in the presented sequence. A run of several null rows therefore carries forward the same most recent drink until another named drink appears.
