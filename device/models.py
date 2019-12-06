#coding=utf-8
from django.db import models
from compute.models import Host
from vms.models import Vm

class Device(models.Model):
    '''
    设备抽象基类
    '''
    TYPE_NOKNOW = 0
    TYPE_GPU = 1
    CHOICES_TYPE = (
        (TYPE_NOKNOW, '未知设备'),
        (TYPE_GPU, 'GPU')
    )

    id = models.AutoField(primary_key=True)
    type = models.SmallIntegerField(choices=CHOICES_TYPE, default=TYPE_NOKNOW, verbose_name='设备类型')
    vm = models.ForeignKey(to=Vm, null=True, blank=True, related_name='device_set', on_delete=models.SET_NULL, verbose_name='挂载于虚拟机')
    attach_time = models.DateTimeField(null=True, blank=True, verbose_name='挂载时间')
    enable = models.BooleanField(default=True, verbose_name='状态')
    remarks = models.TextField(null=True, blank=True, verbose_name='备注')

    class Meta:
        abstract = True

    def type_display(self):
        return self.get_type_display()

    def set_remarks(self, content:str):
        '''
        设置设备备注信息

        :param content: 备注信息
        :return:
            True    # success
            False   # failed
        '''
        try:
            self.remarks = content
            self.save()
        except Exception:
            return False
        return True


class PCIDevice(Device):
    '''
    PCIe设备
    '''
    host = models.ForeignKey(to=Host, on_delete=models.CASCADE, related_name='pci_devices', verbose_name='宿主机')
    address = models.CharField(max_length=100, help_text='format:[domain]:[bus]:[slot]:[function], example: 0000:84:00:0')

    class Meta:
        ordering = ['-id']
        verbose_name = 'PCIe设备' 
        verbose_name_plural = 'PCIe设备'

    def __str__(self):
        return self.host.ipv4 + '_' + self.address

    def user_has_perms(self, user):
        '''
        用户是否有访问此设备的权限

        :param user: 用户
        :return:
            True    # has
            False   # no
        '''
        if not isinstance(user.id, int): # 未认证用户
            return False

        if user.is_superuser:
            return True

        if self.host.group.users.filter(pk=user.pk).exists():
            return True

        return False

    def need_in_same_host(self):
        '''
        设备是否需要与挂载的虚拟机在用同一个宿主机上
        '''
        if self.type in [self.TYPE_GPU]:
            return True
        return False
