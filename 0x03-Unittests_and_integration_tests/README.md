# 0x03. Unittests and Integration Tests

## Overview

Unit testing is the process of verifying that a particular function returns the expected results for different inputs. Unit tests are designed to test standard inputs and corner cases. They should focus solely on the logic within the tested function, mocking external calls such as network requests or database interactions.

The goal of a unit test is to determine whether a function works as expected, assuming that everything outside of it works as intended.

Integration tests, on the other hand, test an entire code path end-to-end, ensuring that all components work together correctly.

### Execute Your Tests

```bash
$ python -m unittest path/to/test_file.py
```

## Resources

Read or watch:

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/44354037/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Learning Objectives

By the end of this project, you should be able to explain:

- The difference between unit and integration tests.
- Common testing patterns such as mocking, parameterizations, and fixtures.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project is mandatory.
- Code should follow the `pycodestyle` style guide (version 2.5).
- All files must be executable.
- All modules should have documentation.
- All classes should have documentation.
- All functions (inside and outside a class) should have documentation.
- Documentation must explain the purpose of the module, class, or method.
- All functions and coroutines must be type-annotated.

## Tasks

### 0. Parameterize a Unit Test

Write a unit test for `utils.access_nested_map` using `@parameterized.expand` for various inputs.

- **File:** `test_utils.py`

### 1. Parameterize a Unit Test with Exceptions

Write a unit test for `utils.access_nested_map` that checks if a `KeyError` is raised for certain inputs using `@parameterized.expand`.

- **File:** `test_utils.py`

### 2. Mock HTTP Calls

Write a unit test for `utils.get_json`, using `unittest.mock.patch` to mock `requests.get`.

- **File:** `test_utils.py`

### 3. Parameterize and Patch

Write a unit test for a memoized method using `unittest.mock.patch`.

- **File:** `test_utils.py`

### 4. Parameterize and Patch as Decorators

Write a unit test for `GithubOrgClient.org` using `@patch` and `@parameterized.expand`.

- **File:** `test_client.py`

### 5. Mocking a Property

Write a unit test for `GithubOrgClient._public_repos_url`.

- **File:** `test_client.py`

### 6. More Patching

Write a unit test for `GithubOrgClient.public_repos`.

- **File:** `test_client.py`

### 7. Parameterize

Write a unit test for `GithubOrgClient.has_license` using `@parameterized.expand`.

- **File:** `test_client.py`

### 8. Integration Test: Fixtures

Write an integration test for `GithubOrgClient.public_repos` using fixtures.

- **File:** `test_client.py`

### 9. Integration Tests

Write integration tests for `GithubOrgClient.public_repos` and `public_repos_with_license`.

- **File:** `test_client.py`
