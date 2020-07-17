import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-amp-by-ByteCore",
    version="0.0.2",
    author="ByteCore",
    author_email="",
    description="AMP helpers for django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/8ByteCore8/django-amp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)