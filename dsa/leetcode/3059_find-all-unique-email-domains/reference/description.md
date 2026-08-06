## Description

Each row contains one lowercase email address. Its domain is the portion after
the `@` separator, and several individuals may share the same domain.

Find every distinct domain whose name ends with the exact suffix `.com`, and
count how many email rows belong to it. Domains with another ending, even if
they contain `com` elsewhere, are excluded. Return one row per qualifying
domain, ordered by the domain text ascending.
