run guide - install and run project's code

WINDOWS 10/11 x86_64 64 bit version

-- Installation --
create an empty working folder on the desktop or anywhere accessible

1. install python
 -place the python zip inside the working folder
 -unzip python zip and place the extracted python folder in the empty working folder
2. install change_dir.py script (moves the interpreter current directory to the working area)
 -put change_dir.py in the python folder
run python.exe
run on python >> exec(open("change_dir.py").read()) <<
this commandis important as it it enables you to read scripts in the working directory instead of inside the embeded python directory.
4. install pip
run on python >> exec(open("change_dir.py").read()) <<
there should be logs of the installation and new files inside the python folder. Pip is now installed
the command window should close, if not close it

*from the get-pip script online on github. credits to the contributors who made it.
https://github.com/pypa/get-pip

Now you should have pip installed on the embeded version of python

4. install requirements for the project's script 

run python.exe
run on python >> exec(open("change_dir.py").read()) <<
pip install -r requirements.txt
