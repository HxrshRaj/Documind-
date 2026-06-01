from utils.config import (
    get_groq_key
)

from agents.groq_agent import (
    enhance_knowledge
)
from agents.knowledge_agent import (
    get_knowledge_summary
)

from utils.config import (
    get_openai_key
)
from agents.knowledge_agent import (
    get_knowledge_summary
)
from agents.time_series_report_agent import (
    generate_time_series_report
)
from agents.clustering_agent import (
    run_clustering
)

from agents.clustering_report_agent import (
    generate_clustering_report
)

from utils.preprocessing import (
    preprocess_data
)
from agents.task_override_agent import (
    get_task_options
)
import streamlit as st
import pandas as pd

from utils.data_loader import load_data

from agents.profiler_agent import generate_profile
from agents.task_detector import detect_task
from agents.model_agent import recommend_models
from agents.training_agent import train_models

from agents.evaluation_agent import (
    evaluate_classification,
    evaluate_regression
)

from agents.explainability_agent import (
    generate_explanation
)

from agents.visualization_agent import (
    create_performance_chart
)

from agents.feature_importance_agent import (
    get_feature_importance
)

from agents.insight_agent import (
    generate_dataset_insights
)

from agents.status_agent import (
    get_agent_status
)

from agents.model_selector import (
    get_best_model
)

from agents.expertise_agent import (
    adapt_explanation
)

from agents.report_generator_agent import (
    build_report
)

from agents.download_report_agent import (
    save_report
)

from agents.report_download_agent import (
    get_report_filename
)

from agents.final_recommendation_agent import (
    generate_final_recommendation
)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="DocuMind",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🤖 DocuMind")

