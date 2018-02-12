from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items
from django.db.models import Q
from admin_tools.menus import Menu

class CustomMenu(Menu):
	def __init__(self, **kwargs):
		Menu.__init__(self, **kwargs)

	def init_with_context(self, context):
		from django.core.urlresolvers import resolve
		request = context['request']

		self.children += [
			items.MenuItem(
					title=_('Beranda'),
					description='Admin Home Page',
					icon='fa fa-home',
					url=reverse('admin:index'),
				),
			]
			
		return super(CustomMenu, self).init_with_context(context)
