SetWorkingDir, C:\Users\your_username\your_working_folder  ; What folder do you want everything to happen in?

Python = python
CompileScript = C:\path\to\compile_with_bib.py  ; Full path to python script in this repository
FullOutputPath = C:\path\to\latest_autoexport.tex.txt  ; Full path to the exported scrivener LaTeX file. Scrivener currently ends everything in in .txt regardless of settings, so best to make the full path end in .txt
BaseName = latest_autoexport  ; not strictly necessary - my Python script uses it because TexMaker passes it in, so it can be compatible with both

^!c::  ; Ctrl Shift C to compile automatically.
	WinActivate, ahk_exe scrivener.exe
	SetKeyDelay, 15
	
	Sleep, 1000  ; Delay right off the bat because otherwise we might lift control from our initial shortcut *after* the next line runs, at which point, the whole thing falls apart
	Send, {LControl Down}
	Sleep, 100
	Send, {LShift Down}
	Sleep, 100
	Send, {e}  ; send ctrl shift e to scrivener (compile command)
	Sleep, 100
	Send, {LShift Up}
	Sleep, 100
	Send, {LControl Up}
	Click, 426, 736, 0
	Sleep, 1500
	WinActivate, Compile ahk_class Qt5QWindowIcon  ; Activate the compile windw
	Send, {Enter}
	Sleep, 200
	Click, 418, 705, 0  ; Make sure we're clicking into the window - this should probably be adjusted
	Sleep, 3500
	WinActivate, Save As Plain Text ahk_class #32770  ; activate the save as window once it comes up, enter the path.
	Send %FullOutputPath%
	Send, {Enter}
	Sleep, 1500
	if WinExist("Confirm Save As ahk_class #32770")  ; If we're overwriting something, confirm that we want to
	{
		WinActivate
		Send, {Left}
		Sleep, 200
		Send, {Enter}
	}
	Sleep, 5000
	Run %Python% %CompileScript% %BaseName% %FullOutputPath%   ; send the script over to python to compile
	Return
	
^!l::  ; enable ctrl shift l to compile only. This helps when I leave the PDF open and only this part fails.
	Run %Python% %CompileScript% %BaseName% %FullOutputPath%
	Return
