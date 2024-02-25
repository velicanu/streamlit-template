# streamlit-template
Template for streamlit apps. Comes with CI having `ruff` and `pytest` ready to
go. Click the `Use this template` button to get started.

## Setup

In a virtual env, Install requirements via:
```
pip install uv
uv pip install -r requirements.txt
```

## Usage

The streamlit app can be started via:
```
streamlit run src/app.py
```

## Tests

Tests are run via pytest:

```
pytest
```

Extra configuration should go into the pyproject.toml file.

## Updating requirements

To update requirements, add/remove what you need into `requirements.in` , then use
uv to `pip compile` a new requirements file.

```bash
# only need to do this once
pip install uv

# edit the requirements.in file
uv pip compile requirements.in -o requirements.txt

# a new requirements.txt file is generated, install the usual way
pip install -r requirements.txt
```
