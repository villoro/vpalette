:: ------------- Unittest + coverage --------------------------------------
nosetests --with-coverage --cover-package=v_palette --cover-erase --cover-inclusive
pause

:: ------------- Pylint ---------------------------------------------------
pylint test
cd v_palette
pylint v_palette
cd..
pause
