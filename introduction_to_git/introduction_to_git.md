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

1. **Install Git:** Git is the actual software for version control. It can be downloaded from <https://git-scm.com/downloads>. For Windows users, if you have an older version of Git for Windows installed, please update to the latest version (or at least v2.29), as recent versions have Git Credential Manager built in. For Linux or Mac users, [install Git Credential Manager](https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/install.md) separately.
2. **Install a GUI Client (Optional, as workshop will use CLI):** Git comes with a command line interface (CLI). You may prefer to work in a GUI client. There are many, and they are evolving rapidly, so they are not listed here. You may be interested in starting with GitHub Desktop.
    * GitHub Desktop
        * Windows/Mac: <https://desktop.github.com/>
        * Linux: <https://github.com/shiftkey/desktop>
    * List of GUI Clients: <https://git-scm.com/downloads/guis>
3. **Create a GitHub Account:** <https://github.com/join>. Keep in mind that Git is the version control software, and GitHub is a hosted version of Git with some social networking capabilities. It is possible to run Git entirely locally, or to connect a Git server managed privately by your organization. GitHub ≠ Git!
4. **Set up 2FA:** GitHub now *requires* two-factor authentication to log in. Instructions on conifguring 2FA are available at <https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication>. You must set up 2FA either using an authenticator app (time-based one-time password app, or TOTP) or using text messaging. We will have to use an authenticator app when we get to the [Python Packaging workshop](/distributing_software/packaging.md) anyway, so I suggest doing that now. However, if you have any problems, just set up text based authentication for now.
    1. Install an authenticator app if you don't already have one. I recommend 2FAS (<https://2fas.com/>) which, is PCMag's current top recommendation. If you would like to consider alternatives, look at the full list in ["The Best Authenticator Apps for 2024"](https://www.pcmag.com/picks/the-best-authenticator-apps).
    2. [Follow GitHub's instructions to link the authenticator app to your account](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication#configuring-two-factor-authentication-using-a-totp-app). If for any reason this doesn't work for you, [configure 2FA using text messages](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication#configuring-two-factor-authentication-using-text-messages).
    3. **Optionally, [configure 2FA with GitHub mobile](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication#configuring-two-factor-authentication-using-github-mobile)**. I find GitHub mobile to be a little easier to use than an authenticator app. It does require having set up an authenticator app or SMS beforehand, so you can't just jump to this step. After doing this, I also went to 2FA settings on GitHub and set GitHub Mobile as my preferred 2FA method.
5. **Install a Diff Viewer (Optional):** A "diff" is a comparison of two files that shows differences between them. Git includes a basic CLI diff viewer, and many GUI Clients also include a diff viewer. Meld (<https://meldmerge.org/>) is a simple, lightweight diff viewer.

# Working with Git

The examples below show CLI commands for working with Git. All of these steps can be accomplished using GUI clients, but as there are so many, no attempt is made to cover their use.

Commands can be run in the terminal on Mac/Linux, and Command Prompt or PowerShell on Windows.

## Create/Clone a Repo

All work in Git is in a **repository**, or "repo". There are two ways to get started working with Git/GitHub:

* If you have an *existing project*, you will need to initialize a *local* Git repo for the project, then add the local repo to GitHub.
* If you are starting a new project, it will be easier to create a new repo in GitHub, then **clone** it locally. This is also the procedure for beginning to contribute to an existing project that someone else is already maintaining in GitHub.

### Adding an Existing Project to Git

**For class, we will not perform these steps, as we will focus on working in a project that is already on GitHub. If you are starting a new project, it is usually easier to create a new, empty repo in GitHub first and clone it locally. (If you have already done some work, you can move the files into the new, empty repo.) Therefore, the instructions in this section are only really useful if you have done significant work on a project locally and later decide to add it to GitHub.**

To add your existing local project to Git, you **initialize** it by navigating to the project folder in the terminal and giving the following command:

```
git init -b main
```

Then follow instructions at <https://docs.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line> to add the project to GitHub.

Optionally, you can specify the name of the main branch using the `-b` switch. GitHub (the organization) is moving toward a convention of using `main` as the name of the main branch, and the instructions above use `git init -b main` to initialize a project using this convention. The Git default if no name is specified is `master`, and (as of January 2023) this still is still pretty widespread among projects on GitHub.

You do not need to specify any info about the project, such as a project name. The project name will be taken from the name of the folder that you run the `git init` command in. **Do make sure that this folder name does not have any spaces in it.** GitHub project names use a variety of different naming conventions, but it seems that the most common convention is all lower case with hyphens as word separators, e.g. `my-awesome-project`.

### Cloning a Repo

For this workshop, you will clone the `temple-geography/git-practice` repo. If you were beginning a completely new project, you would first create the new repo *in GitHub*. Information on creating a new repository is available at <https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-new-repository>.

> For a new project:
> 
> * **DO** create a README for your project.
> * **DO** create a *.gitignore*. GitHub offers several *.gitignore* templates based specific programming languages (<https://github.com/github/gitignore>). If you know what programming language your project will be using, the selected *.gitignore* will ignore file types and folders commonly used for that programming language.
> * It is also a good idea to choose a license. See <https://choosealicense.com/> for more information.
> 
> Our practice project already exists on GitHub, so you can ignore these steps.

To clone the repo, navigate in the terminal to the *parent* folder on your computer. The repo will be copied locally to a *subfolder*. The parent folder could be a folder where you keep all of your work for this course. The repo will be in the course folder, but not all of your coursework will be in the repo subfolder. Additionally, you can have more than one repo in the same parent folder. Later you will create another repo for the term project.

Run `git clone` with GitHub URL of the repo:

```
git clone https://github.com/temple-geography/git-practice
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

# Add all new or changed files for tracking
git add .

# Check status again
git status
```

`git status` will show that Git recognizes that these files differ from the versions in the repository.

Putting the changed versions into the repository is called a **commit**. A commit should come when work has reached a good stopping point. It could mean that a new feature has been completed, or a bug has been fixed. Even if the feature is incomplete, it's usually a good idea to commit after significant changes that still leave the code in a working state. Committing work in progress (WIP) is OK, but not if you commit something that breaks the application. Doing a commit before signing off for the day is probably good. The work may still need to be tested or reviewed, but that comes later. 

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

This suggests another way to think about *when* to commit. Commits create **checkpoints**, a point in the development to which you might want to return. Again, you may not have completed a feature, but if you have made significant progress, the code is in a working state, and you might want to return to this point in the event further development introduces serious problems, commiting lets you revert your work to this checkpoint using `git reset`.


> **Renaming or moving files:** If you rename or move a file on the hard drive, Git will treat this as a file being deleted and a new file being added. Use the command `git mv <old_filename> <new_filename>` so that Git will know that the moved or renamed file is the same file!

## Pushing and Pulling Changes

The changes so far have been made to a local repository, but now I want them to appear in the **remote** so that they can be shared with project collaborators. `origin` is a label for the remote repo. The name is arbitrary, but `origin` is conventional, and was created by default when you cloned the repo. `<branch-name>` is the name of the branch to push to the remote.


```
git push origin scratch
```

Usually, `<branch-name>` will match the branch that you have checked out. It is possible to `git push` a branch that is *not* the one you are working on. I find this somewhat confusing, but it may be useful if you have several feature branches that you are working on at once. You might be working on feature-3 and realize you committed changes to feature-2, but didn't push before checking out feature-3.

Now that I have created this branch, you can download the changes. First you need to **fetch** information about new branches on the remote:

```
git fetch origin
```

Note that the branch name is not specified. If there are multiple new branches, you will get info about all of them.

You can look at the status of local and remote branches (and see which remote branch each local branch **tracks**) with the `-vv` switch for "very verbose":

```
git status -vv
```

You should now see that there is a new **untracked** branch `scratch` on the remote. If you want to work with this branch locally, you need to check it out in a very specific way:

```
git checkout --track origin/scratch
```

This does three things:

1. It makes a local copy of the remote branch `origin/scratch`.
2. It sets up the local `scratch` branch to track `origin/scratch`.
3. It checks out `scratch`.

According to the [Git documentation](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches#_tracking_branches), you can accomplish the same thing with `git checkout scratch`. If `scratch` *only* exists on the remote, and there is no local `scratch` branch tracking it, it will do the same thing as `git checkout --track origin/scratch`. I might ask one of you to test this in class. I found it didn't work as advertised the last time I tried to teach this workshop, and am not sure where it went wrong. In any event, since `git checkout` can do different things depending on whether and where a branch exists, it might be better stick to the more verbose form.

## Practice

In demoing the above, I will have created a new file, edited, and added it to the `scratch` branch. The file will have intentional errors, which you will fix. Try the following.

1. Checkout the `scratch` branch.
2. Create and checkout a new branch with your names or initials, e.g. `feature-lee`. This branches off of `scratch`, so it will include the new file, which was created in `scratch`. If instead you branch off of `main`, your new branch will *not* contain the new file.
3. Even though there are no changes, push this branch to the remote.
3. Create and checkout *another* branch with a new name based on your earlier branch, e.g. `feature-lee2`.
4. Open the new file in a text editor. Fix the errors. Save and close the file.
4. Add and commit the changes.
5. Push the new branch to the remote.

## Creating a Pull Request

Once pushed, you can go to GitHub and you will see the new branch. In order to merge this branch, you will create a **pull request** (PR). When you create a PR, the **base** branch is the one you want to merge your work into (often `main`). The **compare** branch is the one with the new work.

When creating a PR, you may change the message so that it makes sense within the broader project (i.e., don't have to keep the commit message), and you should add a detailed comment. Do not merge your own PRs! PRs should be reviewed by at least one other developer on your team.

Pair up with another student and practice working on pull requests. 

1. Go to GitHub and create a pull request from your `feature-name2` branch to your `feature-name` branch. Assign the other student in your pair as the reviewer.
2. Look at the repo's pull requests. If your partner did step 1 correctly, you should see that "You have a pending review request". Click on it to look at the pull request.
3. Since these changes were made in branches that no one else was working in, you should see a message that "This branch has no conflicts with the base branch". Click the "Merge pull request" button.
4. When the branch has been merged, you can close the pull request. You should also see a message that the merged branch can be deleted. Go ahead and delete the branch.
5. When your partner has approved your PR, go back to the command line and run `git status -vv`. Note that you still have your `feature-name2` branch, but the remote branch is no longer there. You need to manually delete the local branch. Check out any other branch, then delete the unneeded feature branch with `git branch --delete feature-name2`.

Merging can also be accomplished at the command line. You could merge your own feature branch by checking out the base branch (`feature-name`) and then using:

```
git merge feature-name2
```

This merges `feature-name2` into `feature-name`. It skips the PR review. Since we have to push to GitHub to use the PR features on the website, I find it easier to use GitHub's web-based merge than the command line merge. YMMV.

## Resolving Merge Conflicts During PR Review

Generally, only one developer should be working on a branch at a time. If two developers need to add features to `dev`,  they should branch off of `dev`, then seek to merge their branches into `dev`, rather than both edit the `dev` branch directly.

Sometimes those changes may still conflict with each other. If you are working on `feature1` and your colleague is working on `feature2`, but those features are part of the same general area of concern, you may make incompatible changes in the same file. What happens if you do so?

Continue working with the student you partnered with in the last step. For this example, I am going to assume we have two students named Legolas and Gimli. Assume that both of you are adding features to Legolas's branch, which is named `feature-legolas`.

1. Gimli should pull and checkout `feature-legolas` with tracking, as demonstrated above.
2. Gimli should branch off of `feature-legolas`. The branch can be named anything, e.g. `feature-legolas-gimli` or `feature-legolas-mod`. Make changes to the beginning of the file and at multiple places throughout. Remember, we are *trying* to create conflicts that can't be easily resolved.
3. Legolas should make changes directly to `feature-legolas`. That is, don't branch first (which is what we normally *should* do). We are *trying* to create conflicts. Make changes to the beginning of the file and at multiple places throughout. Legolas should push their branch to GitHub.
4. Gimli should now push their feature branch to GitHub. Then, create a PR trying to merge this branch into `feature-legolas`. Tag Legolas as the reviewer.
5. Legolas should review the PR. GitHub will let you know there are merge conflicts. You can examine the conflicts using GitHub's web editor. It will show you the file with *both* contributors' changes highlighted in various places. Legolas can edit the file directly here, choosing which changes to keep, or creating something completely new. When he is done, he can select "Mark as resolved", then confirm the pull request.
6. Since changes have been made on the remote `feature-legolas` branch that are not reflected locally (unless Legolas just rejected all of Gimli's changes, in which case the post-merge remote branch will be the same as his local branch), both developers should pull the remote branch to their local repos.

# Git Gotchas

Git should not be used for sensitive data, such as passwords or API keys. If, for example, you are developing an application that uses a cloud service such as AWS or Azure, you should not include your credentials in the code committed to a repository. *Since Git preserves the history of all files committed to a repo, you cannot just delete the sensitive data!* You will have to rewrite the repo history to purge the file. Information on how to do this is available at <https://docs.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository>.

Git is not ideal for working with large files. This is particularly important to keep in mind for GIS data, which can often be quite large. Git maintains all versions of a binary file, so if your data is regularly changing, the size of you repo will inflate rapidly. Additionally, you probably don't need Git's versioning tools for the *data*. If you do, you might consider using Git Large File Storage (<https://docs.github.com/en/github/managing-large-files/versioning-large-files>). But, really, probably consider using a database such as PostGIS.

Since Git preserves all file history, if you once had a large data file in your repo, all new collaborators will get that file when they clone or fork your repo, even if it is currently deleted! You will probably want to purge the file from the repo history, using the same procedures as above for removing files with sensitive data from the repo history.

# Other Notes

You can work with a git repo on multiple computers using a file sync service such as Dropbox. All the repo files will sync as normal, but the repo status and branches will sync as well. All of this info is stored internally in a hidden folder named `.git`, so as long as your syncing service doesn't exclude hidden files (which might be a user-configurable setting) all info about the repo will sync as well. There's no need to `git push` the repo from your desktop so that you can `git pull` on your laptop to work with it later.





