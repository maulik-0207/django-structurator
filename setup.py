from setuptools import setup, find_packages

# Long description read from your README file
with open('./docs/README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name="django-structurator",
    version="1.0.0",
    author='@maulik-0207',
    author_email='maulikthumar784@gmail.com',
    description='django-structurator is an open-source CLI tool that streamlines and accelerates the setup of well-organized Django projects and apps, enabling developers to focus on building features instead of boilerplate.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/maulik-0207/django-structurator',
    project_urls={
        'Documentation': 'https://github.com/maulik-0207/django-structurator/blob/master/docs/README.md',
        'Source': 'https://github.com/maulik-0207/django-structurator',
        'Tracker': 'https://github.com/maulik-0207/django-structurator/issues',
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'django_structurator': [
            'templates/project_template/*',
            'templates/project_template/**/*',
            'templates/project_template/.*',
            'templates/app_template/*',
            'templates/app_template/**/*',
            'templates/app_template/.*',
        ],
    },
    classifiers=[  # Categorize your package
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python :: 3 :: Only',
    ],
    python_requires='>=3.8',
    install_requires=[
        "django",
        "inquirer"
    ],
    entry_points={
        "console_scripts": [
            "django-str = django_structurator.cli:main",
        ],
    },
    keywords="django project-generator cli tool django-cli",
)
