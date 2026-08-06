## Description

The `Tasks` table stores submitted work. Each row identifies a task with its
unique `task_id`, records the responsible `assignee_id`, and gives the calendar
date on which it was submitted.

Classify every task by its submission day. Saturday and Sunday are weekend
days; Monday through Friday are working days. Return one row containing the
number of weekend submissions as `weekend_cnt` and the number of working-day
submissions as `working_cnt`. The assignee does not affect either count.
