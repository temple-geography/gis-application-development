# Scaffolding

The professor will demonstrate a project scaffold.

# CLAUDE.md

The project directory should have an `AGENTS.md` or `CLAUDE.md` file. Note that `AGENTS.md` is a more general standard, used by OpenAI and others, while Claude Code requires `CLAUDE.md`.

1. `CLAUDE.md` is parsed hierarchically. This means you can have multiple files nested at different levels of your project. When working in a lower-level context, all `CLAUDE.md` files up the directory tree are parsed in order. If guidance is in conflict, lower-level files "win".
2. Document standards appropriate to the project level. This can include coding conventions, or they can be included in lower-level files, particularly if multiple languages are used for a large project.
3. The entire file is parsed when the Claude session starts. This uses tokens but can also blow your context window. Files of more than 100 or 200 lines will not stay in context.

# Work in Sessions

Go to the project folder and enter:

```bash
claude -n <session-name>
```

The session name is optional, but I always name my sessions. It aids in continuing previous work.

Sessions can then be resumed with:

```bash
claude --resume <session-name>
```

or, just:

```bash
claude --resume
```

which will give you a session picker, showing you named sessions to choose from.

Compact often with `/compact` to free up context. If you don't compact and the context window fills, you will be forced to compact, which can take a couple of minutes to do. Context can be **cleared** with `/clear`. Exiting and restarting Claude Code will also clear context, unless you resume a previous session.

# Working with GitHub

Claude Code can control git. Controlling *GitHub* requires installing the GitHub CLI (`gh`). Without GitHub CLI you can create branches, commit, and merge. GitHub CLI allows you to create GitHub issues and PRs, as well push to remotes.

Note, however, that many developers find Claude Code commit messages overly verbose. As I mentioned in class, one-line commits are common, while CC often does multiline commit messages. Issues and especially PRs may also be overly verbose.

GitHub CLI can be downloaded from <https:/cli.github.com/>. After installation, it must be authorized:

```bash
gh auth login
```

Claude Code will then be able to work with git and GitHub directly.

# Project Design with Claude Code and Claude Web

`DESIGN.md`
