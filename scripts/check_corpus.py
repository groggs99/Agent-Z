"""Check whether the processed corpus has basic coverage for IronBridge v0."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

CORPUS_FILE = Path("data/processed/corpus_chunks.jsonl")
REQUIRED_TERMS = [
    "ironclaw",
    "near",
    "intents",
    "zcash",
    "zcg",
    "grant",
    "governance",
    "privacy",
]


def main() -> None:
    if not CORPUS_FILE.exists():
        print("No processed corpus found. Run: python scripts/build_corpus.py")
        return

    records = []
    text_blob_parts = []
    with CORPUS_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            record = json.loads(line)
            records.append(record)
            text_blob_parts.append(record.get("text", ""))

    ecosystem_counts = Counter(record.get("ecosystem", "unknown") for record in records)
    text_blob = "\n".join(text_blob_parts).lower()

    print(f"Chunks: {len(records)}")
    print("Ecosystem coverage:")
    for ecosystem, count in ecosystem_counts.most_common():
        print(f"- {ecosystem}: {count}")

    print("\nRequired term coverage:")
    for term in REQUIRED_TERMS:
        status = "OK" if term in text_blob else "MISSING"
        print(f"- {term}: {status}")


if __name__ == "__main__":
    main()
