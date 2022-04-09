import os
import subprocess

# Variables
project_slug= "{{ cookiecutter.project_slug }}"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

## python del entorno virtual
python_venv =  os.getcwd()+"\\venv\\Scripts\\python.exe"

if __name__=='__main__':

  print(f"{MESSAGE_COLOR}Almost done!")
  print(f"Initializing a git repository...{RESET_ALL}")

  subprocess.call(['git', 'init'])
  subprocess.call(['git', 'add', '*'])
  subprocess.call(['git', 'commit', '-m', 'Init commit'])

  # # Agrega el repo remoto y realiza el primer commit
  # subprocess.call(['git', 'remote', 'add', 'origin', project_github])
  # subprocess.call(['git', 'push', 'origin', 'master'])

  # Iniciar ambiente virtual
  subprocess.call(['py', '-m', 'venv', 'venv'])
  #print('ambiente creado')
  #print('ambiente creado')
  
  # activo ell entorno virtual creado
  subprocess.call('venv\\Scripts\\activate.bat')

  #instalo requirements
  subprocess.call([python_venv, '-m', 'pip', 'install', '-r', 'requirements.txt'])
  
  #desactivo entorno virtual
  subprocess.call(['venv\\Scripts\\deactivate.bat'])

  print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")

  # # Configurar el ambiente para recibir notebooks.

  # if'{{ cookiecutter.project_packages }}' == 'Notebook':
  #   subprocess.call([python_venv,'-m', 'ipykernel', 'install', '--user', '--name', 'venv'])


