## 🚀 How to Run This Project Locally

### 1. Clone the Repository

Clone the repository to your system:

```
git clone https://github.com/<your-username>/SK.git
```

Move into the project folder:

```
cd SK
```

---

### 2. Create a Virtual Environment

Create a Python virtual environment:

```
python -m venv .skResume
```

Activate it:

**Windows**

```
.skResume\Scripts\activate
```

**Mac/Linux**

```
source .skResume/bin/activate
```

---

### 3. Install Dependencies

Install required packages:

```
pip install -r requirements.txt
```

---

### 4. Create Environment Variables

Create a `.env` file in the project root and add:

```
NVIDIA_API_KEY=your_api_key_here
MODEL_NAME=moonshotai/kimi-k2-instruct
BASE_URL=https://integrate.api.nvidia.com/v1
```

---

### 5. Start the Backend Server

Run the FastAPI server:

```
uvicorn app.main:app --reload
```

---

### 6. Test the API

Open the API documentation in your browser:

```
http://127.0.0.1:8000/docs
```

Upload a resume to test the ATS scoring endpoint.
