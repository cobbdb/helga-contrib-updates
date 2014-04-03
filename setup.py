from setuptools import setup, find_packages

setup(
    name="helga-contrib-updates",
    version="0.0.2",
    packages=find_packages(),
    author="Dan Cobb",
    author_email="cobbdb@gmail.com",
    description="A helga plugin to list IRC channel updates.",
    license='MIT',
    url="https://github.com/cobbdb/helga-contrib-updates",
    zip_safe=False,
    keywords="helga plugin irc standup",
    entry_points={
        'helga_plugins': [
            'updates = helga_updates:updates',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Communications :: Chat',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Topic :: Software Development'
    ]
)
