from setuptools import setup
setup(
    name='tr_domain_email',
    version='0.1',
    py_modules=[''],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [cnosole_scripts]
        tr_domain_email=tr_domain_email:cli
    '''
)