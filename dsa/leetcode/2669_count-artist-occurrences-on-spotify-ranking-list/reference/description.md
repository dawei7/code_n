## Description

The `Spotify` table contains ranked tracks. Every row has a unique `id`, a `track_name`, and the `artist` credited for that occurrence. The same artist may appear on multiple rows, whether for different tracks or repeated ranked entries.

Count how many table rows belong to each artist. Return the artist name beside that count under the column name `occurrences`. Order artists by decreasing occurrence count; when two artists have equal counts, order their names in ascending lexicographic order. Every artist present in the table must appear exactly once.
