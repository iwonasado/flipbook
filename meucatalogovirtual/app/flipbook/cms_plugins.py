from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import FlipBookPlugin, FlipBook, FlipBookPage
from django.utils.translation import ugettext as _

class CMSBlogPlugin(CMSPluginBase):
    model = FlipBookPlugin
    name = _("FlipBook Demos")
    render_template = "flipbook/flipbookItem.html"

    def render(self, context, instance, placeholder):
        context.update({
            'flipbooks':FlipBook.objects.filter(demo = True),
            'object':instance,
            'placeholder':placeholder
        })
        return context
    
    
plugin_pool.register_plugin(CMSBlogPlugin)



