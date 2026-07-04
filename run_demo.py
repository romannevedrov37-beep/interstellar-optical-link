from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
DOCS_DIR = PROJECT_ROOT / "docs"

required_docs = [
    "project_scope.md",
    "literature_notes.md",
    "bibliography.bib",
    "model_assumptions.md",
]

print("Checking project documentation files:\n")

for filename in required_docs:
    path = DOCS_DIR / filename

    if path.exists():
        print(f"[OK] {path}")
    else:
        print(f"[MISSING] {path}")
        
