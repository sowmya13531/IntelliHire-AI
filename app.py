import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------- LOAD ENV --------------------

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    st.error("HF_TOKEN not found. Check your .env file.")
    st.stop()

# -------------------- AI CLIENT --------------------

client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=HF_TOKEN
)

# -------------------- PAGE CONFIG --------------------

st.set_page_config(page_title="IntelliHire", page_icon="🚀")
st.title("🚀 IntelliHire - AI Resume & Interview Assistant")

# -------------------- FUNCTIONS --------------------

def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text

def calculate_match_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return round(float(score[0][0]) * 100, 2)

def ai_resume_feedback(resume_text):
    response = client.chat_completion(
        messages=[
            {"role": "system", "content": "You are an ATS resume reviewer. Give strengths, weaknesses, and improvements."},
            {"role": "user", "content": resume_text}
        ],
        max_tokens=600
    )
    return response.choices[0].message.content

# -------------------- UI --------------------

mode = st.radio(
    "Select Feature:",
    ["Interview Answer Generator", "Resume Feedback + JD Match"]
)

if mode == "Interview Answer Generator":

    question = st.text_area("Enter Interview Question:")

    if st.button("Generate Answer"):
        if not question.strip():
            st.warning("Please enter a question.")
            st.stop()

        with st.spinner("Generating Answer..."):
            response = client.chat_completion(
                messages=[
                    {"role": "system", "content": "You are an expert technical interview coach. Use STAR method."},
                    {"role": "user", "content": question}
                ],
                max_tokens=500
            )

            st.success("Answer Generated ✅")
            st.write(response.choices[0].message.content)

# -------------------- RESUME + JD MATCH --------------------

else:

    uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    job_description = st.text_area("Paste Job Description")

    if st.button("Analyze Resume"):

        if not uploaded_resume or not job_description.strip():
            st.warning("Upload resume and paste job description.")
            st.stop()

        with st.spinner("Processing..."):

            resume_text = extract_text_from_pdf(uploaded_resume)

            # AI Feedback
            feedback = ai_resume_feedback(resume_text)

            # Match Score
            match_score = calculate_match_score(resume_text, job_description)

            st.success("Analysis Complete ✅")

            st.subheader("📊 JD Match Score")
            st.metric(label="Match Percentage", value=f"{match_score}%")

            st.subheader("📝 AI Resume Feedback")
            st.write(feedback)

            if match_score < 60:
                st.warning("Low match score. Consider adding missing skills from JD.")
            elif match_score < 80:
                st.info("Moderate match. Small improvements recommended.")
            else:
                st.success("Strong match! Resume aligns well with JD.")