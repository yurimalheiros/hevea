try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = ['hevea']
requires = []

setup(name='hevea',
      version='0.2',
      description='Monitor and compile LaTeX files',
      long_description=open('README.md').read(),
      author=u'Yuri Malheiros',
      author_email='contato@yurimalheiros.com',
      url='https://github.com/yurimalheiros/hevea/',
      packages=packages,
      package_data={'': ['LICENSE', 'README.md'], 'hevea': []},
      package_dir={'hevea': 'hevea'},
      scripts=['scripts/hevea'],
      include_package_data=True,
      license=open('LICENSE').read(),
      zip_safe=False,
      install_requires = ['PyYAML==3.10',
                          'argh==0.21.1',
                          'argparse==1.2.1',
                          'pathtools==0.1.2',
                          'watchdog==0.6.0',
                          'wsgiref==0.1.2'],
      classifiers = ['Development Status :: 2 - Pre-Alpha',
                     'Environment :: Console',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Text Processing :: Markup :: LaTeX'],
)
