## Function Contract

**Database Schemas**

**`Person`**

| Column | Type | Meaning |
|---|---|---|
| `id` | int | Unique person identifier. |
| `name` | varchar | Person's name. |
| `phone_number` | varchar | Ten-character number `xxx-yyyyyyy`; the prefix is a country code and digits may have leading zeroes. |

**`Country`**

| Column | Type | Meaning |
|---|---|---|
| `name` | varchar | Country name. |
| `country_code` | varchar | Unique three-digit code, including any leading zeroes. |

**`Calls`**

| Column | Type | Meaning |
|---|---|---|
| `caller_id` | int | Person who placed the call. |
| `callee_id` | int | Different person who received it. |
| `duration` | int | Call duration in minutes. |

- The `Calls` table has no uniqueness guarantee, so equal call rows count independently.

**Return value**

Return one column named `country`. Include exactly the country names whose average over all incident call endpoints is strictly greater than `AVG(Calls.duration)`. Countries with no call endpoint are absent. Row order is unrestricted.
