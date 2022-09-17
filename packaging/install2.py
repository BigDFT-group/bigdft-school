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


def get_conda():
  install_colab()
  setup_colab()

download()
get_conda()
install_bigdft()


## Run them all
#if not skip():
#    download()
#    install_colab()
#    setup_colab()
#    install_bigdft()

