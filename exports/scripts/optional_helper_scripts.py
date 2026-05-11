Steps Taken to run this project with download links
## Steps Taken to Run This Project

1. Installed Docker Desktop on Windows.  
   Link: [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

2. Read the Label Studio installation guide.  
   Link: [Label Studio Install Guide](https://labelstud.io/guide/install.html)

3. Pulled the Label Studio Docker image.

```bash
docker pull heartexlabs/label-studio:latest
```

4. Ran Label Studio using Docker.

```bash
docker run -it -p 8080:8080 -v ${PWD}/mydata:/label-studio/data heartexlabs/label-studio:latest label-studio --log-level DEBUG
```

5. Opened Label Studio in the browser at:  
   [http://localhost:8080](http://localhost:8080)

6. Downloaded the BCCD dataset from the given links.  
   - [BCCD Dataset on Roboflow](https://public.roboflow.com/object-detection/bccd)  
   - [BCCD Dataset on GitHub](https://github.com/Shenggan/BCCD_Dataset)

7. Selected 10 JPG images from the dataset and used them for annotation.

8. Created a Label Studio project named **BCCD Annotation Assignment**.

9. Added 3 labels: **RBC**, **WBC**, and **Platelets**.

10. Imported the 10 images into the project and annotated at least 5 images.

11. Exported the annotations as a JSON file from Label Studio.

12. Uploaded the required files to GitHub, including README, label config, screenshots, and export file.







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



