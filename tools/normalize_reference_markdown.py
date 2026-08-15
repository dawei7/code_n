import json
import re
from pathlib import Path

repo_root = Path('.')
leetcode_dir = repo_root / 'dsa' / 'leetcode'


def extract_signature(pkg_dir: Path, meta: dict) -> dict | None:
    tpl_file = pkg_dir / "template.py"
    if tpl_file.exists():
        content = tpl_file.read_text(encoding="utf-8")

        class_match = re.search(r"class\s+([a-zA-Z0-9_]+)", content)
        class_name = class_match.group(1) if class_match else ""

        class_methods = re.findall(r"def\s+([a-zA-Z0-9_]+)\s*\(\s*self\s*,?\s*([^)]*)\)\s*(?:->\s*([^:]+))?:", content)

        if class_name and class_name != "Solution" and class_methods:
            methods = []
            for m_name, raw_p, ret_t in class_methods:
                clean_p = ", ".join(p.strip() for p in raw_p.split(",") if p.strip())
                ret_str = f" -> `{ret_t.strip()}`" if ret_t and ret_t.strip() != "None" else ""
                if m_name == "__init__":
                    methods.append(f"- `{class_name}({clean_p})`: Initializes the data structure.")
                else:
                    methods.append(f"- `{m_name}({clean_p}){ret_str}`: Executes operation.")
            return {"kind": "class", "methods": methods}

        m = re.search(r"def\s+([a-zA-Z0-9_]+)\s*\(\s*self\s*,?\s*([^)]*)\)\s*(?:->\s*([^:]+))?:", content)
        if m:
            raw_params = m.group(2).strip()
            ret_type = m.group(3).strip() if m.group(3) else ""
            params = []
            if raw_params:
                for part in raw_params.split(","):
                    part = part.strip()
                    if not part:
                        continue
                    if ":" in part:
                        pname, ptype = part.split(":", 1)
                        params.append({"name": pname.strip(), "type": ptype.strip()})
                    else:
                        params.append({"name": part, "type": ""})
            return {"kind": "function", "params": params, "return_type": ret_type}

    meta_params = meta.get("params")
    ret_type = meta.get("return_type") or ""
    if isinstance(meta_params, list) and len(meta_params) > 0:
        params = []
        for p in meta_params:
            if isinstance(p, dict):
                params.append({
                    "name": p.get("name", "arg"),
                    "type": p.get("type", ""),
                    "description": p.get("description", "").strip()
                })
        if params:
            return {"kind": "function", "params": params, "return_type": ret_type}

    return None


