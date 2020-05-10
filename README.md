# Palettes
[![Build Status](https://travis-ci.com/villoro/v-palette.svg?branch=master)](https://travis-ci.com/villoro/v-palette)

Utility to easily use palettes

## Colors

There are two palettes **material** and **flat**.

### Material Colors
<img src="https://raw.githubusercontent.com/villoro/v-palette/master/assets/material_grid.svg?sanitize=true">

You can view them in a [svg file](https://github.com/villoro/v-palette/blob/master/assets/material_grid.svg). More info at [material.io](https://material.io/design/color/the-color-system.html#color-usage-palettes).

### Flat Colors
<img src="https://raw.githubusercontent.com/villoro/v-palette/master/assets/flat_grid.svg?sanitize=true">

You can view them in a [svg file](https://github.com/villoro/v-palette/blob/master/assets/flat_grid.svg). More info at [html color codes](https://htmlcolorcodes.com/color-chart/flat-design-color-chart/).

## Installation

You can install it with pip by running:

    pip install v-palette


## Usage

You can retrive one color or a list of colors using `get_colors` function:

```python
from v_palette import get_colors

# 1. Retrive one color
get_colors(("red", 100)) # out: '#FFCDD2'

# 2. Retrive some colors
get_colors([("red", 100), ("blue", 100)]) # out: ['#FFCDD2', '#BBDEFB']

# 3. Retrive colors from others palettes
get_colors([("emerald", 100), ("silver", 100)]) # out: ['#D5F5E3', '#F2F3F4']
get_colors([("emerald", 100), ("silver", 100)], palette="flat") # out: ['#D5F5E3', '#F2F3F4']
```

> The parameter `palette` is not necessary if the color you want is not present in the material palette. Since if the color is not found in the default palette it will look at the others palettes.

## Development

This package relies on [poetry](https://villoro.com/post/poetry) and `pre-commit`. In order to develop you need to install both libraries with:

```sh
pip install poetry pre-commit
poetry install
pre-commit install
```

Then you need to add `poetry run` before any python shell command. For example:

```sh
# DO
poetry run python master.py

# don't do
python master.py
```

## Authors
* [Arnau Villoro](https://villoro.com)

## License
The content of this repository is licensed under a [MIT](https://opensource.org/licenses/MIT).

## Nomenclature
Branches and commits use some prefixes to keep everything better organized.

### Branches
* **f/:** features
* **r/:** releases
* **h/:** hotfixs

### Commits
* **[NEW]** new features
* **[FIX]** fixes
* **[REF]** refactors
* **[PYL]** [pylint](https://www.pylint.org/) improvements
* **[TST]** tests
