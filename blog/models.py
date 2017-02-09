#!coding:utf-8
from django.db import models

# Create your models here.
class ky_asset(models.Model):
    asset_type_value =(
        ("server",u"服务器"),
        ("switch",u"交换机"),
        ("firewall",u"防火墙"),
    )
    asset_type = models.CharField(u"资产类型", choices=asset_type_value, max_length=48, default="server")
    name = models.CharField(u"资产名称", max_length=64, unique=True)
    sn = models.CharField(u'资产SN号', max_length=128, unique=True)
    ip=models.GenericIPAddressField(blank=True,null=True)
    memo = models.TextField(u'备注', null=True, blank=True)
    class Meta:
        verbose_name = u"资产总表"
        verbose_name_plural = u"资产总表"# 这个是复数的意思

    def __unicode__(self):
        return "%s:%s"%(self.asset_type,self.name)