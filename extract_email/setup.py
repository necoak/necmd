from setuptools import setup
setup(
    name='extract_email',
    version='0.1',
    py_modules=[''],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [cnosole_scripts]
        extract_email=tr_domain_email:main
    '''
)