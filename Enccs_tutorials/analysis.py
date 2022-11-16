def extract_results(directory):
    from futile.Utils import file_list
    import tarfile
    from os.path import join
    from os import system
    for archive in file_list(directory,suffix='.tar.gz',exclude='files',include_directory_path=True):
        arch = tarfile.open(archive)
        arch.extractall(path=directory)
        arch.close()
    #patch the yaml files from a mistake in the case of low profiling depth
    # !sed -i s/^\ *\:\ null/\ \ \ \ null/g H2O-linear-single/Calculations/time*
    # !sed -i s/^\ *\:\ null/\ \ \ \ null/g H2O-linear-single/Calculations/data*/time*        
    system('sed -i s/^\ *\:\ null/\ \ \ \ null/g '+join(directory,'Calculations','time*'))
    system('sed -i s/^\ *\:\ null/\ \ \ \ null/g '+join(directory,'Calculations','data*','time*'))
        
def dipole_info(log):
    data = {coord+ ' (AU)': log.dipole[i] for i, coord in enumerate(['x', 'y', 'z'])}
    data['Norm (Debye)'] = log.log['Electric Dipole Moment (Debye)']['norm(P)']
    return data

def get_total_time_info(time):
    import yaml
    with open(time) as ifile:
        dt = yaml.load(ifile,Loader=yaml.Loader)
    data = {k: v[1] for k, v in dt['SUMMARY'].items()}
    data.update({'WFN_OPT %': dt['SUMMARY']['WFN_OPT'][0]})
    return data

def plot_timings(times,plottype='Seconds',**kwargs):
    from futile.Time import TimeData
    from matplotlib import pyplot as plt
    tt=TimeData(*times.values(),static=True,plottype=plottype,**kwargs)
    #tweak the name of the labels
    fig=plt.gcf()
    ax=fig.get_axes()
    _=ax[0].set_xticklabels(times.keys(),rotation=90)#,size=self.fontsize)