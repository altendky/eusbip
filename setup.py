import setuptools
import versioneer


with open('README.rst') as f:
    readme = f.read()


setuptools.setup(
    name='eusbip',
    author='Kyle Altendorf',
    description="Ease working with usbip.",
    long_description=readme,
    long_description_content_type='text/x-rst',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='MIT',
    classifiers=[
        # complete classifier list: https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'eusbip = eusbip.cli:main',
        ],
    },
    install_requires=[
        'attrs',
        'click',
    ],
    extras_require={
        'dev': [
            'coverage',
            'gitignoreio',
            'pytest',
            'pytest-cov',
        ],
    },
)
