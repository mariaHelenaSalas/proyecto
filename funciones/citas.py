import  os
import json
import funciones.globales as gf
import modules.corefilesCT as cf
import ui.Uicitas as uict
def newcita():

  title =  """
  *********************************
  *       AGENDAR DE CITAS    *
  *********************************
  """
  gf.borrar_pantalla()
  print(title)
  identificacion = input ('ingrese numero de identificacion :')
  nombre_apellido = input ('ingrese el nombre y el apellido :')
  tipo_de_cita = input ('ingree el especialista:')
  correo_electronico = input ('ingres el correo electronico :')
  ingrese_fecha = input ("ingrese fecha:")
  cita = {
  'identificacion': identificacion,
  'nombre_apellido' : nombre_apellido,
  'tipo_de_cita' : tipo_de_cita,
  'correo_electronico': correo_electronico,
  'ingrese la fecha' : ingrese_fecha,}
  cf.AddData('datacitas',identificacion,cita)

  gf.centroMedico.get('data').update({identificacion:cita})
  if(bool(input("desdea agendar ua cita S(si)) o Enter(no)"))):
    newcita()
  else:
    uict.menucitas(0)
def  searchData():
  criterio = input('ingrese la identificacion del paciente:')
  datacita=gf.centroMedico.get('datacita')
  return datacita

def Modifydata():
    datacita = input = searchData
    if datapaciente:
       print("Datos actuales del paciente:")
       datapaciente = ['nombre y apellidos', 'numero de celular', 'fecha de nacimiento',  'telefono','edad','genero']
       for key in datapaciente:
         if bool(input(f"Desea modificar {key}? (Sí/Si o Enter para No): ")):
               new_value = input(f"Ingrese el nuevo valor para {key}: ")
               dataMedico = new_value

       gf.centroMedico.get('datamedico').update({datapaciente:'identificacion'})
       cf.UpdateFile(gf.centroMedico)
       print("Datos del paciente actualizados correctamente.")
    else:
      print("No se encontró ningún paciente con la identificación proporcionada.")

def removeescita(param):
   data = list(*param)
   identificacion = int(input("ingrese la cita que desea eliminar : "))
   if identificacion in data:
      confirmacion = input("¿esta seguro que  desea eliminar la cita? enter(si) n (no): ")
      if confirmacion.lower()== 'enter':
       del data [identificacion]
      print("usuario eliminado correctamentte")
   else:
      print("usuario no encontrado.")



      





