import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Manually define the correct column names
columns = [
    'Player',      # A
    'Birth Date',  # B (not needed)
    'Ignore1',     # C (not needed)
    'Ignore2',     # D
    'Ignore3',     # E
    'Ignore4',     # F
    'Ignore5',     # G
    'Result',      # H – TARGET
    'Ignore6',     # I
    'Ignore7',     # J
    'Ignore8',     # K
    'Planets combo',     # L
    'Intensity label',   # M (not used, optional)
    'Planets/Intensity', # N
    'Intensity degree',  # O – numeric
    'Match Date',        # P (optional)
    'Ignore9',           # Q
    'Match Stat'         # R (optional)
]

# Load Excel with no headers and manually apply names
df = pd.read_excel("aHistorical_01012024_02142025.xlsx", header=None, names=columns)

# Strip whitespace just in case
df.columns = df.columns.str.strip()

# Drop rows where required columns are missing
required_cols = ['Result', 'Planets combo', 'Intensity degree', 'Planets/Intensity']
df = df.dropna(subset=required_cols)

# Encode
le_result = LabelEncoder()
le_planets = LabelEncoder()
le_symbols = LabelEncoder()

X = pd.DataFrame({
    'planets': le_planets.fit_transform(df['Planets combo']),
    'intensity': df['Intensity degree'].astype(float),
    'symbols': le_symbols.fit_transform(df['Planets/Intensity'])
})
y = le_result.fit_transform(df['Result'])

# Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save
joblib.dump(model, "rf_model.pkl")
joblib.dump(le_result, "le_result.pkl")
joblib.dump(le_planets, "le_planets.pkl")
joblib.dump(le_symbols, "le_symbols.pkl")

print("✅ Model and encoders saved successfully.")
