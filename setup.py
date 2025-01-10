from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="radagast",
    version="1.0.0",
    author="Renato Brescia",
    description="radagast is an open source penetration testing tool, able to perform a web fuzzer attack against http services.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,

    entry_points={
        "console_scripts": [
            "radagast=radagast.radagast:main",
        ],
    },
    python_requires=">=3.6",
)
