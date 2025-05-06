### --- FILE: predict_all.bat ---
@echo off
setlocal enabledelayedexpansion

echo ============================================ > predictions_log.txt
echo Running predictions on all daily files... >> predictions_log.txt
echo ============================================ >> predictions_log.txt

for %%F in (Daily__*.xlsx) do (
    set "predicted=%%~dpnF_predicted.xlsx"

    echo -------------------------------------------- >> predictions_log.txt
    echo Processing: %%F >> predictions_log.txt

    if exist "!predicted!" (
        echo Skipping already predicted: %%F >> predictions_log.txt
        echo Skipping already predicted: %%F
    ) else (
        echo Predicting: %%F >> predictions_log.txt
        echo Predicting: %%F
        py predict_daily.py "%%F" >> predictions_log.txt 2>&1
    )
)

echo -------------------------------------------- >> predictions_log.txt
echo ✅ All predictions complete. >> predictions_log.txt
echo Done. Log written to predictions_log.txt

pause
