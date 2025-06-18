from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
from scipy import stats
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
CLEANED_FOLDER = "cleaned"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CLEANED_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if not file:
            return "No file uploaded."

        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        df = pd.read_csv(path)

        # ✅ Standard transforms
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.lower()
        df.columns = df.columns.str.replace(' ', '_')

        # ✅ Optional: convert date columns
        for col in df.columns:
            if 'date' in col:
                try:
                    df[col] = pd.to_datetime(df[col])
                except:
                    pass

        original = df.copy()

        # ✅ Auto-Clean logic
        if 'autoclean' in request.form:
            df.drop_duplicates(inplace=True)
            df.dropna(inplace=True)

            # Remove outliers using Z-score
            numeric_cols = df.select_dtypes(include=[np.number])
            if not numeric_cols.empty:
                z_scores = np.abs(stats.zscore(numeric_cols, nan_policy='omit'))
                df = df[(z_scores < 3).all(axis=1)]

        cleaned_filename = "cleaned_" + file.filename
        cleaned_path = os.path.join(CLEANED_FOLDER, cleaned_filename)
        df.to_csv(cleaned_path, index=False)

        return render_template("index.html",
                               tables=[original.head().to_html(classes='data'), df.head().to_html(classes='data')],
                               download_link=f"download/{cleaned_filename}")

    return render_template("index.html")

@app.route("/download/<filename>")
def download(filename):
    return send_file(os.path.join(CLEANED_FOLDER, filename), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)