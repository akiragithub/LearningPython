from cx_Freeze import setup, Executable
base = None
##/Remplacer "monprogramme.py" par le nom du script qui lance votre programme
executables = [Executable("interfaces.py"),]
##/Renseignez ici la liste complète des packages utilisés par votre application
packages = ["sqlite3", "config", "tkinter", "tkinter.messagebox", "TkTreectrl",
            "PIL", "Pmw", "mabd2", "mabiblio"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
##//Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "Ma bibliotheque",
    options = options,
    version = "1.0",
    description = 'Voici mon programme',
    executables = executables
)
