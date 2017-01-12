=============================
django-haystack-elasticsearch
=============================


.. image:: https://img.shields.io/pypi/v/django-haystack-elasticsearch.svg
        :target: https://pypi.python.org/pypi/django-haystack-elasticsearch

.. image:: https://img.shields.io/travis/CraveFood/django-haystack-elasticsearch.svg
        :target: https://travis-ci.org/CraveFood/django-haystack-elasticsearch

.. image:: https://pyup.io/repos/github/CraveFood/django-haystack-elasticsearch/shield.svg
     :target: https://pyup.io/repos/github/CraveFood/django-haystack-elasticsearch/
     :alt: Updates


A set of backends for using multiple versions of Elasticsearch on Haystack_.


* Free software: BSD license


How to use
----------

* Make sure that your ``elasticsearch`` library has the same major version as your Elasticsearch server.
* Choose the right backend as your ``ENGINE`` on Haystack.

Elasticsearch 1.x
~~~~~~~~~~~~~~~~~

.. code-block:: sh

    $ pip install "elasticsearch>=1.0.0,<2.0.0" django-haystack-elasticsearch

.. code-block:: python

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack_elasticsearch.elasticsearch.ElasticsearchSearchEngine',
            ...
        },
    }

Elasticsearch 2.x
~~~~~~~~~~~~~~~~~

.. code-block:: sh

    $ pip install "elasticsearch>=2.0.0,<3.0.0" django-haystack-elasticsearch

.. code-block:: python

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack_elasticsearch.elasticsearch2.Elasticsearch2SearchEngine',
            ...
        },
    }

Elasticsearch 5.x
~~~~~~~~~~~~~~~~~

.. code-block:: sh

    $ pip install "elasticsearch>=5.0.0,<6.0.0" django-haystack-elasticsearch

.. code-block:: python

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack_elasticsearch.elasticsearch5.Elasticsearch5SearchEngine',
            ...
        },
    }

Credits
-------

This project was based on the original Elasticsearch backend for Haystack_.
Special thanks to `@PedroAquilino`_ and `@joaojunior`_ for their work towards ES2 support.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Haystack: https://github.com/django-haystack/django-haystack
.. _@PedroAquilino: https://github.com/PedroAquilino
.. _@joaojunior: https://github.com/joaojunior
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

