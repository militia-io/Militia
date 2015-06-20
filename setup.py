from setuptools import setup, find_packages

setup(name='militia',
      version='0.1',
      description='Intelligent and intuitive applications for analysts',
      url='http://github.com/vlall/militia',
      author='V Lall, M Bartoli',
      author_email='vishal.h.lall@gmail.com',
      license='BSD',
    packages=find_packages(exclude=['apps','tests']),
      zip_safe=False)