Build and Deploy Process
------------------------
See https://packaging.python.org/tutorials/packaging-projects/ for a tutorial.

Update Tools
------------
python3 -m pip install --upgrade setuptools wheel
python3 -m pip install --upgrade twine

Build Deployment
----------------
python3 setup.py sdist bdist_wheel

Upload to PyPi
--------------
To live
    python3 -m twine upload dist/*
To test
    python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Installing in Consuming Environment
-----------------------------------
From Live PyPi
    python3 -m pip install lsm9ds1-python

From Test PyPi
    python3 -m pip install --index-url https://test.pypi.org/simple/ lsm9ds1-python