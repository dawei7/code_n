## Function Contract

**Database Schemas**

**`TVProgram`**

| Column | Type | Meaning |
|---|---|---|
| `program_date` | date/datetime | Date and optional time when the program was streamed. |
| `content_id` | int | Identifier of the streamed content item. |
| `channel` | varchar | Channel carrying the program. |

- The composite key is (`program_date`, `content_id`).

**`Content`**

| Column | Type | Meaning |
|---|---|---|
| `content_id` | varchar | Primary identifier joined to `TVProgram.content_id`. |
| `title` | varchar | Display title of the content. |
| `Kids_content` | enum | `Y` for kid-friendly content and `N` otherwise. |
| `content_type` | varchar | Category such as `Movies` or `Series`. |

**Return value**

Return one column named `title`, containing each distinct title of a `Kids_content = 'Y'`, `content_type = 'Movies'` item with at least one matching stream timestamp from June 1, 2020 inclusive through July 1, 2020 exclusive. Output order is unrestricted.
