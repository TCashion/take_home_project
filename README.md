# take_home_project

This is an interview take-home project.

## Local development 

### Setup

Create and activate a virtual environment:

```shell
python -m venv .venv && source .venv/bin/activate
```

```shell
pip install -r requirements.txt
```

### Execution

Run the filter function:

```shell
python src/adls_client.py
```

### Run tests

Executing the following command in your terminal will run tests:

```shell
python -m pytest -v
```

## CI/CD

This repository has CI/CD steps configured through Github actions. The current steps are as follows: 

- `lint`: an initial `lint` step runs `ruff check` on the codebase to ensure the are no linting errors. If this step fails, the following test step does not run. 
- `test`: the `test` step runs `python -m pytest -v tests/` and uploads the test results as a downloadable artifact. See each action's output under the `Upload artifact` section to get the respective artifact's download URL.