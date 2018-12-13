from setuptools import setup, find_packages

with open('./README.md', 'r') as f:
    long_description = f.read()

setup(name='phylactery',
      version='0.2.0',
      description='Curated collection of data structures for Python.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/Yomguithereal/phylactery',
      license='MIT',
      author='Guillaume Plique',
      author_email='kropotkinepiotr@gmail.com',
      keywords='url',
      # python_requires='>=3',
      packages=find_packages(exclude=['test']),
      package_data={'docs': ['README.md']},
      zip_safe=True)
