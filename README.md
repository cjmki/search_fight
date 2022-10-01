# Quick setup guide
## Requirements 
Bellow packages should be installed (have not tested on lower version's of python)
- Python 3.8.9
- pip3
## Adding API keys

```
src/util/constants
```

```python
GOOGLE_API_HOST = "www.googleapis.com"
GOOGLE_API_ENDPOINT = "/customsearch/v1"
GOOGLE_API_CX = "a3307a6a039e048b0"
GOOGLE_API_KEY = "" < ---- here

BING_API_HOST = "api.bing.microsoft.com"
BING_API_ENDPOINT = "/v7.0/search"
BING_API_KEY = "" < ---- here
```
## Create virtual env
```bash
python -m venv env # create virtual env
source /{project directory}/env/bin/activate 
```
## Installing dependencies 

```bash
pip install -r requirements.txt
```

## Running project
```bash
# to run the game
python src/main.py "sample query 1" "sample query 2" "sample query 3" 

# to run tests
pytest --no-header -vv
```

# Developer Guide 

# Linter and pre-commit hooks

Project follows the [black](https://github.com/psf/black) coding standerd and uses [flake8](https://flake8.pycqa.org/en/latest/) as linter

```bash
# add pre commit hoooks to git
pre-commit install

#  initial run 
pre-commit run --all-files
```
After this setup, when git user stages changes flake8 will run black coding standards and do linting fixes. 
