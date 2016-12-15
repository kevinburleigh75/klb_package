from setuptools import setup

setup(name='klb_package',
      version='0.1',
      description='Package experiment',
      url='http://github.com/kevinburleigh75/klb_package',
      author='klb',
      author_email='noone@example.com',
      license='MIT',
      packages=['klb_package'],
      install_requires=[
          'numpy'
      ],
      zip_safe=False)