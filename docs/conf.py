# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import shutil
import os

from rocm_docs import ROCmDocs

# ROCm version numbers
rocm_version = '6.0.0'

latex_engine = "xelatex"
latex_elements = {
    "fontpkg": r"""
\usepackage{tgtermes}
\usepackage{tgheros}
\renewcommand\ttdefault{txtt}
"""
}

# configurations for PDF output by Read the Docs
project = "ROCm Installation on Linux"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2023 Advanced Micro Devices, Inc. All rights reserved."
version = "6.0.0"
release = "6.0.0"
setting_all_article_info = True
all_article_info_os = ["windows"]
all_article_info_author = ""

# pages with specific settings
article_pages = [
    {
        "file":"release",
        "os":["linux"],
        "date":"2023-07-27"
    }
]

exclude_patterns = ['temp']

external_toc_path = "./sphinx/_toc.yml"

docs_core = ROCmDocs("HIP SDK installation Windows")
docs_core.setup()

external_projects_current_project = "rocm"

for sphinx_var in ROCmDocs.SPHINX_VARS:
    globals()[sphinx_var] = getattr(docs_core, sphinx_var)
html_theme_options = {
    "link_main_doc": True
}
