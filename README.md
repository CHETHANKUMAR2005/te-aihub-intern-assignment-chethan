# te-aihub-intern-assignment-chethan
Docker + Label Studio object detection annotation workflow using the BCCD blood cell dataset for RBC, WBC, and Platelets detection.

---
## 1. Project overview

  
The goal is to run **Label Studio** locally using Docker, create an **object detection** project for blood cell images, annotate cells with bounding boxes, and export the annotations in a reusable format for future model training.

In simple words: this project sets up a small local tool where humans draw boxes around red blood cells (RBC), white blood cells (WBC), and platelets in microscope images so that these examples can later be used to train an AI model. 
---

## 2. Dataset

- **Dataset name:** BCCD – Blood Cell Count and Detection dataset  
- **Dataset sources:**
  - Roboflow: https://public.roboflow.com/object-detection/bccd
  - GitHub: https://github.com/Shenggan/BCCD_Dataset 
- Images used in this assignment:
  - I selected **10 images** from the BCCD dataset, for example:  
    `BloodImage_00400.jpg`, `BloodImage_00402-3.jpg`, `BloodImage_00403-5.jpg`, `BloodImage_00404-7.jpg`, `BloodImage_00405-9.jpg`, `BloodImage_00407-11.jpg`, `BloodImage_00408-13.jpg`, `BloodImage_00409-15.jpg`, `BloodImage_00410-17.jpg`, `<one more image name>`.
- **Location in this repository:**
  - `samples/selected_10_images/` – contains the 10 images used for labeling (or instructions to download them).

The images show microscope views of human blood with multiple RBCs, WBCs, and platelets in each frame, which makes them suitable for bounding‑box object detection tasks.

---

## 3. Environment and Docker command

- **OS:** `<Windows 10 / Windows 11 / Ubuntu / etc.>`  
- **Docker:** Docker Desktop `<version>` (or latest)  

To start Label Studio with Docker, I used the following command:

```bash
docker run -it -p 8080:8080 -v ${PWD}/mydata:/label-studio/data heartexlabs/label-studio:latest
```

- `-p 8080:8080` exposes Label Studio at `http://localhost:8080`.  
- `-v ${PWD}/mydata:/label-studio/data` stores all labels and projects in a local `mydata` folder so they persist even if the container stops.

You can adapt the volume path syntax if you are using CMD or Linux instead of PowerShell.

---

## 4. Label Studio project setup

### 4.1 Creating the project

1. Start Docker and run the command above.  
2. Open a browser and go to `http://localhost:8080`.  
3. Sign up or log in to Label Studio. [web:48]  
4. Click **Create Project** and set:
   - **Project name:** `BCCD Annotation Assignment`  
   - Optional description: “Object detection annotations for RBC, WBC, Platelets using BCCD dataset.”
5. Import the 10 selected images from `samples/selected_10_images/`.

### 4.2 Label configuration (labeling interface)

For this assignment, only **three classes** are required: `RBC`, `WBC`, and `Platelets`. 

The labeling interface XML used in this project:

```xml
<View>
  <Image name="image" value="$image"/>
  <RectangleLabels name="label" toName="image">
    <Label value="RBC"/>
    <Label value="WBC"/>
    <Label value="Platelets"/>
  </RectangleLabels>
</View>
```

- `Image` displays the current image.  
- `RectangleLabels` allows drawing bounding boxes.  
- Each `Label` corresponds to one blood cell type. 

This configuration is saved in the repository as:

- `label_config.xml`

---

## 5. Annotation details

- **Total images in project:** 10  
- **Images annotated:** `<at least 5, for example: 7>` 
- **Labeling rules used:**
  - `RBC`: light pink, donut-shaped cells.  
  - `WBC`: larger purple cells with darker nucleus shapes.  
  - `Platelets`: small purple dots noticeably smaller than RBCs.

For each annotated image:

1. Open the image in Label Studio.  
2. Use the rectangle tool to draw a **tight bounding box** around each visible cell.  
3. Choose the correct label (RBC, WBC, Platelets) from the right panel.  

