@echo off
setlocal enabledelayedexpansion

:: Define the list of folders to create
set "folders=bullet blast2 preshoot"

:: Loop through each subfolder in the current directory
for /d %%d in (*) do (
    echo Creating folders in %%d
    for %%f in (%folders%) do (
        mkdir "%%d\%%f"
    )
)

echo Done.
pause