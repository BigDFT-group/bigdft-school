from os.path import join
from os import sep
school_url = 'https://gitlab.com/luigigenovese/bigdft-school'
trunk_url =  '-b 1.9.3-new https://gitlab.com/luigigenovese/bigdft-suite.git'
drive_path = join(sep,'content', 'drive')
training_path = join(drive_path, 'MyDrive','bigdft-school')
packaging_path = join(training_path, 'bigdft-school', 'packaging')
conda_package = join(packaging_path, 'bigdft-suite-1.9.3_rc.2-mpi_openmpi_py37h008c211_0.tar.bz2')
extra_package = join(packaging_path, 'extra_libs.tar.bz2')
prefix = join(training_path, 'install')
bigdft_root_path = join(prefix, 'bin')
bigdft_executable = join(bigdft_root_path, 'bigdft')
bigdft_pythonpath = join(prefix, 'lib', 'python3.7', 'site-packages') # can use python-config for generality

def execute(*args):
  from subprocess import check_output, CalledProcessError, STDOUT
  print('Executing: '+' '.join(args))
  try:
      result = check_output(args,stderr=STDOUT)
      print(result.decode('utf-8'))
  except CalledProcessError as e:
      print('Error Occurred: ','\n', e.output.decode())  

def mount_drive():
  from google.colab import drive
  drive.mount(drive_path, force_remount=True)

def change_dir():
  from os import chdir
  execute('mkdir','-p',training_path)
  chdir(training_path)

def get_repo(url=school_url):
  execute("git","clone",'--depth','1',url)

def set_environment():
  from os import environ
  from sys import path
  environ['BIGDFT_ROOT'] = bigdft_root_path
  path.insert(0, bigdft_pythonpath)

def skip():
   from os.path import isfile
   return isfile(bigdft_executable)

def ok_for_client():
    from os.path import isdir
    return isdir(bigdft_pythonpath)

def untar_bz2(archive,dest='install'):
    execute('mkdir','-p',dest)
    execute('tar','xjf',archive,'-C',dest)


def install_bigdft():
    get_repo()
    untar_bz2(conda_package)
    untar_bz2(extra_package)

def install_client():
    get_repo(url=trunk_url)
    execute('bigdft-suite/Installer.py','-f','ubuntu_MPI.rc','-a','no_upstream','build','bigdft-client','-y')

def install_packages(*args):
  execute('pip','install','-t',bigdft_pythonpath,args)

def full_procedure():
  mount_drive()
  change_dir()
  if not ok_for_client():
    install_client()
  set_environment()

full_procedure()
