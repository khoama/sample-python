# Contributing

## Making a pull request
This repository uses the [fork-and-pull-model](https://docs.github.com/en/github/collaborating-with-pull-requests/getting-started/about-collaborative-development-models#fork-and-pull-model).
1. Fork the [repository](https://github.com/Shiti/sample-python).
2. Clone your forked repository from GitHub using preferred tooling or commandline:
```shell
# Clone your fork to your local machine
git clone git@github.com:<your-username>/sample-python.git
```
3. The project uses [Poetry](https://python-poetry.org/) for packaging and dependency management. Refer instructions to install Poetry [here](https://python-poetry.org/docs/#installation).
4. From the project directory, execute the following commands:
```shell
poetry install
poetry shell
pre-commit install
```
5. Check out a new branch and add your modification. For any code changes, please add/update test cases.
6. The repository uses [Conventional Commits Specification](https://www.conventionalcommits.org/en/v1.0.0/). After adding all the changes to git, using `git add`, commit your changes from commandline:
```shell
poetry shell
cz commit
```
7. Once you have created a commit, rebase your development branch with the original repo and push to your fork:
```shell
# Add upstream repo
git remote add upstream git@github.com:Shiti/sample-python.git
git pull --rebase upstream main

git push origin
```
8. Create the pull request using your fork. Refer [GitHub docs](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).
