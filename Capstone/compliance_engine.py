"""
Preliminary California Privacy Compliance Engine

This module compares extracted contract clauses against
the structured CCPA/CPRA service provider requirements.

It identifies potentially relevant evidence.
It does NOT make a final legal compliance determination.
"""

from legal_rules import get_applicable_rules


def normalize(value):
    """Convert text to lowercase for comparison."""
    return str(value or "").strip().lower()


def find_relevant_clauses(rule, clauses):
    """
    Identify clauses potentially relevant to a legal rule.

    A clause is selected when:
    1. Its category matches a rule category; OR
    2. Its text contains one of the rule's keywords.

    This is preliminary matching, not legal interpretation.
    """

    relevant = []

    rule_categories = {
        normalize(category)
        for category in rule.get("categories", [])
    }

    rule_keywords = [
        normalize(keyword)
        for keyword in rule.get("keywords", [])
        if normalize(keyword)
    ]

    for clause in clauses:

        clause_categories = {
            normalize(category)
            for category in clause.get("categories", [])
        }

        category_match = bool(
            rule_categories.intersection(clause_categories)
        )

        clause_text = normalize(clause.get("text", ""))

        keyword_matches = [
            keyword
            for keyword in rule_keywords
            if keyword in clause_text
        ]

        if category_match or keyword_matches:

            relevant.append({
                "clause_number": clause.get("clause_number"),
                "heading": clause.get("heading"),
                "source": clause.get("source"),
                "source_location": clause.get("source_location"),
                "page_number": clause.get("page_number"),
                "original_text": clause.get("text", ""),
                "matching_categories": sorted(
                    rule_categories.intersection(clause_categories)
                ),
                "matching_keywords": keyword_matches
            })

    return relevant


def review_contract(clauses, contract_role):
    """
    Compare extracted clauses against the applicable
    California privacy requirements.
    """

    if contract_role not in [
        "service_provider_or_contractor"
    ]:
        raise ValueError(
            "This version reviews only service provider "
            "or contractor agreements under 11 CCR section 7051. "
            "Third-party agreements require a separate review."
        )

    rules = get_applicable_rules(contract_role)

    results = []

    for rule in rules:

        evidence = find_relevant_clauses(rule, clauses)

        if evidence:

            status = "EVIDENCE_LOCATED_REVIEW_REQUIRED"

            observation = (
                "Potentially relevant contract wording was located. "
                "A lawyer must determine whether the wording satisfies "
                "the applicable legal requirement."
            )

        else:

            status = "NO_RELEVANT_TEXT_LOCATED"

            observation = (
                "No potentially relevant wording was located by "
                "the preliminary search. This does not establish "
                "that the contract lacks the provision."
            )

        results.append({
            "rule_id": rule["rule_id"],
            "title": rule["title"],
            "authority": rule["authority"],
            "legal_requirement": rule["requirement"],
            "status": status,
            "observation": observation,
            "relevant_clauses": evidence,
            "review_questions": rule["review_questions"]
        })

    return {
        "legal_framework": "California CCPA/CPRA",
        "contract_role": contract_role,
        "review_type": "Preliminary clause-to-rule comparison",
        "final_compliance_determination": False,
        "results": results
    }


def print_compliance_report(report):
    """Display the preliminary review in the terminal."""

    print("=" * 70)
    print("CALIFORNIA CONTRACT PRIVACY REVIEW")
    print("=" * 70)

    print("Legal framework:", report["legal_framework"])
    print("Contract role:", report["contract_role"])
    print("Review type:", report["review_type"])

    print("\nFINAL COMPLIANCE DETERMINATION: NOT MADE")

    for item in report["results"]:

        print("\n" + "-" * 70)
        print("RULE:", item["rule_id"])
        print("TITLE:", item["title"])
        print("AUTHORITY:", item["authority"])
        print("STATUS:", item["status"])

        print("\nLEGAL REQUIREMENT:")
        print(item["legal_requirement"])

        print("\nOBSERVATION:")
        print(item["observation"])

        if item["relevant_clauses"]:

            print("\nPOTENTIALLY RELEVANT CONTRACT WORDING:")

            for clause in item["relevant_clauses"]:

                print("\nClause:", clause["clause_number"])
                print("Heading:", clause["heading"])
                print("Location:", clause["source_location"])
                print("Text:", clause["original_text"])

        print("\nQUESTIONS FOR LEGAL REVIEW:")

        for question in item["review_questions"]:
            print("-", question)

    print("\n" + "=" * 70)
    print("END OF PRELIMINARY REVIEW")
    print("=" * 70)
