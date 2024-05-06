import os
import json
import funciones.globales as gf
import modules.corefiles as cf
import ui.uiPaciente as uipc

def NewPaciente ():

      title =  """
      *********************************
      *       REGISTRO DE PACIENTE     *
      *********************************
      """
      gf.borrar_pantalla()
      print(title)
      identificacion = input("ingrese el numero de identificacion : ")
      nombre_apellido = input("ingrese el nombre y el apellido :" )
      numero_celular = input('ingrese su numero de celular:')
      fecha_nacimiento = input('ingrese su fecha de nacimiento :')
      telefono = input("ingrese su numero de telefono :")
      edad = input('ingrese su edad :')
      genero = input('ingrese su genero :')

   
      paciente = {
      'identificacion': identificacion,
      'nombre:_apellido': nombre_apellido,
      'numero_celular' : numero_celular,
      'fecha_nacimieno' : fecha_nacimiento,
      'telefono' : telefono,
      'edad' : edad,
      'genero' : genero,
      }
   
      cf.AddData('data',identificacion,paciente)
      gf.centroMedico.get('data').update({identificacion:paciente})
      if(bool(input('Desea Registrar Otro Paciente  S(si) o enter (no)'))):
       NewPaciente()
      else:
       uipc.MenuPaciente(0)

def   searchData():
      input('ingrese la identidad del paciente:')
      data=gf.centroMedico.get('datapaciente')
      return data

def Modifydata():
    datapaciente = input = searchData
    if datapaciente:
       print("Datos actuales del paciente:")
       datapaciente = ['nombre y apellidos','identificacion', 'numero de celular', 'fecha de nacimiento',  'telefono','edad','genero']
       for key in datapaciente:
         if bool(input(f"Desea modificar {key}? (Sí/Si o Enter para No): ")):
               new_value = input(f"Ingrese el nuevo valor para {key}: ")
               datapaciente = new_value

       gf.centroMedico.get('datapaciente').update({datapaciente:'identificacion'})
       cf.UpsateFile(gf.centroMedico)
       print("Datos del paciente actualizados correctamente.")
    else:
      print("No se encontró ningún paciente con la identificación proporcionada.")

def removepaciente(param):
   data = list(*param)
   identificacion = int(input("ingrese la identificacion del paciente que desea eliminar : "))
   if identificacion in data:
      confirmacion = input("¿esta seguro que  desea eliminar paciente? enter(si) n (no): ")
      if confirmacion.lower()== 'enter':
       del data [identificacion]
      print("usuario eliminado correctamentte")
   else:
      print("usuario no encontrado.")


  
      