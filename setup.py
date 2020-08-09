from setuptools import setup, find_packages

# Create Short Description
DESC = '''Python OWL is an Open Source Big Data Management and Analytic Service.'''

# Get Python Package Requirements
def getRequirements():
    reqs = []
    with open('requirements.txt') as fp: reqs += fp.readlines()
    reqs = map(str.strip, reqs)
    return reqs

# Initalize Package Setup Upon Pip Installation
setup(
    name = 'owl',
    version = '0.0.1',
    python_requires = '>=3.6',
    description = DESC,
    long_description = DESC,
    author = 'Aidan E. Dykstal',
    author_email = 'dykstala@gmail.com',
    maintainer = 'Aidan E. Dykstal',
    maintainer_email = 'dykstala@gmail.com',
    url = 'https://github.com/dykstal/owl',
    include_package_data = True,
    install_requires = getRequirements(),
    packages = find_packages()
)
