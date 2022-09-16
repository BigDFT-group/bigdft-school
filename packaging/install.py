from os.path import join
from os import sep
repo_url = 'https://gitlab.com/luigigenovese/bigdft-school'
drive_path = join(sep,'content', 'drive')
training_path = join(drive_path, 'MyDrive','bigdft-school')
conda_package = join(training_path, 'bigdft-school', 'packaging', 'bigdft-suite-1.9.3_rc.2-mpi_openmpi_py37h008c211_0.tar.bz2')
prefix = join(training_path, 'install')
bigdft_root_path = join(prefix, 'bin')
bigdft_executable = join(bigdft_root_path, 'bigdft')
bigdft_pythonpath = join(prefix, 'lib', 'python3.7', 'site-packages') # can use python-config for generality

def execute(*args):
  from subprocess import check_output
  print(' '.join(args))
  result = check_output(args)
  print(result.decode('utf-8'))

def mount_drive():
  from google.colab import drive
  drive.mount(drive_path, force_remount=True)

def change_dir():
  from os import chdir
  execute('mkdir','-p',training_path)
  chdir(training_path)

def get_repo():
  execute("git","clone",repo_url)

def set_environment():
  from os import environ
  from sys import path
  environ['BIGDFT_ROOT'] = bigdft_root_path
  path.insert(0, bigdft_pythonpath)

def skip():
   from os.path import isfile
   return isfile(bigdft_executable)

def install_colab():
    from os import system
    from subprocess import check_output
    execute("pip", "install", "-q", "condacolab")

def setup_colab():
    import condacolab
    condacolab.install()

def get_conda():
  install_colab()
  setup_colab()

def activate_conda():
  from subprocess import check_output
  execute('conda', 'create', '-p', prefix)
  execute('conda', 'init', 'bash')
  execute('bash','activate', prefix)

def install_bigdft():
    from subprocess import check_output
    execute('conda','install','-p', prefix, conda_package)
    execute('conda', 'update', '--all')

def install_packages(*args):
  execute('pip','install','-t',bigdft_pythonpath,args)
    
def full_procedure():
  mount_drive()
  change_dir()
  if not skip():
    get_repo()
    get_conda()
    activate_conda()
    install_bigdft()
  set_environment()

full_procedure()
