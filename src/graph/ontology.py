from typing import List

# Define Node Labels
class NodeLabel:
    ANATOMY = "Anatomy"
    CONDITION = "Condition"
    SYMPTOM = "Symptom"
    PROCEDURE = "Procedure"
    MEDICATION = "Medication"
    COMPLICATION = "Complication"
    DIAGNOSTIC = "Diagnostic"  # e.g., MRI, X-Ray

# Define Relationship Types
class RelationType:
    AFFECTS = "AFFECTS"          # Condition -> Anatomy
    CAUSES = "CAUSES"            # Condition -> Symptom
    TREATED_BY = "TREATED_BY"    # Condition -> Procedure
    TREATED_WITH = "TREATED_WITH"# Condition -> Medication
    INVOLVES = "INVOLVES"        # Procedure -> Anatomy
    HAS_RISK = "HAS_RISK"        # Procedure -> Complication
    DIAGNOSED_BY = "DIAGNOSED_BY" # Condition -> Diagnostic

# Lists for LLM extraction
ORTHOPEDIC_ENTITIES = [
    NodeLabel.ANATOMY,
    NodeLabel.CONDITION,
    NodeLabel.SYMPTOM,
    NodeLabel.PROCEDURE,
    NodeLabel.MEDICATION,
    NodeLabel.COMPLICATION,
    NodeLabel.DIAGNOSTIC,
]

ORTHOPEDIC_RELATIONS = [
    RelationType.AFFECTS,
    RelationType.CAUSES,
    RelationType.TREATED_BY,
    RelationType.TREATED_WITH,
    RelationType.INVOLVES,
    RelationType.HAS_RISK,
    RelationType.DIAGNOSED_BY,
]

# Schema definition for LlamaIndex / Neo4j
SCHEMA_CONFIG = {
    "entities": ORTHOPEDIC_ENTITIES,
    "relations": ORTHOPEDIC_RELATIONS
}
