## Description

The `Boxes` table records the apples and oranges stored directly in every box. A box may also contain a chest, identified by `chest_id`; the `Chests` table records the fruit inside each chest type. A `NULL` chest identifier means that box contains no chest.

Find the total numbers of apples and oranges across all boxes, including the contents of a referenced chest each time that chest appears in a box. Chests not referenced by any box contribute nothing.
