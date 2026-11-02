import streamlit as st
import pickle
import PyPDF2
import re
import mysql.connector

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Smart Resume Analyzer")

# Upload PDF
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text


def save_prediction(role):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="As$1%|<>",
        database="resume_analyzer"
    )

    cursor = connection.cursor()
    query = "INSERT INTO predictions (predicted_role) VALUES (%s)"
    cursor.execute(query, (role,))
    connection.commit()
    connection.close()


if uploaded_file is not None:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    cleaned_text = clean_text(text)

    input_vector = vectorizer.transform([cleaned_text])
    prediction = model.predict(input_vector)

    probs = model.predict_proba(input_vector)
    confidence = max(probs[0])

    st.write(f"Confidence: {round(confidence * 100, 2)}%")

    if confidence < 0.40:
        st.warning("Resume does not strongly match any trained role.")
    else:
        st.success(f"Predicted Role: {prediction[0]}")

        if prediction[0] == "Data Scientist":
            st.info("Recommended Skills: SQL, Deep Learning, Feature Engineering")

        elif prediction[0] == "Web Developer":
            st.info("Recommended Skills: Node.js, REST APIs, UI/UX")

        elif prediction[0] == "AI Engineer":
            st.info("Recommended Skills: PyTorch, Model Deployment")

        elif prediction[0] == "Software Engineer":
            st.info("Recommended Skills: System Design, OOP")

        elif prediction[0] == "Backend Developer":
            st.info("Recommended Skills: Docker, Microservices")

        elif prediction[0] == "Non-Technical":
            st.info("Resume appears non-technical or general field.")

        save_prediction(prediction[0])