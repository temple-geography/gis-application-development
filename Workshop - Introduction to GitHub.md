---
title: Introduction to Git and GitHub
author: Lee Hachadoorian
---

# Some Definitions

Repository
: "Repo" for short. Collection of files for a specific project.

Commit
: Atomic unit of work. Delta is the difference between new files and old files. Project's commit history is almost a lab notebook, so write nice descriptive commit messages.

Branch
: Pointer to a specific state after a commit.

Master Branch
: Pointer to latest working version of your project.

# Preparation

1. **Install Git:** Git is the actual software for version control. It can be downloaded from <https://git-scm.com/downloads>.
2. **Install a GUI Client (Optional):** Git comes with a command line interface (CLI). You may prefer to work in a GUI client. There are many, and they are evolving rapidly, so they are not listed here. You may be interested interested in starting with GitHub Desktop.
    * GitHub Desktop
        * Windows/Mac: <https://desktop.github.com/>
        * Linux: <https://github.com/shiftkey/desktop>
    * List of GUI Clients: <https://git-scm.com/downloads/guis>
3. **Create a GitHub Account:** <https://github.com/join>. Keep in mind that Git is the version control software, and GitHub is a hosted version of Git with some social networking capabilities. It is possible to run Git entirely locally, or to connect a Git server managed privately by your organization GitHub ≠ Git!
4. **Install a Diff Viewer (Optional):** A "diff" is a comparison of two files that shows differences between them. Git includes a basic CLI diff viewer, and many GUI Clients also include a diff viewer. Meld (<https://meldmerge.org/>) is a simple, lightweight diff viewer.

# Working with Git

The examples below show CLI commands for working with Git. All of these steps can be accomplished using GUI clients, but as there are so many, no attempt is made to cover their use.

Commands can be run in the terminal on Mac/Linux, Command Prompt or PowerShell on Windows.

## Create/Clone a Repo

All work in Git is in a **repository**, or "repo". There are two ways to get started working with Git/GitHub:

* If you have an *existing project*, you will need to initialize a *local* Git repo for the project, then add the local repo to GitHub.
* If you are starting a new project, it will be easier to create a new repo in GitHub, then **clone** it locally. This is also the procedure for beginning to contribute to an existing project that someone else is already maintaining in GitHub.

We will focus on working in a project that is new or already on GitHub. If you have an existing local project, you can initialize it by navigating to the project folder in the terminal and giving the following command:

```
git init
```

Then follow instructions at <https://docs.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line> to add the project to GitHub.

Optionally, you can specify the name of the main branch using the `-b` switch. GitHub (the organization) seems to be moving toward a convention of using `main` as the name of the main branch, and the instructions above use `git init -b main` to initialize a project using this convention. The Git default if no name is specified is `master`, and this still seems to be the convention on the vast majority of projects on GitHub.

You do not need to specify any info about the project, such as a project name. The project name will be taken from the name of the folder that you run the `git init` command in. Do make sure that this folder name does not have any spaces in it. GitHub project names use a variety of different naming conventions, but it seems to me that the most common convention is all lower case with hyphens as word separators, e.g. `my-awesome-project`.

For this workshop, you will clone the `gis-application-development` repo used for this course. If, instead, you were beginning a completely new project, you would first create the new repo *in GitHub*. Information on creating a new repository is available at <https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-new-repository>. Do create a README for your project. If you know what programming language your project will be using, it is a really good idea to create a *.gitignore*. GitHub will create one that will ignore file types and folders commonly used for that programming language. It is also a good idea to choose a license. See <https://choosealicense.com/> for more information.

To clone the repo, navigate in the terminal to the *parent* folder. The repo will be copied locally to a subfolder. The parent folder could be a folder where you keep all of your work for this course, but not all of your coursework will be in the repo, and later you will create another repo for the term project. Then run `git clone` with GitHub URL of the repo:

```
git clone https://github.com/temple-geography/gis-application-development
```

`cd` into the new subfolder and view the local files with `ls` (Mac/Linix or Windows PowerShell) or `dir` (Windows Command Prompt). You can also view the new folder and its contents in a file browser. Note that the README and these workshop instructions have been copied to your local repo.

Set a user name and email for the repo. The email must be the address associated with your GitHub account. For example, I ran:

```
git config user.name "Lee Hachadoorian"
git config user.email "Lee.Hachadoorian@gmail.com"
```

In the remainder of this workshop you will create a project branch, fix an error in a file, push it to the remote, and create a pull request.


# Git Warnings

Git should not be used for sensitve data, such as passwords or API keys. If, for example, you are developing an application that uses a cloud service such as AWS or Azure, you should not include your credentials in the code committed to a repository. *Since Git preserves the history of all files committed to a repo, you cannot just delete the sensitive data!* You will have to rewrite the repo history to purge the file. Information on how to do this is available at <https://docs.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository>.

Git is not ideal for working with large files. This is particularly important to keep in mind for GIS data, which can often be quite large. Git maintains all versions of a file, so if your data is regularly changing, the size of you repo will inflate rapidly. Additionally, you may not need Git's versioning tools for your data. If you do, you might consider using Git Large File Storage (<https://docs.github.com/en/github/managing-large-files/versioning-large-files>). But, really, probably consider using a database such as PostGIS.

Since Git preserves all file history, if you once had a large data file in your repo, all new collaborators will get that file when they clone or fork your repo! You will probably want to purge the file from the repo history, using the same procedures as above for removing files with sensitive data from the repo history.

***************************************************

# Git Sample Workflow



You will make your changes (adding, editing, or deleting files) in a **branch**. Begin by creating a branch using your name.

```
# Create branch
git branch <branch-name>

# View branches. Active branch has star (*) next to it
git branch

# Checkout the branch you want to work in.
git checkout <branch-name>
```

The example repo includes a Python script **names.py**. Open up **names.py** and add the line `print("Your name")`.


```
# What's the current state of the repo?
git status

# Add file to git for tracking:
git add .

# Or git add a specific file:
git add names.py
```

Now commit your changes. Commits *require* a message. Message is given in quotes after -m flag.

> TIP: It is a best practice to start commit messages with a present tense verb.

```
git commit -m "Add my print statement"
```

Push changes to centralized repo. `origin` is a label for the remote repo. The name is arbitrary, but `origin` is conventional, and was created by default when you cloned the repo. `<branch-name>` is the name of the branch to push to on the remote, and should match the branch that you have checked out. In this case, you have been asked to create a branch with your name.


```
git push origin <branch-name>
```

Once pushed, you can go to GitHub and you will see the new branch. In order to merge this branch, you will create a pull request (PR). When you create a PR, the **base** branch is the one you want to merge your work into (usually `master`). The **compare** branch is the one with the new work.

When creating a PR, you may change the message so that it makes sense within the broader project (i.e., don't have to keep the commit message), and you should add a detailed comment. Do not merge your own PRs! PRs should be reviewed by at one other developer on your team.

When the remote has been updated, you will need to pull the changes to your local repo. You usually only want to pull changes that have been committed to `master`. On your local, you first need to check out master, then pull changes.

```
git checkout master
git pull origin master
```

