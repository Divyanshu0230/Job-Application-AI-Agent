"""
Setup script for the Job Application AI Agent package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="job-application-ai-agent",
    version="0.1.0",
    author="Divyanshu",
    author_email="divyanshupratap23@gmail.com",
    description="AI-powered job application automation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Divyanshu0230/Job-Application-AI-Agent",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "job-application-ai-agent=job_application_ai_agent.__main__:main",
        ],
    },
    include_package_data=True,
) 