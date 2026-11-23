"""
California Privacy Law Requirements Database

Initial scope:
CCPA/CPRA service provider and contractor agreements.

Primary authorities:
- California Civil Code section 1798.100(d)
- 11 CCR section 7050
- 11 CCR section 7051

Regulatory version reviewed:
Effective January 1, 2026.

"""

LEGAL_FRAMEWORK = {
    "name": "California Consumer Privacy Act",
    "short_name": "CCPA/CPRA",
    "contract_role": "service_provider_or_contractor",
    "regulation_version": "Effective January 1, 2026",
    "primary_statute": "California Civil Code section 1798.100(d)",
    "primary_regulation": "11 CCR section 7051",
    "official_source": (
        "https://cppa.ca.gov/regulations/pdf/"
        "ccpa_statute_eff_20260101.pdf"
    )
}


SERVICE_PROVIDER_RULES = [

    {
        "rule_id": "CA-7051-01",
        "title": "Prohibition on sale and sharing",
        "authority": "11 CCR section 7051(a)(1)",
        "requirement": (
            "The contract must prohibit the service provider or "
            "contractor from selling or sharing personal information "
            "collected under the written contract."
        ),
        "review_questions": [
            "Does the contract prohibit the vendor from selling personal information?",
            "Does it prohibit the vendor from sharing personal information?",
            "Are there provisions that appear to authorize sale or sharing?"
        ],
        "categories": [
            "Sale and sharing",
            "Use restrictions"
        ],
        "keywords": [
            "sell",
            "sale",
            "share",
            "sharing",
            "personal information"
        ]
    },

    {
        "rule_id": "CA-7051-02",
        "title": "Specific business purposes",
        "authority": "11 CCR section 7051(a)(2)",
        "requirement": (
            "The contract must identify the specific business "
            "purposes for which the vendor processes personal "
            "information. Generic descriptions, including a "
            "reference to the entire contract, are insufficient."
        ),
        "review_questions": [
            "Does the contract identify the specific processing purposes?",
            "Are the purposes described with sufficient detail?",
            "Does the contract rely only on a generic reference to the services or agreement?"
        ],
        "categories": [
            "Processing purposes",
            "Personal information"
        ],
        "keywords": [
            "business purpose",
            "services",
            "processing",
            "purpose"
        ]
    },

    {
        "rule_id": "CA-7051-03",
        "title": "Restriction on use, retention and disclosure",
        "authority": "11 CCR section 7051(a)(3)",
        "requirement": (
            "The contract must prohibit the vendor from retaining, "
            "using or disclosing personal information for purposes "
            "other than the specified business purposes or purposes "
            "otherwise permitted by the CCPA and its regulations."
        ),
        "review_questions": [
            "Does the contract restrict use to the specified business purposes?",
            "Does it restrict retention outside those purposes?",
            "Does it restrict disclosure outside those purposes?",
            "Are permitted legal exceptions appropriately recognized?"
        ],
        "categories": [
            "Use restrictions",
            "Data retention and deletion",
            "Processing purposes"
        ],
        "keywords": [
            "retain",
            "retention",
            "use",
            "disclose",
            "disclosure",
            "business purpose"
        ]
    },

    {
        "rule_id": "CA-7051-04",
        "title": "Restriction outside the direct business relationship",
        "authority": "11 CCR section 7051(a)(4)",
        "requirement": (
            "The contract must prohibit the vendor from retaining, "
            "using or disclosing personal information outside the "
            "direct business relationship between the vendor and "
            "the business, unless expressly permitted by the CCPA "
            "or its regulations."
        ),
        "review_questions": [
            "Does the contract restrict use outside the direct business relationship?",
            "Does it address combining information obtained from other sources?",
            "Does it recognize exceptions permitted by the CCPA and regulations?"
        ],
        "categories": [
            "Use restrictions",
            "Data sharing",
            "Personal information"
        ],
        "keywords": [
            "direct business relationship",
            "combine",
            "other sources",
            "independent use"
        ]
    },

    {
        "rule_id": "CA-7051-05",
        "title": "Compliance with applicable CCPA obligations",
        "authority": "11 CCR section 7051(a)(5)",
        "requirement": (
            "The contract must require the vendor to comply with "
            "applicable CCPA provisions and provide the same level "
            "of privacy protection required of businesses under "
            "the CCPA and its regulations."
        ),
        "review_questions": [
            "Does the vendor undertake to comply with applicable CCPA requirements?",
            "Does the agreement require an appropriate level of privacy protection?",
            "Does it address relevant consumer-request assistance?",
            "Does it address applicable security obligations?",
            "Does it address audit, risk assessment or ADMT assistance where relevant?"
        ],
        "categories": [
            "Consumer privacy rights",
            "Information security",
            "Audits and compliance"
        ],
        "keywords": [
            "CCPA",
            "privacy protection",
            "consumer request",
            "security",
            "risk assessment",
            "audit"
        ]
    },

    {
        "rule_id": "CA-7051-06",
        "title": "Business monitoring and verification rights",
        "authority": "11 CCR section 7051(a)(6)",
        "requirement": (
            "The contract must grant the business the right to take "
            "reasonable and appropriate steps to ensure that the "
            "vendor uses personal information consistently with "
            "the business's CCPA obligations."
        ),
        "review_questions": [
            "Does the business have a contractual right to monitor vendor compliance?",
            "Can the business conduct reviews or assessments?",
            "Does the contract provide appropriate audit or testing rights?"
        ],
        "categories": [
            "Audits and compliance",
            "Information security"
        ],
        "keywords": [
            "audit",
            "monitor",
            "assessment",
            "testing",
            "compliance"
        ]
    },

    {
        "rule_id": "CA-7051-07",
        "title": "Notice of inability to comply",
        "authority": "11 CCR section 7051(a)(7)",
        "requirement": (
            "The contract must require the vendor to notify the "
            "business after determining that it can no longer "
            "meet its obligations under the CCPA and regulations."
        ),
        "review_questions": [
            "Must the vendor notify the business if it can no longer comply?",
            "Does the contract identify the circumstances requiring notice?",
            "Is the notification obligation sufficiently clear?"
        ],
        "categories": [
            "Audits and compliance",
            "Contractual notification"
        ],
        "keywords": [
            "notify",
            "notification",
            "unable to comply",
            "cannot comply"
        ]
    },

    {
        "rule_id": "CA-7051-08",
        "title": "Rights to stop and remediate unauthorized use",
        "authority": "11 CCR section 7051(a)(8)",
        "requirement": (
            "The contract must grant the business the right, upon "
            "notice, to take reasonable and appropriate steps to "
            "stop and remediate unauthorized use of personal information."
        ),
        "review_questions": [
            "Can the business require the vendor to stop unauthorized use?",
            "Can the business require appropriate remediation?",
            "Does the agreement provide a workable process for exercising these rights?"
        ],
        "categories": [
            "Use restrictions",
            "Audits and compliance",
            "Information security"
        ],
        "keywords": [
            "unauthorized use",
            "remediate",
            "remediation",
            "stop",
            "corrective action"
        ]
    },

    {
        "rule_id": "CA-7051-09",
        "title": "Assistance with consumer privacy requests",
        "authority": "11 CCR section 7051(a)(9)",
        "requirement": (
            "The contract must require the vendor to enable the "
            "business to comply with CCPA consumer requests, or "
            "require the business to inform the vendor of requests "
            "that the vendor must comply with and provide necessary "
            "information."
        ),
        "review_questions": [
            "Does the vendor assist with consumer privacy requests?",
            "Does the contract address deletion requests?",
            "Does it address correction and access requests where relevant?",
            "Does it establish a process for exchanging necessary information?"
        ],
        "categories": [
            "Consumer privacy rights",
            "Data retention and deletion"
        ],
        "keywords": [
            "consumer request",
            "deletion request",
            "access request",
            "correction request",
            "consumer rights"
        ]
    },

    {
        "rule_id": "CA-7051-10",
        "title": "Subcontractor contractual protections",
        "authority": "11 CCR section 7051(b)",
        "requirement": (
            "A service provider or contractor that subcontracts "
            "with another person to provide services to the business "
            "must have a subcontract with that person that complies "
            "with the CCPA and regulations, including section 7051(a)."
        ),
        "review_questions": [
            "Does the agreement permit subcontracting?",
            "Does it require appropriate privacy obligations in subcontractor agreements?",
            "Does it address the vendor's responsibility for subcontractor compliance?"
        ],
        "categories": [
            "Subcontractors",
            "Information security",
            "Use restrictions"
        ],
        "keywords": [
            "subcontractor",
            "subcontract",
            "subprocessor",
            "third party"
        ]
    }
]


