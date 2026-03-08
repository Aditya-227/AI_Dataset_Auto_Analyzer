# 🚀 AI Dataset Auto-Analyzer

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-AutoML-green)
![LLM](https://img.shields.io/badge/LLM-Groq%20%7C%20Ollama-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

An **AI-powered dataset analysis platform** that automatically performs **EDA, pattern detection, ML model recommendations, AutoML training, and natural language dataset Q&A**.

The system combines **Machine Learning automation + Large Language Models** to make dataset exploration fast and interactive.

---

# 🌐 Live Demo

Try the deployed app:


https://ai-dataset-auto-analyzer.streamlit.app/

---

# ✨ Features

### 📊 Automated Dataset Analysis
- Upload **CSV / Excel datasets**
- Automatic **EDA (Exploratory Data Analysis)**
- Detect:
  - Numeric features
  - Categorical features
  - Missing values
  - Correlations

---

### 🔎 Pattern Detection
Automatically detects:

- Potential **target variable**
- **Class imbalance**
- **High correlations**
- Dataset structure insights

---

### 📈 Interactive Visualizations
Powered by **Plotly + Streamlit**

Includes:

- Correlation heatmap
- Feature distributions
- Dataset statistics
- Feature importance charts

---

### 🤖 AutoML Model Training
Automatically:

- Selects target column
- Tests multiple ML models
- Chooses best performing model

Models compared:

- Logistic Regression
- Random Forest
- Gradient Boosting
- Support Vector Machine

Outputs:

- Best model
- Accuracy score
- Feature importance

---

### 💬 Natural Language Dataset Q&A
Ask questions like:

```
How many rows are in this dataset?
Which feature is most important?
What type of problem is this dataset?
```

The AI assistant responds using dataset metadata.

---

### 🧠 Hybrid LLM Architecture

The system automatically switches between:

| Environment | LLM Used |
|-------------|----------|
| Local development | Ollama (local LLM) |
| Cloud deployment | Groq API |

This allows:

- **Offline local development**
- **Fast cloud inference**

---

# 🏗 System Architecture

```
User
 │
 ▼
Streamlit Dashboard
 │
 ▼
Dataset Loader
 │
 ▼
Dataset Analyzer
 │
 ▼
Pattern Detection Engine
 │
 ▼
ML Recommendation Engine
 │
 ▼
Visualization Engine
 │
 ▼
AutoML Trainer
 │
 ▼
LLM Client
 ├── Ollama (Local Development)
 └── Groq API (Cloud Deployment)
```

---

# 🧩 Project Structure

```
AI_Dataset_Auto_Analyzer
│
├── app
│   └── streamlit_app.py
│
├── core
│   ├── dataset_loader.py
│   ├── dataset_analyzer.py
│   ├── pattern_detector.py
│   ├── ml_recommender.py
│   ├── visualization_engine.py
│   └── automl_trainer.py
│
├── llm
│   ├── llm_client.py
│   ├── qa_engine.py
│   ├── insight_engine.py
│   └── prompt_builder.py
│
├── utils
│   └── report_generator.py
│
├── config
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Aditya-227/AI_Dataset_Auto_Analyzer.git
cd AI_Dataset_Auto_Analyzer
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Locally

Start the Streamlit app:

```bash
streamlit run app/streamlit_app.py
```

Open in browser:

```
http://localhost:8501
```

---

# 🔑 API Setup (Groq)

Create a Groq API key:

```
https://console.groq.com/
```

Add it to environment variables:

**Windows**

```bash
set GROQ_API_KEY=your_key_here
```

**Linux / Mac**

```bash
export GROQ_API_KEY=your_key_here
```

---

# ☁️ Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Go to:

```
https://share.streamlit.io
```

3. Deploy using:

```
app/streamlit_app.py
```

4. Add secrets:

```
GROQ_API_KEY = "your_key"
```

---

# 📊 Example Workflow

1️⃣ Upload dataset  
2️⃣ Automatic dataset analysis  
3️⃣ Detect patterns and correlations  
4️⃣ Visualize features  
5️⃣ Train ML model automatically  
6️⃣ Ask AI questions about the dataset  

---

# 📸 Screenshots

### Dataset Overview

![overview](screenshots/1.png)

### AutoML Training

![automl](screenshots/2.png)

### Feature Importance

![importance](screenshots/3.png)

---

# 🚀 Future Improvements

Possible enhancements:

- Dataset **chat interface**
- Feature engineering suggestions
- Model explainability (SHAP)
- Auto hyperparameter tuning
- Report export (PDF)

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Aditya**

GitHub:

```
https://github.com/Aditya-227
```

---

# ⭐ If you like this project

Give it a **star on GitHub** ⭐
