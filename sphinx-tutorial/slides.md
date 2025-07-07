# Sphinx / Mkdocs overview

## July 8, 2025

---

## How to build documentation sites (for python)?

Two steps:
1. Create web site (using a **static site generator**).
2. Host this site on a web server.
    - Typically, pair this with CI to build website automatically and regularly <!-- .element: class="fragment" data-fragment-index="1" -->
    - Choices:  <!-- .element: class="fragment" data-fragment-index="2" -->
      - readthedocs (nemos): easy, for python, works out of the box but less configurable, can build on every PR, free (for open source) <!-- .element: class="fragment" data-fragment-index="2" -->
      - GitHub pages (pynapple): easy, requires some configuration, but more configurable, can't build for every PR, free (for open source) <!-- .element: class="fragment" data-fragment-index="2" -->
      - Jenkins + GitHub pages (plenoptic): hard, requires lots of configuration, but has access to GPU and more resources, free (if you're at Flatiron) <!-- .element: class="fragment" data-fragment-index="2" -->
    - Optional: custom domain name (pynapple, plenoptic) <!-- .element: class="fragment" data-fragment-index="3" -->
- The static part is important: everything runs in user's browser <!-- .element: class="fragment" data-fragment-index="4" -->

#note: but first, big picture: how do we build a documentation site? that's the goal of sphinx or mkdocs. there are two important components: creating the html (and other files) and then hosting them somewhere. the first is what sphinx/mkdocs (or other static site generators) handle, and what we'll focus on today.

Before moving on, couple words about the second part:

And finally: the "static" is important. that means that nothing runs server-side, everything runs in the users browser. This means: no local database (i.e., keeping track of users) or anything too compute heavy. but you can do a lot in users browsers, including interactive plots. As long as you're building a static site, you can find lots of free hosting options

If you need something non-static, it's more complicated and harder to find anything free

---

## Static site generators

Convert text input files to static web sites (html, css, javascript). Many choices:
- sphinx (https://sphinx-doc.org): https://plenoptic.org, https://pynapple.org, https://nemos.readthedocs.io, most python packages (torch, matplotlib, numpy, etc.)
- mkdocs (https://mkdocs.org): https://docs.pi-hole.net, https://recipes.wfbroderick.com
- jekyll (https://jekyllrb.com): https://neurorse.flatironinstitute.org/, https://sciware.flatironinstitute.org, https://presentations.plenoptic.org/, many blogs
- pelican (https://getpelican.com): https://wfbroderick.com

#note: there are many different static site generators that exist. in addition to sphinx and mkdocs, I've also used jekyll and pelican. they all do basically the same thing: convert text into static websites, which is a mix of html, css, javacscript, as talked about in last slide

---

## Sphinx and Mkdocs

Focused on building websites for documentation

<div class='column' style="float:left;width:50%">
Sphinx
<ul>
<li> More established for python projects </li>
<li> <strong>Large</strong> ecosystem of plugins </li>
<li> Originally, only reST, now has support for markdown via MyST </li>
</ul>
</div>

<div class='column' style="float:right;width:50%">
Mkdocs
<ul>
<li> Newer </li>
<li> Easier to set up </li>
<li> More streamlined </li>
<li> Smaller ecosystem (in practice, just <a href="https://squidfunk.github.io/mkdocs-material/">mkdocs-material</a> and maybe <a href="https://smarie.github.io/mkdocs-gallery/">mkdocs-gallery</a>) </li> 
<li> Markdown-first </li>
</ul>
</div>


#note: currently, I pick mkdocs for quick and simple, sphinx for the libraries we use, because they need the bells and whistles

---

## Example

https://github.com/billbrod/sphinx-tutorial
