@ECHO OFF
ECHO [INFO] This script checks ^& prepares the environment for project [RAG practice].
ECHO [TIP_]------ Please ensure Python is installed!
ECHO [TIP_]------ Please ensure Conda is installed!

ECHO [INFO] Continue with the environment setup?
ECHO.
CHOICE /c YN /m "[Y]continue OR [N]exit" /n

IF %errorlevel% equ 2 EXIT /b
IF %errorlevel% equ 1 (
    conda create -n ragtest python=3.11.13
    conda activate ragtest
    python -m pip install -r env.txt
)

ECHO [INFO] BAT execute complete.
PAUSE