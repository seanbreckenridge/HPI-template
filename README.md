# HPI-template

A template for creating your own [HPI](https://github.com/karlicoss/HPI) repository. This could be used to override particular modules from [`karlicoss/HPI`](https://github.com/karlicoss/HPI) for personal use, or creating new modules.

Since HPI is namespace package, the `my` package can be split across multiple repositories/directories on disk, whose submodules all get merged into the single `my` package. For more information, see the [`MODULE_DESIGN` docs](https://github.com/karlicoss/HPI/blob/master/doc/MODULE_DESIGN.org#adding-new-modules) for HPI, and [`reorder_editable`](https://github.com/seanbreckenridge/reorder_editable)

To use this install [`cookiecutter`](https://github.com/cookiecutter/cookiecutter/) (`pip install cookiecutter`), then:

`cookiecutter gh:seanbreckenridge/HPI-template`
