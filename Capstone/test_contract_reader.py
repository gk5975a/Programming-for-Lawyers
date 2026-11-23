from Contract_Reader import read_contract
from clause_extractor import extract_privacy_clauses
from privacy_analyzer import analyze_privacy_clauses

# from Contract_Reader import read_contract
# from clause_extractor import extract_privacy_clauses

from legal_rules import (
    LEGAL_FRAMEWORK,
    SERVICE_PROVIDER_RULES,
    DUE_DILIGENCE_NOTE,
    get_applicable_rules,
    get_rule_by_id,
    validate_rules
)
from compliance_engine import (
    review_contract,
    print_compliance_report
)


# Location of our sample contract
contract_path = "Capstone/sample_vendor_agreement.txt"

print("=" * 60)
print("CONTRACT PRIVACY COMPLIANCE AI AGENT - DOCUMENT READER TEST")
print("=" * 60)

try:

    # Read the contract
    sections = read_contract(contract_path)

    print("\nContract successfully read!")

   # print("Number of sections extracted:", len(sections))

    print("\nCONTENT OF THE SAMPLE VENDOR SERVICE AGREEMENT EXTRACTED IS DISPLAYED AS FOLLOWS")
    print("-" * 60)

    for section in sections:
       # print("\nLocation:", section["location"])
        print("Text:", section["text"])

    print("\n" + "=" * 55)
    print("DOCUMENT READER TEST COMPLETED")
    print("=" * 55)

except Exception as error:

  print("\nERROR:", error)


# Read the sample agreement.
#contract_path = "contracts/sample_vendor_agreement.txt"

print("=" * 60)
print("CONTRACT PRIVACY AI AGENT - CLAUSE IDENTIFICATION TEST")
print("=" * 60)

try:

    # First, extract the contract text.
    contract_sections = read_contract(contract_path)

    # Next, identify privacy-related clauses.
    privacy_clauses = extract_privacy_clauses(contract_sections)

    print("\nContract successfully analyzed.")

    print(
        "Privacy-related clauses identified:",
        len(privacy_clauses)
    )

    print("\nIDENTIFIED PRIVACY CLAUSES")
    print("-" * 60)

    for clause in privacy_clauses:

        print("\nClause:", clause["clause_number"])
        print("Heading:", clause["heading"])

        print(
            "Categories:",
            ", ".join(clause["categories"])
        )

        print(
            "Source:",
            clause["source_location"]
        )

        print("Contract wording:")
        print(clause["text"])

        print("-" * 60)

    print("\nCLAUSE IDENTIFICATION TEST COMPLETED")

except Exception as error:

    print("\nERROR:", error)



print("=" * 65)
print("CONTRACT PRIVACY AI AGENT - AI ANALYSIS TEST")
print("=" * 65)

try:

    # STEP 1: Read the contract.
    print("\nStep 1: Reading contract...")

    sections = read_contract(contract_path)

    print("Contract successfully read.")

    # STEP 2: Identify privacy clauses.
    print("\nStep 2: Identifying privacy clauses...")

    clauses = extract_privacy_clauses(sections)

    print("Privacy clauses identified:", len(clauses))

    # STEP 3: Analyze clauses using Ollama.
    print("\nStep 3: Analyzing clauses using Ollama...")

    analyses = analyze_privacy_clauses(clauses)

    # STEP 4: Display the AI findings.
    print("\n" + "=" * 65)
    print("AI PRIVACY ANALYSIS RESULTS")
    print("=" * 65)

    for result in analyses:

        print("\nClause:", result["clause_number"])
        print("Heading:", result["heading"])

        print("\nOriginal contract wording:")
        print(result["original_text"])

        print("\nAI explanation:")
        print(result["clause_summary"])

        print("\nPotential risks:")

        if result["potential_risks"]:

            for risk in result["potential_risks"]:

                print("-", risk["risk"])
                print("  Reason:", risk["reason"])
                print("  Severity:", risk["severity"])

        else:
            print("No potential risks identified.")

        print("\nMissing or unclear information:")

        for item in result["missing_or_unclear_information"]:
            print("-", item)

        print("\nQuestions for lawyer:")

        for question in result["questions_for_lawyer"]:
            print("-", question)

        print("\nPreliminary observation:")
        print(result["preliminary_observation"])

        print("-" * 65)

    print("\nAI ANALYSIS TEST COMPLETED")

except Exception as error:

    print("\nERROR DURING ANALYSIS:")
    print(type(error).__name__, "-", error)

print("=" * 60)
print("CALIFORNIA PRIVACY LAW DATABASE TEST")
print("=" * 60)

try:

    # Test 1: Validate the database structure.
    print("\n1. Validating legal rules...")

    validate_rules()

    print("[OK] Legal rules are properly structured.")

    # Test 2: Retrieve applicable rules.
    print("\n2. Retrieving service provider requirements...")

    rules = get_applicable_rules(
        "service_provider_or_contractor"
    )

    print("[OK] Rules retrieved:", len(rules))

    # Test 3: Display the legal framework.
    print("\n3. Legal framework:")

    print("Law:", LEGAL_FRAMEWORK["name"])
    print("Primary statute:", LEGAL_FRAMEWORK["primary_statute"])
    print("Primary regulation:", LEGAL_FRAMEWORK["primary_regulation"])
    print("Regulatory version:", LEGAL_FRAMEWORK["regulation_version"])

    # Test 4: Display individual requirements.
    print("\n4. Available contractual requirements:")

    for rule in rules:

        print("\nRule ID:", rule["rule_id"])
        print("Title:", rule["title"])
        print("Authority:", rule["authority"])
        print("Requirement:", rule["requirement"])

    # Test 5: Retrieve one specific rule.
    print("\n5. Testing individual rule retrieval...")

    selected_rule = get_rule_by_id("CA-7051-03")

    if selected_rule:

        print("[OK] Rule found:", selected_rule["title"])

    else:

        print("[ERROR] Rule was not found.")

    # Test 6: Display due diligence note.
    print("\n6. Additional review consideration:")

    print("Authority:", DUE_DILIGENCE_NOTE["authority"])
    print("Explanation:", DUE_DILIGENCE_NOTE["explanation"])

    print("\n" + "=" * 60)
    print("LEGAL RULES DATABASE TEST COMPLETED")
    print("=" * 60)

except Exception as error:

    print("\nERROR:", type(error).__name__, "-", error)

print("\n" + "=" * 60)
print("\n" + "=" * 60)
print("STEP 6: COMPLIANCE ENGINE TEST")

# 1. Read the sample contract.
#contract = read_contract("Capstone/sample_vendor_agreement.txt")

contract = read_contract(contract_path)

# 2. Extract privacy-related clauses.
clauses = extract_privacy_clauses(contract)

print("\nExtracted clauses:", len(clauses))

# 3. Identify the vendor's role.
# This is a manually supplied assumption for this test.
contract_role = "service_provider_or_contractor"

# 4. Compare the clauses with the legal requirements.
report = review_contract(
    clauses,
    contract_role
)

# 5. Display the preliminary review.
print_compliance_report(report)