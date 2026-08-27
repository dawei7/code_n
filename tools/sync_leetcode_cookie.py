"""Extract fresh LeetCode cookies from local Chrome profiles."""
from __future__ import annotations

import json
import os
import shutil
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.extract_euler_chrome_cookies import decrypt_cookie_value, get_chrome_master_key

COOKIE_FILE = ROOT / "dsa" / "leetcode" / "_local" / ".leetcode_cookie"


def sync_cookies():
    master_key = get_chrome_master_key()
    user_data = Path(os.environ["LOCALAPPDATA"]) / "Google" / "Chrome" / "User Data"
    cookie_files = list(user_data.glob("**/Network/Cookies")) + list(user_data.glob("**/Cookies"))
    cookies: dict[str, str] = {}
    for c_file in cookie_files:
        try:
            temp_db = Path(os.environ["TEMP"]) / f"chrome_lc_{os.getpid()}_{c_file.parent.parent.name}.db"
            shutil.copy2(c_file, temp_db)
            conn = sqlite3.connect(temp_db)
            cursor = conn.cursor()
            cursor.execute("SELECT name, encrypted_value, value FROM cookies WHERE host_key LIKE ?", ("%leetcode.com%",))
            for name, encrypted_val, plain_val in cursor.fetchall():
                if plain_val:
                    cookies[name] = plain_val
                elif encrypted_val:
                    try:
                        dec = decrypt_cookie_value(encrypted_val, master_key)
                        if dec:
                            cookies[name] = dec
                    except Exception:
                        pass
            conn.close()
            if temp_db.is_file():
                temp_db.unlink()
        except Exception:
            pass

    print("Found LeetCode cookies:", list(cookies.keys()))
    if "LEETCODE_SESSION" in cookies and "csrftoken" in cookies:
        parts = [
            f"LEETCODE_SESSION={cookies['LEETCODE_SESSION']}",
            f"csrftoken={cookies['csrftoken']}",
        ]
        if "cf_clearance" in cookies:
            parts.append(f"cf_clearance={cookies['cf_clearance']}")
        cookie_str = "; ".join(parts)
        COOKIE_FILE.parent.mkdir(parents=True, exist_ok=True)
        COOKIE_FILE.write_text(cookie_str, encoding="utf-8")
        print("Updated .leetcode_cookie successfully!")
        return True
    else:
        print("Required cookies (LEETCODE_SESSION, csrftoken) not found.")
        return False


if __name__ == "__main__":
    sync_cookies()
