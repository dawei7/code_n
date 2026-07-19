# Patients With a Condition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1527 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/patients-with-a-condition/) |

## Problem Description
### Goal

The `Patients` table records each hospital patient's identifier, name, and a string containing zero or more condition codes. Multiple codes in `conditions` are separated by single spaces, so a code begins either at the start of the string or immediately after a space.

Select the `patient_id`, `patient_name`, and `conditions` of every patient with Type I Diabetes. A Type I Diabetes code is any complete condition token whose text starts with the prefix `DIAB1`; characters may follow that prefix within the same token. Return the qualifying rows in any order.

### Function Contract
**Inputs**

Let $n$ be the number of rows in `Patients`, and define

$$
S = \sum_{p \in \texttt{Patients}} \lvert p.\texttt{conditions} \rvert.
$$

- `Patients.patient_id`: An integer primary key.
- `Patients.patient_name`: The patient's name.
- `Patients.conditions`: A possibly empty string of space-separated condition codes.

**Return value**

Return `patient_id`, `patient_name`, and `conditions` for exactly those rows containing a condition token that starts with `DIAB1`. The app-local query orders rows by `patient_id` for deterministic judging.

### Examples
**Example 1**

- Input conditions: `YFEV COUGH`, an empty string, `DIAB100 MYOP`, `ACNE DIAB100`, and `DIAB201`.
- Output: the rows containing `DIAB100 MYOP` and `ACNE DIAB100`.
- Explanation: In both rows, `DIAB100` is a complete token that begins with `DIAB1`.

**Example 2**

- Input conditions: `DIAB1A`, `DIAB2`, and `XDIAB100`.
- Output: only the row containing `DIAB1A`.
- Explanation: A suffix after `DIAB1` is allowed, but the prefix must begin the condition token.

**Example 3**

- Input conditions: `ACNE DIAB199 FLU` and `ACNE XDIAB199`.
- Output: only the first row.
- Explanation: A valid code may occur after another space-separated condition.
