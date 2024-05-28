from .models import Curso, Profesor, Estudiante, Direccion

def crear_curso(codigo, nombre, version):
    curso = Curso(codigo=codigo, nombre=nombre, version=version)
    curso.save()
    return curso

def crear_profesor(rut, nombre, apellido, activo, creacion_registro, modificacion_registro, creado_por):
    profesor = Profesor(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creacion_registro=creacion_registro, modificacion_registro=modificacion_registro, creado_por=creado_por)
    profesor.save()
    return profesor

def crear_estudiante(rut, nombre, apellido, fecha_nac, activo, creacion_registro, modificacion_registro, creado_por, direccion_id, curso_codigo):
    direccion = Direccion.objects.get(id=direccion_id)
    curso = Curso.objects.get(codigo=curso_codigo)
    estudiante = Estudiante(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, activo=activo, creacion_registro=creacion_registro, modificacion_registro=modificacion_registro, creado_por=creado_por, direccion=direccion, curso=curso)
    estudiante.save()
    return estudiante

def crear_direccion(calle, numero, dpto, comuna, ciudad, region, estudiante_id):
    direccion = Direccion(calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region, estudiante_id=estudiante_id)
    direccion.save()
    return direccion

def obtiene_estudiante(rut):
    return Estudiante.objects.get(rut=rut)

def obtiene_profesor(rut):
    return Profesor.objects.get(rut=rut)

def obtiene_curso(codigo):
    return Curso.objects.get(codigo=codigo)

def agrega_profesor_a_curso(profesor_rut, curso_codigo):
    profesor = Profesor.objects.get(rut=profesor_rut)
    curso = Curso.objects.get(codigo=curso_codigo)
    curso.profesores.add(profesor)
    curso.save()

def agrega_cursos_a_estudiante(estudiante_rut, curso_codigo):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    curso = Curso.objects.get(codigo=curso_codigo)
    estudiante.curso = curso
    estudiante.save()

def imprime_estudiante_cursos(estudiante_rut):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    cursos = estudiante.curso.all()
    for curso in cursos:
        print(curso.nombre)
