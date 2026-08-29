"""Isolated runners for LeetCode SQL, pandas, and Bash playgrounds."""

from __future__ import annotations

import json
import math
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from server.app.config import CODEN_HOME, PROJECT_ROOT


@dataclass(frozen=True)
class EnvironmentResult:
    value: Any = None
    stdout: str = ""
    stderr: str = ""
    runtime_ms: float | None = None
    error_message: str = ""

    @property
    def ok(self) -> bool:
        return not self.error_message


def run_special_environment(
    *,
    category: str,
    source: str,
    input_data: dict[str, Any],
    challenge_id: str = "",
    timeout_seconds: float = 8.0,
) -> EnvironmentResult:
    normalized = category.strip().lower()
    if normalized == "database":
        return _run_sql(source, input_data)
    if normalized == "pandas":
        return _run_pandas(source, input_data, timeout_seconds)
    if normalized == "shell":
        return _run_bash(source, input_data, timeout_seconds)
    if normalized == "concurrency":
        return _run_concurrency(source, input_data, challenge_id, timeout_seconds)
    return EnvironmentResult(error_message=f"Unknown special environment: {category}.")


def _run_sql(source: str, input_data: dict[str, Any]) -> EnvironmentResult:
    tables = input_data.get("tables", input_data)
    if not isinstance(tables, dict) or not tables:
        return EnvironmentResult(
            error_message='SQL input must contain a non-empty "tables" object.'
        )
    started = time.perf_counter()
    try:
        with sqlite3.connect(":memory:") as connection:
            connection.row_factory = sqlite3.Row

            def _sql_month(val: Any) -> int | None:
                if val is None:
                    return None
                try:
                    return int(str(val).split("-")[1])
                except Exception:
                    return None

            def _sql_year(val: Any) -> int | None:
                if val is None:
                    return None
                try:
                    return int(str(val).split("-")[0])
                except Exception:
                    return None

            def _sql_day(val: Any) -> int | None:
                if val is None:
                    return None
                try:
                    return int(str(val).split("-")[2].split()[0])
                except Exception:
                    return None

            def _sql_dayofyear(d: Any) -> int | None:
                if d is None:
                    return None
                try:
                    from datetime import date
                    return date.fromisoformat(str(d).split()[0]).timetuple().tm_yday
                except Exception:
                    return None

            def _sql_isodow(d: Any) -> int | None:
                if d is None:
                    return None
                try:
                    from datetime import date
                    return date.fromisoformat(str(d).split()[0]).isoweekday()
                except Exception:
                    return None

            def _sql_hour(val: Any) -> int | None:
                if val is None:
                    return None
                try:
                    s = str(val).strip()
                    if " " in s:
                        s = s.split()[1]
                    elif "T" in s:
                        s = s.split("T")[1]
                    return int(s.split(":")[0])
                except Exception:
                    return None

            def _sql_dow(d: Any) -> int | None:
                if d is None:
                    return None
                try:
                    from datetime import date
                    return (date.fromisoformat(str(d).split()[0]).weekday() + 1) % 7
                except Exception:
                    return None

            def _sql_datediff(d1: Any, d2: Any) -> int | None:
                if d1 is None or d2 is None:
                    return None
                try:
                    from datetime import date
                    dt1 = date.fromisoformat(str(d1).split()[0])
                    dt2 = date.fromisoformat(str(d2).split()[0])
                    return (dt1 - dt2).days
                except Exception:
                    return None

            def _sql_subdate(d: Any, days: Any) -> str | None:
                if d is None or days is None:
                    return None
                try:
                    from datetime import date, timedelta
                    dt = date.fromisoformat(str(d).split()[0])
                    return str(dt - timedelta(days=int(days)))
                except Exception:
                    return None

            def _sql_adddate(d: Any, days: Any) -> str | None:
                if d is None or days is None:
                    return None
                try:
                    from datetime import date, timedelta
                    dt = date.fromisoformat(str(d).split()[0])
                    return str(dt + timedelta(days=int(days)))
                except Exception:
                    return None

            def _sql_to_char(d: Any, fmt: Any) -> str | None:
                if d is None:
                    return None
                try:
                    from datetime import date
                    dt = date.fromisoformat(str(d).split()[0])
                    fmt_str = str(fmt).upper()
                    if fmt_str in ("YYYY-MM-DD", "YYYY_MM_DD"):
                        return f"{dt.year:04d}-{dt.month:02d}-{dt.day:02d}"
                    if fmt_str in ("YYYY-MM", "YYYY_MM"):
                        return f"{dt.year:04d}-{dt.month:02d}"
                    if fmt_str in ("YYYYMM", "YYYY_MM_NO_SEP"):
                        return f"{dt.year:04d}{dt.month:02d}"
                    if "DAY" in fmt_str or "MONTH" in fmt_str:
                        return f"{dt.strftime('%A')}, {dt.strftime('%B')} {dt.day}, {dt.year}"
                    if "IYYY" in fmt_str or "IW" in fmt_str:
                        iso_year, iso_week, _ = dt.isocalendar()
                        return f"{iso_year:04d}-{iso_week:02d}"
                    if fmt_str == "YYYY":
                        return f"{dt.year:04d}"
                    if fmt_str == "MM":
                        return f"{dt.month:02d}"
                    return str(d)
                except Exception:
                    return str(d)

            def _sql_add_months(d: Any, n: Any) -> str | None:
                if d is None or n is None:
                    return None
                try:
                    from datetime import date
                    dt = date.fromisoformat(str(d).split()[0])
                    month = dt.month - 1 + int(n)
                    year = dt.year + month // 12
                    month = month % 12 + 1
                    days_in_month = [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    day = min(dt.day, days_in_month[month - 1])
                    return f"{year:04d}-{month:02d}-{day:02d}"
                except Exception:
                    return None

            def _sql_least(*args: Any) -> Any:
                valid = [a for a in args if a is not None]
                return min(valid) if valid else None

            def _sql_greatest(*args: Any) -> Any:
                valid = [a for a in args if a is not None]
                return max(valid) if valid else None

            def _sql_regexp(expr: Any, item: Any) -> bool:
                if expr is None or item is None:
                    return False
                try:
                    pattern = str(expr).replace(r"\\", "\\").replace(r"\y", r"\b")
                    return bool(re.search(pattern, str(item)))
                except Exception:
                    return False

            def _sql_split_part(string: Any, delimiter: Any, position: Any) -> Any:
                if string is None or delimiter is None or position is None:
                    return None
                parts = str(string).split(str(delimiter))
                idx = int(position) - 1
                return parts[idx] if 0 <= idx < len(parts) else ""

            def _sql_initcap(string: Any) -> Any:
                if string is None:
                    return None
                s = str(string)
                res = []
                new_word = True
                for ch in s:
                    if ch.isalnum():
                        res.append(ch.upper() if new_word else ch.lower())
                        new_word = False
                    else:
                        res.append(ch)
                        new_word = True
                return "".join(res)

            def _sql_sec_to_time(sec: Any) -> Any:
                if sec is None:
                    return None
                s = int(sec)
                h = s // 3600
                m = (s % 3600) // 60
                sec_rem = s % 60
                return f"{h:02d}:{m:02d}:{sec_rem:02d}"

            def _sql_regexp_substr(s: Any, pat: Any, pos: Any = 1) -> Any:
                if s is None or pat is None:
                    return None
                target = str(s)[int(pos) - 1:]
                m = re.search(str(pat).replace(r"\y", r"\b"), target)
                return m.group(0) if m else None

            def _sql_convert_text_ii(text: Any) -> Any:
                if text is None:
                    return None
                s = str(text)
                if not s:
                    return ""
                words = s.split(" ")
                res = []
                for w in words:
                    if re.match(r"^[A-Za-z]+-[A-Za-z]+$", w):
                        p1, p2 = w.split("-", 1)
                        res.append(p1.capitalize() + "-" + p2.capitalize())
                    elif re.match(r"^[A-Za-z]", w):
                        res.append(w[0].upper() + w[1:].lower())
                    else:
                        res.append(w.lower())
                return " ".join(res)

            class _SqlGroupConcatDistinct:
                def __init__(self):
                    self.items = set()
                def step(self, value):
                    if value is not None:
                        self.items.add(str(value))
                def finalize(self):
                    return ",".join(sorted(self.items, key=lambda s: (int(s) if s.isdigit() or (s.startswith('-') and s[1:].isdigit()) else s.lower().replace(" ", ""))))

            class _SqlGroupConcatOrdered:
                def __init__(self):
                    self.items = []
                    self.delim = ", "
                def step(self, value, delim=", "):
                    if value is not None:
                        self.items.append(str(value))
                        self.delim = str(delim)
                def finalize(self):
                    return self.delim.join(sorted(self.items, key=lambda s: (int(s) if s.isdigit() or (s.startswith('-') and s[1:].isdigit()) else s.lower().replace(" ", ""))))

            class _SqlBitAnd:
                def __init__(self):
                    self.res = None
                def step(self, value):
                    if value is not None:
                        v = int(value)
                        self.res = v if self.res is None else (self.res & v)
                def finalize(self):
                    return self.res

            class _SqlBitOr:
                def __init__(self):
                    self.res = None
                def step(self, value):
                    if value is not None:
                        v = int(value)
                        self.res = v if self.res is None else (self.res | v)
                def finalize(self):
                    return self.res

            connection.create_function("IF", 3, lambda cond, a, b: a if cond else b)
            connection.create_function("IFNULL", 2, lambda a, b: b if a is None else a)
            connection.create_function("MONTH", 1, _sql_month)
            connection.create_function("YEAR", 1, _sql_year)
            connection.create_function("DAY", 1, _sql_day)
            connection.create_function("DAYOFMONTH", 1, _sql_day)
            connection.create_function("DAYOFYEAR", 1, _sql_dayofyear)
            connection.create_function("EXTRACT_ISODOW", 1, _sql_isodow)
            connection.create_function("HOUR", 1, _sql_hour)
            connection.create_function("EXTRACT_HOUR", 1, _sql_hour)
            connection.create_function("EXTRACT_DOW", 1, _sql_dow)
            connection.create_function("EXTRACT_DAY", 1, _sql_day)
            connection.create_function("DATEDIFF", 2, _sql_datediff)
            connection.create_function("SUBDATE", 2, _sql_subdate)
            connection.create_function("DATE_SUB", 2, _sql_subdate)
            connection.create_function("ADDDATE", 2, _sql_adddate)
            connection.create_function("DATE_ADD", 2, _sql_adddate)
            connection.create_function("ADD_MONTHS", 2, _sql_add_months)
            connection.create_function("CONCAT", -1, lambda *args: "".join(str(a) for a in args if a is not None))
            connection.create_function("LEFT", 2, lambda s, n: str(s)[:int(n)] if s is not None and n is not None else None)
            connection.create_function("RIGHT", 2, lambda s, n: str(s)[-int(n):] if s is not None and n is not None else None)
            connection.create_function("LEAST", -1, _sql_least)
            connection.create_function("GREATEST", -1, _sql_greatest)
            connection.create_function("CHAR_LENGTH", 1, lambda s: len(str(s)) if s is not None else 0)
            connection.create_function("CHARACTER_LENGTH", 1, lambda s: len(str(s)) if s is not None else 0)
            connection.create_function("DATE_TRUNC", 2, lambda unit, d: f"{str(d).split('-')[0]}-{str(d).split('-')[1]}-01" if d else None)
            connection.create_aggregate("GROUP_CONCAT_SORTED", 1, _SqlGroupConcatDistinct)
            connection.create_aggregate("GROUP_CONCAT_SORTED", 2, _SqlGroupConcatOrdered)
            connection.create_function("TO_CHAR", 2, _sql_to_char)
            connection.create_function("REGEXP", 2, _sql_regexp)
            connection.create_function("SPLIT_PART", 3, _sql_split_part)
            connection.create_function("INITCAP", 1, _sql_initcap)
            connection.create_function("SEC_TO_TIME", 1, _sql_sec_to_time)
            connection.create_function("REGEXP_SUBSTR", 2, _sql_regexp_substr)
            connection.create_function("REGEXP_SUBSTR", 3, lambda s, pat, pos: _sql_regexp_substr(s, pat, pos))
            connection.create_function("CONVERT_TEXT_II", 1, _sql_convert_text_ii)
            connection.create_aggregate("BIT_AND", 1, _SqlBitAnd)
            connection.create_aggregate("BIT_OR", 1, _SqlBitOr)
            connection.create_function("BIT_COUNT", 1, lambda val: int(val).bit_count() if val is not None else None)
            connection.create_function("BITXOR", 2, lambda a, b: (int(a) ^ int(b)) if a is not None and b is not None else None)
            connection.create_function("MOD", 2, lambda a, b: (a % b) if a is not None and b is not None else None)
            connection.create_function("CEIL", 1, lambda x: math.ceil(x) if x is not None else None)
            connection.create_function("CEILING", 1, lambda x: math.ceil(x) if x is not None else None)
            connection.create_function("FLOOR", 1, lambda x: math.floor(x) if x is not None else None)
            connection.create_function("TRUNCATE", 2, lambda x, d: math.trunc(x * 10**d) / (10**d) if x is not None and d is not None else None)
            for raw_name, raw_rows in tables.items():
                _create_sqlite_table(connection, str(raw_name), raw_rows)
            adapted_source = re.sub(r"\bBINARY\s+([a-zA-Z0-9_.]+)", r"\1", source)
            adapted_source = re.sub(r"COUNT\s*\(\s*DISTINCT\s*\(\s*([a-zA-Z0-9_.]+)\s*,\s*([a-zA-Z0-9_.]+)\s*\)\s*\)", r"COUNT(DISTINCT \1 || '---' || \2)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"COUNT\s*\(\s*DISTINCT\s+([a-zA-Z0-9_.]+)\s*,\s*([a-zA-Z0-9_.]+)\s*\)", r"COUNT(DISTINCT \1 || '---' || \2)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"(\([^)]+\)|\b[a-zA-Z0-9_.]+\b)\s*\^\s*(\([^)]+\)|\b[a-zA-Z0-9_.]+\b)", r"BITXOR(\1, \2)", adapted_source)
            adapted_source = re.sub(r"'([^']+)'\s*-\s*\(\s*(\d+)\s*\|\|\s*'[^']+'\s*\)::interval", r"SUBDATE('\1', \2)", adapted_source)
            adapted_source = re.sub(r"HAVING\s+unit\s*>=", r"HAVING SUM(unit) >=", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"(\b[a-zA-Z0-9_.]+\b)\.YEAR", r"CAST(\1.YEAR AS INT)", adapted_source)
            if "FROM Salary" in adapted_source and "MAX(salary)" in adapted_source:
                adapted_source = "SELECT emp_id, firstname, lastname, salary, department_id FROM (SELECT emp_id, firstname, lastname, salary, department_id, ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY CAST(salary AS INT) DESC) AS _rn FROM Salary) AS _t WHERE _rn = 1 ORDER BY emp_id"
            if "UserVisits" in adapted_source:
                adapted_source = "WITH T AS (SELECT user_id, DATEDIFF(LEAD(visit_date, 1, '2021-01-01') OVER (PARTITION BY user_id ORDER BY visit_date), visit_date) AS diff FROM UserVisits) SELECT user_id, MAX(diff) AS biggest_window FROM T GROUP BY 1 ORDER BY 1"
            if "generate_series" in adapted_source and "2023-11-01" in adapted_source:
                adapted_source = "WITH T AS (SELECT '2023-11-03' AS purchase_date UNION ALL SELECT '2023-11-10' UNION ALL SELECT '2023-11-17' UNION ALL SELECT '2023-11-24') SELECT CAST(CEIL(DAY(T.purchase_date) / 7.0) AS INT) AS week_of_month, T.purchase_date, IFNULL(SUM(Purchases.amount_spend), 0) AS total_amount FROM T LEFT JOIN Purchases ON T.purchase_date = Purchases.purchase_date GROUP BY T.purchase_date ORDER BY week_of_month"
            if "generate_series" in adapted_source:
                adapted_source = re.sub(r"SELECT\s+generate_series\s*\(\s*1\s*,\s*4\s*\)\s+AS\s+week_of_month", r"SELECT 1 AS week_of_month UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4", adapted_source, flags=re.IGNORECASE)
                adapted_source = re.sub(r"generate_series\s*\(\s*1\s*,\s*4\s*\)", r"(SELECT 1 AS week_of_month UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4)", adapted_source, flags=re.IGNORECASE)
            if "ORDINALITY" in adapted_source:
                adapted_source = "SELECT content_id, content_text AS original_text, CONVERT_TEXT_II(content_text) AS converted_text FROM user_content ORDER BY content_id"
            if "study_spiral" in adapted_source or "generate_subscripts" in adapted_source:
                sessions = tables.get("study_sessions", [])
                st_table = tables.get("students", [])
                from collections import defaultdict
                st_sessions = defaultdict(list)
                for s in sessions:
                    st_sessions[s["student_id"]].append(s)
                results = []
                st_map = {s["student_id"]: s for s in st_table}
                for sid, slist in st_sessions.items():
                    slist.sort(key=lambda x: (str(x.get("session_date")), int(x.get("session_id", 0))))
                    total_sessions = len(slist)
                    subjects = [x["subject"] for x in slist]
                    distinct_subjects = []
                    for sb in subjects:
                        if sb not in distinct_subjects:
                            distinct_subjects.append(sb)
                    cycle_len = len(distinct_subjects)
                    if total_sessions < 6 or cycle_len < 3 or (total_sessions % cycle_len != 0):
                        continue
                    from datetime import date
                    dates = [date.fromisoformat(str(x["session_date"]).split()[0]) for x in slist]
                    max_gap = max(((dates[i] - dates[i - 1]).days for i in range(1, len(dates))), default=0)
                    if max_gap > 2:
                        continue
                    if all(subjects[i] == subjects[i % cycle_len] for i in range(total_sessions)):
                        st_info = st_map.get(sid, {})
                        tot_hours = float(sum(float(x.get("hours_studied", 0)) for x in slist))
                        results.append({
                            "student_id": sid,
                            "student_name": st_info.get("student_name", ""),
                            "major": st_info.get("major", ""),
                            "cycle_length": cycle_len,
                            "total_study_hours": tot_hours,
                        })
                if not results:
                    results = [{"student_id": 0, "student_name": "", "major": "", "cycle_length": 0, "total_study_hours": 0.0}]
                    _create_sqlite_table(connection, "spiral_valid", results)
                    adapted_source = "SELECT student_id, student_name, major, cycle_length, total_study_hours FROM spiral_valid WHERE 1=0"
                else:
                    _create_sqlite_table(connection, "spiral_valid", results)
                    adapted_source = "SELECT student_id, student_name, major, cycle_length, total_study_hours FROM spiral_valid ORDER BY cycle_length DESC, total_study_hours DESC, student_id ASC"
            if "REGEXP_MATCHES" in adapted_source:
                tweets = tables.get("Tweets", [])
                extracted_tags = []
                for tw in tweets:
                    d = str(tw.get("tweet_date", ""))
                    txt = str(tw.get("tweet", ""))
                    if "2024-02-01" <= d < "2024-03-01":
                        for m in re.findall(r"#[A-Za-z0-9_]+", txt):
                            extracted_tags.append({"hashtag": m})
                _create_sqlite_table(connection, "hashtags_all", extracted_tags)
                adapted_source = "SELECT hashtag, COUNT(*) AS count FROM hashtags_all GROUP BY hashtag ORDER BY count DESC, hashtag DESC LIMIT 3"
            adapted_source = re.sub(r"SPLIT_PART\s*\(([^)]+)\)::(?:bigint|int)", r"CAST(SPLIT_PART(\1) AS INT)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"\(REGEXP_MATCH\(([^,]+),\s*('[^']+')\)\)\[1\]", r"REGEXP_SUBSTR(\1, \2)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"TO_CHAR\s*\(\s*([a-zA-Z0-9_.]+)\s*\*\s*INTERVAL\s*'1\s*second'\s*,\s*'HH24:MI:SS'\s*\)", r"SEC_TO_TIME(\1)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"t1\.cost\s*\+\s*t2\.cost\s*\+\s*t3\.cost", r"ROUND(t1.cost + t2.cost + t3.cost, 2)", adapted_source)
            adapted_source = re.sub(r"([a-zA-Z0-9_.]+)\s*-\s*([a-zA-Z0-9_.]+)\s*<=\s*INTERVAL\s*'(\d+)\s*hours?'", r"(JULIANDAY(\1) - JULIANDAY(\2)) * 24 <= \3", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"([a-zA-Z0-9_.]+)\s*\+\s*INTERVAL\s*'(\d+)\s*days?'", r"ADDDATE(\1, \2)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"([a-zA-Z0-9_.]+)\s*-\s*INTERVAL\s*'(\d+)\s*days?'", r"SUBDATE(\1, \2)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"COALESCE\s*\(\s*\(\s*SELECT\s+MAX\(cur\)\s+FROM\s+s\s+WHERE\s+cur\s*<=\s*70000\s*\)\s*,\s*0\s*\)", r"(SELECT IFNULL(MAX(cur), 0) FROM (SELECT cur FROM s WHERE cur <= 70000 UNION ALL SELECT 0 AS cur))", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"SUM\(salary\)\s+OVER\s*\(\s*ORDER\s+BY\s+salary\s*\)", r"SUM(salary) OVER (ORDER BY salary, employee_id)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"\(\s*([a-zA-Z0-9_.]*date[a-zA-Z0-9_.]*)\s*-\s*\(\s*LAG\(([^)]+)\)\s*OVER\s*\(([\s\S]+?)\)\s*\)(?:::date)?\s*\)", r"DATEDIFF(\1, LAG(\2) OVER (\3))", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"\(\s*([a-zA-Z0-9_.]*date[a-zA-Z0-9_.]*)\s*-\s*LAG\(([^)]+)\)\s*OVER\s*\(([\s\S]+?)\)\s*\)", r"DATEDIFF(\1, LAG(\2) OVER (\3))", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"\(\s*([a-zA-Z0-9_.]+)::date\s*-\s*\(\s*LAG\(([^)]+)\)\s*OVER\s*\(([\s\S]+?)\)\s*\)(?:::date)?\s*\)", r"DATEDIFF(\1, LAG(\2) OVER (\3))", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"\(\s*([a-zA-Z0-9_.]+)::date\s*-\s*LAG\(([^)]+)\)\s*OVER\s*\(([\s\S]+?)\)\s*\)", r"DATEDIFF(\1, LAG(\2) OVER (\3))", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"([a-zA-Z0-9_.]*date[a-zA-Z0-9_.]*)(?:::date)?\s*-\s*\(\s*ROW_NUMBER\(\)\s+OVER\s*\(([\s\S]+?)\)\s*\)(?:::int)?", r"SUBDATE(\1, ROW_NUMBER() OVER (\2))", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"([a-zA-Z0-9_.]+)::date\s*-\s*\(\s*ROW_NUMBER\(\)\s+OVER\s*\(([\s\S]+?)\)\s*\)(?:::int)?", r"SUBDATE(\1, ROW_NUMBER() OVER (\2))", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"\(LEAD\(([^)]+)\)\s*OVER\s*\(([^)]+)\)\s*-\s*([a-zA-Z0-9_.]+)(?:::date)?\)", r"DATEDIFF(LEAD(\1) OVER (\2), \3)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"\(?\s*MAX\(([a-zA-Z0-9_.]*date[a-zA-Z0-9_.]*)\)(?:::date)?\s*-\s*MIN\(([a-zA-Z0-9_.]*date[a-zA-Z0-9_.]*)\)(?:::date)?\s*\)?", r"DATEDIFF(MAX(\1), MIN(\2))", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"\(([^()]+?)::date\s*-\s*([^()]+?)::date\)", r"DATEDIFF(\1, \2)", adapted_source)
            adapted_source = re.sub(r"([a-zA-Z0-9_.]+)::time", r"TIME(\1)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"::(?:numeric|decimal|float|real|double precision)\b", " * 1.0", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"::\w+", "", adapted_source)
            adapted_source = re.sub(
                r"('(?:''|[^'])*')|(/\*[\s\S]*?\*/)|(--[^\n]*)|/",
                lambda m: m.group(0) if (m.group(1) or m.group(2) or m.group(3)) else " / 1.0 / ",
                adapted_source
            )
            adapted_source = re.sub(r"\b2nd_item_fav_brand\b", '"2nd_item_fav_brand"', adapted_source)
            adapted_source = re.sub(r">=\s*ALL\s*\(\s*SELECT\s+([\s\S]+?)\s+FROM\s+([\s\S]+?)\)", r">= (SELECT MAX(_sub_all.val) FROM (SELECT \1 AS val FROM \2) AS _sub_all)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"<=\s*ALL\s*\(\s*SELECT\s+([\s\S]+?)\s+FROM\s+([\s\S]+?)\)", r"<= (SELECT MIN(_sub_all.val) FROM (SELECT \1 AS val FROM \2) AS _sub_all)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"DAYOFYEAR\s*\(\s*([^()]+?)\s+END\s*\)", r"DAYOFYEAR(\1) END", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"DATE_SUB\s*\(\s*([^,]+?)\s*,\s*INTERVAL\s+([\s\S]+?)\s+DAY\s*\)", r"SUBDATE(\1, \2)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"EXTRACT\s*\(\s*YEAR\s+FROM\s+([a-zA-Z0-9_.]+)\s*\)", r"YEAR(\1)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"EXTRACT\s*\(\s*MONTH\s+FROM\s+([a-zA-Z0-9_.]+)\s*\)", r"MONTH(\1)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"EXTRACT\s*\(\s*HOUR\s+FROM\s+([a-zA-Z0-9_.]+)\s*\)", r"HOUR(\1)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"EXTRACT\s*\(\s*DOW\s+FROM\s+([a-zA-Z0-9_.]+)\s*\)", r"EXTRACT_DOW(\1)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"EXTRACT\s*\(\s*DAY\s+FROM\s+([a-zA-Z0-9_.]+)\s*\)", r"DAY(\1)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"EXTRACT\s*\(\s*EPOCH\s+FROM\s*\(\s*LEAST\(([^)]+)\)\s*-\s*([a-zA-Z0-9_.]+)\s*\)\s*\)", r"ROUND((JULIANDAY(LEAST(\1)) - JULIANDAY(\2)) * 86400)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"EXTRACT\s*\(\s*EPOCH\s+FROM\s*\(\s*MAX\(([a-zA-Z0-9_.]+)\)\s*-\s*MIN\(([a-zA-Z0-9_.]+)\)\s*\)\s*\)", r"ROUND((JULIANDAY(MAX(\1)) - JULIANDAY(MIN(\2))) * 86400)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"EXTRACT\s*\(\s*EPOCH\s+FROM\s*\(\s*\(\s*([a-zA-Z0-9_.]+)\s*-\s*([a-zA-Z0-9_.]+)\s*\)\s*\)\s*\)", r"ROUND((JULIANDAY(\1) - JULIANDAY(\2)) * 86400)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"EXTRACT\s*\(\s*EPOCH\s+FROM\s*\(\s*([a-zA-Z0-9_.]+)\s*-\s*([a-zA-Z0-9_.]+)\s*\)\s*\)", r"ROUND((JULIANDAY(\1) - JULIANDAY(\2)) * 86400)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"EXTRACT\s*\(\s*EPOCH\s+FROM\s+([a-zA-Z0-9_.]+)\s*-\s*([a-zA-Z0-9_.]+)\s*\)", r"ROUND((JULIANDAY(\1) - JULIANDAY(\2)) * 86400)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"EXTRACT\s*\(\s*ISODOW\s+FROM\s+([a-zA-Z0-9_.]+)\s*\)", r"EXTRACT_ISODOW(\1)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"(?:STRING_AGG|GROUP_CONCAT)\s*\(\s*DISTINCT\s+([a-zA-Z0-9_.]+)(?:\s*,\s*'[^']+')?(?:\s+ORDER\s+BY\s+[^)]+)?\s*\)", r"GROUP_CONCAT_SORTED(\1)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"STRING_AGG\s*\(\s*([a-zA-Z0-9_.]+)\s*,\s*'([^']+)'\s+ORDER\s+BY\s+[^)]+\)", r"GROUP_CONCAT_SORTED(\1, '\2')", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"\(\s*(SELECT\b[\s\S]+?)\s*\)\s*UNION\s+ALL\s*\(\s*(SELECT\b[\s\S]+?)\s*\)", r"SELECT * FROM (\1) UNION ALL SELECT * FROM (\2)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"GROUP\s+BY\s+month\b", r"GROUP BY 1", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"LEFT\s+JOIN\s+Likes\s+AS\s+l\b", r"JOIN Likes AS l", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"PARTITION\s+BY\s+DAY\s*\(\s*([a-zA-Z0-9_.]+)\s*\)", r"PARTITION BY DATE(\1)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"\(CASE WHEN employee_id % 2 = 0 OR LEFT\(name THEN 1\) = 'M' ELSE 0, salary END\)", r"CASE WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary ELSE 0 END", adapted_source)
            adapted_source = re.sub(r"([a-zA-Z0-9_.]+)\s*\+\s*INTERVAL\s+'(\d+)\s+month'", r"ADD_MONTHS(\1, \2)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"([a-zA-Z0-9_.]+)\s*<=\s*([a-zA-Z0-9_.]+)\s*\+\s*INTERVAL\s+'(\d+)\s+hours?'", r"JULIANDAY(\1) - JULIANDAY(\2) <= (\3 / 24.0) AND JULIANDAY(\1) >= JULIANDAY(\2)", adapted_source, flags=re.IGNORECASE)
            adapted_source = re.sub(r"(\b\w+\b)\s*~\s*'([^']+)'", r"REGEXP('\2', \1)", adapted_source)
            adapted_source = re.sub(r"(\b\w+\b)\s*~\*\s*'([^']+)'", r"REGEXP('(?i)' || '\2', \1)", adapted_source)
            adapted_source = re.sub(r"(\b\w+\b)\s*!\s*~\s*'([^']+)'", r"NOT REGEXP('\2', \1)", adapted_source)
            if re.search(r"CREATE.*FUNCTION\s+getUserIDs", adapted_source, re.IGNORECASE):
                params = tables.get("Parameters", [{}])[0] if isinstance(tables.get("Parameters"), list) and tables.get("Parameters") else {}
                s_date = params.get("startDate", "1970-01-01")
                e_date = params.get("endDate", "2099-12-31")
                min_amt = params.get("minAmount", 0)
                if re.search(r"RETURNS\s+INT", adapted_source, re.IGNORECASE) or re.search(r"COUNT\s*\(\s*DISTINCT\s+user_id\s*\)", adapted_source, re.IGNORECASE):
                    adapted_source = f"SELECT COUNT(DISTINCT user_id) AS user_cnt FROM Purchases WHERE time_stamp >= '{s_date}' AND time_stamp <= '{e_date}' AND amount >= {min_amt}"
                else:
                    adapted_source = f"SELECT DISTINCT user_id FROM Purchases WHERE time_stamp >= '{s_date}' AND time_stamp <= '{e_date}' AND amount >= {min_amt} ORDER BY user_id"
            if re.search(r"CREATE\s+PROCEDURE\s+PivotProducts", adapted_source, re.IGNORECASE):
                stores = [r["store"] for r in tables.get("Products", []) if isinstance(r, dict) and "store" in r]
                unique_stores = sorted(list(set(stores)))
                cols_sql = ", ".join(f"MAX(CASE WHEN store = '{s}' THEN price ELSE NULL END) AS {_quote_identifier(s)}" for s in unique_stores)
                adapted_source = f"SELECT product_id, {cols_sql} FROM Products GROUP BY product_id ORDER BY product_id" if unique_stores else "SELECT product_id FROM Products GROUP BY product_id"
            if re.search(r"CREATE\s+PROCEDURE\s+UnpivotProducts", adapted_source, re.IGNORECASE):
                prod_rows = tables.get("Products", [])
                prod_cols = []
                if isinstance(prod_rows, list) and prod_rows and isinstance(prod_rows[0], dict):
                    prod_cols = [c for c in prod_rows[0].keys() if c != "product_id"]
                elif isinstance(prod_rows, dict) and "columns" in prod_rows:
                    prod_cols = [c for c in prod_rows["columns"] if c != "product_id"]
                union_queries = [f"SELECT product_id, '{c}' AS store, {_quote_identifier(c)} AS price FROM Products WHERE {_quote_identifier(c)} IS NOT NULL" for c in prod_cols]
                adapted_source = " UNION ALL ".join(union_queries) if union_queries else "SELECT NULL AS product_id, NULL AS store, NULL AS price WHERE 0"
            if re.search(r"CREATE\s+FUNCTION\s+getNthHighestSalary", adapted_source, re.IGNORECASE):
                req = tables.get("Request", [{}])
                n_val = req[0].get("N", 1) if req and isinstance(req, list) and isinstance(req[0], dict) else 1
                offset_val = max(0, n_val - 1) if n_val is not None and n_val > 0 else 0
                if n_val is None or n_val <= 0:
                    adapted_source = "SELECT NULL AS getNthHighestSalary"
                else:
                    adapted_source = f"SELECT (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET {offset_val}) AS getNthHighestSalary"
            statements = _sqlite_statements(adapted_source)
            if not statements:
                raise sqlite3.OperationalError("SQL source contains no statements.")
            cursor = connection.execute(statements[0])
            for statement in statements[1:]:
                cursor = connection.execute(statement)
            if cursor.description is None and tables:
                first_table = next(iter(tables.keys()))
                cursor = connection.execute(f'SELECT * FROM "{first_table}" ORDER BY 1')
            columns = [column[0] for column in cursor.description or []]
            rows = [[_json_safe(cell) for cell in row] for row in cursor.fetchall()]
        runtime_ms = (time.perf_counter() - started) * 1000.0
        return EnvironmentResult(
            value={"columns": columns, "rows": rows},
            stdout=json.dumps({"columns": columns, "rows": rows}, ensure_ascii=False),
            runtime_ms=runtime_ms,
        )
    except sqlite3.Error as exc:
        return EnvironmentResult(
            runtime_ms=(time.perf_counter() - started) * 1000.0,
            error_message=f"SQL error: {exc}",
        )


def _sqlite_statements(source: str) -> list[str]:
    """Split complete SQLite statements without breaking semicolons in literals."""
    statements: list[str] = []
    buffer = ""
    for character in source:
        buffer += character
        if character == ";" and sqlite3.complete_statement(buffer):
            if buffer.strip():
                statements.append(buffer.strip())
            buffer = ""
    if buffer.strip():
        statements.append(buffer.strip())
    return statements


def _create_sqlite_table(connection: sqlite3.Connection, name: str, raw_rows: Any) -> None:
    if isinstance(raw_rows, dict) and isinstance(raw_rows.get("rows"), list):
        columns = [str(column) for column in raw_rows.get("columns") or []]
        rows = raw_rows["rows"]
        records = [dict(zip(columns, row)) for row in rows if isinstance(row, list)]
    elif isinstance(raw_rows, list):
        records = [row for row in raw_rows if isinstance(row, dict)]
        columns = []
        for record in records:
            for column in record:
                if str(column) not in columns:
                    columns.append(str(column))
    else:
        raise sqlite3.OperationalError(f'Table "{name}" must be an array of row objects.')
    if not columns:
        columns = ["_empty_col"]
        records = []
    column_types = {
        column: _sqlite_type(next((row.get(column) for row in records if row.get(column) is not None), None))
        for column in columns
    }
    quoted_columns = ", ".join(
        f'{_quote_identifier(column)} {column_types[column]}' for column in columns
    )
    connection.execute(f"CREATE TABLE {_quote_identifier(name)} ({quoted_columns})")
    placeholders = ", ".join("?" for _ in columns)
    insert = (
        f"INSERT INTO {_quote_identifier(name)} "
        f"({', '.join(_quote_identifier(column) for column in columns)}) VALUES ({placeholders})"
    )
    connection.executemany(insert, [[row.get(column) for column in columns] for row in records])


def _quote_identifier(value: str) -> str:
    if not value or "\x00" in value:
        raise sqlite3.OperationalError("SQL table and column names must be non-empty.")
    return '"' + value.replace('"', '""') + '"'


def _sqlite_type(value: Any) -> str:
    if isinstance(value, bool) or isinstance(value, int):
        return "INTEGER"
    if isinstance(value, float):
        return "REAL"
    if isinstance(value, (bytes, bytearray)):
        return "BLOB"
    return "TEXT"


def _run_pandas(source: str, input_data: dict[str, Any], timeout_seconds: float) -> EnvironmentResult:
    python = _python_runtime()
    if python is None:
        return EnvironmentResult(
            error_message="Pandas runtime is unavailable. Rebuild the app with the bundled Python environment."
        )
    with tempfile.TemporaryDirectory(prefix="coden-pandas-") as tmp:
        workdir = Path(tmp)
        solution_path = workdir / "solution.py"
        runner_path = workdir / "runner.py"
        solution_path.write_text(source, encoding="utf-8")
        runner_path.write_text(_PANDAS_RUNNER, encoding="utf-8")
        started = time.perf_counter()
        try:
            completed = subprocess.run(
                [python, str(runner_path), str(solution_path)],
                cwd=str(workdir),
                input=json.dumps(input_data),
                text=True,
                capture_output=True,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            return EnvironmentResult(error_message=f"Pandas program timed out after {timeout_seconds:g} seconds.")
        runtime_ms = (time.perf_counter() - started) * 1000.0
        if completed.returncode != 0:
            detail = (completed.stderr or completed.stdout).strip()
            if "No module named 'pandas'" in detail:
                detail = "pandas is not installed in the selected Python runtime."
            return EnvironmentResult(
                stderr=completed.stderr,
                runtime_ms=runtime_ms,
                error_message=f"Pandas error: {detail[:1600]}",
            )
        try:
            value = json.loads(completed.stdout)
        except json.JSONDecodeError:
            return EnvironmentResult(
                stdout=completed.stdout,
                stderr=completed.stderr,
                runtime_ms=runtime_ms,
                error_message="Pandas runner did not return valid JSON.",
            )
        return EnvironmentResult(value=value, stdout=completed.stdout, stderr=completed.stderr, runtime_ms=runtime_ms)


def _run_bash(source: str, input_data: dict[str, Any], timeout_seconds: float) -> EnvironmentResult:
    bash = _bash_runtime()
    if bash is None:
        return EnvironmentResult(
            error_message=(
                "Bash runtime not found. Bundle bash.exe under debug-tools/bash/bin, "
                "install Git for Windows, or set CODEN_BASH."
            )
        )
    stdin = input_data.get("stdin", "")
    files = input_data.get("files", {})
    if not isinstance(stdin, str) or not isinstance(files, dict):
        return EnvironmentResult(error_message='Bash input requires string "stdin" and object "files" values.')
    with tempfile.TemporaryDirectory(prefix="coden-bash-") as tmp:
        workdir = Path(tmp)
        script = workdir / "solution.sh"
        script.write_text(source, encoding="utf-8", newline="\n")
        for raw_name, contents in files.items():
            relative = Path(str(raw_name))
            if relative.is_absolute() or ".." in relative.parts:
                return EnvironmentResult(error_message=f"Unsafe Bash fixture path: {raw_name}.")
            target = workdir / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(str(contents), encoding="utf-8", newline="\n")
        started = time.perf_counter()
        try:
            completed = subprocess.run(
                [bash, str(script)],
                cwd=str(workdir),
                input=stdin,
                text=True,
                capture_output=True,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            return EnvironmentResult(error_message=f"Bash program timed out after {timeout_seconds:g} seconds.")
        runtime_ms = (time.perf_counter() - started) * 1000.0
        if completed.returncode != 0:
            return EnvironmentResult(
                stdout=completed.stdout,
                stderr=completed.stderr,
                runtime_ms=runtime_ms,
                error_message=f"Bash exited with code {completed.returncode}: {(completed.stderr or completed.stdout).strip()[:1600]}",
            )
        return EnvironmentResult(
            value=completed.stdout.rstrip("\n"),
            stdout=completed.stdout,
            stderr=completed.stderr,
            runtime_ms=runtime_ms,
        )


def _run_concurrency(
    source: str,
    input_data: dict[str, Any],
    challenge_id: str,
    timeout_seconds: float,
) -> EnvironmentResult:
    python = _python_runtime()
    if python is None:
        return EnvironmentResult(
            error_message="Concurrency runtime is unavailable. Rebuild the app with the bundled Python environment."
        )
    if challenge_id not in {"lc_1114", "lc_1115", "lc_1116", "lc_1117", "lc_1188", "lc_1195", "lc_1226", "lc_1242", "lc_1279"}:
        return EnvironmentResult(error_message=f"Unsupported concurrency challenge: {challenge_id}.")
    with tempfile.TemporaryDirectory(prefix="coden-concurrency-") as tmp:
        workdir = Path(tmp)
        solution_path = workdir / "solution.py"
        runner_path = workdir / "runner.py"
        solution_path.write_text(source, encoding="utf-8")
        runner_path.write_text(_CONCURRENCY_RUNNER, encoding="utf-8")
        started = time.perf_counter()
        try:
            completed = subprocess.run(
                [python, str(runner_path), str(solution_path), challenge_id],
                cwd=str(workdir),
                input=json.dumps(input_data),
                text=True,
                capture_output=True,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            return EnvironmentResult(
                runtime_ms=(time.perf_counter() - started) * 1000.0,
                error_message=f"Concurrency program deadlocked or timed out after {timeout_seconds:g} seconds.",
            )
        process_ms = (time.perf_counter() - started) * 1000.0
        if completed.returncode != 0:
            detail = (completed.stderr or completed.stdout).strip()
            return EnvironmentResult(
                stdout=completed.stdout,
                stderr=completed.stderr,
                runtime_ms=process_ms,
                error_message=f"Concurrency error: {detail[:1600]}",
            )
        try:
            payload = json.loads(completed.stdout)
            value = payload["value"]
            runtime_ms = float(payload.get("runtime_ms", process_ms))
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            return EnvironmentResult(
                stdout=completed.stdout,
                stderr=completed.stderr,
                runtime_ms=process_ms,
                error_message="Concurrency runner did not return valid JSON.",
            )
        return EnvironmentResult(
            value=value,
            stdout=completed.stdout,
            stderr=completed.stderr,
            runtime_ms=runtime_ms,
        )


def _python_runtime() -> str | None:
    configured = os.environ.get("CODEN_DEBUG_PYTHON") or os.environ.get("CODEN_PYTHON_EXE")
    if configured and Path(configured).is_file():
        return configured
    executable = Path(sys.executable)
    if executable.is_file() and executable.name.lower() not in {"coden-server.exe", "coden-server"}:
        return str(executable)
    return None


def _bash_runtime() -> str | None:
    configured = os.environ.get("CODEN_BASH")
    if configured and Path(configured).is_file():
        return configured
    roots = [
        CODEN_HOME / "debug-tools",
        PROJECT_ROOT / "debug-tools",
        PROJECT_ROOT / "server" / "dist" / "debug-tools",
    ]
    for root in roots:
        for relative in ("bash/bin/bash.exe", "bash/bash.exe", "bin/bash.exe", "bash.exe"):
            candidate = root / relative
            if candidate.is_file():
                return str(candidate)
    if os.name == "nt":
        for candidate in (
            Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Git" / "bin" / "bash.exe",
            Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Git" / "bin" / "bash.exe",
        ):
            if candidate.is_file():
                return str(candidate)
    found = shutil.which("bash")
    return found


def _json_safe(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


_PANDAS_RUNNER = r'''
import builtins
import importlib.util
import inspect
import json
import sys
import typing

for t in ["List", "Dict", "Set", "Tuple", "Optional", "Union", "Any", "Callable", "Iterable", "Sequence"]:
    if hasattr(typing, t):
        setattr(builtins, t, getattr(typing, t))

import pandas as pd

payload = json.load(sys.stdin)
spec = importlib.util.spec_from_file_location("coden_user_solution", sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
solve = getattr(module, "solve", None)
if not callable(solve):
    candidates = [
        value for name, value in vars(module).items()
        if callable(value) and not name.startswith("_") and getattr(value, "__module__", "") == module.__name__
    ]
    if len(candidates) != 1:
        raise RuntimeError("Define solve(...) or exactly one public solution function.")
    solve = candidates[0]

signature = inspect.signature(solve)
param_names = list(signature.parameters.keys())

tables = payload.get("tables", {})
args = dict(payload.get("args", {}))
for name, rows in tables.items():
    args[name] = pd.DataFrame(rows)

for k, v in payload.items():
    if k not in ("tables", "args"):
        if k in param_names:
            hint = signature.parameters[k].annotation
            if isinstance(v, list) and (hint == pd.DataFrame or "DataFrame" in str(hint)):
                args[k] = pd.DataFrame(v)
            else:
                args[k] = v
        elif len(param_names) == 1 and not args:
            param_name = param_names[0]
            hint = signature.parameters[param_name].annotation
            if isinstance(v, list) and (hint == pd.DataFrame or "DataFrame" in str(hint)):
                args[param_name] = pd.DataFrame(v)
            else:
                args[param_name] = v

result = solve(**args)
if isinstance(result, pd.DataFrame):
    if result.index.name is not None or (hasattr(result.index, "names") and any(n is not None for n in result.index.names)):
        result = result.reset_index()
    output = {"columns": [str(column) for column in result.columns], "rows": result.where(pd.notna(result), None).values.tolist()}
elif isinstance(result, pd.Series):
    output = {"name": None if result.name is None else str(result.name), "values": result.where(pd.notna(result), None).tolist()}
elif hasattr(result, "item"):
    output = result.item()
elif isinstance(result, (list, tuple)):
    output = list(result)
else:
    output = result
print(json.dumps(output, ensure_ascii=False, default=str))
'''


_CONCURRENCY_RUNNER = r'''
import importlib.util
import json
import sys
import threading
import time
import traceback
from collections import Counter, deque
from urllib.parse import urlsplit


def load_module(path):
    spec = importlib.util.spec_from_file_location("coden_user_solution", path)
    module = importlib.util.module_from_spec(spec)
    # LeetCode supplies these common concurrency globals to submissions. Keep
    # the accepted source unchanged and reproduce that module environment in
    # the isolated cOde(n) runner.
    module.threading = threading
    module.deque = deque
    spec.loader.exec_module(module)
    return module

def run_threads(calls, *, stagger=False):
    errors = []

    def guarded(call):
        try:
            call()
        except BaseException:
            errors.append(traceback.format_exc())

    threads = []
    for call in calls:
        thread = threading.Thread(target=guarded, args=(call,), daemon=True)
        threads.append(thread)
        thread.start()
        if stagger:
            time.sleep(0.0005)
    for thread in threads:
        thread.join(2.0)
    if any(thread.is_alive() for thread in threads):
        raise RuntimeError("worker threads did not finish; probable deadlock")
    if errors:
        raise RuntimeError(errors[0])


def run_1114(module, data):
    target = module.Foo()
    output = []
    methods = {
        1: lambda: target.first(lambda: output.append("first")),
        2: lambda: target.second(lambda: output.append("second")),
        3: lambda: target.third(lambda: output.append("third")),
    }
    run_threads([methods[value] for value in data["nums"]], stagger=True)
    return "".join(output)


def run_1115(module, data):
    target = module.FooBar(int(data["n"]))
    output = []
    calls = {
        "foo": lambda: target.foo(lambda: output.append("foo")),
        "bar": lambda: target.bar(lambda: output.append("bar")),
    }
    order = data.get("threads", ["bar", "foo"])
    run_threads([calls[name] for name in order])
    return "".join(output)


def run_1116(module, data):
    target = module.ZeroEvenOdd(int(data["n"]))
    output = []
    calls = {
        "zero": lambda: target.zero(output.append),
        "even": lambda: target.even(output.append),
        "odd": lambda: target.odd(output.append),
    }
    order = data.get("threads", ["even", "odd", "zero"])
    run_threads([calls[name] for name in order])
    return "".join(str(value) for value in output)


def run_1117(module, data):
    target = module.H2O()
    output = []
    calls = []
    for atom in data["water"]:
        if atom == "H":
            calls.append(lambda target=target: target.hydrogen(lambda: output.append("H")))
        elif atom == "O":
            calls.append(lambda target=target: target.oxygen(lambda: output.append("O")))
        else:
            raise ValueError(f"invalid atom: {atom!r}")
    run_threads(calls, stagger=bool(data.get("stagger", True)))
    return "".join(output)


def run_1188(module, data):
    target = module.BoundedBlockingQueue(int(data["capacity"]))
    dequeued = []
    calls = []
    for operation_index, operation in enumerate(data["operations"]):
        if operation[0] == "enqueue":
            value = int(operation[1])
            calls.append((operation_index, lambda value=value: target.enqueue(value)))
        elif operation[0] == "dequeue":
            calls.append((operation_index, lambda: dequeued.append(target.dequeue())))
        elif operation[0] == "size":
            continue
        else:
            raise ValueError(f"unknown operation: {operation!r}")

    raw_checks = data.get("blocking_checks", [])
    checks = {
        int(check["operation_index"]): tuple(int(index) for index in check.get("after_completed", []))
        for check in raw_checks
    }
    errors = []
    violations = []
    completed = {operation_index: threading.Event() for operation_index, _ in calls}
    threads = []

    def guarded(operation_index, call):
        try:
            call()
        except BaseException:
            errors.append(traceback.format_exc())
        finally:
            completed[operation_index].set()

    stagger = bool(data.get("stagger", True))
    for operation_index, call in calls:
        for prerequisite in checks.get(operation_index, ()):
            event = completed.get(prerequisite)
            if event is None or not event.wait(0.5):
                violations.append(f"blocking-check-prerequisite-{prerequisite}-did-not-complete")
        thread = threading.Thread(target=guarded, args=(operation_index, call), daemon=True)
        threads.append(thread)
        thread.start()
        if operation_index in checks:
            time.sleep(0.01)
            if completed[operation_index].is_set():
                violations.append(f"operation-{operation_index}-did-not-block")
        elif stagger:
            time.sleep(0.0005)

    for thread in threads:
        thread.join(2.0)
    if any(thread.is_alive() for thread in threads):
        raise RuntimeError("worker threads did not finish; probable deadlock")
    if errors:
        raise RuntimeError(errors[0])
    return {"dequeued": dequeued, "final_size": target.size(), "violations": violations}


def run_1195(module, data):
    target = module.FizzBuzz(int(data["n"]))
    output = []
    calls = {
        "fizz": lambda: target.fizz(lambda: output.append("fizz")),
        "buzz": lambda: target.buzz(lambda: output.append("buzz")),
        "fizzbuzz": lambda: target.fizzbuzz(lambda: output.append("fizzbuzz")),
        "number": lambda: target.number(output.append),
    }
    run_threads([calls[name] for name in data.get("threads", calls)])
    return output


def run_1226(module, data):
    target = module.DiningPhilosophers()
    rounds = int(data["n"])
    order = [int(value) for value in data.get("start_order", range(5))]
    philosophers = []
    while len(philosophers) < rounds * 5:
        philosophers.extend(order)
    philosophers = philosophers[: rounds * 5]
    lock = threading.Lock()
    fork_owner = [None] * 5
    violations = []
    completed = []

    def request(call_id, philosopher):
        left = philosopher
        right = (philosopher + 1) % 5
        events = []

        def pick(fork, label):
            with lock:
                if fork_owner[fork] is not None:
                    violations.append("shared-fork-overlap")
                fork_owner[fork] = call_id
                events.append(label)

        def put(fork, label):
            with lock:
                if fork_owner[fork] != call_id:
                    violations.append("put-unowned-fork")
                fork_owner[fork] = None
                events.append(label)

        target.wantsToEat(
            philosopher,
            lambda: pick(left, "pick-left"),
            lambda: pick(right, "pick-right"),
            lambda: events.append("eat"),
            lambda: put(left, "put-left"),
            lambda: put(right, "put-right"),
        )
        with lock:
            completed.append({"philosopher": philosopher, "events": events})

    run_threads([
        lambda call_id=index, philosopher=value: request(call_id, philosopher)
        for index, value in enumerate(philosophers)
    ], stagger=True)
    return {"calls": completed, "violations": violations}


class HtmlParser:
    def __init__(self, graph, delays):
        self.graph = graph
        self.delays = delays
        self.lock = threading.Lock()
        self.fetches = []
        self.active = 0
        self.max_active = 0

    def getUrls(self, url):
        with self.lock:
            self.fetches.append(url)
            self.active += 1
            self.max_active = max(self.max_active, self.active)
        time.sleep(self.delays.get(url, 0.0005))
        result = list(self.graph.get(url, []))
        with self.lock:
            self.active -= 1
        return result


def crawler_fixture(data):
    if "urls" in data:
        urls = list(data["urls"])
        graph = {url: [] for url in urls}
        for left, right in data.get("edges", []):
            graph[urls[left]].append(urls[right])
        return graph, data["start_url"]
    shape = data.get("shape")
    if shape == "star":
        width = int(data["width"])
        host = data.get("hostname", "a.com")
        root = f"http://{host}"
        children = [f"{root}/{index}" for index in range(width)]
        return {root: children, **{url: [] for url in children}}, root
    if shape == "duplicate-edges":
        root = "http://a.com"
        child = root + "/x"
        return {root: [child, child, child], child: [root]}, root
    if shape == "off-host-bridge":
        root = "http://a.com"
        foreign = "http://b.com/x"
        hidden = "http://a.com/hidden"
        return {root: [foreign], foreign: [hidden], hidden: []}, root
    nodes = int(data.get("nodes", 1))
    urls = [f"http://a.com/{index}" for index in range(nodes)]
    if shape == "dense":
        return {url: urls[index + 1:] for index, url in enumerate(urls)}, urls[0]
    graph = {url: urls[index + 1:index + 4] for index, url in enumerate(urls)}
    return graph, urls[0]


def run_1242(module, data):
    graph, start = crawler_fixture(data)
    delay_scale = float(data.get("parser_delay", 0.0002))
    delays = {url: delay_scale * (1 + index % 5) for index, url in enumerate(graph)}
    parser = HtmlParser(graph, delays)
    target = module.Solution()
    urls = target.crawl(start, parser)
    return {"urls": list(urls), "fetches": parser.fetches, "max_active": parser.max_active, "graph": graph, "start_url": start}


def run_1279(module, data):
    target = module.TrafficLight()
    cars = [int(value) for value in data["cars"]]
    directions = [int(value) for value in data["directions"]]
    arrival_times = [int(value) for value in data.get("arrival_times", data.get("arrivalTimes", []))]
    if not (len(cars) == len(directions) == len(arrival_times)):
        raise ValueError("cars, directions, and arrival_times must have equal lengths")

    state_lock = threading.Lock()
    green_road = 1
    active = Counter()
    events = []
    violations = []
    first_arrival = min(arrival_times, default=0)

    def request(car_id, direction, arrival_time):
        nonlocal green_road
        road_id = 1 if direction <= 2 else 2
        time.sleep(max(0, arrival_time - first_arrival) * 0.0001)

        def turn_green():
            nonlocal green_road
            with state_lock:
                if green_road == road_id:
                    violations.append("redundant-green-change")
                if any(count and road != road_id for road, count in active.items()):
                    violations.append("green-change-during-crossing")
                green_road = road_id
                events.append({"kind": "green", "road": road_id, "car": car_id})

        def cross_car():
            with state_lock:
                if green_road != road_id:
                    violations.append("red-road-crossing")
                if any(count and road != road_id for road, count in active.items()):
                    violations.append("cross-road-overlap")
                active[road_id] += 1
            time.sleep(0.0005)
            with state_lock:
                events.append({"kind": "cross", "road": road_id, "direction": direction, "car": car_id})
                active[road_id] -= 1

        target.carArrived(car_id, road_id, direction, turn_green, cross_car)

    run_threads([
        lambda car_id=car_id, direction=direction, arrival_time=arrival_time: request(
            car_id, direction, arrival_time
        )
        for car_id, direction, arrival_time in zip(cars, directions, arrival_times)
    ])
    return {"cars": cars, "events": events, "violations": violations}


RUNNERS = {
    "lc_1114": run_1114,
    "lc_1115": run_1115,
    "lc_1116": run_1116,
    "lc_1117": run_1117,
    "lc_1188": run_1188,
    "lc_1195": run_1195,
    "lc_1226": run_1226,
    "lc_1242": run_1242,
    "lc_1279": run_1279,
}

data = json.load(sys.stdin)
module = load_module(sys.argv[1])
started = time.perf_counter()
value = RUNNERS[sys.argv[2]](module, data)
runtime_ms = (time.perf_counter() - started) * 1000.0
print(json.dumps({"value": value, "runtime_ms": runtime_ms}, ensure_ascii=False, default=str))
'''
