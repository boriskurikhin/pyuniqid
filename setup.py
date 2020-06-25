from distutils.core import setup
setup(
    name = 'pyuniqid',
    packages = ['pyuniqid'],
    version = '0.1',
    license='MIT',
    description = 'A Unique Hexatridecimal ID generator',
    long_description ='A Unique Hexatridecimal ID generator',
    author = 'Boris Skurikhin',
    author_email = 'boriskurikhin@gmail.com',
    url = 'https://github.com/boriskurikhin/pyuniqid',
    download_url = 'https://github.com/boriskurikhin/pyuniqid/archive/v_01.0.tar.gz',
    keywords = ['unique', 'id', 'unique identifier', 'hexatridecimal', 'unique id', 'uniqid'],
    install_requires=[
        'netifaces',
        'numpy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)