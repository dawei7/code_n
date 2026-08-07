## Function Contract

**Input**

- `Ads`: the advertisement-action table described above.

Let $r$ be the number of action rows and $a$ the number of distinct advertisement identifiers.

**Return value**

Return one row for each distinct `ad_id`, with these columns:

- `ad_id`: the advertisement identifier.
- `ctr`: its percentage click-through rate, rounded to two decimal places.

An advertisement represented only by `Ignored` rows still appears, with `ctr` equal to `0`. Sort by `ctr` descending and then by `ad_id` ascending when rates tie.
