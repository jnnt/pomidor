from setuptools import setup


setup(
    name='pomidor',
    packages=['pomidor'],
    install_requires=[
        'click',
        'pyserial',
        'pyYAML',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'pomidor = pomidor.poller:toggl_poll',
        ],
    }
)
