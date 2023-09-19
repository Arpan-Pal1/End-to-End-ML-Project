import setuptools


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"


REPO_NAME = "End-to-End-ML-Project-Red-Wine-Quality-Prediction-" 
AUTHOR_USER_NAME = "Arpan Pal"

SRC_REPO = "mlProject"

AUTHOR_EMAIL = "arpanpalme@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author =  AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for ml app",
    Long_description = long_description,
    Long_description_content = "text/markdown",
    url = f"https://github.com/(AUTHOR USER NAME)/(REPO NAME)",
    project_urls ={
    "Bug Tracker": "https://github.com/AUTHOR USER NAME/REPO NAME/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")

)