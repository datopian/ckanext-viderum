import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.viderum import helpers as viderum_helpers

class ViderumPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'viderum/templates')


class ViderumSpatialPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'viderum_spatial/templates')

	# ITemplateHelpers

    def get_helpers(self):
        return {
                'viderum_get_default_extent': viderum_helpers.viderum_get_default_extent,
                }