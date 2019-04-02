import io
from setuptools import setup

setup(
    name="v_palette",
    version="1.1.0",
    author="Arnau Villoro",
    author_email="arnau@villoro.com",
    packages=["v_palette"],
    include_package_data=True,
    license="MIT",
    description=("Utility to easily use material design colors"),
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/villoro/v-palette",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
)
