import setuptools 

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__= "0.0.1"

REPO_NAME = "e2e-Text-Summarizer-OLMo-7B"
AUTHOR_USER_NAME = "qml219"
SRC_REPO = "e2e-Text-Summarizer-OLMo-7B"
AUTHOR_EMAIL = "leminhquan2192002@gmail.com"

# Package local packages so that the project distribution can be distributed and installed elsewhere. (ex: installed by pip)
setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer with OLMo 7B",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)