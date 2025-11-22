# Publish to Test PyPI and PyPI

## Publish to Test PyPI with UV

- **uv publish**

  First, add the Test PyPI index configuration to your `pyproject.toml` under the `[tool.uv.index]` section:

  ```toml
  [[tool.uv.index]]
  name = "testpypi"
  url = "https://test.pypi.org/simple/"
  publish-url = "https://test.pypi.org/legacy/"
  explicit = true
  ```

  Then, you can publish your package to Test PyPI using the following command:

  ```bash
  uv publish --index testpypi --token $TEST_PYPI_API_TOKEN
  ```

  `$TEST_PYPI_API_TOKEN` is your Test PyPI API token stored in your environment variables.

- **uv install test package from Test PyPI**

  First, create a new virtual environment for testing.

  ```bash
  uv venv .venv-test
  source .venv-test/bin/activate
  ```

  Then, install your package (`publish_python_package101` in this case) from Test PyPI.

  ```bash
  uv pip install --index-url https://test.pypi.org/simple publish_python_package101
  ```

  I use `uv pip install` just because I don't want to manage dependencies with uv in `.venv-test`

- **check installation**

  ```bash
  python -c "import publish_python_package101; print(publish_python_package101.__version__)"
  python example/getting_started.py 
  ```

  You should see the version number of your package printed out.


## Tips

- **Publish after version up**

  Before publishing to TestPyPI / PyPI, make sure to update the version number in `pyproject.toml`. For example, if the current version is `0.1.0`, change it to `0.1.1` or any other appropriate version number.

  After updating the version number, just make sure your distribution files are up to date by running:

  ```bash
  rm -rf dist/
  uv build
  ```
