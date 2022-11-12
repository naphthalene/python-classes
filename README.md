# Setup

# Python Lessons

## Week 1 - Data Representation and Classes

Implement some geometric shapes as plotted on a cartesian plane as
Python classes. Provide methods for area, length and others. The code
stubs and tests have been provided.

## Week 2 - Source Control and Ergonomics

Read the `README`! This file is in every repository, by convention. It
describes how to install the package, test it, and any related
documentation.

### Part 1 - Workstation Setup

To setup your workstation (shell, environment, packages), you will need
to do the following:

#### Install `pyenv`

`pyenv` is used to manage multiple versions of python on your system. It
should be installed by the operating system package manager.

```
sudo apt-get install pyenv      # Ubuntu/Debian
sudo pacman -Syu pyenv          # Arch
```

#### Install correct version of Python

```
pyenv install 3.9.6
pyenv global 3.9.6
```

Verify you're using the correct versions of `pip` and `python` by
running:

```
pip --version
```

#### Install Poetry

```
pip install poetry
```

This is used to manage virtual environments - 'python-in-a-folder'
groups of installed packages.

#### Install the requirements of the repository

```
poetry install
```

This will install all of the requirements you specify in
`pyproject.toml` file.

#### Emacs - activating environments

In order for `emacs` to find code definitions and give you
suggestions, we need to activate the virtualenv we've created.

Get the path of the virtualenv from your terminal:

```
poetry env info --no-ansi \
  | grep -E 'Path.*virtualenvs' \
  | tr -s ' ' \
  | cut -d ' ' -f 2
```

Next we will activate this environment, to make emacs aware of the
packages we've installed:

Run `M-x pyvenv-activate <RET>`, provide the output of the command
above, then hit `<RET>` once more. If you are working on a python file
and want to reload it, run `s-; w r`.

That reads as: super + `;` together, release super, followed by `w`,
followed by `r`). When you see `<RET>` that means press `Enter`.

We are using `lsp-pyright`. Here is the snippet you need in your
`.emacs` configuration:

```
; Python
(add-hook 'python-mode-hook #'(lambda ()
                                (require 'lsp-pyright)
                                (lsp)))
; `s-l` is often swallowed by wm, remap it to `s-;`
(setq lsp-keymap-prefix "s-;")
```

#### Using VSCode Instead

VS Code has great support for Python, and should be considered for use
instead of emacs at this point.

#### Running Tests

```
poetry run pytest
```

Do this often to make sure you are on the right track. As you build more
of your code on top of other code, you always want to know how the
building blocks behave under each other.

### Part 2 - Git and Github

The next part of your workstation, is how you save, backup, and share
your code with others.

#### Shell

Your shell is the program that lets you type and run commands, set
environment variables, send data between two programs, and much
more.

The most common shells are `bash`, `sh`, and `zsh`. I prefer `zsh`
together with `oh-my-zsh` to provide a very comfortable interactive
experience. `sh` is not recommended for interactive use, but is
available on any UNIX/linux system you work with and is the most
compatible. `bash` is the default on most systems, and is very similar
to `zsh`.

#### Git

Git is similar to the shell - mastering it is very important! As a
developer, you are often not working alone, and it is necessary to share
your code with others. `git` is one of a long line of different tools
for managing source code. Managing code can become a very difficult
task, unless you carefully and frequently commit those changes to
something that keeps different versions of it for you.

##### Viewing the Current Status

Anything you do with `git` should always start and end with running:

```
git status
```

This gives you an overview of the status of your local `clone`. A
`clone` is a local directory that has been matched up with a Github
project.

##### Saving (Committing)

`git` does this by way of `commits` to `branches`. A `commit` is
broadly-speaking two things: a message intended for humans to read, and
a `changeset`, which is a collection of files that were added, removed,
or modified. A `branch` keeps track of all of the changes you make by
chaining together `commits`.

```
git commit [-m "Optional message"]

# Shortcut:
#   gc
```

If you don't specify a message with `-m "..."`, it will open an editor
for you to author your message in!

##### Sharing (Pushing/Pulling)

When you make commits, they are only available to you, on your
workstation, until you `push` them to another computer. While `git` is
designed to allow people to `push` and `pull` code in all sorts of ways,
it is most often used in a `centralized` way. For us, this means using
Github as the center of where both of us `push` to and `pull` from.

When you `push`, you usually `push` a specific local `branch` to a
remote `branch`. The remote and local branches usually share the same
name. For example, you may be working on a branch called `main`
locally. After making a few commits, you want to synchronize the changes
with the central server - Github. So you run:

```
git checkout main
git push origin main

# Shortcut:
#   gco main
#   ggpush
```

The name `origin` here is the default name for where you `cloned` your
local repository from.

What this means is that for a repository that I own on github, I can
push and pull branches, made of one or more commits.

If another contributer wants to do the same, they will need to be aware
of the changes other people are doing. To get an update of all of the
changes people have been making on a repository, I can run:

```
git fetch

# Shortcut:
#   gf
```

Then if I want to update my local copy of `main`, run:

```
git checkout main
git pull origin main

# Shortcut:
#   gco main
#   ggpush
```

## Week 3 - Diving into Functions

The purpose of this week is to get a better understanding of functions
in Python. While you have already seen many examples of functions, there
are some specifics that should be considered.

### Function Inputs and Outputs

As you may have already seen, functions in Python (and many other
languages)
