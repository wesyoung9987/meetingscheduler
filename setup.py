import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meeting_scheduler",
    version="0.0.3",
    author="Wes Young",
    author_email="wes.young14@gmail.com",
    description="A meeting scheduler package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wesyoung9987/meetingscheduler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
