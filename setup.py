from setuptools import setup

setup(name='viminit',
      version='0.2',
      description='Set up a vimlang plugin project directory.',
      url='http://github.com/vmchale/viminit',
      author='Vanessa McHale',
      author_email='tmchale@wisc.edu',
      license='BSD3',
      packages=['viminit'],
      scripts=['bin/viminit'],
      install_requires=[
          'gitpython',
      ],
      zip_safe=False)