Screenshots saved in `screenshots/`:

- `docker_running.png` – Docker container running Label Studio.  
- `label_studio_project.png` – project view with imported tasks.  
- `annotated_example.png` – one example image with labeled bounding boxes.

---

## 6. Exported annotations

After finishing annotation:

1. In Label Studio, open the project.  
2. Go to **Export**.  
3. Choose **Label Studio JSON** format and download the export. 

The exported file is stored in:

- `exports/"C:\Users\Chethan Kumar M\Downloads\label_studio_export.json.json"

Optional bonus (if implemented):

- `exports/coco_or_yolo_export_optional/` – converted annotations in COCO or YOLO format for use with common detection frameworks.

---

## 7. How to reproduce this project

1. **Clone the repository**

   ```bash
   git clone <your_repo_clone_url>
   cd te-aihub-intern-assignment-chethan
   ```

2. **Start Label Studio with Docker**

   ```bash
   docker run -it -p 8080:8080 -v ${PWD}/mydata:/label-studio/data heartexlabs/label-studio:latest
   ```

3. **Open Label Studio**

   - Visit `http://localhost:8080` in your browser and log in.

4. **Create a new project**

   - Name: `BCCD Annotation Assignment`  
   - Import the 10 images from `samples/selected_10_images/` (or follow `samples/selected_10_images_or_download_instructions.txt` if images are not included).

5. **Configure labels**

   - Open **Settings → Labeling Interface**.  
   - Paste the contents of `label_config.xml`.  
   - Save.

6. **Annotate**

   - Open tasks, draw bounding boxes, and label cells as `RBC`, `WBC`, or `Platelets`.

7. **Export annotations**

   - Use the Export button to create a JSON export and place it in `exports/label_studio_export.json`.

---

## 8. Demo video

- **Google Drive link:** `<paste your 3-minute video link here>`

The video demonstrates:

- Docker container running Label Studio.  
- The `BCCD Annotation Assignment` project in the UI.  
- Configured labels (RBC, WBC, Platelets).  
- An example annotated image.  
- The location of the export file in this repository.

---

## 9. Issues faced and solutions

- **Issue 1: Docker image download or startup errors**  
  - *Fix:* Ensured Docker Desktop was running, pulled the `heartexlabs/label-studio:latest` image again, and verified that port 8080 was free.

- **Issue 2: Images not appearing in Label Studio tasks**  
  - *Fix:* Confirmed that only `.jpg` files were imported, not `.xml` files, and refreshed the project after upload. 

- **Issue 3: Confusion about label configuration**  
  - *Fix:* Used the Label Studio documentation and assignment instructions to define exactly three `RectangleLabels`: RBC, WBC, Platelets.

(You can edit these issues to match your real experience.)

---

## 10. AI tools used

During this assignment, I used AI tools for assistance:

- ChatGPT / Gemini / Perplexity/claude_ai for:
  - Clarifying Docker run commands for Label Studio.  
  - Designing the `label_config.xml` for bounding boxes.  
  - Drafting and structuring this README in clear language.

I reviewed all suggestions and ensured that I understand every command and configuration before including them in the final project.

---

## 11. Annotation quality plan for 2,500 images

If this project were scaled up to **2,500 images** annotated by business users, I would ensure quality using the following process:

1. **Clear written guidelines**  
   - Provide a short document with visual examples of RBC, WBC, and Platelets, including tricky cases (overlapping cells, tiny platelets, partially visible cells at the image border).

2. **Onboarding and practice set**  
   - Give new annotators a small practice batch (e.g., 20 images).  
   - Review their annotations, give feedback, and only then let them work on the full dataset.

3. **Double-annotation on a subset**  
   - Have some images labeled by two different annotators.  
   - Use disagreement reports to identify confusing cases and refine the guidelines.

4. **Regular spot checks**  
   - Periodically review a random sample of completed images to ensure consistency in box tightness and label choice.

5. **Feedback loop and updates**  
   - Update the guidelines when recurring mistakes are found.  
   - Communicate changes clearly to all annotators to keep quality consistent over time.

---


