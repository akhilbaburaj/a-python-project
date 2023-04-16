# My Kalculator

Creates a very basic module of python using build functions. To automate the full process we use the following things.

* Python version - py37 - 3.11 (You can restrict to what you want but I wanted to test against all these version)
* pyproject.toml - New Standard to create builds (I wanted to skip setup.py and setup.cfg)
* Flake8 - Code Quality Check (can be added with plugin but this example does not use them)
* Pylint - Code Quality Check (Has similar behavior as Flake8 but has its quality score)
* Pytest - Run testing again the code (Verify if your functions work)
* Tox - Wrapper to excute all the above (Saves times by running 1 command)


# Functions available:

```
import kalc.calc as my_kalc
my_kalc.add2numbers(3,7)
my_kalc.substract2numbers(1,6)
my_kalc.divide2numbers(1,4)
my_kalc.multiply2numbers(3,8)
```


## Editible mode:
Start by making a venv and while inside the directory where pyproject.toml is present install the module in editable mode.
` pip install -e .`


## Run Tox:
Run tox from the folder where `tox.ini` is present and it will execute all the steps sequentially. I have knowingly not fixed the syntax errors identified `pylint` so expect the code quality to be bad. 

## Things youu realise cause you are bad in coding:

Note: My pip module is called `my-kalculator` but the actual functions of the module is inside `kalc`.
```
/a-python-project$ tree -d
.
└── my_kalculator    <<< actual project name >>>
    ├── dist
    ├── src
    │   ├── kalc     <<< actual module with code >>>
    └── tests
```

Thus, importing as `my_kalculator` does not work since there is actually no such code directory.
```
>>> import my_kalculator
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'my_kalculator'
```

Also, I don't have any code/import under `__init__.py` to refer to the functions such as `add2numbers` thus, I cannot directly refer them from the module.
```
>>> import kalc
>>> kalc.add2numbers(4,5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'kalc' has no attribute 'add2numbers'
```

Hence, I had to explicitly refer the py file that has the code. Making changes to accomodate such mistakes would execution requirement such as. The below works but make be it is not the ideal way you should approach.
```
>>> import kalc.calc
>>> kalc.calc.add2numbers(4,5)
Kalculating...: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:01<00:00, 98.91it/s]
Result is 9
>>> exit()
```
