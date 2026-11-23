import re

# Categories of privacy-related contract provisions.
PRIVACY_CATEGORIES = {
    "Personal information": [
        r"\bpersonal information\b",
        r"\bpersonal data\b",
        r"\b customer information\b",
        r"\bconsumer information\b",
        r"\bsensitive personal information\b",
    ],

    "Processing purposes": [
        r"\bprocess(?:ing)?\b",
        r"\bpurpose of (?:the )?services\b",
        r"\bprovide the services\b",
        r"\bcollect(?:ion)? of personal information\b",
    ],

    "Use restrictions": [
        r"\buse of personal information\b",
        r"\buse personal information\b",
        r"\bpermitted use\b",
        r"\bbusiness purpose\b",
        r"\bcommercial purpose\b",
    ],

    "Sale and sharing": [
        r"\bsell(?:ing)? personal information\b",
        r"\bshare(?:d|s|ing)? personal information\b",
        r"\btargeted advertising\b",
        r"\bcross.context behavioral advertising\b",
    ],

    "Data retention and deletion": [
        r"\bretain(?:ing)?\b",
        r"\bretention\b",
        r"\bdelet(?:e|ion|ing)\b",
        r"\breturn of personal information\b",
        r"\btermination\b",
    ],

    "Information security": [
        r"\binformation security\b",
        r"\bsecurity safeguards\b",
        r"\btechnical safeguards\b",
        r"\badministrative safeguards\b",
        r"\bphysical safeguards\b",
        r"\bprotect customer information\b",
    ],

    "Subcontractors": [
        r"\bsubcontractor(?:s)?\b",
        r"\bsub.processor(?:s)?\b",
        r"\bthird.party service provider(?:s)?\b",
    ],

    "Consumer privacy rights": [
        r"\bconsumer rights\b",
        r"\baccess request\b",
        r"\bdeletion request\b",
        r"\bcorrection request\b",
        r"\bopt.out\b",
        r"\bconsumer request\b",
    ],

    "Data breach notification": [
        r"\bdata breach\b",
        r"\bsecurity incident\b",
        r"\bbreach notification\b",
        r"\bunauthorized access\b",
    ],

    "Audits and compliance": [
        r"\baudit(?:s|ing)?\b",
        r"\bmonitor compliance\b",
        r"\bcompliance with applicable privacy laws\b",
        r"\bdemonstrate compliance\b",
    ],

    "Confidentiality": [
        r"\bconfidential information\b",
        r"\bconfidentiality\b",
        r"\bconfidential treatment\b",
    ],
}


# Recognizes numbered headings such as:
# 1. PARTIES
# 2. SERVICES
# 5. DATA RETENTION
HEADING_PATTERN = re.compile(
    r"^\s*(\d+(?:\.\d+)*)[.)]?\s+"
    r"([A-Z][A-Z0-9 /&(),'-]{1,80})\s*$"
)


def split_into_clauses(text):
    """
    Divide document text into numbered clauses.

    If no numbered headings are found, return the
    entire text as one section.
    """
    lines = text.splitlines()

    clauses = []
    current_heading = "Unnumbered section"
    current_number = None
    current_lines = []
    found_heading = False

    for line in lines:

        match = HEADING_PATTERN.match(line)

        if match:
            found_heading = True

            # Save the previous clause.
            if current_lines:
                clauses.append({
                    "clause_number": current_number,
                    "heading": current_heading,
                    "text": "\n".join(current_lines).strip()
                })

            current_number = match.group(1)
            current_heading = match.group(2).strip()
            current_lines = [line.strip()]

        else:
            current_lines.append(line.strip())

    # Save the final clause.
    if current_lines and found_heading:
        clauses.append({
            "clause_number": current_number,
            "heading": current_heading,
            "text": "\n".join(current_lines).strip()
        })

    if not found_heading and text.strip():
        clauses.append({
            "clause_number": None,
            "heading": "Unnumbered section",
            "text": text.strip()
        })

    return clauses


def classify_clause(clause_text):
    """
    Identify all privacy categories that match
    the wording of a clause.
    """
    matched_categories = []

    for category, patterns in PRIVACY_CATEGORIES.items():

        for pattern in patterns:

            if re.search(
                pattern,
                clause_text,
                flags=re.IGNORECASE
            ):
                matched_categories.append(category)
                break

    return matched_categories


def extract_privacy_clauses(document_sections):
    """
    Accept sections from contract_reader.py.

    Split the text into clauses and identify
    clauses containing privacy-related terms.
    """
    findings = []

    for section in document_sections:

        clauses = split_into_clauses(section["text"])

        for clause in clauses:

            categories = classify_clause(clause["text"])

            # Only retain clauses matching a privacy category.
            if categories:

                findings.append({
                    "source": section["source"],
                    "source_location": section["location"],
                    "page_number": section["page_number"],
                    "clause_number": clause["clause_number"],
                    "heading": clause["heading"],
                    "categories": categories,
                    "text": clause["text"]
                })

    return findings