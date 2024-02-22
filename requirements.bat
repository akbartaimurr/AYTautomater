@echo off

REM Install requirements
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install requirements
    exit /b 1
)

REM Run Python file
python text-to-speech.py
IF %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to run the Python file
    exit /b 1
)

echo Finished running the Python file
exit /b 0