def surgical_clean_markdown(text: str, sig: dict | None) -> str:
    # 1. Remove raw HTML wrappers from scraper (div, meta, script, style)
    text = re.sub(r'<div\b[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</div>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<meta[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</?(?:script|style)[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<li\b[^>]*>\s*(.*?)\s*(?:</li>|(?=<li\b|</(?:ul|ol)>|\Z))', r'- \1\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'</li>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</?(?:ul|ol)\b[^>]*>', '\n', text, flags=re.IGNORECASE)

    # 2. Convert unspaced Example titles to headings
    text = re.sub(r'^(?:\*\*)?Example\s+(\d+)\s*:?(?:\*\*)?\s*$', r'#### Example \1', text, flags=re.MULTILINE | re.IGNORECASE)

    # 3. Ensure double newlines before and after all headings
    text = re.sub(r'([^\n])\n(#{1,6}\s+[^\n]+)', r'\1\n\n\2', text)
    text = re.sub(r'^(#{1,6}\s+[^\n]+)\n([^\n#])', r'\1\n\n\2', text, flags=re.MULTILINE)

    # 4. Normalize example bullet points
    lines = text.split("\n")
    new_lines = []
    in_example = False

    i = 0
    while i < len(lines):
        line = lines[i]
        trimmed = line.strip()

        if re.match(r"^#{1,6}\s+Example\s+\d+", trimmed, re.IGNORECASE):
            in_example = True
            new_lines.append(line)
            i += 1
            continue
        elif (
            re.match(r"^#{1,3}\s+\d+\.\s+", trimmed)
            or trimmed.startswith("### Constraints")
            or trimmed.startswith("### 4. Constraints")
            or trimmed.startswith("### Follow-up")
            or trimmed.startswith("### Note")
        ):
            in_example = False
            new_lines.append(line)
            i += 1
            continue

        if in_example:
            input_match = re.match(r"^(?:-\s*)?(?:\*\*)?Input:\s*(?:\*\*)?\s*(.*)$", trimmed, re.IGNORECASE)
            output_match = re.match(r"^(?:-\s*)?(?:\*\*)?Output:\s*(?:\*\*)?\s*(.*)$", trimmed, re.IGNORECASE)
            expl_match = re.match(r"^(?:-\s*)?(?:\*\*)?Explanation:\s*(?:\*\*)?\s*(.*)$", trimmed, re.IGNORECASE)

            if input_match:
                val = input_match.group(1).strip()
                new_lines.append(f"- **Input:** {val}")
                i += 1
                continue
            elif output_match:
                val = output_match.group(1).strip()
                new_lines.append(f"- **Output:** {val}")
                i += 1
                continue
            elif expl_match:
                val = expl_match.group(1).strip()
                if not val and i + 1 < len(lines):
                    next_idx = i + 1
                    while next_idx < len(lines) and not lines[next_idx].strip():
                        next_idx += 1
                    if next_idx < len(lines) and not re.match(r"^(?:#|-|\*\*)", lines[next_idx].strip()):
                        val = lines[next_idx].strip()
                        i = next_idx
                new_lines.append(f"- **Explanation:** {val}")
                i += 1
                continue

        new_lines.append(line)
        i += 1

    text = "\n".join(new_lines)

    # 5. Fix generic placeholder contracts
    generic_patterns = [
        r"-\s*`n`:\s*Input parameter\.\s*\n+-\s*Returns expected result\.",
        r"-\s*`n`:\s*Input parameter\.",
    ]

    has_generic = any(re.search(pat, text) for pat in generic_patterns)
    if has_generic and sig:
        if sig.get("kind") == "class" and sig.get("methods"):
            contract_lines = ["**Methods**\n"]
            contract_lines.extend(sig["methods"])
            new_contract = "\n".join(contract_lines)
        elif sig.get("params"):
            params = sig["params"]
            ret_type = sig.get("return_type") or "the result"

            contract_lines = ["**Inputs**\n"]
            for p in params:
                p_name = p.get("name", "arg")
                p_type = p.get("type", "")
                p_desc = p.get("description", "").strip()
                type_str = f" (`{p_type}`)" if p_type else ""
                desc_str = f": {p_desc}" if p_desc else f": Input parameter{type_str}."
                contract_lines.append(f"- `{p_name}`{desc_str}")

            contract_lines.append("\n**Return value**\n")
            contract_lines.append(f"- Returns `{ret_type}`." if ret_type else "- Returns the expected result.")

            new_contract = "\n".join(contract_lines)
        else:
            new_contract = None

        if new_contract:
            text = re.sub(
                r"(### 2\. Function Contract\s*\n+)(?:-\s*`n`:\s*Input parameter\.(?:\s*\n+-\s*Returns expected result\.)?)",
                r"\1" + new_contract,
                text,
            )

    # 6. Re-ensure heading spacing
    text = re.sub(r'([^\n])\n(#{1,6}\s+[^\n]+)', r'\1\n\n\2', text)
    text = re.sub(r'^(#{1,6}\s+[^\n]+)\n([^\n#])', r'\1\n\n\2', text, flags=re.MULTILINE)

    # 7. Collapse excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text).strip() + '\n'
    return text


def normalize_file(file_path: Path, pkg_dir: Path, meta: dict) -> bool:
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

    sig = extract_signature(pkg_dir, meta)
    updated = surgical_clean_markdown(content, sig)

    if updated != content:
        file_path.write_text(updated, encoding="utf-8")
        return True
    return False


def run_full_normalization():
    pkgs = sorted([
        p for p in leetcode_dir.iterdir()
        if p.is_dir() and not p.name.startswith(("_", "."))
    ])

    total_modified = 0
    for pkg in pkgs:
        meta_file = pkg / "metadata.json"
        meta = {}
        if meta_file.exists():
            try:
                meta = json.loads(meta_file.read_text(encoding="utf-8"))
            except Exception:
                meta = {}

        targets = []
        if (pkg / "doc.md").exists():
            targets.append(pkg / "doc.md")
        if (pkg / "reference").exists():
            for ref_file in (pkg / "reference").glob("*.md"):
                # NEVER touch editorial.md!
                if ref_file.name != "editorial.md":
                    targets.append(ref_file)

        for target in targets:
            if normalize_file(target, pkg, meta):
                total_modified += 1

    print(f"Surgical normalization complete! Total files updated: {total_modified} across {len(pkgs)} packages.")


if __name__ == "__main__":
    run_full_normalization()
