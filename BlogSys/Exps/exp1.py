import datetime
from django.template import Template, Context
from multiprocessing.util import get_temp_dir
from django.template.loader import get_template
from BlogSys import urls
 
rawTemp ='''
{% ifequal section 'sitenews' %}
    Site News
{% else %}
    No News Here
{% endifequal %}
'''
 
t = Template(rawTemp)
sections  = 'sitenew'
 
c = Context({'section' : sections})
 
print(t.render(c))
