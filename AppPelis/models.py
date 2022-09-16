from statistics import mode
from django.db import models

ANOS = (('2000','2000'),('2001','2001'),('2002','2002'),('2003','2003'),('2004','2004'),('2005','2005'),
('2006','2006'),('2007','2007'),('2008','2008'),('2009','2009'),('2010','2010'),('2011','2011'),('2012','2012'),
('2013','2013'),('2014','2014'),('2015','2015'),('2016','2016'),('2017','2017'),('2018','2018'),('2019','2019'),
('2020','2020'),('2021','2021'),('2022','2022'))
GENEROS = (('ACC','Acción'),('ANI','Anime'),('CF','Ciencia ficción'),('CLA','Clásicas'),('COM','Comedias'),('DEP','Deportes'),('DOC','Documentales'),('DRM','Dramas'),
('EXT','Extranjeras'),('FAN','Fántasticas'),('MEX','Mexicanas'),('ROM','Románticas'),('TER','Terror'))

# Create your models here.
class Pelicula(models.Model):
	nombre = models.CharField(verbose_name='Nombre',max_length=50)
	genero = models.CharField(choices=GENEROS, 
	verbose_name='Seleccionar género',
	max_length=70,
	default='ACC')
	anos = models.CharField(choices=ANOS,
	verbose_name='Seleccionar año',
	max_length=4,
	default='2000')
	sinopsis=models.TextField(null=True)
	director=models.CharField(max_length=70)
	pais=models.CharField(max_length=70)
	precio=models.FloatField(null=True)
	image=models.ImageField(verbose_name='Elija una imagen',upload_to='pelis-image',null=True)

	def __str__(self):
		return self.nombre

class Meta:
	verbose_name ='Pelicula'
	verbose_name_plural='Peliculas'

