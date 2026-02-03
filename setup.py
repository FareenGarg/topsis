from setuptools import setup, find_packages

setup(
    name="Topsis-FareenGarg-102303971",
    version="1.0.0",
    author="Fareen Garg",
    author_email="fareengarg@example.com",
    description="A Python package for TOPSIS method",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
)
