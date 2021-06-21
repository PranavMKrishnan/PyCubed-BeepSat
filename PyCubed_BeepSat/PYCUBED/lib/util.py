from pycubed import cubesat
import os

print('Cubesat Debugging Tools: clear_all_but_files(), clear_nvm(),  clear_dataset(rng,rad,or gps), clear_all()')

def clear_nvm(last_reg=50):
    last_reg+=1
    print('Before clearing counters and flags:\n\t{}'.format(cubesat.micro.nvm[:last_reg]))
    cubesat.micro.nvm[:last_reg]=bytearray(last_reg)
    print('\n\nAfter:\n\t{}'.format(cubesat.micro.nvm[:last_reg]))

def clear_logs():
    print('Clearing logs.')
    try: os.remove('/sd/log.txt')
    except: pass

def clear_dataset(ds):
    name=None
    for i in ('rng','rad','gps','b'):
        if i in ds:
            name=i
    if name is not None:
        print('Clearing {} data. This can take a while.'.format(name))
        for d in cubesat.fs.ilistdir('/'+name):
            try:
                os.remove('/sd/{}/{}'.format(name,d[0]))
            except Exception as e:
                print('{},{}'.format(e,'/sd/{}/{}'.format(name,d)))

def clear_all_but_files(last_reg=50):
    last_reg+=1
    print('Before clearing counters and flags:\n\t{}'.format(cubesat.micro.nvm[:last_reg]))
    print('Clearing all but files')
    for i in range(21):
        cubesat.micro.nvm[i]=0
    for i in range(27,last_reg):
        cubesat.micro.nvm[i]=0
    print('After:\n\t{}'.format(cubesat.micro.nvm[:last_reg]))

def clear_all():
    try:
        os.remove('/sd/default.txt')
    except:
        pass
    print('Clearing data. This can take a while.')
    for i in ('gps','rng','data','logs','rad'):
        try:
            for d in os.listdir('/sd/'+i):
                try:
                    os.remove('/sd/'+i+'/'+d)
                except Exception as e:
                    print('{} {} {}'.format(i,d,e))
        except:
            continue

def clear_for_flight():
    clear_logs()
    clear_all()
    clear_nvm()

def clear_balloon():
    clear_dataset('b')
