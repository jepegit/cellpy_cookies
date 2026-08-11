# cellpy cookies

Cookiecutter templates that set up the folder structure and the Jupyter notebooks
for a `cellpy` session, so you do not have to build them from scratch every time.

## Templates

| Template | Requires `cellpy` | Purpose |
|---|---|---|
| `standard` | >= 2.1 | The main template: a batch experiment split over notebooks for loading, life, cycles, ICA and plots. Start here. |
| `single` | >= 2.1 | One cell, one notebook, written for `quarto` rendering (html / docx). |
| `ife` | >= 2.1 | `standard` plus IFE extras: an interactive `panel` app for tweaking dQ/dV parameters and a `HoloViews` pickle workflow in the plots notebook. Needs `panel`, `holoviews` and `hvplot` in addition to `cellpy`. |
| `standard_1_x` | 1.x only | The `standard` template frozen at its `cellpy` 1.x state. Use it if you cannot upgrade yet. |
| `ife_1_x` | 1.x only | The `ife` template frozen at its `cellpy` 1.x state. |
| `standard_1_0_0` | 1.0.0 only | Older frozen variant, kept for reproducing old sessions. |

The templates check your installed `cellpy` version in a `pre_gen_project` hook and
refuse to generate if it does not match, so you cannot accidentally create 1.x
notebooks against `cellpy` 2 (or the other way around). The hook can only abort - it
cannot redirect you - so pick the right template yourself.

## Creating a session

Through `cellpy` (it fetches the templates from GitHub for you):

```bash
cellpy new --list                 # see the available templates
cellpy new --template standard
```

Or with `cookiecutter` directly:

```bash
cookiecutter gh:jepegit/cellpy_cookies --directory standard
```

Both ask for the project name, session id, author and so on.

`cellpy new` only knows the three live templates (`standard`, `ife`, `single`) - they
are the ones registered in `cellpy.utils.template_registry`. The frozen 1.x templates
are reachable through `cookiecutter` only:

```bash
cookiecutter gh:jepegit/cellpy_cookies --directory standard_1_x
cookiecutter gh:jepegit/cellpy_cookies --directory ife_1_x
cookiecutter gh:jepegit/cellpy_cookies --directory standard_1_0_0
```

## What you get

```bash
cellpy_project/
└── 2026_01_01_experiment_001
    ├── cellpy_batch_experiment_001.json   (written when you run the loader notebook)
    ├── data
    │   ├── external
    │   ├── interim
    │   ├── processed
    │   └── raw
    ├── out
    │   └── note.md
    ├── 00_experiment_001_notes.ipynb
    ├── 01_experiment_001_loader.ipynb
    ├── 02_experiment_001_life.ipynb
    ├── 03_experiment_001_cycles.ipynb
    ├── 04_experiment_001_ica.ipynb
    └── 05_experiment_001_plots.ipynb
```

Run the notebooks in order. `01_..._loader` builds the journal (`batch.load`) and
saves it in the experiment folder; the other notebooks pick it up from there with
`allow_from_journal=True`. The `single` template gives you one notebook instead.

## Notes

- Remember to save your notebooks.
- The `02` - `04` notebooks use `cellpy.collect` (`summary_collector`,
  `cycles_collector`, `ica_collector`); `collection.save("out")` writes the collected
  frames, `collection.plot()` draws them.
- Loading from a lab database (the `batch_col` / `Batch.from_db` path) only works
  where that database is reachable; everything else runs off the journal and the
  cellpy-files.
