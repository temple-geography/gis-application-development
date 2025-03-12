# Creating Documentation for Python with Sphinx

Sphinx is designed to generate documentation for self-contained code in Python. It can automatically generate documentation based on **docstrings** that you write within each class and function. You can also include additional documentation about the project, such as an installation guide, getting started, tutorials, etc.

This exercise utilizes Sphinx and the Sphinx RTD (Read the Docs) theme, which have already been installed in the course conda environment. If you are working in a different environment they can be installed with:

```sh
conda install sphinx sphinx_rtd_theme
```


## Writing Docstrings in Your Code

We will use NumPy-style docstrings. NumPy and Google-style docstrings are supported by the Napolean extension. I find both of them to be far preferable to the default reStructuredText docstring format recommended by [PEP 287 – reStructuredText Docstring Format](https://peps.python.org/pep-0287/).

I will only cover NumPy-style docstrings. Information on these formats is available in the Sphinx documentation:

* reStructuredText docstrings: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>
* NumPy and Google docstrings: <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>

A basic template for a NumPy docstring is:

```python
def my_func(arg1, arg2 = None):
    """This is a short summary.

    This is an extended summary.

    It can span multiple lines, but should be kept short. Extensive discussion can happen in Notes or other sections.
   
    Parameters
    --------------------------

    arg1 : type
        Some variable
    arg2 : type, optional
        Some other variable

    Returns
    --------------------------
    type
        Information about return value.

    Notes
    -----------------------------
    You can now include paragraphs and paragraphs of additional explanation.

    Examples
    ------------------------------

    A place for code examples:
   
    >>> my_func(x, y)
    return_value

    Explanation of example.
    """

    pass
```

At the very least, your docstring should include these three elements:

* A **Short Summary**.
* **Parameters** (or a statement that there are no input parameters).
* **Return** type and value (or a statement that the function or method returns None).

NumPy supports a total of 15 different sections *which will not all be covered here*. The full list is available at the [NumPy Style Guide Docstring Standard](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard).

Some useful sections are:

* **Extended Summary:** From the documentation, "This section should be used to clarify *functionality*, not to discuss implementation detail or background theory, which should rather be explored in the Notes section below."
* **Other Parameters:** Use to document little-used parameters *only if the function has a large number of parameters*.
* **Notes:** A more extensive discussion of the algorithm, implementation, etc.
* **References:** You may be implementing an algorithm, method, calculated measure or index, etc., from an academic source. You can list such sources in the References section.
* **Examples:** Code examples of typical use.

If you are documenting a **class**, your class may have **attributes** and **methods**.

* The **Parameters** section should include the parameters found in the class's `__init__` method, i.e. the parameters used by the instance constructor.
* If your class included non-method attributes, you should include an **Attributes** section after the Parameters section.
    * Individual attributes may have their own docstrings in the setter/getter methods, in which case they should be merely listed by name in the Attributes section. Otherwise, use the same format as in the Parameters section to show an attribute's type and meaning.
* You usually do not need a **Methods** section. Methods should be documented as any other function.

In all of the above cases of class docstrings, omit `self` as a parameter.

## Turning your docstrings into html

#### Step 1: Preparations

Before using Sphinx, it's important to create a directory specifically for the files that will be generated. Open the terminal, activate the correct conda environment, and `cd` to the directory with your code and documentation files.

#### Step 2: Run Quickstart

Run `sphinx-quickstart`. You will be asked questions about the configurations that you'd like to use.

The first question is whether you want to create a "_build" subdirectory, or separate "source" and "build" directories. The default is to *not* create separate source and build directories, and that is how I will demo it in class.

The quickstart will create a file called "conf.py" in your working directory that controls the main configurations for your documentation. It will also create a master document called "index.rst", which will function as the outline for your welcome page and contain the root of the table of contents tree.

#### Step 3: Edit Configurations

If your Python scripts are in another directory, you need to tell Sphinx where to find them. Open up the "conf.py" file and navigate to the path setup. You will want to uncomment the import statements and the sys.path.insert statement. Put the path for the folder with your python files into `sys.path.insert(0, os.path.abspath('path goes here'))`

The extensions list is empty by default (find `extensions = []` in the configuration script). In order for Sphinx to automatically interpret and generate documentation based on docstrings, we need to add `'sphinx.ext.autodoc'` to the extensions list. We will use NumPy-style docstrings, so also add `'sphinx.ext.napoleon'` to the extensions. (You would do the same thing for Google-sytle docstrings.)

If you will add a large number of extensions, you may put them on separate lines like this:

```python
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon"
]
```

For aesthetics, you can change the html theme as well. Try `'sphinx_rtd_theme'` instead of the default (currently alabaster).

#### Step 4: Creating .rst Files from Python Files

Run `sphinx-apidoc`. To specify output path and sourcepath, use `-o . .`. This command specificaly would use the current folder as the output path and look for .py files in the current folder. This will create an .rst file for each python file based on the docstrings in them. 

#### Step 5: Adding .rst Files to your Table of Contents

In order for the generated .rst files to be displayed, you need to add them to the table of contents in the index.rst file. You can list them in the order they should appear under the existing toctree. You can also add more toctrees to split your files into multiple groups.


#### Step 6: Generate the HTML Documentation

Run `make html`. This will build the html pages from the .rst files in your working directory.


## Hosting your documentation using GitHub and Read the Docs

You can host documentation for free online using [ReadtheDocs.org](https://readthedocs.org/). If you push your documentation to your github repo, you can logon to Read the Docs and host it from your github repo. Read the docs even supports versioned documentation and has instructions on how to utilize it. 

You might not want to push everything from your working directory to your repo. You will want to use a `.gitignore` file to specify the files and folders that won't be pushed. 

After you've added, committed, and pushed your repo, you can logon to Read the Docs and import your repo. It will look for the appropriate files in your repo to build and host the documentation.
