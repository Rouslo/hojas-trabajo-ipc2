# -*- coding: utf-8 -*-
"""2. Lista circular.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fSsJX739J4YEX5K21DT2Z82-D_Z0NVsu

# **Listas Circulares**
**Definición de la clase Receta**
"""

class receta:
  def __init__(self, paciente, fecha_nac, doctor, colegiado, fecha_cita,
               hora_cita, tipo_consulta, tratamiento):
    self.paciente = paciente
    self.fecha_nac = fecha_nac
    self.doctor = doctor
    self.colegiado = colegiado
    self.fecha_cita = fecha_cita
    self.hora_cita = hora_cita
    self.tipo_consulta = tipo_consulta
    self.tratamiento = tratamiento

"""**Definición de la clase Nodo**"""

class nodo:
  def __init__(self, receta=None, siguiente=None):
    self.receta = receta
    self.siguiente = siguiente

"""**Definición de la clase Lista Circular**"""

class lista_circular:
  def __init__(self):
    self.primero = None

  def insertar(self, receta):
    if self.primero is None:
      self.primero = nodo(receta = receta)
      self.primero.siguiente = self.primero
    else:
      actual = nodo(receta = receta, siguiente = self.primero.siguiente)
      self.primero.siguiente = actual
  
  def recorrer(self):
    if self.primero is None:
      return
    actual = self.primero
    print("Paciente: ", actual.receta.paciente, "| Fecha de nacimiento: ",
            actual.receta.fecha_nac, "| Doctor: ", actual.receta.doctor, 
            "| Colegiado: ", actual.receta.colegiado, "| Fecha de cita: ",
            actual.receta.fecha_cita, "| Hora de cita: ", actual.receta.hora_cita,
            "| Tipo de consulta: ", actual.receta.tipo_consulta, "| Tratamiento",
            actual.receta.tratamiento)
    while actual.siguiente != self.primero:
      actual = actual.siguiente
      print("Paciente: ", actual.receta.paciente, "| Fecha de nacimiento: ",
            actual.receta.fecha_nac, "| Doctor: ", actual.receta.doctor, 
            "| Colegiado: ", actual.receta.colegiado, "| Fecha de cita: ",
            actual.receta.fecha_cita, "| Hora de cita: ", actual.receta.hora_cita,
            "| Tipo de consulta: ", actual.receta.tipo_consulta, "| Tratamiento",
            actual.receta.tratamiento)
      
  def eliminar(self, colegiado, fecha_cita, hora_cita):
    actual = self.primero
    anterior = None
    no_encontrado = False

    while actual and actual.receta.colegiado != colegiado and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
      anterior = actual
      actual = actual.siguiente

      if actual == self.primero:
        no_encontrado = True
        print("No encontrado")
        break

    if not no_encontrado:
      if anterior is not None:
        anterior.siguiente = actual.siguiente
        actual.siguiente = None
      else:
        while actual.siguiente != self.primero:
          actual = actual.siguiente
        actual.siguiente = self.primero.siguiente
        self.primero = self.primero.siguiente

  def modificar(self, paciente, nueva_fecha_cita, nueva_hora_cita):
    actual = self.primero
    while actual is not None:
      if actual.receta.paciente == paciente:
        actual.receta.fecha_cita = nueva_fecha_cita
        actual.receta.hora_cita = nueva_hora_cita
        break
      actual = actual.siguiente

"""**Creación de objetos Receta**


"""

r1 = receta("Gerson López", "03-10-1990", "Melvin Ortiz", 20156, "17-01-2023", "11:30",
            "Medicina general", "2 pildoras de acetaminofén cada 6 horas")
r2 = receta("Karen Gómez", "08-05-2000", "Jorge Merida", 8567, "31-01-2023", "09:00", 
            "Medicina interna", "Tylenol de 20 ml cada 4 horas")
r3 = receta("Luis García", "17-09-1987", "Melvin Ortiz", 20157, "02-02-2023", "12:00", 
            "Medicina general", "2 cucharadas de Pepto-Bismol cada hora hasta que la diarrea desaparezca")

"""**Inserción**"""

lista_c = lista_circular()
lista_c.insertar(r1)
lista_c.insertar(r2)
lista_c.insertar(r3)

"""**Recorrer lista**"""

lista_c.recorrer()

"""**Eliminar un nodo de la lista**"""

lista_c.eliminar(8567, "31-01-2023", "09:00")
lista_c.recorrer()

lista_c.eliminar(20156, "17-01-2023", "11:30")
lista_c.recorrer()

"""**Modificar**"""

lista_c.modificar("Luis García", "20-01-2023", "02:00")

lista_c.recorrer()