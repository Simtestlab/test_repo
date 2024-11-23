
with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

reqs = [req for req in requirements]
name="Stl CAN Tool",
version='0.0.1',
author="Siva",
author_email="nallasivmselvaraj@gamil.com",
description="simtestlab work dirctory",
long_description=long_description,
long_description_content_type="text/markdown",
install_requires=reqs,
include_package_data=True,
