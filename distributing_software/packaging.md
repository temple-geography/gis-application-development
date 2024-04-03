---
title: Python Packaging with Flit
author: Lee Hachadoorian
---

# Preparation

## Creating and Configuring a User Account on TestPyPI

Create a user account on TestPyPi: <https://test.pypi.org/account/register/>

Creating the account will require setting up two-factor authentication (2FA) using an authenticator app on your smartphone. I find 2FAS (<https://2fas.com/>) to be very easy to use, and I like that it is open source. However, there are many 2FA apps to choose from. If you already have one installed on your smart device, continue to use what you are comfortable with. If you would like recommendations on alternatives, you can refer to PCMag's ["The Best Authenticator Apps for 2024"](https://www.pcmag.com/picks/the-best-authenticator-apps).

Additionally, in order to upload packages, you need to create an API Token for your account. (You can use your password to log in to the website, but you cannot use password authentication to upload packages.) Go to TestPyPI Account Settings and scroll down to the API Token link. Once you have created the token, copy it *immediately* and save it somewhere you will remember. We will use it next.

In order to upload packages to TestPyPI, you need to create a configuration file named `.pypirc` in your home folder. On Windows, your home folder is `C:\Users\YOUR_USERNAME`. On Mac or Linux, it is `/home/YOUR_USERNAME`. Copy the following contents to the `.pypirc` file. Note that since PyPI and TestPyPI now *require* the use of API tokens, your username in this file should be left as `__token__`, not changed to your actual username. The password for TestPyPI should be set to the API token that you just created. This will *not* be the same token for the real PyPI.

```
[distutils]
index-servers =
   pypi
   testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = <PyPI token>

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = <TestPyPI token>
```

The instructions for creating an account on the real Python Package Index at <https://pypi.org/> are the same. We are not going to do that in this workshop, but when you publish a completed packages, remember to follow the steps to create and configure your PyPI account, and publish it to PyPI, not TestPyPI.

## Build Tool Installation

Install Flit, a Python build tool, into a fresh conda environment. Flit does not have to be run in your development environment! Therefore, it will be easier to have Flit in its own environment, rather than install it into multiple project environments. The following command will create a conda environment named `flit`. I recommend not installing anything else into this environment.

```sh
conda create -n flit python flit
```

# Creating a Simple Project

Create a folder on your hard drive named `packaging_tutorial`. Then create the following subfolders and files:

```
packaging_tutorial/
├── pyproject.toml
├── README.md
├── example_package_YOUR_USERNAME_HERE/
│   ├── __init__.py
│   └── example.py
└── tests/
```

Remember to replace `YOUR_USERNAME_HERE` with your TestPyPI username.

The files should be created with a text editor (such as Notepad++).

`__init__.py` should be left empty.

Edit `example.py` to add the following content:

```python
def add_one(number):
    return number + 1
```

Edit `README.md`. The text that you add here will appear on your project page on TestPyPI. You can enter the following text, enter your own text, or if you want to you can copy a more complex README from another project.

```
# Example Package

This is a simple example package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
```

The `project.toml` file is where you enter your project metadata, such as version number, license, etc. When you build your package, the metadata will be included in the package, so that when you upload your package to PyPI, it will help other developers understand what your package does, where to find documentation, how to contact you, etc.

Use the following template to add content to `project.toml`. Edit it to use your own project name, which should have your username embedded so that it doesn't conflict with any other project on the test PyPI server. Update the `authors` section with your own name and email. *Also, change the Homepage and Issues URLs to be the GitHub repository and Issues tracker of your term project!* These are not the real URLs for this example package, but I want you to get experience customizing this file.

```
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "example_package_YOUR_USERNAME_HERE"
version = "0.0.1"
authors = [
  { name="Example Author", email="author@example.com" },
]
description = "A small example package"
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
Homepage = "https://github.com/pypa/sampleproject"
Issues = "https://github.com/pypa/sampleproject/issues"
```

Note that this example project uses an MIT License. You should [choose a license](https://choosealicense.com/) for a real project. You may have already done this when you created the GitHub repo for your term project, in which case you should make sure that the license that appears here matches what you have chosen.

# Building and Uploading Your Package

Open the terminal (or on Windows open Anaconda Prompt) and navigate to the directory with `project.toml`. For this tutorial, that corresponds to the directory named `packaging_tutorial`. For your term projects, that will be your repository directory, i.e. the folder that you use for `git push` and other `git` commands.

Activate the `flit` environment with

```sh
conda activate flit
```

Flit can be run two ways. `flit build` will create a `dist/` folder and build a compiled version of your project called a **wheel** and a zipped version of your source code. `flit publish` will both build the package *and* upload it to PyPI. We do not need to specify the package, or where to find the source code. All of the project metadata will be read from `project.toml`, and Flit will find the source code in your repo and use it to build the package.

If you have configured your repository with the standard Python `.gitignore` file, the `dist/` folder will be ignored. That is, when you `git push` your repo, neither `dist/` and its contents will not be pushed to GitHub.

Note that `flit publish` will publish the package to the real PyPI by default! In order to publish it to the test server, we specify the repository in the command call:

```sh
flit publish --repository testpypi
```

If you set up `.pypirc` correctly, you should not be prompted for login credentials. The username (`__token__`) and password (actually your API token) will be read from that file. If username or password are missing, you will be prompted to provide them, *but remember that you cannot use password authentication to upload files to PyPI and TestPyPI*. If prompted, you still have to supply the username `__token__` and your API token as the password.

When it is done, your package URL will appear in the terminal. Depending on what terminal application you are using, you may be able to CTRL-click this link to go to your TestPyPI project page. Otherwise, copy the link, or login to <http://test.pypi.org> and go to "Your projects".

On Windows, packaging took mere seconds (significantly faster than using the standard Python `build` tool). Flit seems to run considerably slower on Linux. When I first ran `flit build` on Linux, I got the message `Fetching list of valid trove classifiers` and then nothing happened for a good 15 minutes. I'm not sure why this step took so long, but it should only happen the first time you run `flit build`. After that, package building took mere seconds.

`flit publish` also ran faster on Windows (mere seconds) than Linux (a few minutes), even on the same network. 

# REFERENCES

The workshop instructions primarily come from the [Flit documentation website](https://flit.pypa.io/en/latest/index.html).

I started with the official [Python Packaging Tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/). The tutorial uses `build` to build the wheel and `twine` to upload it to PyPI. The tutorial uses Hatchling by default as its build backend, but in April 2024 a recent bug (<https://github.com/pypa/hatch/issues/1329>) meant that Hatchling was generating builds that `twine` could not upload. The bug has been fixed, but at that point I started exploring Flit, and found that (a) it was simpler to use, and (b) it builds the packages a lot faster than `build`.

Both the Python Packaging Tutorial and the Flit documentation are written (as of April 2024) as if you can still use password authentication to upload packages to PyPI. The instructions above on 2FA and creating API tokens is added so that an absolute beginner will have everything they need in one place.

For Python project structure, I referred to the [Structuring Your Project](https://docs.python-guide.org/writing/structure/) article at The Hitchhiker's Guide to Python. Note that the Python Packaging Tutorial recommends keeping all source code in a `src` directory, in which case your package would appear at `packaging_tutorial/src/example_package_YOUR_USERNAME_HERE`. I prefer the Hitchhiker's Guide to Python recommendation to not nest your package inside a `src` directory, and have followed that here.
