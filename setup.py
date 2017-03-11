from setuptools import setup

setup(name='vimsetup',
      version='0.1',
      description='Set up a vimlang plugin project directory.',
      url='http://github.com/vmchale/vimsetup',
      author='Vanessa McHale',
      author_email='tmchale@wisc.edu',
      license='BSD3',
      packages=['vimsetup'],
      scripts=['bin/vimsetup'],
      install_requires=[
          'gitpython',
      ],
      zip_safe=False)
