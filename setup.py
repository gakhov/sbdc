from setuptools import setup
from setuptools import find_packages

execfile('sbdc/version.py')

setup(
    name="sbdc",
    version=__version__,
    description="SBDC: Segment-based document clustering",
    author="Andrii Gakhov",
    author_email="andrii.gakhov@gmail.com",
    license="Apache License 2.0",
    url="https://github.com/gakhov/sbdc",
    keywords=["clustering", "nlp"],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    install_requires=[
        "numpy >= 1.7.0",
    ],
    extras_require=dict(
        test=[
            "pytest == 2.6.4",
            "pytest-cov == 1.8.1",
            "pytest-pep8 == 1.0.6",
            "mock == 1.0.1"
        ],
    ),
    packages=find_packages(),
    zip_safe=False
)
