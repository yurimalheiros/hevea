# Hevea

Hevea monitors a directory for .tex file changes and generate a .pdf.

## Install

```
$ pip install hevea
```

## How to use

```
$ hevea directory
```

If there is not a Makefile in the watched directory you need to use:

```
$ hevea directory --makefile main_tex_file
```

