import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="myservice", # Replace with your own username
    version="0.0.1",
    scripts = ['myservice'],
    author="Matias Puerta",
    author_email="matias@tdomo.com",
    description="Example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tutte/new-python-project-template",
    packages=['src','config'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
