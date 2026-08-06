## Description

Design a `TodoList` that lets multiple users add tasks, retrieve their unfinished work, filter unfinished tasks by tag, and mark owned tasks as complete. Every added task has a description, a globally unique due date, and zero or more tags.

Task IDs start at `1` and increase globally by one for each successful addition, regardless of user. Retrieval operations return task descriptions ordered by increasing due date and never include completed tasks. Completing a task changes state only when the requested task exists, belongs to the supplied user, and is still unfinished; every other completion request does nothing.
