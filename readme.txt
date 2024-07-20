Build and Deploy Process
------------------------
See https://packaging.python.org/tutorials/packaging-projects/ for a tutorial.

Update Tools
------------
python3 -m pip install --upgrade setuptools wheel
python3 -m pip install --upgrade twine

Build Deployment
----------------
rm dist/*
python3 setup.py sdist bdist_wheel

Upload to PyPi
--------------
Note that twine complains about a missing keyring backend. You can ignore this.

To live
    python3 -m twine upload dist/*
To test
    python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Installing in Consuming Environment
-----------------------------------
From Live PyPi
    pip3 install lsm9ds1-rjg

From Test PyPi
    pip3 install--index-url https://test.pypi.org/simple/ lsm9ds1-rjg