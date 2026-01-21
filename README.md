# Internship_Task_4_Backend-Project-2-Debugging-
#  Flask Notes Application – Bug Fix & Refactor

##  Project Overview
This project focuses on debugging and refactoring a broken Flask-based Notes application. The original application contained multiple functional and structural bugs that prevented users from adding notes correctly.

The objective was to identify the bugs, fix them systematically, and document the resolution process in a professional manner. The application now allows users to add notes through a text field and displays them dynamically as an unordered list on the same page.

A detailed PDF report documenting all bugs and fixes is included in this repository.

---

##  Features
- ✔️ Add notes using a text input field
- ✔️ Display notes dynamically on the same page
- ✔️ Prevent empty note submissions with validation
- ✔️ Clean Flask project structure using templates
- ✔️ Separate backend logic and frontend UI
- ✔️ Port isolation to avoid conflicts with other apps
- ✔️ Bug documentation included in PDF format

---

##  Technologies Used
- Python
- Flask
- HTML (Jinja Templates)
- Jupyter Notebook
- ReportLab (PDF generation)

---

##  Project Structure
Task_3/
│
├── app.py
├── templates/
│ └── home.html
└── Task3_Bug_Report.pdf


---

##  Bugs Identified & Fixes

### Bug 1 – Form did not send POST request
- **Issue:** HTML form was missing `method="POST"`, so data was never sent correctly.
- **Fix:** Added `method="POST"` to the form tag.

### Bug 2 – Button type not defined
- **Issue:** Button did not explicitly specify submit type.
- **Fix:** Added `type="submit"` to ensure consistent behavior.

### Bug 3 – No validation for empty input
- **Issue:** Empty notes could be submitted without feedback.
- **Fix:** Added backend validation and UI warning message.

### Bug 4 – Template folder structure missing
- **Issue:** Flask could not locate HTML file when not placed inside `templates` folder.
- **Fix:** Created proper `templates` directory and moved HTML file.

### Bug 5 – Port conflict with other Flask apps
- **Issue:** Multiple apps were running on the same port.
- **Fix:** Changed the port number to avoid conflicts.

All bugs and fixes are documented in the PDF report.

---

##  How to Run the Project

### Step 1 – Install Flask

Run in terminal or Jupyter:
pip install flask


---

### Step 2 – Navigate to Project Folder



cd Task_3


---

### Step 3 – Run Application



python app.py


---

### Step 4 – Open in Browser



http://127.0.0.1:5002/


---

##  How to Use

1. Enter a note in the text field.
2. Click **Add Note**.
3. The note will appear in the list below.
4. Empty inputs will show a warning message.

---

##  Documentation

The repository includes a detailed PDF report:
- Bug descriptions
- Root causes
- Fix approaches
- Final outcome summary

File:
file:///C:/Users/lakshmilokeswari/Downloads/Task3_Bug_Report.pdf



---

##  Learning Outcomes
- Flask routing and form handling
- Debugging real-world issues
- Template rendering using Jinja
- Input validation
- Project structuring
- Technical documentation

---

#  Author
**Bathula Venu Gopal**  
Data Science Intern – Innomatics Research Labs  
Batch 419
