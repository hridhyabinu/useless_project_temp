<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



# [Project Name] 🎯


## Basic Details
### Team Name: [Name]


### Team Members
- Team Lead: [Hridhya Binu] - [Viswajyothi College of Engineering and Technology]


### Project Description
[the mukham mokkum entram is actucally a useless project that was completely generated from a stupid way for thinking i have tried to make an intro video for this project but due to PC limitation i was not able to run the result as i expected hope that the ]

### The Problem (that doesn't exist)
In a world where humans have been looking in mirrors and seeing faces for thousands of years, there has been a tragic, catastrophic lack of software explicitly confirming that your face indeed contains eyes, a nose, and a mouth in Malayalam.

### The Solution (that nobody asked for)
An AI-powered computer vision engine that processes image uploads, extracts MediaPipe 3D face mesh landmarks, and produces a highly dramatic breakdown of your facial components—complete with an auto-playing retro intro video splash modal.

## Technical Details
### Technologies/Components Used
For Software:
- **Languages:** Python, HTML5, JavaScript, CSS3
- **Frameworks & Libraries:** FastAPI, OpenCV (`opencv-python`), MediaPipe Face Mesh, NumPy, Uvicorn
- **Styling & UI:** Tailwind CSS (via CDN), Google Fonts (`Cormorant Garamond` & `JetBrains Mono`)
- **Deployment & Hosting:** GitHub Pages (Frontend), Hugging Face Spaces / Render (Backend API)

For Hardware:
- *None (Software only)*

---

### Implementation

#### Installation
1. Clone the repository:
   git clone [https://github.com/hridhyabinu/useless_project_temp.git](https://github.com/hridhyabinu/useless_project_temp.git)
   cd useless_project_temp
   pip install fastapi uvicorn opencv-python mediapipe numpy

# Run
[]https://hridhyabinu.github.io/useless_project_temp/
python main.py

### Project Documentation
For Software:

Screenshots 

screenshot 1
<img width="1010" height="474" alt="WhatsApp Image 2026-09-06 at 10 39 39 (2)" src="https://github.com/user-attachments/assets/22569e52-503d-4090-8399-0f432fd95430" />
*this is the home screen

screenshot 2
<img width="978" height="451" alt="WhatsApp Image 2026-09-06 at 10 39 39 (1)" src="https://github.com/user-attachments/assets/b0f6d4fe-fa35-4e22-8a4d-bb2449a21393" />
*the user will be able to upload their pic. this is the 2nd frame

screenshot 3
<img width="978" height="451" alt="WhatsApp Image 2026-09-06 at 10 39 39 (1)" src="https://github.com/user-attachments/assets/1da0ef23-31f7-4b5c-b2b3-2e521693a641" />

*this is 3rd frame. this frames shows the results i.e, the number of faces, the number of eyes, nose, lips and mouth

# Diagrams
+-------------------+        +----------------------+        +-----------------------+
|  User Image Input |  --->  | FastAPI /analyze API |  --->  |  MediaPipe Face Mesh  |
+-------------------+        +----------------------+        +-----------------------+
                                                                         |
+------------------------------------------------------------------------+
|
v
+-----------------------+        +----------------------+        +-----------------------+
| Landmark Matrix Math  |  --->  | JSON Count Response  |  --->  | Malayalam Tally Display|
+-----------------------+        +----------------------+        +-----------------------+
*Workflow Explanation:*
1. **User Input:** The frontend interface captures a user-uploaded image via the HTML5 canvas stage.
2. **API Request:** The image is sent as a `multipart/form-data` payload to the FastAPI `/analyze` endpoint via HTTP POST.
3. **Landmark Extraction:** The backend decodes the binary stream using OpenCV (`cv2.imdecode`) and passes the RGB image to MediaPipe's 3D Face Mesh model.
4. **Anatomical Calculation:** MediaPipe detects facial landmark meshes. The API counts detected face instances and calculates the feature tallies (eyes, noses, mouths, lips) mathematically.
5. **JSON Response:** A JSON object containing the feature breakdown counts and status message is returned to the client.
6. **Malayalam Tally Display:** The frontend dynamically updates the UI cards with the calculated metrics and their Malayalam labels (*Mukha Ennam*, *Kannugal*, *Mooku*, etc.).

### Project Demo
# Video
https://drive.google.com/file/d/1FQLe7fDOhCagN0_ZUSvksZ-2gmFqWriF/view?usp=sharing

# Additional Demos
[]
https://hridhyabinu.github.io/useless_project_temp/

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



