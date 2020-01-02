# pdfLaTeX->BibTeX/biber->pdf
# Adapted from https://tex.stackexchange.com/a/308727

import os
import sys
import subprocess
import shutil

pdf_reader = r"C:\Program Files (x86)\Foxit Software\Foxit PhantomPDF\FoxitPhantomPDF.exe"
texlive_folder = r"c:\users\dsx\programs\texlive\2019\tlpkg"
latex_files_subfolder = "latex_products"
path_items = [os.path.join(texlive_folder, "tlperl", "bin"),
                os.path.join(texlive_folder, "tlgs", "bin"),
                os.path.join(texlive_folder, "tlpkg", "texworks")
             ]
             
# add the TeX components to the path
os.environ["PATH"] += os.pathsep + os.pathsep.join(path_items)
# set up the commands we'll want to run, in order - the arguments come from what
# TeXworks wants to pass to the commands by default if we ran this all manually
# arg order
# 1 basename
# 2 fullname
# 3 synctexoption
# we'll actually ignore basename and get it from fullname

basename = sys.argv[1]
fullname = sys.argv[2]
sync_tex_option = "-synctex=1"  # sys.argv[3]

original_fullname = fullname
rename = False
# Do some parameter reworking to make sure it's always a .tex file
if fullname.endswith(".txt"):
    fullname = fullname[:-4]  # strip it off
    rename = True
if not fullname.endswith(".tex"):
    fullname += ".tex"
    rename = True
if rename is True and os.path.exists(original_fullname):
    if os.path.exists(fullname):
        os.remove(fullname)
    os.rename(original_fullname, fullname)
    
folder, basename = os.path.split(fullname)
os.chdir(folder)
# os.chdir(os.path.join(folder, "latex_products"))

full_latex_files_subfolder = os.path.join(folder, latex_files_subfolder)
if not os.exists(full_latex_files_subfolder):
    os.makedirs(full_latex_files_subfolder)

print("Input Fullname: {}".format(original_fullname))
print("Processed Fullname: {}".format(fullname))

commands = [  # we'll run each of these - we run pdflatex->biber->pdflatex beacause if we don't do that, then bibliographies don't work
    ['pdflatex.exe', sync_tex_option, "-interaction=nonstopmode", fullname],
    ['biber.exe', os.path.splitext(basename)[0]],
    ['pdflatex.exe', sync_tex_option, "-interaction=nonstopmode", fullname],
]

return_code = 0  # start with a normal return code
for c in commands:  # run each command in order
    try:
        print(c)
        output = subprocess.check_output(c)
        print(output)
    except subprocess.CalledProcessError as exc:                                                                            
        print("error code, {}, {}".format(exc.returncode, exc.output))
        return_code = exc.returncode  # if we get any kind of exception, set it as our return code
                                        # but still try to run the rest

print("Opening {}".format(basename.replace(".tex", ".pdf")))
subprocess.Popen([pdf_reader, basename.replace(".tex", ".pdf")])  # open the PDF
try:
    basename_noext = os.path.splitext(basename)[0]
    for potential_file in os.listdir(folder):
        if basename_noext in potential_file and not (potential_file.endswith(".pdf") or potential_file.endswith(".tex")):
            shutil.move(os.path.join(folder, potential_file), os.path.join(full_latex_files_subfolder, potential_file))
except FileNotFoundError:
    print("Error moving files")  # not critical to do anything else - we're just trying to keep things clean
    
close_or_not = input("Review log and press any key to close")
sys.exit(return_code)  # return the last error code we got so that if there was an error we let TeXworks know
    
