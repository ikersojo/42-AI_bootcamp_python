# module00
---
# ex00: $PATH
## basic info
Python Version: 3.7.x (recommended) --> not available in miniconda (for ARM64?), in Urduliz ok, but in my laptop version 3.8 used instead (oldest one).

Norm: [PEP 8 standard](https://www.python.org/dev/peps/pep-0008/)

Norminette: [pycodestyle](https://pypi.org/project/pycodestyle)

## version and environment management

**conda** is a program which allows you to manage your Python packages and different working environments.

### install conda in 42 Urduliz clusters
```
MYPATH="/goinfre/$USER/miniconda3"
curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
sh Miniconda3-latest-MacOSX-x86_64.sh -b -p $MYPATH

$MYPATH/bin/conda init zsh
$MYPATH/bin/conda config --set auto_activate_base false
source ~/.zshrc
```

### install conda in my laptop (macbook pro M1pro - Monterey)
```
brew install --cask miniconda
conda init zsh
conda config --set auto_activate_base false
source ~/.zshrc
```

### setup bootcamp environment
create the environment:
```
conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy
```

and check the environment:
```
conda info --envs
conda activate 42AI-$USER
which python3
python3 -V
python3 -c "print('Hello World!')"
```

to go back to base:
```
conda deactivate
```

## answers.txt
Find the commands to:
- Output a list of installed packages and their versions.
- Show the package metadata of numpy.
- Remove the package numpy.
- (Re)install the package numpy.
- Freeze your python packages and their versions in a requirements.txt file you have to turn-in.

---
# ex01: Rev Alpha

- To import args to the porgram(similar to **argc, argv** in c)
```python
import sys
sys.argv
```

- The arguments in a list can be joined together in a string, usinng the join buil-in method,using a given separator:
```python
# join list elements using " " in-between the elements
	string = " ".join(my_list)

# since we want to skip the first element (0), we start on element 1, using the slice method of a string /list.
	" ".join(sys.argv[1::])
```

- The string modificaation has been done following the same approach as in C exercises (commeneted in src) and using built-in methods to simplify steps:
```python
# a built-in function in python to reverse strings, [start:stop:step] to slice a list. If none, the default value is [from start:to the end: one by one]:
	rev = string[::-1]

# a built-in function to swapcases:
	string.swapcase()

# and they can be combined:
	string[::-1].swapcase()
```

It can be done in a single line:
```python
print(" ".join(sys.argv[1::])[::-1].swapcase())
```

---
# ex02: Rev Alpha

- The try block lets you test a block of code for errors.
- The except block lets you handle the error.
- The else block lets you execute code when there is no error.
- The finally block lets you execute code, regardless of the result of the try and except blocks.

---
# ex03: Functional file

- in function is used to loop through strings or lists:
```python
	for c in s: # each char c in string s
	
	# elif (c == '!' or c == '.' or c == ',' or c == '?'or c == ':' or c == ';'):
	elif (c in '!.,?:;'):
```

- __name__ is an internal variable which stores "__main__" if the .py has been launched or the name of the fail if imported:
```python
if (__name__ == '__main__'):
```
