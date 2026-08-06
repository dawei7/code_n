## Description

The `Contacts` table identifies people by `id` and stores each person's first and last names. The `Calls` table records a contact, whether the call was `incoming` or `outgoing`, and its duration in seconds. Each call belongs to the contact whose `Contacts.id` equals its `contact_id`.

Find the three longest calls in each direction. Report the contact's `first_name`, the call `type`, and the duration converted from seconds to the fixed `HH:MM:SS` form. The final result must be sorted by `type`, raw `duration`, and `first_name`, with all three keys in descending order.
