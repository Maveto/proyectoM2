from django.db import models

# Create your models here.

class Lectura(models.Model):
	Titulo = models.CharField(max_length=50)
	Tema = models.CharField(max_length=50)
	Contenido = models.TextField()

	def __str__(self):
		return "{0}".format(self.Titulo)

class Docente(models.Model):
	Nombre = models.CharField(max_length=30)
	Apellido_Paterno = models.CharField(max_length=30)
	Apellido_Materno = models.CharField(max_length=30)
	Mail = models.EmailField(max_length=254)
	CI = models.CharField(max_length=8)

	def __str__(self):
		return "{0} {1}, {2}".format(self.Apellido_Paterno,self.Apellido_Materno,self.Nombre)

"""class Curso(models.Model):
	Docente = models.ForeignKey(Docente,null=False,blank=False,on_delete=models.CASCADE)
	Lectura = models.ForeignKey(Lectura,null=False,blank=False,on_delete=models.CASCADE)

	def __str__(self):
		return "{0} ({1})".format(self.Lectura,self.Docente)"""


class Course(models.Model):
	id = models.AutoField(primary_key = True)
	code_course = models.CharField('Código', max_length=10)
	name_course = models.CharField('Curso', max_length=100)
	website_course = models.URLField('Web Site', max_length=250, null=True, blank=True, 
		help_text="Escriba la dirección completa incluido http:// o https://")
	description_course = models.TextField('Descripción', max_length=100, 
		null=True, blank=True, help_text="Maximo 100 caracteres")
	prerequisites_course = models.TextField('Pre-requisitos', max_length=300, 
		null=True, blank=True)
	content = models.ForeignKey('Lectura',on_delete=models.CASCADE, null=True)
	docente = models.ForeignKey('Docente',on_delete=models.CASCADE, null=True)
	course_document = models.FileField('Documento del curso', upload_to='cursos/',
		blank=True, null=True, 
		help_text='Documento describiendo el contenido del curso/publicidad.')
	past_course = models.BooleanField('Descontinuado', default=False)
	image = models.ImageField(upload_to='cursosImg/',null=True,blank=True,help_text='Imagen de portada')
	class Meta:
		verbose_name_plural = 'Cursos del Instituto'
		ordering = ['id']
	def __str__(self):
		return self.name_course