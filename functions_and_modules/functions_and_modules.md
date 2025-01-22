# Functions and Modules

Review:

1. Function definition: Circles and ellipses
2. Documentation: Use NumPy-style docstrings
3. [Module structure](module_structure.py)
4. Importing modules

# Basic Project/Package Structure

We will discuss this in more detail, when we get to the module on Distributing Software, but when you form project teams and create your project repository, start out with the following structure:

application_or_package_name

```
repository-name/
├── README.md
├── application_or_package_name/
│   ├── __init__.py
│   └── <code files>
├── docs/
└── tests/
```

Note the the repository name does not have to be the same as the application or package name, although it often is. For example, the PySAL project uses `pysal` as it's organization name, repository name, *and* package name.

For very simple packages, your code module and tests module may be a single file in the root directory. All of you will almost definitely be creating more complex packages or applications than that.

If your project is a Python **package**, your root directory should have a `pyproject.toml` file, which contains metadata about package building. This would be omitted for a GUI application.

When you first form project teams and create a project repository you should:

1. Choose a license.
2. Set up the repository with the Python .gitignore.
