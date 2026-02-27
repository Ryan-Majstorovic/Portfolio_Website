project = "Portfolio"
author = "Ryan Majstorovic"

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autosectionlabel",
]

templates_path = ["source/_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["source/_static"]

suppress_warnings = ["autosectionlabel.*"]


def setup(app):
    app.add_css_file("css/my_theme.css")