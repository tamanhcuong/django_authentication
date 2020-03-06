from django.db import models
import calendar
import time
import uuid
from permission.models import PermissionModel


class RoleModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    permissions = models.ManyToManyField(PermissionModel, related_name = "role_permission" )
    time_created = models.BigIntegerField(
        default=calendar.timegm(time.gmtime()))
    time_modified = models.BigIntegerField(
        default=calendar.timegm(time.gmtime()))
    # created_by = models.CharField(blank=True, max_length=255)
    # modified_by = models.CharField(blank=True, max_length=255)

    # link table  
    def save(self,*args,**kwargs):
   	self.time_modified=calendar.timegm(time.gmtime())
   	if self._state.adding is True:
   		self.time_created=calendar.timegm(time.gmtime())
   	super(RoleModel,self).save(*args,**kwargs)

    class Meta:
        db_table = 'role'