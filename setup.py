from setuptools import setup

try:
    with open('LICENSE', 'r') as f:
        _license = f.read()
except:
    _license = ''

try:
    with open('README', 'r') as f:
        _readme = f.read()
except:
    _readme = ''

setup(
  name='pyqt_finance',
  packages=['pyqt_finance'],
  version='0.0.1',
  description='Custom QWidget for display historical stock data',
  author='Andrew Porter',
  author_email='porter.r.andrew@gmail.com',
  license=_license,
  long_description=_readme,
  url='https://github.com/AndrewRPorter/pyqt-finance',
  download_url='https://github.com/AndrewRPorter/pyqt-finance/releases',
  install_requires=['setuptools', 'pandas', 'requests', 'yahoo-historical', 'matplotlib'],
 )
