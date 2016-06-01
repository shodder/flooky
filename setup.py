'''
flooky
----

Basic flask project setup
'''

from setuptools import setup, find_packages


setup(
    name='flooky',
    version='0.1',
    url='github.com/siomnhodder/flooky',
    license='',
    author='Simon Hodder',
    author_email='hodder.simon@gmail.com',
    description='Basic flask project setup',
    long_description=__doc__,
    # For packaging
    include_package_data=True,
    packages=find_packages('src', exclude=['tests']),
    package_data={'':['*.odx'],},
    # As we put our packages in sub folder src do the following:
    package_dir={'': 'src'},
    install_requires=[
        'pymysql',
        'flask',
        'click',
    ],
    tests_require=[
        'pytest',
        'pytest-xdist',
        'pytest-cov',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    extras_require={
        'testing': ['pytest', 'pytest-xdist', 'pytest-cov', ],
    },
    entry_points={
        'console_scripts': [
            'flooky=flooky.cli:cli',
        ],
    },
)
