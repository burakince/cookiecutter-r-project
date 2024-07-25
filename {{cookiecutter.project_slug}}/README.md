# {{cookiecutter.project_name}}

{{cookiecutter.project_desc}}

Started on {{cookiecutter.start_date}}.

## Directory structure

* **R** - Resuable R code (functions etc.)

## Restarting R Session

Please use the following command to restart your R session

```bash
system("R")
```

## devtools usage

Please use devtools with `library(devtools)` command. If it's not installed yet, you need to install it with `install.packages("devtools")` command.

Please look at [package development cheatsheet](https://raw.githubusercontent.com/rstudio/cheatsheets/main/package-development.pdf) for more details.

### Building Document

We can generate documents with the following command

```R
document()
```

### Building Package

We can build a package with the following command.

```R
build()
```
