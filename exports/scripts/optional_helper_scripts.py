Check that export file exists and is not empty

# scripts/optional_helper_scripts.py

import json
from pathlib import Path

EXPORT_PATH = Path("exports/label_studio_export.json")

def validate_export():
    if not EXPORT_PATH.exists():
        print(f"[ERROR] Export file not found: {EXPORT_PATH}")
        return

    try:
        data = json.loads(EXPORT_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("[ERROR] Export file is not valid JSON.")
        return

    if not data:
        print("[ERROR] Export file is empty (no tasks).")
        return

    # Label Studio JSON is usually a list of tasks with 'annotations'
    num_tasks = len(data)
    num_with_annotations = sum(1 for task in data if task.get("annotations"))

    print(f"[OK] Found {num_tasks} tasks.")
    print(f"[OK] {num_with_annotations} tasks contain annotations.")

    if num_with_annotations == 0:
        print("[WARNING] No annotations found. Did you export after labeling?")
    else:
        print("[SUCCESS] Export file looks valid.")

if __name__ == "__main__":
    validate_export()


 script to list label counts

# scripts/optional_helper_scripts.py

import json
from collections import Counter
from pathlib import Path

EXPORT_PATH = Path("exports/label_studio_export.json")

def count_labels():
    if not EXPORT_PATH.exists():
        print(f"[ERROR] Export file not found: {EXPORT_PATH}")
        return

    data = json.loads(EXPORT_PATH.read_text(encoding="utf-8"))
    counts = Counter()

    for task in data:
        for ann in task.get("annotations", []):
            for result in ann.get("result", []):
                # Label Studio object detection results usually store labels under "rectanglelabels"
                value = result.get("value", {})
                labels = value.get("rectanglelabels") or []
                for label in labels:
                    counts[label] += 1

    print("Label counts in export:")
    for label, n in counts.items():
        print(f"  {label}: {n}")

if __name__ == "__main__":
    count_labels()



