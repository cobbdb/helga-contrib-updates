from setuptools import setup, find_packages

setup(
    name="helga-contrib-updates",
    version="1.0.1",
    packages=find_packages(),
    py_modules=['helga_contrib_updates'],
    author="Dan Cobb, Shaun Duncan",
    author_email="cobbdb@gmail.com, shaun.duncan@gmail.com",
    description="A helga plugin to list and record IRC channel updates.",
    license='MIT',
    url="https://github.com/cobbdb/helga-contrib-updates",
    keywords="helga plugin irc standup",
    entry_points={
        'helga_plugins': [
            'updates = helga_contrib_updates:updates',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
