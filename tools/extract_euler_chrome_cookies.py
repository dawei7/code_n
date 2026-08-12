"""Extract Project Euler cookies from Chrome browser profile on Windows."""

from __future__ import annotations

import base64
import ctypes
import json
import os
import shutil
import sqlite3
from pathlib import Path
from ctypes import wintypes

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class DATA_BLOB(ctypes.Structure):
    _fields_ = [("cbData", wintypes.DWORD), ("pbData", ctypes.POINTER(ctypes.c_char))]


def decrypt_dpapi(encrypted_bytes: bytes) -> bytes:
    blob_in = DATA_BLOB(len(encrypted_bytes), ctypes.create_string_buffer(encrypted_bytes, len(encrypted_bytes)))
    blob_out = DATA_BLOB()
    if ctypes.windll.crypt32.CryptUnprotectData(ctypes.byref(blob_in), None, None, None, None, 0, ctypes.byref(blob_out)):
        data = ctypes.string_at(blob_out.pbData, blob_out.cbData)
        ctypes.windll.kernel32.LocalFree(blob_out.pbData)
        return data
    raise RuntimeError("CryptUnprotectData failed")


def get_chrome_master_key() -> bytes:
    local_state_path = Path(os.environ["LOCALAPPDATA"]) / "Google" / "Chrome" / "User Data" / "Local State"
    if not local_state_path.is_file():
        raise FileNotFoundError(f"Local State file not found at {local_state_path}")
    data = json.loads(local_state_path.read_text(encoding="utf-8"))
    encrypted_key = base64.b64decode(data["os_crypt"]["encrypted_key"])
    if encrypted_key.startswith(b"DPAPI"):
        return decrypt_dpapi(encrypted_key[5:])
    return decrypt_dpapi(encrypted_key)


def decrypt_cookie_value(encrypted_val: bytes, master_key: bytes) -> str:
    if not encrypted_val:
        return ""
    if encrypted_val.startswith(b"v10") or encrypted_val.startswith(b"v11") or encrypted_val.startswith(b"v20"):
        nonce = encrypted_val[3:15]
        ciphertext = encrypted_val[15:]
        aesgcm = AESGCM(master_key)
        decrypted = aesgcm.decrypt(nonce, ciphertext, None)
        return decrypted.decode("utf-8", errors="ignore")
    return decrypt_dpapi(encrypted_val).decode("utf-8", errors="ignore")


def get_project_euler_cookies() -> dict[str, str]:
    master_key = get_chrome_master_key()
    user_data = Path(os.environ["LOCALAPPDATA"]) / "Google" / "Chrome" / "User Data"
    
    # Look for all Cookies databases across Default, Profile 1, Profile 2, etc.
    cookie_files = list(user_data.glob("**/Network/Cookies")) + list(user_data.glob("**/Cookies"))
    
    cookies = {}
    for c_file in cookie_files:
        try:
            temp_db = Path(os.environ["TEMP"]) / f"chrome_cookies_{os.getpid()}_{c_file.parent.parent.name}.db"
            shutil.copy2(c_file, temp_db)
            conn = sqlite3.connect(temp_db)
            cursor = conn.cursor()
            cursor.execute("SELECT name, encrypted_value, value FROM cookies WHERE host_key LIKE '%projecteuler.net%'")
            for name, encrypted_val, plain_val in cursor.fetchall():
                if plain_val:
                    cookies[name] = plain_val
                elif encrypted_val:
                    print(f"Cookie {name} header: {encrypted_val[:10]!r}")
                    try:
                        dec = decrypt_cookie_value(encrypted_val, master_key)
                        if dec:
                            cookies[name] = dec
                    except Exception as err:
                        print(f"Error decrypting {name} in {c_file}: {err}")
            conn.close()
            if temp_db.is_file():
                temp_db.unlink()
        except Exception as err:
            pass

    return cookies


def main():
    print("Extracting Project Euler cookies from Chrome profiles...")
    cookies = get_project_euler_cookies()
    print(f"Found {len(cookies)} cookies:")
    for k, v in cookies.items():
        print(f"  {k} = {v[:30]}..." if len(v) > 30 else f"  {k} = {v}")
    cookie_str = "; ".join(f"{k}={v}" for k, v in cookies.items())
    print("\nFull Cookie String:")
    print(cookie_str)


if __name__ == "__main__":
    main()
