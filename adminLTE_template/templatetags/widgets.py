from django import template
register = template.Library()
from django import forms

@register.filter(name='addcls')
def addcls(field, css):
	if hasattr(field, 'as_widget'):
		return field.as_widget(attrs={"class":css})
	else:
		return None

@register.filter(name='atribut')
def atribut(field_, attr_):
	if hasattr(field_, 'as_widget'):
		attrs = {}
		attrs_from_str = attr_.split("|")
		for attr in attrs_from_str:
			k_, v_ = attr.split(":")
			attrs.update({k_: v_})
		return field_.as_widget(attrs=attrs)
	else:
		return None

@register.filter('is_select')
def is_select(field):
	if isinstance(field.field.widget, forms.RadioSelect) or isinstance(field.field.widget, forms.widgets.CheckboxSelectMultiple or isinstance(field.field.widget, forms.ModelMultipleChoiceField)):
		return False
	return isinstance(field.field.widget, forms.Select) or str(field.field.widget.__class__.__name__) == 'RelatedFieldWidgetWrapper'

@register.filter('is_multipleselect')
def is_multipleselect(field):
	return isinstance(field.field.widget, forms.ModelMultipleChoiceField)

@register.filter('is_date')
def is_date(field):
	return isinstance(field.field.widget, forms.DateInput)

@register.filter('is_datetime')
def is_datetime(field):
	return isinstance(field.field.widget, forms.SplitDateTimeWidget)

@register.filter('is_time')
def is_time(field):
	return isinstance(field.field.widget, forms.TimeInput)
	
@register.filter('is_file')
def is_file(field):
	return isinstance(field.field.widget, forms.FileInput)

@register.filter('is_readonlypassword')
def is_readonlypassword(field):
	from django.contrib.auth.forms import ReadOnlyPasswordHashWidget
	return isinstance(field.field.widget, ReadOnlyPasswordHashWidget)

@register.filter(name='get_filter_choices')
def get_filter_choices(spec, cl):
	if spec:
		return list(spec.choices(cl))
	else:
		return ()

# @register.filter(name='filter_bulan_tahun')
# def filter_bulan_tahun(val, arg):
# 	data = ""
# 	# print val
# 	if arg == "bulan":
# 		val = val.split("-")[0]
# 		# print val
# 		if val == "01":
# 			data = "Januari"
# 		elif val == "02":
# 			data = "Februari"
# 		elif val == "03":
# 			data = "Maret"
# 		elif val == "04":
# 			data = "April"
# 		elif val == "05":
# 			data = "Mei"
# 		elif val == "06":
# 			data = "Juni"
# 		elif val == "07":
# 			data = "Juli"
# 		elif val == "08":
# 			data = "Agustus"
# 		elif val == "09":
# 			data = "September"
# 		elif val == "10":
# 			data = "Oktober"
# 		elif val == "11":
# 			data = "November"
# 		elif val == "12":
# 			data = "Desember"
# 	elif arg == "tahun":
# 		data = val.split("-")[1]
# 	return data