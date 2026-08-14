"""
Setup para instalação da biblioteca keylogger_edu
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="keylogger-edu",
    version="1.0.0",
    author="Educational Team",
    author_email="labforense@github.com",
    description="Biblioteca educacional para aprendizado de segurança ofensiva",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/labforense/keylogger-educacional",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education :: Testing",
        "Topic :: Security",
        "License :: OSI Approved :: Creative Commons License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pynput>=1.7.6",
        "cryptography>=41.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "flake8>=4.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "keylogger-edu=keylogger_edu.cli:main",
        ],
    },
    keywords="keylogger security education offensive",
    project_urls={
        "Documentation": "https://github.com/labforense/keylogger-educacional",
        "Source": "https://github.com/labforense/keylogger-educacional",
        "Tracker": "https://github.com/labforense/keylogger-educacional/issues",
    },
)
