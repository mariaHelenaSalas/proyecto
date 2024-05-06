import modules.corefiles as cf
import funciones.globales as gf
import funciones.paciente as pc
import main

def MenuPaciente(op : int):
    title =  """
    ##################################
    #   ADMINISTACION DE MEDICOS     #
    ##################################
    """
    MenuPacienteop =  '1. Buscar Paciente \n2 Agregar Paciente \n3. Editar iniformacion del paciente\n4. Eliminar paciente \n5. salir'
    gf.borrar_pantalla()
    if (op != 4):
       print(title)
       print(MenuPacienteop)
       try:
           op  = int(input(",)"))
       except ValueError:
            print("opcion no tiene formato adecuado")   
            gf.pausar_pantalla()
            MenuPacienteop(0)
       else:
         match (op):  
               case 1:
                    pc.searchData
               case 2:   
                    pc.NewPaciente()
               case  3:  
                   pc.Modifydata()
               case 4:
                   pass
               case 5:
                    main.mainMenu(0)
               case _: 
                print('la opcion ingresada no esta disponible en las opciones')
                gf.pausar_pantalla    
                 
