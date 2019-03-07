from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='amazonreviewscrap',
      version='0.1',
      description='Amazon review scrapper',
      long_description ='Amazon review scrapper. Without any IP block It will work with selenium and bs4',
      classifiers=[
          'Development Status :: .1 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6.7',
          'Topic :: Text Processing :: Linguistic',
      ],
      keywords='amazon scrapper datascrap-amazon review-scrap-amazon',
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
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )