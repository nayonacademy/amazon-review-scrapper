from setuptools import setup

setup(name='amazonreviewscrap',
      version='0.1',
      description='Amazon review scrapper. Without any IP block It will work with selenium and bs4',
      url='https://github.com/nayonacademy/amazon-review-scrapper',
      author='Shariful Islam Nayon',
      author_email='si.nayon@gmail.com',
      license='MIT',
      packages=['amazonreviewscrap'],
      install_requires=[
          'beautifulsoup4',
          'requests',
          'selenium',
          'webdriver-manager'
      ],
      zip_safe=False)