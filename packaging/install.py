from os.path import join
from os import sep
school_url = 'https://github.com/BigDFT-group/bigdft-school'
trunk_url = 'https://gitlab.com/l_sim/bigdft-suite.git'
data_url = 'https://gitlab.com/luigigenovese/bigdft-school/-/raw/main/'
school_branch = 'devel'
base_path = join(sep, 'content')
drive_path = join(base_path, 'drive')
training_path = join('bigdft-school')
packaging_path = join('packaging')
conda_package = join(
    packaging_path,
    'bigdft-suite-1.9.3_rc.2-mpi_openmpi_py37h008c211_0.tar.bz2')
extra_package = join(packaging_path, 'extra_libs.tar.bz2')
prefix = join('install')
bigdft_root_path = join(prefix, 'bin')
bigdft_executable = join(bigdft_root_path, 'bigdft')
# can use python-config for generality
bigdft_pythonpath = join(prefix, 'lib', 'python3.7', 'site-packages')


def execute(*args):
    from subprocess import check_output, CalledProcessError, STDOUT
    print('Executing: '+' '.join(args))
    try:
        result = check_output(args, stderr=STDOUT)
        print(result.decode('utf-8'))
    except CalledProcessError as e:
        print('Error Occurred: ', '\n', e.output.decode())


def mount_drive():
    from google.colab import drive
    drive.mount(drive_path, force_remount=True)


def close_drive():
    from google.colab import drive
    drive.flush_and_unmount()


def ensure_dir(pth):
    from os.path import abspath
    execute('mkdir', '-p', abspath(pth))


def change_dir(pwd=training_path):
    from os import chdir
    ensure_dir(pwd)
    chdir(pwd)


def get_repo(url=school_url, options=[]):
    execute("git", "clone", '--depth', '1', *options, url)


def set_environment():
    from os import environ, pathsep
    from os.path import abspath
    from sys import path
    environ['BIGDFT_ROOT'] = abspath(bigdft_root_path)
    ppath = abspath(bigdft_pythonpath)
    if ppath not in path:
        path.insert(0, ppath)
    environ['PYTHONPATH'] = pathsep.join(path)


def skip():
    from os.path import isfile
    return isfile(bigdft_executable)


def ok_for_client():
    from os.path import isdir
    return isdir(bigdft_pythonpath)


def untar_archive(archive, dest='install'):
    ensure_dir(dest)
    options = {'.tar.gz': 'xf',
               '.tgz': 'xf',
               '.tar.bz2': 'xjf',
               '.tar.xz': 'xJf'}
    for opt, option in options.items():
        if archive.endswith(opt):
            break
    execute('tar', option, archive, '-C', dest)


def install_colab():
    packages('condacolab', path=None, options=['-q'])


def setup_colab():
    import condacolab
    condacolab.install()


def install_bigdft():
    execute("conda", "install", conda_package)
    execute("conda", "update", "--all")


def get_conda():
    install_colab()
    setup_colab()


def full_suite():
    get_conda()
    change_dir(base_path)
    get_school_repo()
    install_bigdft()


def set_ready():
    from os import environ, path
    environ['BIGDFT_ROOT'] = ''
    change_dir(path.join(base_path, training_path))


def client(locally=False):
    from os.path import join
    from os import environ
    if locally:
        base = base_path
    else:
        base = join(drive_path, 'MyDrive')
        mount_drive()
    change_dir(base)
    get_school_repo()
    if not ok_for_client():
        get_repo(url=trunk_url, options=['-b', school_branch])
        environ['JHBUILD_RUN_AS_ROOT'] = 'please do it'
        execute('python', 'bigdft-suite/Installer.py', '-f',
                'ubuntu_MPI.rc', '-a', 'no_upstream',
                'build', 'bigdft-client', '-q', '-y')
    set_environment()


def get_school_repo():
    get_repo()
    change_dir(training_path)


def get_remote_file(path, output):
    execute('wget', data_url + path, '-O', output, '2>/dev/null')


def packages(*args, path=bigdft_pythonpath, options=[]):
    if path is not None:
        execute('pip', 'install', '-t', path, *options, *args)
    else:
        execute('pip', 'install', *options, *args)


def data(archive, dest='.'):
    from os.path import basename
    get_remote_file(archive, basename(archive))
    untar_archive(basename(archive), dest=dest)


def purge_drive():
    from os.path import join
    change_dir(base_path)
    execute('rm', '-rf', join(drive_path, 'MyDrive', training_path))
