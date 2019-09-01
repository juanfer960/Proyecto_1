from django.db import models
import datetime


# Create your models here.

class SiteAdmin(models.Model):
    site_login = models.EmailField(verbose_name="Correo electrónico", unique=True)
    site_password = models.CharField(verbose_name="Clave", max_length=30)
    site_name = models.CharField(verbose_name="Compañía", max_length=255, unique=True)
    site_url = models.CharField(verbose_name="URL", max_length=300, unique=True)


class SiteProjects(models.Model):
    prj_site = models.ForeignKey(SiteAdmin, on_delete=models.CASCADE, editable=False)
    prj_name = models.CharField(verbose_name="Proyecto", max_length=255, unique=True)
    prj_description = models.TextField(verbose_name="Descripción", blank=True)
    prj_budget = models.DecimalField(verbose_name="Valor estimado a pagar", decimal_places=2, max_digits=20)
    prj_creationdate = models.DateField(verbose_name="Fecha de creación", default=datetime.date.today)


class ProjectDesigns(models.Model):

    PRJDSG_STATUSES = {
        ('P', 'En proceso'),
        ('D', 'Disponible'),
    }

    prjdsg_project = models.ForeignKey(SiteProjects, on_delete=models.CASCADE, editable=False)
    prjdsg_login = models.EmailField(verbose_name="Correo electrónico")
    prjdsg_firstname = models.CharField(verbose_name="Nombres", max_length=255)
    prjdsg_lastname = models.CharField(verbose_name="Apellidos", max_length=255)
    prjdsg_price = models.DecimalField(verbose_name="Precio solicitado", decimal_places=2, max_digits=20)
    prjdsg_uploaddate = models.DateField(verbose_name="Entregado", default=datetime.date.today)
    prjdsg_status = models.CharField(verbose_name="Estado", max_length=20, choices=PRJDSG_STATUSES)
    prjdsg_original_file = models.ImageField(upload_to='originals', null=True)
    prjdsg_processed_file = models.ImageField(upload_to='processed', null=True)
