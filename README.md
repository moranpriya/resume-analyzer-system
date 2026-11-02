# resume-analyzer-system

A Machine Learning-based web application that analyzes uploaded resumes (PDF files) and predicts the most suitable job role based on the skills, experience, and keywords extracted from the resume.

The application uses Natural Language Processing (NLP) techniques and a Logistic Regression classification model to automate resume screening and job-role prediction.

## 🚀 Features

- **PDF Resume Upload:** Upload resumes in PDF format.
- **Text Extraction:** Extract textual information from uploaded resumes using PyPDF2.
- **Text Preprocessing:** Clean and normalize extracted text before analysis.
- **TF-IDF Vectorization:** Convert resume text into numerical features using Term Frequency–Inverse Document Frequency.
- **Job Role Prediction:** Predict the suitable job category using a trained Logistic Regression model.
- **MySQL Integration:** Store prediction records in a MySQL database.
- **Interactive Interface:** Simple and user-friendly interface developed using Streamlit.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend / Interface | Streamlit |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF Vectorizer |
| ML Algorithm | Logistic Regression |
| PDF Processing | PyPDF2 |
| Data Handling | Pandas |
| Database | MySQL |
| Model Storage | Pickle |

## 📁 Project Structure

```text
resume-analyzer-system/
│
├── data/
│   └── resumes.csv
│
├── app.py
├── train_model.py
├── model.pkl
├── vectorizer.pkl
├── README.md
└── requirements.txt
```

### File Description

- `app.py` – Main Streamlit application for uploading resumes, extracting text, predicting job roles, and saving predictions.
- `train_model.py` – Loads the training dataset, performs TF-IDF vectorization, trains the Logistic Regression model, and saves the trained model.
- `data/resumes.csv` – Dataset containing resume text and corresponding job-role labels.
- `model.pkl` – Saved trained machine learning model.
- `vectorizer.pkl` – Saved TF-IDF vectorizer used for transforming resume text.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/moranpriya/resume-analyzer-system.git
```

### 2. Navigate to the Project Directory

```bash
cd resume-analyzer-system
```

### 3. Install Dependencies

```bash
pip install streamlit pandas scikit-learn PyPDF2 mysql-connector-python
```

### 4. Train the Machine Learning Model

Run the following command to train the model using the dataset:

```bash
python train_model.py
```

After successful execution, the following files will be generated:

- `model.pkl`
- `vectorizer.pkl`

### 5. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser.

## 🧠 Machine Learning Workflow

The project follows these steps:

1. **Dataset Collection:** Collect resume descriptions and their corresponding job-role categories.
2. **Data Preprocessing:** Clean the text by converting it into lowercase and removing unnecessary characters.
3. **Feature Extraction:** Apply TF-IDF vectorization to transform textual data into numerical representations.
4. **Model Training:** Train a Logistic Regression classifier using the extracted features.
5. **Model Saving:** Save the trained classifier and vectorizer using Pickle.
6. **Resume Upload:** Allow users to upload PDF resumes through the Streamlit interface.
7. **Text Extraction:** Extract the resume content using PyPDF2.
8. **Prediction:** Transform the extracted text using the saved vectorizer and predict the appropriate job role.
9. **Database Storage:** Store prediction information in MySQL.

## 📊 Dataset

The project uses a CSV dataset containing resume descriptions and their corresponding job roles.

**Dataset format:**

| text | role |
|---|---|
| Experience in Python, SQL and Machine Learning... | Data Scientist |
| Developed applications using Java and C++... | Software Engineer |
| Experience in HTML, CSS and JavaScript... | Web Developer |

The dataset can be extended with additional resume descriptions and job-role categories to improve the model's learning capability.

## 🔮 Future Improvements

- Improve prediction accuracy using a larger and more diverse dataset.
- Add more job-role categories.
- Integrate advanced NLP techniques.
- Extract skills, education, and work experience separately.
- Provide personalized job recommendations.
- Add resume scoring and improvement suggestions.
- Develop an admin dashboard to analyze prediction records.
- Deploy the application on a cloud platform.

## 👩‍💻 Author

**Puja Priya Moran**

Computer Science & Engineering Student

**GitHub:** [@moranpriya](https://github.com/moranpriya)

---

⭐ If you find this project useful, consider giving the repository a star!


