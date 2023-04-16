# My Kalculator

Creates a very basic pip module of python and runs tests and lint checks against them. To automate the full process we use the following things:

* Python version(s) - python3.7 <-> python3.11 (You can restrict to what you want. Make sure the host these version else, it will fail)
* pyproject.toml - New Standard to create builds (I wanted to skip setup.py and setup.cfg)
* Flake8 - Code Quality Check (can be added with plugin but this example does not use anything fancy)
* Pylint - Code Quality Check (Has similar behavior as Flake8 but has its own quality score and rules)
* Pytest - Run testing again the code (verify if your functions work/run)
* Build - Python package builder (Needed only when you want to Build a `tar.gz` or `whl` file)
* Setuptools - Wrapper to do package building using the build module.
* Tox - Wrapper to excute all the above (Our automated way to all the above as per a configuration file)


# Functions available:

```
import kalc.calc as my_kalc
my_kalc.add2numbers(3,7)
my_kalc.substract2numbers(1,6)
my_kalc.divide2numbers(1,4)
my_kalc.multiply2numbers(3,8)
```



## Editible mode:
When working with modules you want to iterate and test quickly. To do so, build using editable mode. Now, changes done to file can be quickly tested. It is best to have a venv to do this.

I use `python3` instead of python cause the host's `python` may refer to some other version. Within venv `python3` tends to always be the intended version.

Create Venv : `python3 -m venv venv`
Source Venv : `~/venv/bin/activate`
Update Pip : `python3 -m pip install --upgrade pip`
Install Package : ` pip3 install -e .`


## Run Tox:
Run tox from the folder where `tox.ini` is present and it will execute all the steps sequentially. I have knowingly not fixed the syntax errors identified `pylint` so expect the code quality to be bad. 

## Things you realize cause you are new to all of this:

Note: My pip module name is called `my-kalculator` while the project name is `my_kalculator`. Also, the actual functions of the module is inside `kalc`.
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

Also, I don't have any code/import under `__init__.py` to refer/import  the functions such as `add2numbers` thus, I cannot directly use them from the module.
```
>>> import kalc
>>> kalc.add2numbers(4,5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'kalc' has no attribute 'add2numbers'
```

Hence, I had to explicitly refer the py file(code_dir.file_name) that has the code. The below method works but it is not the ideal way you should approach.
```
>>> import kalc.calc
>>> kalc.calc.add2numbers(4,5)
Kalculating...: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:01<00:00, 98.91it/s]
Result is 9
>>> exit()
```
