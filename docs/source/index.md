# Sphinx tutorial

Lots of text here, all *markdown*.

Look at us citing things! {cite:alp}`Portilla2000-param-textur`.

And using math: $e^{i\pi}=-1$

## Bibliography

```{bibliography} references.bib
:style: plain
```

:::{toctree}
:caption: Very Important
:glob: true
:titlesonly: true

another_page
notebooks/*
API Documentation <api/modules>
:::
