# sphinx-tutorial

Introduction to python docs sites.

To view presentation, run `python -m http.server 8008` (or whatever port you want) in the root directory of this project, then open `localhost:8008/sphinx-tutorial` in your browser. Or go to https://billbrod.github.io/sphinx-tutorial/.

To build the sphinx documentation, create a new virtualenv and install this package (with docs requirements), then run sphinx:

``` sh
uv venv -p 3.12 venv
source venv/bin/activate
uv pip install -e .[docs]
make -C docs html -O="-T"
```

This will create the site in `docs/build/html`. You can open up the site in your browser (e.g., `firefox docs/build/html/index.html`).
