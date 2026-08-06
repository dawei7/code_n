## Description

The `Person` table stores one row per person, identified by the primary key `person_id`. Each row also contains the person's `name` and a `profession` chosen from `Doctor`, `Singer`, `Actor`, `Player`, `Engineer`, or `Lawyer`.

Report every person's identifier together with a formatted name. The formatted value must place the first letter of the profession inside parentheses immediately after the complete name, with no whitespace inserted between them. For example, a singer named `Alex` becomes `Alex(S)`.

Return the rows ordered by `person_id` in descending order. Name the formatted output column `name`.
