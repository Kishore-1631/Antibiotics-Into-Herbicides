from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField()
    email=models.EmailField(unique=True)
    department=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    emp_id = models.CharField(null=True, max_length=50)
    # BIOHERB_ANALYSIS
    grant = models.BooleanField(null=True, default=False)
    revoke = models.BooleanField(null=True, default=False)
    # BIOQUOTIENT SCAN
    accept = models.BooleanField(null=True, default=False)
    decline = models.BooleanField(null=True, default=False)
    # HERBICONVERSION NEXUS
    admit = models.BooleanField(null=True, default=False)
    deny = models.BooleanField(null=True, default=False)