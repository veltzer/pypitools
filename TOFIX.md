# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pypitools/common.py:166` - `package_it()` (and `upload_by_setup` at `common.py:48`, `register_by_setup` at `common.py:122`, `install_from_local` at `src/pypitools/main.py:32`, `get_package_fullname` at `src/pypitools/name_utils.py:15`) all run `python setup.py ...`, but every fleet package (this one included, `pyproject.toml:2`) is hatchling/pyproject with no `setup.py`, so `package`, `check`, `upload`, `register`, `install_from_local` cannot work at all; port packaging to `python -m build` (or `uv build`) and read name/version from `pyproject.toml`, or formally retire the tool in favour of `uv build`/`uv publish`, which is what the fleet actually uses.
- `src/pypitools/common.py:131` - `twine register` and `setup.py register`/`upload` (`common.py:123`, `common.py:58`) are endpoints PyPI removed years ago; drop the `register` endpoint and the `SETUP`/`TWINE` register methods (`src/pypitools/configs.py:18-22`).

## Medium

- `src/pypitools/process_utils.py:32` - when the child exits non-zero, `ValueError` is raised before the `PYTHONWARNINGS` restore at `process_utils.py:39-43`, leaking `PYTHONWARNINGS=ignore` into the rest of the process; move the restore into a `try/finally`.
- `src/pypitools/main.py:185` - `bump` promises to check, bump, commit, tag, push and upload but only calls `check_if_needed()` (the real step is commented out at `main.py:195`); implement it or remove the endpoint.
- `src/pypitools/main.py:47` - `install_from_local` hardcodes `--quiet` and then adds it again when `pip_quiet` is set (`main.py:49-50`), so `--pip-quiet=false` has no effect; remove the hardcoded flag.
- `src/pypitools/main.py:41` - input validation via `assert` (stripped under `python -O`), and the message says "too many files" even when `dist/` is empty; raise a real error with an accurate message.
- `pyproject.toml:40` - `wheel` and `setuptools` are runtime dependencies only because of the `setup.py` code paths; drop them once packaging is ported.

## Low

- `src/pypitools/name_utils.py:29` - the wheel filename is `<fullname>-py3-none-any.whl`, but wheel names normalise `-` to `_` in the project name, so any dashed package name yields a path that does not exist; build the name from the normalised project name.
- `src/pypitools/common.py:16` - `check_by_twine` with both `upload_sdist` and `upload_wheel` off runs `twine check` with no files; and success is judged by counting stdout lines (`common.py:28-29`) instead of the exit code; rely on `check_call_collect`'s return-code check.
- `src/pypitools/main.py:97` - the `upload` docstring says behaviour can be overridden via a `pypi.cnf` file; no code reads such a file; fix the docstring.
- `doc/TODO.txt:1` - items (build via `python -m build`, gemfury git push, bumpr) are stale relative to the fleet's `uv build`/`uv publish` process; prune once the tool's future is decided.
