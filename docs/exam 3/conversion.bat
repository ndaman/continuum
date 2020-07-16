@ECHO OFF
SETLOCAL
SET "sourcedir=E:\Downloads\Sync\Teaching\Mechanics of Materials\lectures\exam 3"
PUSHD "%sourcedir%"
FOR /f "delims=" %%a IN (
 'dir /b /s /a-d *.tex'
 ) DO (
 IF NOT EXIST "%%~dpna.md" pandoc "%%a" -f latex --ascii -t markdown_github -o "%%~dpna.md"
 )
)
popd
GOTO :EOF
