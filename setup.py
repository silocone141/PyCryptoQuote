from setuptools import setup, find_packages


setup(
    name='PyCryptoQuote',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    url="",
    author="silocone",
    license="MIT",
    install_requires=[
        "Click",
        "pyyaml",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'pycq = PyCryptoQuote:cli',
        ],
    },
)
