# 🌀 tennis-pendulum-predictor
A custom machine learning model to predict OVER or UNDER tennis match results using symbolic planetary patterns, intensity degrees, and astrological wave signals.

This Python-based system analyzes historical match outcomes and trains a forecasting model designed to capture the "pendulum effect" in astrological symbols—each symbol's tendency to swing between streaks of wins (OVER) and losses (UNDER).

## ✨ Features
- Astrology-Informed Forecasting: Utilizes unique astrological patterns from Columns L, M, and N (up to 768 unique combinations).
- Custom Model Architecture: Focused on capturing trend reversals and signal saturation using wave analysis.
- Daily Predictions: Accepts Excel files containing match-day data and outputs OVER/UNDER predictions per player.
- Windows-Compatible: Fully runnable on Windows environments via Python scripts.
- Batch Processing: Easily processes multiple daily prediction files with consistent formatting.

##🏆 Contest-Based Development
This model was developed for a $250 guaranteed-prize contest, with the objective of building the most accurate predictor (target: ≥70% accuracy).
Participants are evaluated against 40 unseen daily result files. The top performer will win and may be invited for additional projects.

## 📂 Project Files
- train_model.py: Trains the model on historical labeled Excel data.
- predict_daily.py: Predicts OVER/UNDER for each player using daily match files.
- data/: Contains sample historical and test-day Excel files for training and validation.

## 🔍 Goal
To identify and model hidden patterns in astrological symbols and intensity signals that correlate with match results. The tool aims to forecast when these symbols shift behavior—much like predicting tides in a pendulum swing.
