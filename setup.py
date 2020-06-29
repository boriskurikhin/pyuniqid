from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyuniqid',
    packages=['pyuniqid'],
    version='1.2',
    license='MIT',
    description='A Unique Hexatridecimal ID generator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Boris Skurikhin',
    author_email='boriskurikhin@gmail.com',
    url='https://github.com/boriskurikhin/pyuniqid',
    download_url='https://test.123',
    keywords=[
        'unique',
        'id',
        'unique identifier',
        'hexatridecimal',
        'unique id',
        'uniqid'],
    install_requires=[
        'netifaces',
        'numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
