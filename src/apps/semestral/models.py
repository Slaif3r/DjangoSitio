from django.db import models

class Profesor(models.Model):
    nombreProf   = models.CharField(max_length = 50, blank = False, default = None, verbose_name = 'Nombre')
    apellidoProf = models.CharField(max_length = 50, blank = False, default = None, verbose_name = 'Apellido')
    cedulaProf   = models.CharField(max_length = 50, blank = False, default = None, verbose_name = 'Cedula')
    fecha_de_creacionProf      = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_de_actualizacionProf = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    class Meta:
        verbose_name_plural = 'Profesor'
        db_table = 'profesor'
        ordering = ['nombreProf', 'apellidoProf']
    def __unicode__(self, *args, **kwargs):
        # Python 2
        return '{}'.format(self.nombreProf)
    def __str__(self, *args, **kwargs):
        # Python 3
        ctx = {
            'nombre': self.nombreProf,
            'apellido': self.apellidoProf
        }
        return '{nombre} - {apellido}'.format(**ctx)

class Estudiante(models.Model):
    HOMBRE = 'hombre'
    MUJER = 'mujer'
    OTROS = 'otros'

    GENRE_CHOICES = (
        (HOMBRE, "Hombre"),
        (MUJER, "Mujer"),
        (OTROS, "Otros"),
    )

    nombreEST    = models.CharField(max_length=100, blank=False, null=False, default='', verbose_name='Nombre')
    apellidoEST  = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name='Apellido')
    edadEST      = models.PositiveIntegerField(blank=True, null=True, verbose_name='Edad')
    generoEST    = models.CharField(max_length=30, choices=GENRE_CHOICES, default=OTROS,
                                   blank=True, null=True, verbose_name='Género')
    salarioEST   = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True,
                                  verbose_name='Salario')

    fecha_de_creacionEST       = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_de_actualizacionEST  = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name_plural = 'Estudiantes'
        db_table = 'estudiantes'
        ordering = ['nombreEST', 'apellidoEST']

    def __unicode__(self, *args, **kwargs):
        # Python 2
        return '{}'.format(self.nombreEST)

    def __str__(self, *args, **kwargs):
        # Python 3
        ctx = {
            'nombre': self.nombreEST,
            'apellido': self.apellidoEST
        }
        return '{nombre} - {apellido}'.format(**ctx)



class Asignatura(models.Model):
	
    SISTEMAS = '0'
    INDUSTRIAL = '1'
    CIVIL = '2'
    ELECTRICA = '3'
    CIENCIAS_Y_TECNOLOGIA = '4'

    FACULTAD_CHOICES = (
        (SISTEMAS, "Facultad de Sistemas"),
        (INDUSTRIAL, "Facultad de Industrial"),
        (CIVIL, "Facultad de Civil"),
        (ELECTRICA, "Facultad de Eléctrica"),
        (CIENCIAS_Y_TECNOLOGIA, "Facultad de Ciencias y Tecnología"),
    )

    nombre      = models.CharField(max_length=100, blank=False, null=False, default='', verbose_name='Nombre')
    descripcion = models.TextField(blank=True, null=True, default='', verbose_name='Descripción')
    codigo      = models.CharField(max_length=10, blank=True, null=True, verbose_name='Código')
    facultad    = models.CharField(max_length=30, choices=FACULTAD_CHOICES, default=SISTEMAS,
                                blank=True, null=True, verbose_name='Facultad')
    fecha_de_creacion      = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_de_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    profesor    = models.ForeignKey(Profesor, null=True, blank=True, default=None, verbose_name='Profesor')
    

    class Meta:
        verbose_name_plural = 'Asignaturas'
        db_table = 'asignaturas'
        ordering = ['facultad', 'nombre', ]

    def __unicode__(self, *args, **kwargs):
        # Python 2
        return '{}'.format(self.nombre)

    def __str__(self, *args, **kwargs):
        # Python 3
        return '{} - {}'.format(self.facultad_selected, self.nombre)

    @property
    def facultad_selected(self):
        return self.get_facultad_display()

class Notas(models.Model):
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    fecha_de_creacionNot      = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_de_actualizacionNot = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    asignatura        = models.ForeignKey(Asignatura, blank=True, null=True, verbose_name = 'Asignatura')
    estudiante        = models.ForeignKey(Estudiante, blank=True, null=True, verbose_name = 'Estudiante')

    class Meta:
        verbose_name_plural = 'Notas'
        db_table = 'notas'
        ordering = ['nota', 'asignatura', 'estudiante' ]

    def __unicode__(self, *args, **kwargs):
        # Python 2
        return '{} - {} - {}'.format(self.nota, self.asignatura, self.estudiante)

    def __str__(self, *args, **kwargs):
        # Python 3
        return '{} - {} - {}'.format(self.nota, self.asignatura, self.estudiante)

   