import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

def app():
    st.title("🤖 Model Training & Evaluation")

    df = pd.read_csv("air_pollution_app/data/air_pollution.csv")
    df = df.drop(columns=['No', 'PM2.5', 'PM2.5_Rolling'], errors='ignore')

    # Encode categorical variables
    for col in ['station', 'season', 'peak_hour']:
        if col in df.columns:
            df[col] = LabelEncoder().fit_transform(df[col])

    X = df.drop(columns=['AQI_PM2.5'])
    y = df['AQI_PM2.5']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- Decision Tree ---
    dt_model = DecisionTreeClassifier(random_state=42)
    dt_model.fit(X_train, y_train)
    dt_preds = dt_model.predict(X_test)
    dt_acc = accuracy_score(y_test, dt_preds)

    # --- Random Forest ---
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_preds = rf_model.predict(X_test)
    rf_acc = accuracy_score(y_test, rf_preds)

    # --- Accuracy Comparison ---
    st.subheader("📈 Accuracy Comparison")
    fig_acc, ax_acc = plt.subplots(figsize=(6, 4))
    models = ['Decision Tree', 'Random Forest']
    accuracies = [dt_acc, rf_acc]
    colors = ['skyblue', 'lightgreen']

    ax_acc.bar(models, accuracies, color=colors)
    ax_acc.set_ylim(0.7, 1.0)
    ax_acc.set_ylabel('Accuracy')
    ax_acc.set_title('Model Accuracy Comparison')
    for i, acc in enumerate(accuracies):
        ax_acc.text(i, acc + 0.01, f"{acc:.2f}", ha='center', fontsize=12)
    st.pyplot(fig_acc)

    # --- Classification Reports ---
    st.subheader("📋 Classification Reports")
    st.markdown("**Decision Tree**")
    st.text(classification_report(y_test, dt_preds))
    st.markdown("**Random Forest**")
    st.text(classification_report(y_test, rf_preds))

    # --- Confusion Matrices ---
    labels = rf_model.classes_  # consistent label ordering
    dt_cm = confusion_matrix(y_test, dt_preds, labels=labels)
    rf_cm = confusion_matrix(y_test, rf_preds, labels=labels)

    st.subheader("📊 Confusion Matrices")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Decision Tree**")
        fig_dt_cm, ax1 = plt.subplots(figsize=(6, 4))
        sns.heatmap(dt_cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels, ax=ax1)
        ax1.set_xlabel('Predicted')
        ax1.set_ylabel('Actual')
        st.pyplot(fig_dt_cm)

    with col2:
        st.markdown("**Random Forest**")
        fig_rf_cm, ax2 = plt.subplots(figsize=(6, 4))
        sns.heatmap(rf_cm, annot=True, fmt='d', cmap='Greens', xticklabels=labels, yticklabels=labels, ax=ax2)
        ax2.set_xlabel('Predicted')
        ax2.set_ylabel('Actual')
        st.pyplot(fig_rf_cm)
