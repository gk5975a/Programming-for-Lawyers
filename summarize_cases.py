#!/usr/bin/env python3
"""
Summarize legal case passages into a structured outline.

The script reads a text file that contains one or more case opinions or excerpts
and emits a new file where each case is prefixed with sections:

    1. Introduction
    2. Brief Facts
    3. Procedural History
    4. Reasoning of the Court
    5. Conclusion

The implementation is intentionally simplistic – it relies on
regular‑expression based heuristics to locate the typical headings used
in U.S. appellate opinions (e.g., ``Facts:``, ``Procedural History:``,
``Opinion of the Court:``, ``Conclusion:``.)  If any of these headings are
missing, the corresponding section is left blank.

The script can be run from the command line::

    python summarize_cases.py INPUT_FILE.txt OUTPUT_FILE.txt

It will read the contents of ``INPUT_FILE.txt`` and write a structured
summary to ``OUTPUT_FILE.txt``.

The goal is to provide a reusable skeleton that can later be extended
with NLP models or more advanced parsers.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List, Tuple


# ---------- Helper functions ----------

def read_text(file_path: str | Path) -> str:
    """Return the file contents as a single string.

    Parameters
    ----------
    file_path
        Path to a readable text file.
    """
    return Path(file_path).read_text(encoding="utf-8")


def write_text(file_path: str | Path, content: str) -> None:
    """Write ``content`` to ``file_path``.

    Parameters
    ----------
    file_path
        Destination file path.
    content
        Text to write.
    """
    Path(file_path).write_text(content, encoding="utf-8")


# ---------- Parsing logic ----------

def split_into_cases(text: str) -> List[str]:
    """Split the document into individual cases.

    The heuristic looks for lines that look like a case name followed by a
    short description (e.g., ``Smith v. Jones, 123 U.S. 456 (2020)``).
    Lines that match a pattern beginning with ``[A-Za-z]`` and containing a
    ``v`` or ``vs`` are treated as the start of a new case.
    """
    # Split by blank lines to get paragraphs
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    cases = []
    current_case = []
    case_start_pattern = re.compile(r"^.*\bv\s*vs?\s*.*$", re.I)
    for para in paragraphs:
        if case_start_pattern.match(para):
            if current_case:
                cases.append("\n\n".join(current_case))
                current_case = []
        current_case.append(para)
    if current_case:
        cases.append("\n\n".join(current_case))
    return cases


def extract_section(text: str, heading: str) -> str:
    """Return the text belonging to *heading*.

    It finds the first occurrence of ``heading`` (case‑insensitive) and
    returns the text up to the next heading or the end of the document.
    """
    heading_regex = re.compile(rf"^\s*{re.escape(heading)}\s*:\s*$", re.I | re.MULTILINE)
    matches = list(heading_regex.finditer(text))
    if not matches:
        return ""
    start = matches[0].end()
    # Find the next heading
    next_headings = re.compile(r"^\s*[A-Za-z]+\s*:\s*$", re.I | re.MULTILINE)
    following = next_headings.search(text, pos=start)
    end = following.start() if following else len(text)
    return text[start:end].strip()


def summarize_case(case_text: str) -> str:
    """Return a structured summary for a single case.

    The function extracts the following sections if available:

    * Introduction (everything up to the first known heading)
    * Brief Facts
    * Procedural History
    * Reasoning of the Court
    * Conclusion

    Each section is prefixed with an explicit heading.
    """
    # Define possible headings used in the heuristics
    headings = {
        "facts": "Facts",  # often used
        "procedural history": "Procedural History",
        "reasoning": "Opinion of the Court",  # or sometimes "Opinion"
        "conclusion": "Conclusion",
    }

    # Introduction: everything before the first known heading
    all_headings_pattern = re.compile(r"^\s*([A-Za-z]+)\s*:\s*$", re.I | re.MULTILINE)
    first_heading_match = all_headings_pattern.search(case_text)
    intro_end = first_heading_match.start() if first_heading_match else len(case_text)
    introduction = case_text[:intro_end].strip()

    facts = extract_section(case_text, headings["facts"])
    procedural = extract_section(case_text, headings["procedural history"])
    reasoning = extract_section(case_text, headings["reasoning"])
    conclusion = extract_section(case_text, headings["conclusion"])

    output = []
    output.append("Introduction:\n" + (introduction or "(None)"))
    output.append("\n\nBrief Facts:\n" + (facts or "(None)"))
    output.append("\n\nProcedural History:\n" + (procedural or "(None)"))
    output.append("\n\nReasoning of the Court:\n" + (reasoning or "(None)"))
    output.append("\n\nConclusion:\n" + (conclusion or "(None)"))
    return "\n".join(output)


# ---------- Entry point ----------

def main(argv: List[str]) -> None:
    if len(argv) < 3:
        print("Usage: python summarize_cases.py INPUT_FILE.txt OUTPUT_FILE.txt", file=sys.stderr)
        sys.exit(1)
    input_path, output_path = argv[1], argv[2]

    raw_text = read_text(input_path)
    cases = split_into_cases(raw_text)
    summaries = [summarize_case(c) for c in cases]
    final_text = "\n\n=== \n\n".join(summaries)
    write_text(output_path, final_text)
    print(f"Wrote structured summary for {len(cases)} case(s) to {output_path}")


if __name__ == "__main__":
    main(sys.argv)
