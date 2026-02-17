# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from rocm_docs import ROCmDocs

# This is the latest supported ROCm version supported by Windows
win_rocm_version = '7.1.1'
# Radeon Software Pro Installer version bundled with the HIP SDK installer
radeon_software_pro_version = '23.30'

latex_engine = "xelatex"
latex_elements = {
    "fontpkg": r"""
\usepackage{tgtermes}
\usepackage{tgheros}
\renewcommand\ttdefault{txtt}
"""
}

# configurations for PDF output by Read the Docs
project = "HIP SDK on Windows"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2026 Advanced Micro Devices, Inc. All rights reserved."
version = "7.1.1"
release = "7.1.1"
setting_all_article_info = True
all_article_info_os = ["windows"]
all_article_info_author = ""

exclude_patterns = ['temp']

external_toc_path = "./sphinx/_toc.yml"

docs_core = ROCmDocs("HIP SDK installation (Windows)")
docs_core.setup()

external_projects_current_project = "rocm"
html_theme = "rocm_docs_theme"
html_theme_options = {
    "flavor": "generic",
    "header_title": f"ROCm™ Software 7.1.1",
    "nav_secondary_items": {
        "GitHub": "https://github.com/ROCm/rocm-install-on-windows",
        "Community": "https://github.com/ROCm/ROCm/discussions",
        "Blogs": "https://rocm.blogs.amd.com/",
        "ROCm Developer Hub": "https://www.amd.com/en/developer/resources/rocm-hub.html",
        "System and Infra Docs": "https://instinct.docs.amd.com/",
        "Infinity Hub": "https://www.amd.com/en/developer/resources/infinity-hub.html",
        "Support": "https://github.com/ROCm/ROCm/issues/new/choose",
    },
}


for sphinx_var in ROCmDocs.SPHINX_VARS:
    globals()[sphinx_var] = getattr(docs_core, sphinx_var)

rst_prolog = f"""
.. |radeon_software_pro_version| replace:: {radeon_software_pro_version}
.. |win_rocm_version| replace:: {win_rocm_version}
"""

html_theme_options = {
    "link_main_doc": True
}
