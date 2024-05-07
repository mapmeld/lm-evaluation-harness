from typing import List

def doc_to_text_context(doc) -> str:
    sequence = doc["sequence"]
    return f"""Is the following sequence long non-coding RNA (LncRNA)?

### Sequence:
{sequence}

### Answer:\n"""


def doc_to_choice(doc) -> List[str]:
    return ["No", "Yes"]
