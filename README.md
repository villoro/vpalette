# Palettes
[![Build Status](https://travis-ci.com/villoro/v-palette.svg?branch=master)](https://travis-ci.com/villoro/v-palette)
[![codecov](https://codecov.io/gh/villoro/v-palette/branch/master/graph/badge.svg)](https://codecov.io/gh/villoro/v-palette)

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
