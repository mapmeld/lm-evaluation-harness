from typing import List


qed = "∎"  # from math symbols


def doc_to_text_context(doc) -> str:
    sequence = doc["sequence"]
    return f"""Is the following an alternative polyadenylation site?

### Sequence:
{sequence}

### Answer:\n"""


def doc_to_biotoken_context(doc) -> str:
    sequence = "".join([f"{qed}{nt}" for nt in doc["sequence"]])
    return f"""Is the following an alternative polyadenylation site?

### Sequence:
{sequence}

### Answer:\n"""


def doc_to_choice(doc) -> List[str]:
    return ["No", "Yes"]
