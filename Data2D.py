import h5py
import numpy as np
from datetime import datetime



class Data2D():

    # constructor function, run when a new object is created
    def __init__(self):
        self.data = None   # data, 2D array
        self.start_time = None  # starting time using datetime
        self.taxis = []  # time axis in second from start_time
        self.chan = [] # fiber distance
        self.x = []  # fiber physical location
        self.y = []  # fiber physical location
        self.z = []  # fiber physical location
        self.md = []  # fiber measured depth along the well
        self.attrs = {'Python Class Version':'1.0'} # data attributes
    
    def saveh5(self,filename):
        f = h5py.File(filename,'w')
        dset = f.create_dataset('data',data=self.data)
        f.create_dataset('chan',data=self.chan)
        f.create_dataset('taxis',data=self.taxis)
        f.create_dataset('x',data=self.x)
        f.create_dataset('y',data=self.y)
        f.create_dataset('z',data=self.z)
        f.create_dataset('md',data=self.md)
        dset.attrs['start time'] = self.start_time.strftime('%Y%m%d_%H%M%S.%f')
        for k in self.attrs.keys():
            dset.attrs[k] = self.attrs[k]
        f.close()


    def loadh5(self,filename):
        f = h5py.File(filename,'r')
        self.data = f['data'][:,:]
        self.taxis = f['taxis'][:]
        self.chan = f['chan'][:]
        self.x = f['x'][:]
        self.y = f['y'][:]
        self.z = f['z'][:]
        self.start_time = datetime.strptime(f['data'].attrs['start time'],'%Y%m%d_%H%M%S.%f')
        self.attrs = {}
        for k in f['data'].attrs.keys():
            if k == 'start time':
                continue
            self.attrs[k] = f['data'].attrs[k]
        f.close()