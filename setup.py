from setuptools import setup, find_packages

setup(
    name="imdb_flask",
    version="0.0.1",
    description="imdb_flask",
    author="Team",
    author_email="",
    # url="https://github.com/CleverSoftwareSolutions/fashion_flask/",
    package_dir={"": "src/"},
    packages=find_packages("src/"),
)
