_base = "https://gitlab.com/luigigenovese/bigdft-school/-/blob/main/packaging/"
_pkg = "bigdft-suite-1.9.3_rc.2-mpi_openmpi_py37h008c211_0.tar.bz2"

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

# Run them all
if not skip():
    download()
    install_colab()
    setup_colab()
    install_bigdft()

