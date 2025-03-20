# Creating Documentation for Python with Sphinx

Sphinx is designed to generate documentation Python projects. It can automatically generate documentation based on **docstrings** that you write within each class and function. You can also include additional documentation about the project, such as an installation guide, getting started, tutorials, etc.

## Preparation

This exercise utilizes Sphinx and the Sphinx RTD (Read the Docs) theme, which have already been installed in the `gus8066` conda environment. If you are working in a different environment they can be installed with:

```sh
conda install sphinx sphinx_rtd_theme
```

Additionally, download the contents of this folder, which contain a fake project containing a package directory and a docs directory.

```sh
documentation (stand-in for a project root, can be named anything)
├── docs
│   └── installation.rst
├── my_package
│   ├── areal_weighting.py
│   ├── binary_method.py
│   └── __init__.py
└── sphinx_getting_started.md (this tutorial, not needed)
```

This follows the standard Python package structure that we saw in the workshop on [Functions and Modules](/functions_and_modules/functions_and_modules.md). We omit the `tests` directory and other standard contents.


## Generating Basic Documentation

Sphinx can be used to write documentation for *anything* using [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) files. Thus, we will start with a basic workflow.

### Initializing a Documentation Project

Before you can generate documentation, Sphinx requires source files, an output directory, and some basic configuration information.

Sphinx provides `sphinx-quickstart`, a utility which creates several required files and configurations. Open a terminal, activate the `gus8066` environment, and `cd` to the `docs` folder (that is, the folder that contains the `installation.rst` file).
Then run `sphinx-quickstart`.

You will be asked the following questions:
 
1. `> Separate source and build directories (y/n) [n]:`
    * Hit `Enter` to accept the default, which will create a `_build` subdirectory. The output (build) directory can be anything, *but `docs/_build` is in the standard Python `.gitignore`, so you should accept this default.
2. `> Project name:` This can be anything.
3. `> Author name(s):` Put your name.
4. `> Project release []:` This is a fake package, so you can put anything, such as `0.1`.
5. `> Project language [en]:` Hit `Enter` to accept the default.

Look in your docs folder. You will see that several new folders and files have been created.

### Editing Source Files

Sphinx source files use [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). We are starting with one source file, `installation.rst`. It has fake text describing (not really) how to install your Python package or application. Look at it now.

Open `index.rst`, a file created by `sphinx-quickstart`. This is the source for the home page of your documentation. The default content of `index.rst` is:

```rst
.. my_project documentation master file, created by
   sphinx-quickstart on Wed Mar 19 12:33:08 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

my_project documentation
========================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:
```

Some lines begin with two dots (`..`). This is the beginning of a **directive**. A complete directive is written in the form `..<directive>::`. Note that the top block starts with two dots, but does not end with the double colon. This is a comment, and will not appear in the output.

At the bottom is the **toctree** directive. This is where you provide links to other files in your documentation. The file name is provided without an extension. We want our installation instructions to appear in the table of contents, so we add the filename `installation` after the toctree header. The indentation should be at the same level as the rest of the block, which, oddly (for those of us familiar with Markdown) is *three* spaces. Edit the file now. The results should look like this:

```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
```

Save and close the file.

### Generating and Viewing the Documentation

Using Sphinx to generate the documentation is easy. In the terminal, with `docs` as the current directory, just use the command:

```sh
make html
```

The documentation has now been generated as HTML in `_build/docs`. The file `index.html` is the home page, so open this in your browser. Note that the section title "How to use this module" from `installation.rst` appears in the table of contents, not the filename. Links to the subsections appear as well.

