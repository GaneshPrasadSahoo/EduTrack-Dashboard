import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EduTrack Dashboard", layout="wide")

st.markdown("""
    <style>
        .reportview-container { background-color: #f5f5f5; }
        .sidebar .sidebar-content { background-color: #333; color: white; }
        h1 { color: blue; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>📊 EduTrack Dashboard</h1>", unsafe_allow_html=True)

upload_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.markdown("<h3 style='color: orange;'>📜 Dataset Preview:</h3>", unsafe_allow_html=True)
    st.write(df.head())

    st.markdown("<h3 style='color: darkblue;'>🔍 Search & Filter Students:</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        sort_option = st.radio("Sort by:", ["Highest to Lowest %", "Lowest to Highest %"])
        df_sorted = df.sort_values(by="Percentage", ascending=(sort_option == "Lowest to Highest %"))
        df_sorted["Rank"] = range(1, len(df_sorted) + 1)

    with col2:
        search_query = st.text_input("Search Student Name")
        if search_query:
            df_sorted = df_sorted[df_sorted["Student Name"].str.contains(search_query, case=False)]

    with col3:
        filter_status = st.selectbox("Filter by Status", ["All", "Pass", "Fail"])
        if filter_status != "All":
            df_sorted = df_sorted[df_sorted["Status"] == filter_status]

    st.markdown("<h3 style='color: blue;'>📌 Full Student Rankings:</h3>", unsafe_allow_html=True)
    st.write(df_sorted)

    st.markdown("<h3 style='color: green;'>📈 Class Statistics:</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("📌 Total Students", len(df))
    col2.metric("✅ Total Passed", len(df[df['Status'] == 'Pass']))
    col3.metric("❌ Total Failed", len(df[df['Status'] == 'Fail']))
    st.write(f"📊 **Class Average %:** {df['Percentage'].mean():.2f}%")

    st.markdown("<h3 style='color: purple;'>🏆 Top 5 Students:</h3>", unsafe_allow_html=True)
    st.write(df_sorted.head(5)[["Rank", "Student Name", "Percentage", "Grade", "Status"]])

    st.markdown("<h3 style='color: blue;'>📊 Top 5 Students by Percentage:</h3>", unsafe_allow_html=True)
    top_5 = df_sorted.head(5)
    fig, ax = plt.subplots(figsize=(5, 3))  
    ax.bar(top_5["Student Name"], top_5["Percentage"], color="blue")
    plt.xlabel("Student Name")
    plt.ylabel("Percentage")
    plt.title("Top 5 Students")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.markdown("<h3 style='color: red;'>🥧 Pass vs Fail Distribution:</h3>", unsafe_allow_html=True)
    status_counts = df["Status"].value_counts()
    fig, ax = plt.subplots(figsize=(4, 3))  
    ax.pie(status_counts, labels=status_counts.index, autopct="%1.1f%%", colors=["green", "red"], startangle=90)
    plt.title("Pass vs Fail")
    st.pyplot(fig)

    st.markdown("<h3 style='color: darkblue;'>⬇️ Download Processed Data:</h3>", unsafe_allow_html=True)
    csv = df_sorted.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "student_dashboard.csv", "text/csv", key='download-csv')

else:
    st.warning("⚠️ Please upload a CSV file to proceed.")
