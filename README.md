# EduTrack Dashboard

EduTrack Dashboard is a student performance tracking tool that allows educators to analyze and visualize student data efficiently. With an intuitive interface, users can upload CSV files, filter and search student records, and view performance insights through interactive charts and statistics.

## Features
- 📂 **CSV File Upload:** Easily upload student data in CSV format.
- 📜 **Dataset Preview:** View the first few rows of the uploaded dataset.
- 🔍 **Search & Filter:** Search students by name and filter by pass/fail status.
- 📊 **Ranking & Sorting:** Sort students based on percentage and display rankings.
- 📈 **Class Statistics:** View total students, pass/fail counts, and class average.
- 🏆 **Top Performers:** Identify the top 5 students with the highest percentage.
- 📉 **Data Visualization:** Bar charts for top performers and pie charts for pass/fail distribution.
- ⬇️ **Download Processed Data:** Export the filtered and sorted data as a CSV file.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/GaneshPrasadSahoo/EduTrack-Dashboard.git
   cd EduTrack-Dashboard
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the Streamlit app:
```sh
streamlit run app.py
```
Then, open the provided local URL in your browser.

## Dependencies
Ensure you have the following Python packages installed:
```txt
streamlit
pandas
matplotlib
```

## Project Structure
```
├── app.py                 # Main Streamlit application
├── requirements.txt       # Required dependencies
├── README.md              # Project documentation
```

## How to Use
1. Upload a CSV file containing student data.
2. View dataset preview and filter students by name or status.
3. Sort students based on percentage and see rankings.
4. Analyze class performance using metrics and charts.
5. Download the processed data as a CSV file.

## Example CSV Format
```
Student Name,Percentage,Grade,Status
John Doe,85,A,Pass
Jane Smith,72,B,Pass
Alice Brown,49,C,Fail
```

## License
This project is licensed under the MIT License.

## Author
Developed by **Ganesh Prasad Sahoo**.

