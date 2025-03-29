from setuptools import setup, find_packages

setup(
    name='geompy3',
    version='1.0.0',
    packages=find_packages(),
    author="Ja",
    description="description",
    install_requires=[],  # Nie ma potrzeby dodawania 'math'
    entry_points={
        'console_scripts': [
            'geompy3=geompy3.scripts:main',  # Zmienna 'main' w pliku 'scripts.py'
        ],
    },
)
