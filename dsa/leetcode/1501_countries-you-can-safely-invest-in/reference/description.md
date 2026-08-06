## Description

The `Person` table identifies people and stores each telephone number in the form `xxx-yyyyyyy`, where the first three digits are a country code. The `Country` table translates those three-character codes into country names. The `Calls` table records a caller, a different callee, and the call duration in minutes; duplicate call rows are permitted.

For each country represented by a participant in at least one call, consider every call endpoint belonging to that country. A domestic call therefore contributes its duration twice to that country's calculation, once for each participant, while an international call contributes once to each participant's country. Return the countries whose endpoint-weighted average duration is strictly greater than the global average duration across call rows. Name the only output column `country`; result rows may appear in any order.
