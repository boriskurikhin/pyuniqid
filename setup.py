from setuptools import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'pyuniqid',
    packages = ['pyuniqid'],
    version = '1.0',
    license='MIT',
    description = 'A Unique Hexatridecimal ID generator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Boris Skurikhin',
    author_email = 'boriskurikhin@gmail.com',
    url = 'https://github.com/boriskurikhin/pyuniqid',
    download_url = 'https://github.com/boriskurikhin/pyuniqid/archive/v_01.1.zip',
    keywords = ['unique', 'id', 'unique identifier', 'hexatridecimal', 'unique id', 'uniqid'],
    install_requires=[
        'netifaces',
        'numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)