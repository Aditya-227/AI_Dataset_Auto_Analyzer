import sys
import os
import pickle
from pathlib import Path

# add project root to python path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
from core.dataset_loader import DatasetLoader
from core.dataset_analyzer import DatasetAnalyzer
from core.pattern_detector import PatternDetector
from core.ml_recommender import MLRecommender
from core.visualization_engine import VisualizationEngine
from llm.qa_engine import QAEngine
from llm.insight_engine import InsightEngine
from core.automl_trainer import AutoMLTrainer
from utils.report_generator import generate_report

st.title("AI Dataset Auto-Analyzer")

uploaded_file = st.file_uploader(
    "Upload dataset",
    type=["csv", "xlsx"]
)

if uploaded_file:

    # Load dataset
    loader = DatasetLoader()
    context = loader.load_dataset(uploaded_file)

    # Analyze dataset
    analyzer = DatasetAnalyzer()
    context = analyzer.analyze(context)

    # Detect patterns
    detector = PatternDetector()
    context = detector.detect(context)

    # ML recommendations
    recommender = MLRecommender()
    recommendations = recommender.generate_recommendations(context)

    # Visualization engine
    viz = VisualizationEngine()
    heatmap = viz.correlation_heatmap(context)
    distributions = viz.numeric_distributions(context)

    st.success("Dataset loaded and analyzed")

    # Tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Overview",
        "EDA",
        "Patterns",
        "Visualizations",
        "AutoML",
        "AI Insights"
    ])

    # ----------------------
    # TAB 1 — OVERVIEW
    # ----------------------
    with tab1:

        st.subheader("Dataset Info")
        st.write("Rows:", context.rows)
        st.write("Columns:", context.columns)

        st.subheader("Column Names")
        st.write(context.column_names)

        st.subheader("Dataset Preview")
        st.dataframe(context.dataframe.head())

        st.subheader("ML Recommendations")
        st.write("Problem Type:", recommendations["problem_type"])

        st.write("Suggested Models:")
        for model in recommendations["models"]:
            st.write("-", model)

        report = generate_report(context, recommendations)

        st.download_button(
            label="Download Dataset Report",
            data=report,
            file_name="dataset_report.txt",
            mime="text/plain"
        )

    # ----------------------
    # TAB 2 — EDA
    # ----------------------
    with tab2:

        st.subheader("Feature Types")

        st.write("Numeric Features:", context.numeric_features)
        st.write("Categorical Features:", context.categorical_features)
        st.write("Datetime Features:", context.datetime_features)

        st.subheader("Missing Values")

        if context.missing_values:
            st.write(context.missing_values)
        else:
            st.write("No missing values detected")

        if context.correlations is not None:
            st.subheader("Correlation Matrix")
            st.dataframe(context.correlations)

    # ----------------------
    # TAB 3 — PATTERNS
    # ----------------------
    with tab3:

        st.subheader("Detected Patterns")

        st.write("Potential Target Variable:", context.patterns["potential_target"])
        st.write("Class Imbalance:", context.patterns["class_imbalance"])

        st.write("High Correlations:")

        if context.patterns["high_correlations"]:
            for pair in context.patterns["high_correlations"]:
                st.write(pair)
        else:
            st.write("No strong correlations detected")

    # ----------------------
    # TAB 4 — VISUALIZATIONS
    # ----------------------
    with tab4:

        st.subheader("Correlation Heatmap")

        if heatmap:
            st.plotly_chart(heatmap, use_container_width=True)

        st.subheader("Feature Distributions")

        for col, fig in distributions.items():
            st.plotly_chart(fig, use_container_width=True)

    # ----------------------
    # TAB 5 — AUTOML
    # ----------------------
    with tab5:

        st.subheader("AutoML Model Training")

        target_column = st.selectbox(
            "Select Target Column",
            context.column_names
        )

        if st.button("Train Model Automatically"):

            context.patterns["potential_target"] = target_column

            trainer = AutoMLTrainer()
            result = trainer.train(context)

            if result:

                st.write("Model Score:", round(result["score"], 3))

                if "model_results" in result:

                    st.subheader("Model Comparison")

                    for model_name, model_score in result["model_results"].items():
                        st.write(f"{model_name}: {model_score:.3f}")

                if result["importance"] is not None:

                    st.subheader("Feature Importance")

                    importance = result["importance"].head(10)

                    st.bar_chart(importance)

                else:

                    st.write("Feature importance not available for this model.")

                # DOWNLOAD TRAINED MODEL
                import pickle

                model_bytes = pickle.dumps(result["model"])

                st.download_button(
                    label="Download Trained Model",
                    data=model_bytes,
                    file_name="trained_model.pkl",
                    mime="application/octet-stream"
                )

            else:
                st.write("Model training failed for the selected target.")

    # ----------------------
    # TAB 6 — AI INSIGHTS
    # ----------------------
    with tab6:

        st.subheader("Ask Questions About Dataset")

        question = st.text_input("Ask a question")

        if question:
            qa = QAEngine()
            answer = qa.ask(context, question)

            st.write("Answer:")
            st.write(answer)

        st.subheader("AI Dataset Insights")

        if st.button("Generate AI Insights"):

            engine = InsightEngine()
            insights = engine.generate_insights(context)

            st.write(insights)