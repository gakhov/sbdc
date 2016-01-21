from setuptools import setup
from setuptools import find_packages


setup(
    name="sbdc",
    version="0.0.1",
    description="Segment-based document clustering pipeline",
    author="Andrii Gakhov",
    author_email="andrii.gakhov@gmail.com",
    license="Apache License 2.0",
    url="https://github.com/gakhov/sbdc",
    install_requires=[
        "numpy",
    ],
    extras_require={
    },
    packages=find_packages()
)