DUE_DILIGENCE_NOTE = {
    "authority": "11 CCR section 7051(c)",
    "title": "Business due diligence",
    "explanation": (
        "Whether the business conducts due diligence on its "
        "service providers and contractors is relevant to whether "
        "it has reason to believe that a vendor is using personal "
        "information in violation of the CCPA. This is a review "
        "consideration, not a separate mandatory contract clause."
    )
}


def get_applicable_rules(contract_role):
    """
    Return the rules applicable to the identified vendor role.
    """

    if contract_role == "service_provider_or_contractor":
        return SERVICE_PROVIDER_RULES

    if contract_role == "third_party":
        raise NotImplementedError(
            "Third-party rules under 11 CCR section 7053 "
            "will be added in a later development stage."
        )

    raise ValueError(
        "Unknown contract role. Identify whether the vendor "
        "is a service provider, contractor or third party."
    )


def get_rule_by_id(rule_id):
    """
    Retrieve one legal requirement using its unique ID.
    """

    for rule in SERVICE_PROVIDER_RULES:

        if rule["rule_id"] == rule_id:
            return rule

    return None


def validate_rules():
    """
    Check that every legal rule has the required information.
    """

    required_fields = [
        "rule_id",
        "title",
        "authority",
        "requirement",
        "review_questions",
        "categories",
        "keywords"
    ]

    for rule in SERVICE_PROVIDER_RULES:

        for field in required_fields:

            if field not in rule:
                raise ValueError(
                    f"{rule.get('rule_id', 'Unknown rule')} "
                    f"is missing {field}"
                )

    return True