st.subheader(
    "Autonomous Agentic AI Orchestrator"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header(
    "Dataset Upload"
)

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

st.sidebar.header(
    "User Expertise"
)
st.sidebar.header(
    "Task Override"
)

task_override = st.sidebar.selectbox(

    "Select Task",

    get_task_options()

)

user_level = st.sidebar.selectbox(
    "Select Expertise Level",
    [
        "Beginner",
        "Intermediate",
        "Expert"
    ]
)

# -----------------------------
# Main Logic
# -----------------------------
if uploaded_file is not None:

    try:

        df = load_data(
            uploaded_file
        )

        st.success(
            "Dataset Loaded Successfully"
        )

        # -----------------------------
        # Agent Status Dashboard
        # -----------------------------
        st.write(
            "## Agent Status Dashboard"
        )

        status = get_agent_status()

        status_df = pd.DataFrame({

            "Agent":
                list(status.keys()),

            "Status":
                list(status.values())

        })

        st.dataframe(
            status_df,
            use_container_width=True
        )

        st.write("---")

        # -----------------------------
        # Dataset Profile
        # -----------------------------
        profile = generate_profile(
            df
        )

        st.write(
            "## Dataset Profile"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Rows",
                profile["rows"]
            )

        with col2:

            st.metric(
                "Columns",
                profile["columns"]
            )

        with col3:

            st.metric(
                "Missing Values",
                profile["missing_values"]
            )

        col4, col5, col6 = st.columns(3)

        with col4:

            st.metric(
                "Numerical Columns",
                profile[
                    "numerical_columns"
                ]
            )

        with col5:

            st.metric(
                "Categorical Columns",
                profile[
                    "categorical_columns"
                ]
            )

        with col6:

            st.metric(
                "Memory Usage (KB)",
                profile[
                    "memory_usage_kb"
                ]
            )

        st.write("---")

        st.write(
            "## Task Detection Agent"
        )

        target_column = st.selectbox(
            "Select Target Column",
            df.columns
        )

        if st.button(
            "Analyze Dataset"
        ):
            task, reason = detect_task(
                df,
                target_column
            )

            if task_override != "Auto Detect":

                task = task_override

                reason = (
                  "User manually selected task."
                )

            st.success(
                f"Detected Task: {task}"
            )

            st.info(
                f"Reason: {reason}"
            )

            # -----------------------------
            # RAG Knowledge Layer
            # -----------------------------
            try:

                retrieved_knowledge = (
                    get_knowledge_summary(
                        task
                    )
                )

                groq_key = get_groq_key()

                enhanced_knowledge = (
                    enhance_knowledge(
                        retrieved_knowledge,
                        task,
                        groq_key
                    )
                )

                st.write(
                    "## Knowledge Base Insights"
                )

                st.info(
                    enhanced_knowledge
                )

            except Exception as e:

                enhanced_knowledge = (
                    "Knowledge enhancement unavailable."
                )

                st.error(
                    str(e)
                )

                st.warning(
                    enhanced_knowledge
                )

            st.write("---")

            # -----------------------------
            # Dataset Insights
            # -----------------------------
            st.write(
                "## Dataset Insights"
            )

            insights = (
                generate_dataset_insights(
                    profile,
                    task
                )
            )

            for insight in insights:

                st.write(
                    f"• {insight}"
                )

            st.write("---")

            # -----------------------------
            # Model Recommendation
            # -----------------------------
            st.write(
                "## Recommended Models"
            )

            recommendations = (
                recommend_models(
                    task
                )
            )

            for model in (
                recommendations[
                    "models"
                ]
            ):

                st.write(
                    f"✅ {model}"
                )

            st.info(
                recommendations[
                    "reason"
                ]
            )

            st.write("---")

            # -----------------------------
            # Training
            # -----------------------------
            outputs = train_models(
                df,
                target_column,
                task
            )

            st.write(
                "## Model Performance"
            )

            performance_rows = []

            # -----------------------------
            # Classification
            # -----------------------------
            if task == "Classification":

                for (
                    model_name,
                    values
                ) in outputs.items():

                    metrics = (
                        evaluate_classification(
                            values[
                                "y_true"
                            ],
                            values[
                                "y_pred"
                            ]
                        )
                    )

                    performance_rows.append({

                        "Model":
                            model_name,

                        **metrics

                    })

                performance_df = (
                    pd.DataFrame(
                        performance_rows
                    )
                )

            # -----------------------------
            # Regression
            # -----------------------------
            elif task == "Regression":

                for (
                    model_name,
                    values
                ) in outputs.items():

                    metrics = (
                        evaluate_regression(
                            values[
                                "y_true"
                            ],
                            values[
                                "y_pred"
                            ]
                        )
                    )

                    performance_rows.append({

                        "Model":
                            model_name,

                        **metrics

                    })

                performance_df = (
                    pd.DataFrame(
                        performance_rows
                    )
                )

            elif task == "Clustering":

                clustering_df = preprocess_data(
                    df,
                    target_column
                )

                X = clustering_df.drop(
                    columns=[target_column]
                )

                clustering_results = (
                    run_clustering(X)
                )

                st.write(
                    "## Clustering Results"
                )

                st.success(
                    f"Silhouette Score: "
                    f"{clustering_results['silhouette_score']}"
                )

                clustering_report = (
                    generate_clustering_report(
                        clustering_results[
                            "silhouette_score"
                        ]
                    )
                )

                st.info(
                    clustering_report
                )

                performance_df = None

            elif task == "Time Series":

                st.write(
                    "## Time Series Analysis"
                )

                report = (
                    generate_time_series_report()
                )

                st.info(
                    report
                )

                performance_df = None

            else:

                st.warning(
                    f"{task} workflow integration is coming next."
                )

                performance_df = None
            if performance_df is not None:

                st.dataframe(
                    performance_df,
                    use_container_width=True
                )

                chart = (
                    create_performance_chart(
                        performance_df,
                        task
                    )
                )

                st.plotly_chart(
                    chart,
                    use_container_width=True
                )

                best_models, best_score, metric = (
                    get_best_model(
                        performance_df,
                        task
                    )
                )

                if len(best_models) == 1:

                    best_model = (
                        best_models[0]
                    )

                    st.success(
                        f"🏆 Best Model: {best_model}"
                    )

                    explanation = (
                        generate_explanation(
                            task,
                            best_model,
                            best_score
                        )
                    )

                    adapted_explanation = (
                        adapt_explanation(
                            explanation,
                            user_level
                        )
                    )

                    st.write(
                        "## Executive Summary"
                    )

                    st.info(
                        adapted_explanation
                    )

                    # -----------------------------
                    # Feature Importance
                    # -----------------------------
                    model_object = (
                        outputs[
                            best_model
                        ]["model"]
                    )

                    feature_names = (
                        outputs[
                            best_model
                        ][
                            "feature_names"
                        ]
                    )

                    importance_df = (
                        get_feature_importance(
                            model_object,
                            feature_names
                        )
                    )

                    if (
                        importance_df
                        is not None
                    ):

                        st.write(
                            "## Feature Importance"
                        )

                        st.dataframe(
                            importance_df,
                            use_container_width=True
                        )

                    # -----------------------------
                    # Final Recommendation
                    # -----------------------------
                    st.write(
                        "## Final Recommendation"
                    )

                    final_recommendation = (
                        generate_final_recommendation(
                            task,
                            best_model
                        )
                    )

                    st.success(
                        final_recommendation
                    )

                    # -----------------------------
                    # Executive Report
                    # -----------------------------
                    st.write(
                        "## Executive Report"
                    )

                    report_text = (
                        build_report(
                            task,
                            best_model,
                            best_score,
                            adapted_explanation,
                            enhanced_knowledge
                        )
                    )

                    report_text += (

                        "\n\n"

                        "RAG KNOWLEDGE INSIGHTS\n"

                        "=====================\n\n"

                        + enhanced_knowledge
                    )

                    st.text_area(
                        "Generated Report",
                        report_text,
                        height=300
                    )

                    # -----------------------------
                    # Download Report
                    # -----------------------------
                    filename = (
                        get_report_filename(
                            task
                        )
                    )

                    file_path = (
                        save_report(
                            report_text,
                            filename
                        )
                    )

                    with open(
                        file_path,
                        "rb"
                    ) as file:

                        st.download_button(

                            label=
                            "📥 Download Report",

                            data=file,

                            file_name=
                            filename,

                            mime=
                            "text/plain"
                        )

                else:

                    st.warning(
                        f"Multiple models achieved the same top {metric}."
                    )

                    for model in best_models:

                        st.write(
                            f"• {model}"
                        )

        st.write("---")

        st.write(
            "## Dataset Preview"
        )

        st.dataframe(
            df.head(),
            use_container_width=True
        )

    except Exception as e:

        st.error(
            str(e)
        )

else:

    st.info(
        "Please upload a CSV file to begin."
    )    