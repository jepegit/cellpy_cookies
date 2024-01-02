# How to use it

This notebook is compatible with `quarto` (for example for exporting to different formats).

Have a look at the following web-pages for some introductary information:

https://quarto.org/docs/get-started/

https://quarto.org/docs/get-started/hello/jupyter.html

To run it, open a shell window in jupyter-lab and run one of these:

```bash

quarto render 01_{{cookiecutter.notebook_name}}.ipynb --to html
quarto render 01_{{cookiecutter.notebook_name}}.ipynb --to docx
quarto preview 01_{{cookiecutter.notebook_name}}.ipynb

```
