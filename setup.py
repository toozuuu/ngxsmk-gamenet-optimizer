#!/usr/bin/env python3
"""
GameNet Optimizer Setup Script
Open source gaming optimization tool
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ngxsmk-gamenet-optimizer",
    version="1.0.0",
    author="toozuuu",
    author_email="sachindilshan040@gmail.com",
    description="A comprehensive, open-source network and system optimization tool for gamers",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/toozuuu/ngxsmk-gamenet-optimizer",
    project_urls={
        "Bug Reports": "https://github.com/toozuuu/ngxsmk-gamenet-optimizer/issues",
        "Source": "https://github.com/toozuuu/ngxsmk-gamenet-optimizer",
        "Documentation": "https://github.com/toozuuu/ngxsmk-gamenet-optimizer/wiki",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "ngxsmk-gamenet-optimizer=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.json"],
    },
    keywords=[
        "gaming",
        "optimization",
        "network",
        "performance",
        "fps",
        "latency",
        "bandwidth",
        "memory",
        "system",
        "open-source",
    ],
    license="MIT",
    zip_safe=False,
)
