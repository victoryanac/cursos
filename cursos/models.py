from django.db import models

# Create your models here.

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    dpto = models.CharField(max_length=10, null=True, blank=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estudiante_id = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comuna}, {self.ciudad}, {self.region}"



class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField()
    modificacion_registro = models.DateField()
    creado_por = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True, primary_key=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesores = models.ManyToManyField(Profesor)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField()
    modificacion_registro = models.DateField()
    creado_por = models.CharField(max_length=50)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE, to_field='estudiante_id', db_column='estudiante_id')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
