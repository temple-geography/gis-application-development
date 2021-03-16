# Creating Documentation for Python with Sphinx

Sphinx is designed to generate documetation for self-contained code in python

It generates documentation based on docstrings that you write within each class and function.


## Installs:

`conda install -c conda-forge sphinx`

`conda install -c conda-forge sphinx_rtd_theme` 


## Writing Docstrings inside your code

When writing docstrings to be interpreted by Sphinx, you need to use reST (restructured text) formatting. Sphinx also supports Numpy/Google style docstrings if you import the appropriate extensions which will be covered down below. 

Link to reST formatting: `https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html`

Link to Google formatting: `https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html`


## Turning your docstrings into html

#### Step 1: Preperations

Before using Sphinx, it's important to create a directory specifically for the files that will be generated. Make sure to cd to the directory you created before continuing.

#### Step 2: Run Quickstart

Run `sphinx-quickstart`. You will be asked questions about the configurations that you'd like to use.

This quickstart will create a file called conf.py in your working directory that controls the main configurations for your documentation. It will also create a master document called index.rst, which will function as the outline for your welcome page and contain the root of the table of contents tree.

#### Step 3: Edit configurations

If your python scripts are in another directory, you need to tell Sphinx where to find them. Open up the conf.py file and navigate to the path setup. You will want to uncomment the import statements and the sys.path.insert statement. Put the path for the folder with your python files into `sys.path.insert(0, os.path.abspath('path goes here'))`

In order for sphinx to automatically interpret and generate documentation based on docstrings, we need to add `'sphinx.ext.autodoc'` to the extensions list in conf.py. If you prefer "google" style docstrings, also add `'sphinx.ext.napoleon'` to the extensions.

For aesthetics, you can change the html theme as well. Try `'sphinx_rtd_theme'` instead of the default.

#### Step 4: Creating .rst files from python files

Run `sphinx-apidoc`. To specify output path and sourcepath, use `-o . .` this command specificaly would use current folder as output path and look for .py files in the current folder. This will create a .rst file for each python file based on the docstrings in them. 

#### Step 5: Adding .rst files to your table of contents

In order for the generated .rst files to be displayed, you need to add them to the table of contents in the index.rst file. You can list them in the order they should appear under the existing toctree. You can also add more toctrees to split your files into multiple groups.


#### Step 6:

Run `make html`. This will build the html pages from the .rst files in your working directory.


## Hosting your documentation using Github and read the docs

You can host documentation for free online using ReadtheDocs.org. If you push your documentation to your github repo, you can logon to readthedocs and host it from your github repo. Read the docs even supports versioned documentation and has instructions on how to utilize it. 

You might not want to push everything from your working directory to your repo. You will want to use git ignore to specify the files and folders that won't be pushed (touch .gitignore). 

After you've added, committed, and pushed your repo, you can logon to ReadtheDocs and import your repo. It will look for the appropriate files in your repo to build and host the documentation.
