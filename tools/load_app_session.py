import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.extract_euler_chrome_cookies import decrypt_dpapi

bin_file = ROOT / ".coden-data" / "leetcode-session.bin"
raw_bytes = bin_file.read_bytes()
print("Raw bytes len:", len(raw_bytes))

decrypted = decrypt_dpapi(raw_bytes).decode("utf-8")
data = json.loads(decrypted)
print("Decrypted successfully!")
print("Keys:", list(data.keys()))
print("Session preview:", data.get("session", "")[:30] + "...")
print("CSRF preview:", data.get("csrfToken", "")[:30] + "...")
print("Clearance preview:", data.get("cloudflareClearance", "")[:30] + "...")

parts = [
    f"LEETCODE_SESSION={data['session']}",
    f"csrftoken={data['csrfToken']}",
]
if data.get("cloudflareClearance"):
    parts.append(f"cf_clearance={data['cloudflareClearance']}")

cookie_str = "; ".join(parts)
cookie_file = ROOT / "dsa" / "leetcode" / "_local" / ".leetcode_cookie"
cookie_file.write_text(cookie_str, encoding="utf-8")
print("Updated .leetcode_cookie successfully from app's verified session!")
