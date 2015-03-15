cryptsy_api
===========

Python library for all cryptsy.com API's.

Includes mostly complete documentation tested live for correctness, partialy borrowed from
    https://www.cryptsy.com/pages/api.

Full documentation, extensibility and ipython/pydev user-friendliness in mind.


|Build Status| |Coveralls| |Documentation Status| |Requirements Status|
|Downloads| |Latest Version| |Supported Python versions|
|Supported Python implementations| |Development Status| |Wheel Status|
|Egg Status| |Download format| |License|


Installation
------------
::
    pip install cryptsy_api


Examples
--------
::
    # use only public services
    from cryptsy_api import *
    c = CryptsyApi()
    c.markets(1)

    # direct key specification
    from cryptsy_api import *
    c = CryptsyApi('public key', 'private key')
    c.markets.fees(1)
    
    # class configuration
    class MyCryptsyApiConfig(CryptsyApiConfig):
        public_key = 'mypublickey'
        private_key = 'myprivatekey'

    c = CryptsyApi(MyCryptsyApiConfig)
    c.info()

TODO
----
* Integration testing of ? marked responses and samples.
* Non-(Sphinx/napoleon style) documentation system without too much blank lines.
* Unit tests.
* Github services integration (travis, badges, etc.).

Nice to have
------------
* Push support.
* Models.

.. |Build Status| image:: https://travis-ci.org/katakumpo/cryptsy_api.svg
   :target: https://travis-ci.org/katakumpo/cryptsy_api
.. |Coveralls| image:: https://coveralls.io/repos/katakumpo/cryptsy_api/badge.png?branch=master
   :target: https://coveralls.io/r/katakumpo/cryptsy_api?branch=master
.. |Downloads| image:: https://pypip.in/download/cryptsy_api/badge.svg
   :target: https://pypi.python.org/pypi/cryptsy_api/
.. |Latest Version| image:: https://pypip.in/version/cryptsy_api/badge.svg
   :target: https://pypi.python.org/pypi/cryptsy_api/
.. |Supported Python versions| image:: https://pypip.in/py_versions/cryptsy_api/badge.svg
   :target: https://pypi.python.org/pypi/cryptsy_api/
.. |Supported Python implementations| image:: https://pypip.in/implementation/cryptsy_api/badge.svg
   :target: https://pypi.python.org/pypi/cryptsy_api/
.. |Development Status| image:: https://pypip.in/status/cryptsy_api/badge.svg
   :target: https://pypi.python.org/pypi/cryptsy_api/
.. |Wheel Status| image:: https://pypip.in/wheel/cryptsy_api/badge.svg
   :target: https://pypi.python.org/pypi/cryptsy_api/
.. |Egg Status| image:: https://pypip.in/egg/cryptsy_api/badge.svg
   :target: https://pypi.python.org/pypi/cryptsy_api/
.. |Download format| image:: https://pypip.in/format/cryptsy_api/badge.svg
   :target: https://pypi.python.org/pypi/cryptsy_api/
.. |License| image:: https://pypip.in/license/cryptsy_api/badge.svg
   :target: https://pypi.python.org/pypi/cryptsy_api/
.. |Documentation Status| image:: https://readthedocs.org/projects/cryptsy_api-py/badge/?version=latest
   :target: https://cryptsy_api-py.readthedocs.org/en/latest/
.. |Codeship| image:: https://www.codeship.io/projects/c6e982d0-493e-0132-73e9-7e9eac026bf8/status
   :target: https://www.codeship.io/projects/46084
.. |Requirements Status| image:: https://requires.io/github/katakumpo/cryptsy_api/requirements.svg?branch=master
   :target: https://requires.io/github/katakumpo/cryptsy_api/requirements/?branch=master
