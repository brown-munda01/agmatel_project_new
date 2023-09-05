from django.db import models

# Create your models here.


class Data1(models.Model):
    
    school_id=models.IntegerField(max_length=10, null=True)
    location_name=models.CharField( max_length=100, null=True)
    contact_person_name=models.CharField( max_length=100,null=True)
    contact_no=models.CharField( max_length=100,null=True)



    site_readiness=models.CharField( max_length=100, null=True)
    aipl_dc_no=models.CharField( max_length=100, null=True)
    docket_no=models.CharField( max_length=100, null=True)
    bill_no=models.CharField( max_length=100, null=True)



    computer_desktop=models.CharField(max_length=1000, null=True)
    interactive_panel=models.CharField( max_length=100, null=True)
    invertor=models.CharField( max_length=100, null=True)
    io_device=models.CharField( max_length=100, null=True)


    
    hd_web_camera=models.CharField(max_length=100, null=True)
    ups_for_desktop=models.CharField( max_length=1000, null=True)
    pa_system=models.CharField( max_length=100, null=True)
    multi_printer=models.CharField( max_length=100, null=True)

    
    dev_mgmt_app=models.CharField(max_length=100, null=True)
    wifi_router=models.CharField( max_length=100, null=True)
    
    
