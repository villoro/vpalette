:: create the files
python setup.py sdist bdist_wheel

:: upload to pip
python -m twine upload dist/*
