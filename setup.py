from setuptools import setup, find_packages

setup(
    name='CalmDownSpike',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'sqlalchemy',
        'psycopg2'
    ],
    entry_points={
        'console_scripts': [
            'calmdownspike=app.main:main',
        ],
    },
)