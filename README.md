# Scrivener LaTeX Automation for Windows
These scripts enable a single keystroke to:
1. Compile a Scrivener document
2. Run that file through LaTeX with a bibliography
3. Open the PDF for viewing

I was tired of the manual export while working in Scrivener, which meant I didn't export often, which meant I often had hard-to-find LaTeX errors. This pipeline lets me preview relatively quickly to make sure I'm still on track.

## Notes
First, these scripts likely won't be 100% of what anyone else needs. I only made them somewhat generalizable and they're not my best code, but they're good enough to share in case anyone else finds them useful. I tried to comment at least the most important things. You may need to do some tweaking, but **these scripts should be a good starting point for people looking to quickly compile LaTeX documents from Scrivener on Windows**.

## Setup
You'll need both AutoHotkey 1 and Python 3 on your computer in order to run this full pipeline. Autohotkey handles the Scrivener export and Python handles the LaTeX runs, so install whichever you need if you're not going to use all of this code.

1. Make sure your Scrivener compile dialog is set up the way you want it - this just exports the settings you had the previous time you compiled
2. Download both the .ahk and .py scripts in this repository.
3. Configure the variables at the top of both scripts in your text editor of choice - each one has paths specific to the projects you're working on, where your LaTeX installation is, etc, that you'll need to edit to match your computer.
3. Run the .ahk script with AutoHotKey - a macro utility for Windows. The script will automatically go through the keystrokes/typing/clicking needed to export for you. This script was written and tested with AutoHotkey 1.1.32 on Windows 10 using the Scrivener 3 Beta.

## Usage
Once it runs, you can use the keystroke Ctrl Shift C to run the whole pipeline and the keystroke Ctrl Shift L to just run the LaTeX compilation. The latter command is for the situation where LaTeX failed, but you don't need to re-export from Scrivener.
