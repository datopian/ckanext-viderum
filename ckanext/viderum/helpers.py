from ckan.common import config


def viderum_get_default_extent():
    ''' Get default extent setting for spatial search map. '''
    return config.get('ckanext.viderum.default_extent', False)