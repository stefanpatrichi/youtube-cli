
from setuptools import setup, find_packages

setup(
    name='commandline-yt-client',
    version='0.0.1',
    description='Commandline youtube client',
    long_description='Searches youtube and ouputs selected video with mpv',
    author='Grady Arnold',
    author_email='gradyarnold11@gmail.com',
    url='https://github.com/blithersoup/commandline-yt-client',
    platforms=['any'],
    license='GPU',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pyinstaller',
    ],
    entry_points={
        'console_scripts': [
            'cli = src.main.cli:search'
        ]
    },
)