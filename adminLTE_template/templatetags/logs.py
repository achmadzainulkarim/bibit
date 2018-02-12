from django import template
register = template.Library()

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