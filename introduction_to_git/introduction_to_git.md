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
2. **Install a GUI Client (Optional):** Git comes with a command line interface (CLI). You may prefer to work in a GUI client. There are many, and they are evolving rapidly, so they are not listed here. You may be interested in starting with GitHub Desktop.
    * GitHub Desktop
        * Windows/Mac: <https://desktop.github.com/>
        * Linux: <https://github.com/shiftkey/desktop>
    * List of GUI Clients: <https://git-scm.com/downloads/guis>
3. **Create a GitHub Account:** <https://github.com/join>. Keep in mind that Git is the version control software, and GitHub is a hosted version of Git with some social networking capabilities. It is possible to run Git entirely locally, or to connect a Git server managed privately by your organization. GitHub ≠ Git!
4. **Install a Diff Viewer (Optional):** A "diff" is a comparison of two files that shows differences between them. Git includes a basic CLI diff viewer, and many GUI Clients also include a diff viewer. Meld (<https://meldmerge.org/>) is a simple, lightweight diff viewer.

# Working with Git

The examples below show CLI commands for working with Git. All of these steps can be accomplished using GUI clients, but as there are so many, no attempt is made to cover their use.

Commands can be run in the terminal on Mac/Linux, and Command Prompt or PowerShell on Windows.

## Create/Clone a Repo

All work in Git is in a **repository**, or "repo". There are two ways to get started working with Git/GitHub:

* If you have an *existing project*, you will need to initialize a *local* Git repo for the project, then add the local repo to GitHub.
* If you are starting a new project, it will be easier to create a new repo in GitHub, then **clone** it locally. This is also the procedure for beginning to contribute to an existing project that someone else is already maintaining in GitHub.

### Adding an Existing Project to Git

**For class, we will not perform these steps, as we will focus on working in a project that is already on GitHub. If you are starting (or have recently started) a new project, it is usually easier to create a new, empty repo in GitHub first and clone it locally. (If you had already done some work, you can move the files into the new repo.) Therefore, the instructions in this section are only really useful if you have done significant work on a project locally and decided later to add it to GitHub.**

To add your existing local project to Git, you **initialize** it by navigating to the project folder in the terminal and giving the following command:

```
git init
```

Then follow instructions at <https://docs.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line> to add the project to GitHub.

Optionally, you can specify the name of the main branch using the `-b` switch. GitHub (the organization) is moving toward a convention of using `main` as the name of the main branch, and the instructions above use `git init -b main` to initialize a project using this convention. The Git default if no name is specified is `master`, and (as of April 2022) this still seems to be the convention on the vast majority of projects on GitHub.

You do not need to specify any info about the project, such as a project name. The project name will be taken from the name of the folder that you run the `git init` command in. **Do make sure that this folder name does not have any spaces in it.** GitHub project names use a variety of different naming conventions, but it seems to me that the most common convention is all lower case with hyphens as word separators, e.g. `my-awesome-project`.

### Cloning a Repo

For this workshop, you will clone the `temple-geography/git-practice` repo. If you were beginning a completely new project, you would first create the new repo *in GitHub*. Information on creating a new repository is available at <https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-new-repository>.

For a new project:

* **DO** create a README for your project.
* **DO** create a *.gitignore*, if you know what programming language your project will be using. Select your programming language and GitHub will create a *.gitignore* that will ignore file types and folders commonly used for that programming language.
* It is also a good idea to choose a license. See <https://choosealicense.com/> for more information.

I have already created a practice project already exists, so you can ignore these steps.

To clone the repo, navigate in the terminal to the *parent* folder on your computer. The repo will be copied locally to a subfolder. The parent folder could be a folder where you keep all of your work for this course. Not all of your coursework will be in the repo. Additionally, you can have more than one repo in the same parent folder. Later you will create another repo for the term project.

Run `git clone` with GitHub URL of the repo:

```
git clone https://github.com/temple-geography/gis-application-development
```

`cd` into the new subfolder and view the local files with `ls` (Mac/Linix or Windows PowerShell) or `dir` (Windows Command Prompt). You can also view the new folder and its contents in a file browser. Note that the README has been copied to your local repo.

Set a user name and email for the repo. The email must be the address associated with your GitHub account. For example, I ran:

```
git config user.name "Lee Hachadoorian"
git config user.email "Lee.Hachadoorian@gmail.com"
```

I did not use my work email, Lee.Hachadoorian@temple.edu, because my GitHub account is connected to my personal email address.

In the remainder of this workshop you will create a project branch, fix an error in a file, push it to the remote, and create a pull request.

## Creating Branches

A **branch** is a group of changes. Branches are created so that work in progress can be kept separate from the main branch, usually in order to add a new feature or bug fix.

A branch needs a name. It is usually a good idea to give descriptive names, such as a short name for the feature being added or bug being fixed. A big project will often have a branch named `dev` (or something similar), which is the current development version. Feature branches may be branched off of `dev`, and once all milestone features are merged into `dev`, `dev` will be merged into `master`.

To begin, I will make a branch named `scratch`. I will add a file. You will branch off of `scratch`.

I will demo the following steps. **Do not do these steps at this time.**

```
# Create branch
git branch <branch-name>

# View branches. Active branch has star (*) next to it
git branch

# Checkout the branch you want to work in.
git checkout <branch-name>
```

## Working with Files

Once a branch is checked out, files can be added, edited, or deleted directly from your hard drive. If you add or change files, the changes are not yet **tracked** by Git. You can check the status of current files with:

```
git status
```

Files must be added to Git for tracking. This can be done with a specific filename, but usually you want to add all new files:


```
# Add a specific file for tracking
git add <filename>

# Add all new files for tracking
git add .

# Check status again
git status
```

`git status` will show that Git recognizes that these files differ from the versions in the repository.

Putting the changed versions into the repository is called a **commit**. A commit should come when work has reached a good stopping point. It could mean that a new feature has been completed, or a bug has been fixed. Even if the work is incomplete, it's usually a good idea to do a commit before signing off for the day. The work may still need to be tested or reviewed, but that comes later. 

Commits *require* a message. The message is given in quotes after the `-m` flag.

```
git commit -m "Adding new files"
```

So far we are working with only one branch. It is common to work with repos that have multiple branches. *Even if work on a branch is incomplete, you will want to commit your work before you switch branches.* There is another option command, `git stash`, which allows you to "stash" (store) your work in an extradimensional pocket universe (←not literally true) so that you can switch branches. However, it's much simpler to commit the work you have so far. The main reason you might not want to is if you are *really concerned* that the code you have is in a very bad state, and might want to abandon the changes. If that is the case, you might consider trying to fix it before moving on.

If you do want to abandon the changes before a commit, this can be easily accomplished with:

```
# Abandon changes to a single tracked file
git reset <filename>

# Abandon all changes
git reset
```

> **Renaming or moving files:** If you rename or move a file on the hard drive, Git will treat this as a file being deleted and a new file being added. Use the command `git mv` so that Git will know that the moved or renamed file is the same file!

## Pushing and Pulling Changes

The changes so far have been made to a local repository, but now I want them to appear in the **remote** so that they can be shared with project collaborators. `origin` is a label for the remote repo. The name is arbitrary, but `origin` is conventional, and was created by default when you cloned the repo. `<branch-name>` is the name of the branch to push to the remote, and should match the branch that you have checked out.


```
git push origin scratch
```

Now that I have created this branch, you can download the changes. There are two ways to do this: **fetch** and **pull**. A **pull** attempts to merge the files/data with your local repo. It should usually not be done with uncommitted changes in your files. If your purpose is to bring down only new branches without merging, this can be accomplished with a **fetch**. Fetching is non-destructive. It is perfect for getting a new branch that does not exist locally. It will also bring down new files in an existing branch. If your local branch has changed, it will merge if there are no merge conflicts, otherwise it will fail.

Fetch the new branch with

```
git fetch origin
```

Note that the branch name is not specified. If there are multiple new branches, they will all be downloaded.

## Practice

In demoing the above, I will have created a new file, edited, and added it to the `scratch` branch. The file will have intentional errors, which you will fix. Now you should try these steps:

1. Checkout the `scratch` branch.
2. Create and checkout a new branch with your name or initials. This branches off of `scratch`, so it will include the new file, which was created in `scratch`. If instead you branch off of `master`, your new branch will *not* contain the new file.
3. Open the new file in a text editor. Fix the errors. Save and close the file.
4. Add and commit the changes.
5. Push the new branch to the remote.

## Creating a Pull Request

Once pushed, you can go to GitHub and you will see the new branch. In order to merge this branch, you will create a pull request (PR). When you create a PR, the **base** branch is the one you want to merge your work into (often `master`). The **compare** branch is the one with the new work.

When creating a PR, you may change the message so that it makes sense within the broader project (i.e., don't have to keep the commit message), and you should add a detailed comment. Do not merge your own PRs! PRs should be reviewed by at one other developer on your team.

For this exercise, assign another student as the reviewer. Then work with that student to review and merge the pull request.

**Additional instruction forthcoming.**

# Git Gotchas

Git should not be used for sensitve data, such as passwords or API keys. If, for example, you are developing an application that uses a cloud service such as AWS or Azure, you should not include your credentials in the code committed to a repository. *Since Git preserves the history of all files committed to a repo, you cannot just delete the sensitive data!* You will have to rewrite the repo history to purge the file. Information on how to do this is available at <https://docs.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository>.

Git is not ideal for working with large files. This is particularly important to keep in mind for GIS data, which can often be quite large. Git maintains all versions of a file, so if your data is regularly changing, the size of you repo will inflate rapidly. Additionally, you may not need Git's versioning tools for your data. If you do, you might consider using Git Large File Storage (<https://docs.github.com/en/github/managing-large-files/versioning-large-files>). But, really, probably consider using a database such as PostGIS.

Since Git preserves all file history, if you once had a large data file in your repo, all new collaborators will get that file when they clone or fork your repo! You will probably want to purge the file from the repo history, using the same procedures as above for removing files with sensitive data from the repo history.




