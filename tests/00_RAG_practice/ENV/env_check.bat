@ECHO OFF
ECHO [INFO] This script checks ^& prepares the environment for project [RAG practice].
ECHO [TIP_]------ Please ensure Python is installed!
ECHO [TIP_]------ Using virtual environment (Conda for example) is recommended!

ECHO [INFO] Continue with the environment setup?
ECHO.
CHOICE /c YN /m "[Y]continue OR [N]exit" /n

IF %errorlevel% equ 2 EXIT /b
IF %errorlevel% equ 1 (
    python --version
    python -m pip install --upgrade pip
    python -m pip install -r env.txt
)

ECHO [INFO] BAT execute complete.
PAUSE