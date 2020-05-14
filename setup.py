import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matplotlib_backend_qtquick",
    version="0.0.6",
    author="Jovan Mitrevski",
    author_email="j.p.mitrevski@gmail.com",
    description="A QtQuick backend for matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmitrevs/matplotlib_backend_qtquick",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
