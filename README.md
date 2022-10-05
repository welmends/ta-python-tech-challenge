## Python Challenge - Team International

Technical Challenge Senior Python Engineer

### Getting started

- Install Python version 3.6 or greater
- Use Makefile to run the project
- Run the default application:
  - `make run`
- Run the test cases:
  - `make test`
- Run the performance validation:
  - `make performance`

### Project structure

    .
    ├── app
    |   ├── performance
    |   |   ├── __init__.py
    |   |   └── performance.py
    |   ├── src
    |   |   ├── __init__.py
    |   |   ├── data_capture.py
    |   |   └── stats.py
    |   ├── test
    |   |   ├── __init__.py
    |   |   ├── test_data_capture.py
    |   |   └── test_stats.py
    |   ├── __init__.py
    |   └── app.py
    ├── .gitignore
    ├── LICENSE
    ├── Makefile
    └── README.md

### Notes

- The main logic is haddle by the DataCapture and Stats classes.
- The project was written following the best practices, such as encapsulation, DRY, and YAGNI.
- Both DataCapture and Stats classes have documentation built-in.
- Some tests cases were written with a greate coverage about the project.
- `add`, `less`, `greater` and `between` operations have time complexity of `O(1)`.
- `build_stats` have time complexity of `O(1)`, considering that all values will be less then 1,000 and this is a constant.
- Some performance validation about the time complexity were implemented.
