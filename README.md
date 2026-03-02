# 🚀 IntelliHire-AI
### AI-Powered Resume Analyzer & Interview Assistant

IntelliHire-AI is an end-to-end AI application that analyzes resumes against job descriptions and generates intelligent interview answers using Natural Language Processing (NLP) and zephyr-7b-beta Large Language Models (LLM) via Hugging Face Infernce API.
This project demonstrates practical implementation of machine learning concepts, LLM API integration, and full-stack AI application development.

# 📌 Project Objective
The goal of this project is to simulate how modern Applicant Tracking Systems (ATS) evaluate resumes and assist candidates in preparing for interviews using AI-powered feedback and answer generation.

# 🧠 Core Technologies Used
* **Python** – Core programming language
* **Streamlit** – Web application framework
* **Natural Language Processing (NLP)** – Text vectorization & similarity
* **TF-IDF (Term Frequency–Inverse Document Frequency)** – Text representation technique
* **Cosine Similarity** – Text similarity measurement
* **Large Language Models (LLMs)** – Resume feedback & interview answer generation - (**zephyr-7b-beta LLM**)
* **Hugging Face Inference API** – Model hosting and inference
* **PyMuPDF** – PDF text extraction
* **Environment Variables (.env)** – Secure API key handling

# 🏗️ System Architecture Overview
User Input → Streamlit Interface →
Resume Text Extraction →
Text Vectorization (TF-IDF) →
Similarity Calculation (Cosine Similarity) →
LLM API Call →
AI Response Display

The system integrates classical NLP techniques with modern LLM-based generative AI.

# 📄 Feature 1: Resume Analyzer & Job Description Matching

### Step 1: Resume Upload

* User uploads resume in PDF format.
* The application extracts textual content from the document.

### Step 2: Text Processing

* Resume text and Job Description text are processed.
* Stopwords are removed.
* Text is converted into numerical vectors using TF-IDF.

### Step 3: Similarity Computation

* Cosine Similarity calculates how closely the resume matches the job description.
* A percentage match score is generated.

### Step 4: AI-Based Resume Feedback

* The extracted resume text is sent to a Large Language Model.
* The LLM analyzes strengths, weaknesses, and improvement suggestions.
* Structured feedback is generated similar to ATS systems.

# 🎯 Feature 2: Interview Answer Generator

### Step 1: User Inputs Interview Question

The user provides a technical or behavioral question.

### Step 2: LLM Processing

* The question is sent to a hosted Large Language Model via API.
* A system prompt instructs the model to respond using the STAR method (Situation, Task, Action, Result).

### Step 3: AI Response

* The model generates a structured, professional interview answer.

This simulates AI-powered interview coaching.

# 🤖 Large Language Model (LLM) Integration

This project uses a hosted LLM via the Hugging Face Inference API.

# 🔐 Security & API Key Management

The API key is stored securely using environment variables.

* API keys are not hardcoded
* Sensitive credentials are excluded using `.gitignore`
* Ensures safe public repository sharing

# 💼 Real-World Applications

This project simulates:

* Applicant Tracking Systems (ATS)
* AI-powered resume evaluation platforms
* AI interview coaching systems
* HR-tech AI tools

# 🎓 Skills Demonstrated

* End-to-end AI application development
* NLP fundamentals
* API integration (Hugging Face API via zephyr-7b-beta LLM)
* LLM prompt engineering
* Secure credential handling
* Web app deployment with Streamlit
* Real-world problem solving

# 🚀 How to Clone and Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sowmya13531/IntelliHire-AI.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd IntelliHire-AI
```

### 3️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```


### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```


### 5️⃣ Create .env File

Create a file named:

```
.env
```

Inside it, add:

```
HF_TOKEN=your_huggingface_api_key
```


### 6️⃣ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

Locally.

# 📌 Future Enhancements

* Skill gap detection
* Resume keyword highlighting
* Database integration
* User authentication
* Deployment on cloud platforms



# 🏁 Conclusion

IntelliHire-AI is an AI project that combines:

* Classical NLP techniques
* Modern LLM-based AI
* Real-world API integration
* Web application development

It demonstrates strong foundational knowledge in Artificial Intelligence, Machine Learning, and software engineering.

## Author
# Sowmya Kanithi
AI Ml Engineer - Software Engineer - NLP - Gen AI - Global Innovative Technologies Enthusiast .

Open to Opportunities....And Collaborations.... :)
