from setuptools import setup


setup(
    name='pomidor',
    packages=['pomidor'],
    install_requires=[
        'click',
        'requests',
        'pyserial'
    ],
    entry_points={
        'console_scripts': [
            'toggl-poll = pomidor.poller:toggl_poll',
        ],
    }
)
