My HPI Modules

## Installation

Requires `python3.7+`

To install, this first requires you first install [`karlicoss/HPI`](https://github.com/karlicoss/HPI). For example:

```
# install karlicoss HPI
git clone https://github.com/karlicoss/HPI ./HPI
python3 -m pip install -e ./HPI

# install my HPI
git clone https://github.com/{{ cookiecutter.username }}/HPI ./HPI-{{ cookiecutter.username }}
python3 -m pip install -e ./HPI-{{ cookiecutter.username }}
```

### Tests

```bash
pip install -e '.[testing]'
mypy -p my
pytest
```