> **Note:** A large number of output options other than HTML are possible, but are not discussed here. See [Builders](https://www.sphinx-doc.org/en/master/usage/builders/index.html) for more info.

After reviewing, leave the web page open. We will regenerate the documentation as we make changes, and it will be easiest to just reload the page in your browser, rather than having to reopen from the filesystem.

> **Note:** You might see examples online that tell you to generate the documentation with the following command:
>
>     sphinx-build -M html sourcedir outuputdir
> 
> Which for our project would be:
> 
>     sphinx-build -M html . _build
> 
> This works, but `make html` is more widely used and less verbose. Under the hood, it actually just calls `sphinx-build`, and passes in source and build directories which were set when you ran `sphinx-quickstart.

### Customizing the Documentation

The default theme, Alabaster, is a little boring. We are going to use the commonly used Read The Docs theme. To set this theme, open `conf.py`, a configuration file that was created by `sphinx-quickstart`. At the bottom of `conf.py`, you will see a setting for `html_theme`. Change this to:

```python
html_theme = 'sphinx_rtd_theme'
```

Save `conf.py` and rerun `make html`. Then reload the web page to view the new theme.

## Autodocumenting Source Code

Creating intallation instructions, quickstarts, and tutorials is useful, but the real power of Sphinx comes from autodocumenting your project based on docstrings. If you were writing your code with foresight, you used docstrings to document the functions and classes you were creating. These docstrings will form the basis for our automated documentation.

### Writing Docstrings in Your Code

We will use NumPy-style docstrings. NumPy and Google-style docstrings are supported by Sphinx's Napolean extension. I find both of them to be far preferable to the default reStructuredText docstring format recommended by [PEP 287 – reStructuredText Docstring Format](https://peps.python.org/pep-0287/).

Information on these formats is available in the Sphinx documentation:

* reStructuredText docstrings: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>
* NumPy and Google docstrings: <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>

I will only cover NumPy-style docstrings. The workshop files `areal_weighting.py` and `binary_method.py` both contain classes with docstrings. The classes are fake, having methods that do nothing and return `None`.

A basic template for a NumPy docstring is:

```python
def my_func(arg1, arg2 = None):
    """This is a short summary.

    This is an extended summary.

    It can span multiple lines, but should be kept short. Extensive 
    discussion can happen in Notes or other sections.
   
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

### Edit Configuration Files to Support Autodoc

In order to automatically generate documentation source files from the docstrings, we need to modify `conf.py`.

First, Sphinx needs to know where to find the (code) source files. We are running `make html` in the docs directory. If you followed our recommended project directory structure, the package you are documenting is in a sibling directory. But you import that package from the *parent* directory, which is the parent to both `my_package` and `docs`. Therefore, the path to parent needs to be put in the configuration file. Put the following lines in `conf.py`, right before the Project Information section:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path('..').resolve()))
```

Then you need to add the autodoc extension and, in order to support NumPy-style docstrings, the Napoleon extension. Replace the line `extensions = []` with:

```python
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon"
]
```

> **Note:** If your project structure uses the convention of having your package in a `src` directory, your path needs to point to that directory. Replace the `sys.path.insert` line with `sys.path.insert(0, str(Path('..', 'src').resolve()))`.

### Generate API Documentation

Generating the documentation happens in two steps. First, `sphinx-apidoc` is used to generate new source *documentation* files which contain directives to look in the source *code*. Then, when `make html` is run, the documentation is actually generated from the docstrings.

So begin by running `sphinx-apidoc`. This requires specifying the output directory for the source documentation files (which is just the current directory, `.` in the command below) and the path to the package you are documenting:

```sh
sphinx-apidoc -o . ../my_package
```

This has created two new files in your `docs` folder:

* `modules.rst`
* `my_package.rst`

`my_package.rst` contains directives that will generate the API documentation from the docstrings in the package named `my_package`. `modules.rst` merely contains a toctree with a pointer to `my_package`. If your project contained additional packages or modules, each package would get its own `<package_name>.rst` file, and they would appear in `modules.rst` toctree.

What we *don't* yet have is a pointer to `modules.rst`. If we want this to actually appear in our documentation, we need to add it to `index.rst`. Do this now. Add `modules` (remember we don't need the filename extension) on a new line after `installation`.

Run `make html` again and reload the web page.

The Contents should now show both "How to use this module" and "my_package". Note the navigation buttons at the bottom. They allow you to move sequentially through the documentation, forward and backward. The order of the sections is determined by the order that the files are listed in the `index.rst` toctree (and toctrees further down the hierarchy).

## Hosting Your Documentation

So far we've just created the documentation on our local computers. If you are publishing your Python project, you probably also want to make the documentation public. The Sphinx documentation covers several free hosting options in [Appendix: Deploying a Sphinx project online](https://www.sphinx-doc.org/en/master/tutorial/deploying.html).

The first two options, Read the Docs ([ReadtheDocs.org](https://readthedocs.org/)) and GitHub Pages, are probably the most popular. Note that RTD makes use of a GitHub repo, so for either option you can create your Python project in GitHub. For GitHub Pages you can automate building the documentation with GitHub Actions. For RTD, a basic workflow is to log in to RTD and import your GitHub repo. It will look for the documentation source files in your GitHub repo, and build and host the documentation. But it is possible to automate the RTD process with GitHub Actions as well. Details go beyond the scope of this workshop.

