import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="mcavatar", # Replace with your username

    version="1.0.0",

    author="parsel",

    author_email="parsel.pip@gmail.com",

    description="Lightweight & Blazing-Fast minecraft skin asset tool",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/parsel-l/mcavatar",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.6',

)
