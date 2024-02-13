import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

REPO_NAME="WINE QUALITY PREDICTION"
AUTHOR='GIRUPA'
SRC_REPO='mlproject'


setuptools.setup(
    name=SRC_REPO,
    version='0.1.2',
    author=AUTHOR,
    description="A SMALL PYTHON PACKAGE FOR ML APP .",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR}/{REPO_NAME}',
    project_urls={
        "Bug Tracker": f'https://github.com/{AUTHOR}/{REPO_NAME}/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    install_requires=[
          'numpy',
          'pandas',
          'scikit-learn==0.24.1',
          'tensorflow>=2.6.0',      
          'imbalanced-learn',         # For handling imbalance classes in data
          'matplotlib',                 # Plotting library
          'seaborn',                   # Data visualization library     
          'sklearn-crfsuite',          # Conditional Random Fields for sklearn
          'nltk',                      # Natural language tool kit
          'beautifulsoup4',            # To parse HTML files  
          'requests',                  # To make HTTP requests to web pages
          'gunicorn'                   # To run the app on gunicorn server
     ],
)