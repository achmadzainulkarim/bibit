from django import template
register = template.Library()

@register.filter(name='timedelta_jam')
def timedelta_jam(timedelta_):
	tjk = timedelta_.total_seconds() / 3600
	return str(tjk)
	
@register.assignment_tag
def zero_timedelta():
	return timedelta(0)

@register.assignment_tag
def adding(a_, b_):
	t=a_+b_
	return t

@register.assignment_tag
def mod(a_, b_):
	t=a_%b_
	return t

@register.assignment_tag
def sub(a_, b_):
	t=a_-b_
	return t

@register.assignment_tag
def mul(a_, b_):
	t = a_ * b_
	return t

@register.assignment_tag
def div(a_, b_):
	t = a_ / b_
	return t

@register.filter(name='get_range')
def get_range(a_):
	return range(a_)