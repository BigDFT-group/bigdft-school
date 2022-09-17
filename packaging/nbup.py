_base = "https://gitlab.com/luigigenovese/bigdft-school/-/raw/main/packaging/"
_pkg = "bigdft-suite-1.9.3_rc.2-mpi_openmpi_py37h008c211_0.tar.bz2"

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

def skip():
   from os import environ
   return "BIGDFT_ROOT" in environ

def download():
    from os import system
    system("wget " + _base + _pkg)

def install_colab():
    from os import system
    system("pip install -q condacolab")

def setup_colab():
    import condacolab
    condacolab.install()

def install_bigdft():
    from os import system
    system("conda install " + _pkg + " ; conda update --all")

def original_libraries():
  from os import listdir, path
  return listdir('/lib/x86_64-linux-gnu') + listdir('/usr/local/lib')

def get_conda():
  install_colab()
  setup_colab()

def bigdft_libraries(previous_files):
  from subprocess import check_output
  from os.path import abspath, basename
  result = check_output(['ldd', '/usr/local/bin/bigdft'])
  newlibs = []
  for val in result.decode('utf-8').split('\n'):
    filename = val.split('=>')[-1]
    library = filename.split('(')[0]
    lib = basename(library).strip().lstrip().rstrip()
    filepath=abspath(library).split()[-1]
    if lib not in previous_files:
      print(lib,filepath, lib in previous_files)
      newlibs.append(filepath)
  return newlibs

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

def copy_files(filelist, dest):
  import os
  import shutil
  for file_name in src_files:
     shutil.copy(full_file_name, dest, follow_symlinks=True)

def extract_tarfile(archive, dest):
  from nbup import execute
  execute('mkdir','-p',dest)
  execute('tar', 'xjf', archive, '-C', dest)

def package_libraries():
  from os import listdir,path
  return listdir(path.join('install','lib'))


result=original_libraries()
mount_drive()
change_dir()
download()
extract_tarfile()
pkg_libs=package_libraries()
get_conda()
install_bigdft()
newlibs=bigdft_libraries(result)
from os.path import basename
newlibs = [l for l in newlibs if basename(l) not in pkg_libs]
print(newlibs)


## Run them all
#if not skip():
#    download()
#    install_colab()
#    setup_colab()
#    install_bigdft()

