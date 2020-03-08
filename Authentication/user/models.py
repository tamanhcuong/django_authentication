from django.db import models
import calendar
import time
import uuid
from role.models import RoleModel


class UserModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    role = models.ManyToManyField(RoleModel, related_name = "user_role")    
    time_created = models.BigIntegerField(
        default=calendar.timegm(time.gmtime()))
    time_modified = models.BigIntegerField(
        default=calendar.timegm(time.gmtime()))    
    # created_by = models.CharField(blank=True, max_length=255)
    # modified_by = models.CharField(blank=True, max_length=255)

    # link table
    #permissions = models.ManyToManyField(PermissionModel)
    def save(self,*args,**kwargs):
        self.time_modified=calendar.timegm(time.gmtime())       
        if self._state.adding is True:
            self.time_created=calendar.timegm(time.gmtime())
        super(UserModel,self).save(*args,**kwargs)

    class Meta:
        db_table = 'user'