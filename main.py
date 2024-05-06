import modules.corefiles as cf
import funciones.globales as gf
import ui.UiMedico as uimd
import ui.uiPaciente as uipc
import ui.Uicitas as uict
import modules.corefilesCT as mdct
import modules.corefileMD as mdmd

def mainMenu(op):
    gf.borrar_pantalla()
    title = """
    ######################################
    #    BIENVENIDOS AL  CENTRO MEDICO   #
    ######################################
    """
    mainMenuop = "1. medicos\n2. pacientes\n3. agendar cita\n4. salir"
    if (op !=3):
        print(title)
        print(mainMenuop)
        try:
            opcion = int(input(':)'))
        except ValueError:
            print('error en la opcion ingresada')
            gf.pausar_pantalla()
            mainMenu()
        else:
            match (opcion):
                
                case 1:
                    uimd.MenuMedico(0)
                case 2:
                    uipc.MenuPaciente(0)
                case 3:
                    uict.menucitas(0)
                case 4:
                    print('salir')
                
            
if __name__=='__main__':
    cf.MY_DATABASE ='data/pacientes.json'
    mdct.MY_DATABASECT ='datacitas/.json'
    mdmd.MY_DATABASEMD ='datamedico/.json'
    cf.checkFile(gf.centroMedico)
    mainMenu(0)

