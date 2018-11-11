from setuptools import setup

setup(name='colored_json_print',
      version='0.1',
      description='Colored json string output for your console.',
      long_description='Fast and easy way to print colored json object output to your console.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Console :: Shell',
      ],
      keywords='console shell color print output',
      url='',
      author='Matt Andrzejczuk',
      author_email='cinicraft@me.com',
      license='MIT',
      packages=['colored_json_print'],
      install_requires=['git+https://github.com/MattAndrzejczuk/PyInk.git', 'pygments'],
      include_package_data=True,
      zip_safe=False)
