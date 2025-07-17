@ECHO OFF
ECHO [INFO] This script run tests for project [RAG practice].
ECHO [TIP_]------ Please ensure the ENV is prepared!

:START
call conda activate ragtest
cd /d C:\Users\14545\Desktop\001_project\ReConsciousTy\tests\00_RAG_practice\RAGpack
python EmbeddingRAG.py

ECHO [INFO] BAT execute complete.
ECHO [INFO] re-run the ragtest or not?
ECHO.
CHOICE /c YN /m "[Y]re-run OR [N]exit" /n
IF %errorlevel% equ 2 EXIT /b
IF %errorlevel% equ 1 goto :START

PAUSE