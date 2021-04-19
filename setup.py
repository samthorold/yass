import setuptools


with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="yass",
    version="0.1.0",
    author="Sam Thorold",
    author_email="sam.thorold@gmail.com",
    description="Yet Another Sudoku Solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
