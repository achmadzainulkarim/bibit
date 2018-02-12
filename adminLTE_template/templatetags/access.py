from django import template
from django.contrib.auth.models import Group
register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
	try:
		group = Group.objects.get(name=group_name)
	except Exception, e:
		return False
	
	return True if group in user.groups.all() else False

from django.contrib.admin.models import LogEntry

import datetime
from dateutil.relativedelta import relativedelta

@register.assignment_tag
def get_logs(user, total_):
	if user.is_superuser:
		logs = LogEntry.objects.all()
	elif not user.is_anonymous():
		logs = LogEntry.objects.filter(user=user)
	else:
		logs = LogEntry.objects.none()
	if total_:
		return [logs[:total_], logs.count()]
	else:
		return [logs, logs.count()]