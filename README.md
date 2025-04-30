# EAMSET Rank Predictor

**EAMSET Rank Predictor** is a Python tool that predicts the cutoff rank for a given college, branch, and category in AP EAMCET, using historical cutoff data and polynomial regression.

---

## 🧩 How It Works

1. **User Input:**  
   - Enter the college code (e.g., `JNTUK`), category (e.g., `OC`, `BC`, `SC`, `ST`), and branch (e.g., `CSE`, `ECE`, `EEE`).
2. **Data Lookup:**  
   - The script reads cutoff data from CSV files for the years 2013–2016.
   - It extracts the relevant cutoff rank for your chosen college, category, and branch.
3. **Prediction:**  
   - Using cutoff ranks from previous years, the script fits linear, quadratic, and cubic regression models.
   - It predicts the cutoff rank for the next year (2017) and visualizes the trend.
4. **Visualization:**  
   - Displays a matplotlib graph showing actual cutoffs and the regression fits.

---

## 🗂️ Project Structure

```
EAMSET-Rank-Predictor/
├── eamcet_rank.py
└── README.md
```

- **for_year20XX.csv:** Historical cutoff data for each year.
- **eamcet_rank.py:** Main Python script (the code you posted).

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Required libraries: `matplotlib`, `numpy`, `scipy`

Install dependencies (if needed):
```bash
pip install matplotlib numpy scipy
```

### Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sruthivellore/EAMSET-Rank-Predictor.git
   cd EAMSET-Rank-Predictor
   ```

2. **Run the script:**
   ```bash
   python eamcet_rank.py
   ```

3. **Follow the prompts:**  
   Enter the college code, category, and branch as requested.

   Example:
   ```
   Enter College Code :  JNTUK
   Category           :  OC
   Branch             :  CSE
   ```

4. **View the prediction:**  
   - The script will print the predicted cutoff for 2017.
   - A graph will pop up showing the historical cutoffs and the regression fits.

---

## 📝 Code Overview

- **to_open_files(files, code, category, branch):**  
  Reads a CSV file for a given year, finds the row with the matching college code, and retrieves the cutoff rank for the specified category and branch.

- **check_branch(parts, category, branch):**  
  Maps category+branch (e.g., `OCCSE`) to the correct column in the data row.

- **predict_value_of_y(xs, ys):**  
  Fits linear, quadratic, and cubic regression models to the cutoff data and predicts the next year's cutoff. Plots the data and fits using matplotlib.

- **squared_error(x, y):**  
  Calculates the R-squared value for the regression fit.

- **uppercase(word):**  
  Helper function to ensure inputs are uppercase.

---

## 📥 Input Format

- **College Code:** 3-5 letter code (e.g., `JNTUK`)
- **Category:** `OC`, `BC`, `SC`, `ST`
- **Branch:** `CSE`, `ECE`, `EEE`

**Note:** The script expects the CSV files to be formatted with columns corresponding to each category-branch combination, and the mapping in `check_branch()` must match the column order.

---

## 📊 Output

- **Console:** Predicted cutoff rank for 2017.
- **Graph:** Visual representation of historical cutoffs and regression predictions.

## 👩‍💻 Author

Developed by [sruthivellore](https://github.com/sruthivellore).

---
