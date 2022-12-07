from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return '{0}/{1}'.format("buses_photos",filename)


class bus_data(models.Model):
    bus_num = models.AutoField(primary_key=True)
    bus_Name = models.CharField(max_length=100, blank=False, null=False )
    bus_Model = models.CharField(max_length=100, blank=False, null=False)
    bus_route = models.CharField(max_length=100, blank=False, null=False)
    ticket_Price = models.IntegerField(max_length=15, blank=False, null=False)
    bus_Photo = models.FileField(upload_to=user_directory_path, null=True, verbose_name="")
    

    class Meta:
        db_table = 'buses' 


class paxDetails(models.Model):
    pax_name = models.CharField(max_length=100)
    pax_gender = models.CharField(max_length=100)
    contact_num = models.IntegerField()
    mail = models.EmailField()
    # date =models.DateField()
    # total_pax = models.IntegerField()

    class Meta:
        db_table = 'pax_details' 