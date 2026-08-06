## Description

The `TVProgram` table records when a content item was streamed and on which channel. The `Content` table stores that item's title, whether it is intended for children, and its content category.

Report the distinct titles whose content is marked kid-friendly (`Kids_content = 'Y'`), whose category is exactly `Movies` (`content_type = 'Movies'`), and which appeared in at least one television program during June 2020. A qualifying title must satisfy all three conditions through a matching `content_id`. Return the result rows in any order.
