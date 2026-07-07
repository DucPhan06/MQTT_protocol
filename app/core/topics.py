def normalize_topic(raw_name: str) -> str:
    return raw_name.strip().lower().replace(" ", "_")