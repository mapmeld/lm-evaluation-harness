qed = "∎"  # from math symbols


def doc_to_target(doc) -> str:
    return ["No", "Yes"][doc["label"]]


def doc_to_text_context(doc) -> str:
    sequence = doc["sequence"]
    return f"""Is the following sequence long non-coding RNA (LncRNA)?

### Sequence:
{sequence}

### Answer:\n"""


def doc_to_biotoken_context(doc) -> str:
    sequence = "".join([f"{qed}{nt}" for nt in doc["sequence"]])
    return f"""Is the following sequence long non-coding RNA (LncRNA)?

### Sequence:
{sequence}

### Answer:\n"""
