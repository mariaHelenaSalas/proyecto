import os
import json
import funciones.globales as gf
import modules.corefileMD as cf
import ui.UiMedico as umc

def NewMedic ():

   title =  """
   *********************************
   *       REGISTRO DE MEDICOS     *
   *********************************
   """
   gf.borrar_pantalla()
   print(title)
   identificacion = input("ingrese el numero de identificacion : ")
   nombre_apellido = input("ingrese el nombre y el apellido :" )
   correo_electronico = input("ingrese su correo electronico :" )
   numero_consultorio = input("ingrese el numero del consultorio:")
   hora_atencion = input("ingrese el hora de la consulta:")
   medico = {'identificacion': identificacion,
                   'nombre y apellido': nombre_apellido,
                    'numero_consultorio' : numero_consultorio,
                    'horario_atencion' : hora_atencion,
                    'correo_electronico' : correo_electronico,}


   cf.AddData('datamedico',identificacion,medico)
   gf.centroMedico.get('datamedico').update({identificacion:medico})
   if(bool(input("desdea ingresar otro medico S(si)) o Enter(no)"))):
      NewMedic()
   else:
    umc.MenuMedico(0)
    
def searchData():
   input ('ingrese la identificacion del medico:')
   dataMedico=gf.centroMedico.get('dataMedico')
   return dataMedico


def Modifydata():
    identificacion = input("ingrese la identificacion del medico que desea editar:")
    if dataMedico:
       print("Datos actuales del medico:")
       dataMedico = ['nombre y apellidos', 'numero de celular', 'fecha de nacimiento',  'telefono','edad','genero']
       for key in dataMedico:
         if bool(input(f"Desea modificar {key}? (Sí/Si o Enter para No): ")):
               new_value = input(f"Ingrese el nuevo valor para {key}: ")
               dataMedico = new_value

       gf.centromedico.get('datamedico').update({dataMedico:'identificacion'})
       cf.UpdateFile(gf.centromedico)
       print("Datos del medico actualizados correctamente.")
    else:
      print("No se encontró ningún medico con la identificación proporcionada.")
  

def removeespecialista(param):
   data = list(*param)
   identificacion = int(input("ingrese la identificacion del medico que desea eliminar : "))
   if identificacion in data:
      confirmacion = input("¿esta seguro que  desea eliminar medico? enter(si) n (no): ")
      if confirmacion.lower()== 'enter':
       del data [identificacion]
      print("usuario eliminado correctamentte")
   else:
      print("usuario no encontrado.")


   











