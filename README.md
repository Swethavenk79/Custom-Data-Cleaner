# Custom Data Cleaning Web Tool (No Code)

A no-code web application that helps users clean messy CSV files with one click. Built using Python, Flask, and Pandas, it allows users to preview, auto-clean, and download cleaned datasets.

## Features

- Upload CSV files via a simple web interface  
- Preview original and cleaned data side-by-side  
- Remove duplicates and null values automatically  
- Apply standard data transformations  
- One-click auto-clean functionality  
- (Planned) ML-based cleaning suggestions  
- Download cleaned data instantly  

## Tech Stack

- Python 3.12+
- Flask
- Pandas
- HTML/CSS
- JavaScript (optional)

## Project Structure

```
custom-data-cleaner/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── script.js
├── uploads/
├── cleaned/
├── model/
└── requirements.txt
```

## How to Run Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/YourUsername/custom-data-cleaner.git
   cd custom-data-cleaner
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate    # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   python app.py
   ```

5. **Open in browser:**
   ```
   http://127.0.0.1:5000/
   ```

## To Do

- [ ] Add outlier detection
- [ ] Implement ML-based cleaning recommendations
- [ ] Improve UI with Bootstrap
- [ ] Enable column-specific operations
