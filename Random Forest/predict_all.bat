@echo off
echo Running predictions on all daily files... > predictions_log.txt

for %%F in (Daily__*.xlsx) do (
    echo Processing: %%F >> predictions_log.txt
    if exist "%%~nF_predicted.xlsx" (
        echo Skipped: %%~nF_predicted.xlsx already exists >> predictions_log.txt
    ) else (
        py predict_daily.py "%%F" >> predictions_log.txt 2>&1
    )
)

echo All done. Output saved to predictions_log.txt
pause
