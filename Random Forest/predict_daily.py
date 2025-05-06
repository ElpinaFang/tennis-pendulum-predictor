import pandas as pd
import joblib
import sys
import os
from sklearn.metrics import accuracy_score

# --- Get input file ---
if len(sys.argv) > 1:
    daily_file = sys.argv[1]
else:
    daily_file = input("Enter the daily Excel filename (e.g. Daily__02152025.xlsx): ").strip()

# --- Check file exists ---
if not os.path.isfile(daily_file):
    print(f"[ERROR] File not found: {daily_file}")
    sys.exit(1)

# --- Manually assign column names ---
columns = [
    'Player', 'Birth Date', 'Ignore1', 'Ignore2', 'Ignore3', 'Ignore4', 'Ignore5',
    'Result', 'Ignore6', 'Ignore7', 'Ignore8',
    'Planets combo', 'Intensity label', 'Planets/Intensity',
    'Intensity degree', 'Match Date', 'Ignore9', 'Match Stat'
]

# --- Load file with no headers ---
df = pd.read_excel(daily_file, header=None, names=columns)
df.columns = df.columns.str.strip()

# --- Drop missing input values ---
df = df.dropna(subset=['Planets combo', 'Intensity degree', 'Planets/Intensity'])

# --- Load model and encoders ---
model = joblib.load("rf_model.pkl")
le_result = joblib.load("le_result.pkl")
le_planets = joblib.load("le_planets.pkl")
le_symbols = joblib.load("le_symbols.pkl")

# --- Filter out unseen symbols before transforming ---
df = df[df['Planets/Intensity'].isin(le_symbols.classes_)]
df = df[df['Planets combo'].isin(le_planets.classes_)]

# --- Prepare features ---
X = pd.DataFrame({
    'planets': le_planets.transform(df['Planets combo']),
    'intensity': df['Intensity degree'].astype(float),
    'symbols': le_symbols.transform(df['Planets/Intensity'])
})

# --- Predict ---
preds = model.predict(X)
df['Predicted_Result'] = le_result.inverse_transform(preds)

# --- Output ---
print("\n[PREDICTIONS]:")
print(df[['Player', 'Predicted_Result']])

# --- Optional accuracy check ---
if df['Result'].notna().sum() > 0:
    y_true = df['Result'].str.strip()
    y_pred = df['Predicted_Result'].str.strip()
    accuracy = accuracy_score(y_true, y_pred)
    print(f"\n[ACCURACY]: {accuracy:.2%}")
else:
    print("\n[INFO]: No actual results to compare — skipping accuracy check.")

# --- Save output to file (auto rename if exists) ---
base_output = os.path.splitext(daily_file)[0] + "_predicted"
output_file = base_output + ".xlsx"
counter = 1
while os.path.exists(output_file):
    output_file = f"{base_output}_{counter}.xlsx"
    counter += 1

df.to_excel(output_file, index=False)
print(f"\n[SAVED]: {output_file}")
