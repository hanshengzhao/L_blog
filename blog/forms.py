#!coding:utf-8
import sys
import os,django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["DJANGO_SETTINGS_MODULE"]="django_test.settings"
django.setup()

from django import forms


FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                            ('green', 'Green'),
                            ('black', 'Black'))
PHONE_CHOICES = (
    ('iphone','苹果手机'),
    ('vivo','vivo手机'),
)

class NameForm(forms.ModelForm):


    name = forms.CharField(label=u'用户名', max_length=100,error_messages={'max_length':u'最大长度为100'},widget=forms.TextInput(attrs={'class': 'special','id': 'myFIELD'}))
    password = forms.CharField(label=u'密码', max_length=100,widget=forms.PasswordInput)
    phone = forms.ChoiceField(label=u'使用的手机',required=False,choices=PHONE_CHOICES)
    url = forms.URLField()
    favorite_colors = forms.MultipleChoiceField(label=u'最喜欢的颜色',required=False,
                                                widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)


if __name__ == "__main__":
    data= {'name':'hansz','password':'django','phone':'vivo','url':'http://1.1.2.3','favorite_colors':'black'}
    # data = {}
    f = NameForm(data,auto_id='id_for_%s')
    # f = NameForm()
    print 100*"*",'渲染在p标签中  '
    print f.as_p()
    # print f['name']
    # print 100 * "*",' 以表格的形式将它们渲染在<tr> 标签中'
    # print f.as_table()
    # print 100 * "*" ,'渲染在li标签中   '
    # print f.as_ul()