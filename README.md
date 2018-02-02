# Ckan Viderum

This extension extends CKAN footer.html and provide links to Viderum page.

## Installation

To install ckanext-viderum:

1. Activate your CKAN virtual environment, for example:

```
. /usr/lib/ckan/default/bin/activate
```

2. Install the ckanext-viderum Python package into your virtual environment:

```
pip install ckanext-viderum
```

3. Add ``viderum`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

```
sudo service apache2 reload
```


## Config Settings

There are no required configuration options used by the extension.

## Development Installation

To install ckanext-viderum for development, activate your CKAN virtualenv
and do:

```
git clone https://github.com/ViderumGlobal/ckanext-viderum.git
cd ckanext-viderum
python setup.py develop
pip install -r dev-requirements.txt
```
