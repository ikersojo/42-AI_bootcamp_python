# module00
---
# ex00: $PATH
## basic info
Python Version: 3.7.x (recommended)

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
which python
python -V
python -c "print('Hello World!')"
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
