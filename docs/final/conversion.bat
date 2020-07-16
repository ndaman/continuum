@ECHO OFF
SETLOCAL
SET "sourcedir=D:\Sync\Sync\Teaching\Mechanics of Materials\lectures\final"
PUSHD "%sourcedir%"
FOR /f "delims=" %%a IN (
 'dir /b /s /a-d *.tex'
 ) DO (
 IF NOT EXIST "%%~dpna.md" pandoc "%%a" -f latex --ascii -t markdown_github -o "%%~dpna.md"
 )
)
popd
GOTO :EOF
