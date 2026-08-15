"""Script to standardize and verify `if __name__ == '__main__': print(solve())` across all Euler solutions."""

from __future__ import annotations

import re
from pathlib import Path


def update_main_block(content: str) -> str:
    pattern = r"\n*if\s+__name__\s*==\s*['\"]__main__['\"]\s*:[\s\S]*$"
    standard_block = '\n\n\nif __name__ == "__main__":\n    print(solve())\n'

    if re.search(pattern, content):
        new_content = re.sub(pattern, standard_block, content)
    else:
        new_content = content.rstrip() + standard_block

    return new_content


def main() -> None:
    euler_dir = Path("dsa/euler")
    updated_count = 0
    total_count = 0
    matching_count = 0
    non_matching = []

    for sol_file in sorted(euler_dir.glob("**/solution.py")):
        total_count += 1
        content = sol_file.read_text(encoding="utf-8")
        new_content = update_main_block(content)

        if new_content != content:
            sol_file.write_text(new_content, encoding="utf-8")
            updated_count += 1
            content = new_content

        if content.endswith('\nif __name__ == "__main__":\n    print(solve())\n'):
            matching_count += 1
        else:
            non_matching.append(sol_file)

    print(f"Total Euler solution files checked: {total_count}")
    print(f"Files updated in this run: {updated_count}")
    print(f"Files with exact standard block: {matching_count} / {total_count}")
    if non_matching:
        print("Non-matching files:")
        for f in non_matching[:10]:
            print(f"  {f}")


if __name__ == "__main__":
    main()
