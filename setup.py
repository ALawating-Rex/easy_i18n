import setuptools

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy_i18n",
    version="1.0.0",
    author="aex",
    author_email="aex.chen@qq.com",
    description="an easy way come true i18n for python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ALawating-Rex/easy_i18n",
    packages=["easy_i18n"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
