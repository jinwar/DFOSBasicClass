import h5py
import numpy as np
from datetime import datetime



class Data2D():

    # constructor function, run when a new object is created
    def __init__(self):
        self.data = None   # data, 2D array
        self.start_time = None  # starting time using datetime
        self.taxis = []  # time axis in second from start_time
        self.chan = [] # fiber channel number
        self.md = []  # fiber physical distance or location
        self.attrs = {'Python Class Version':'1.1'} # data attributes
    
    def saveh5(self,filename):
        f = h5py.File(filename,'w')
        # save main dataset
        dset = f.create_dataset('data',data=self.data)
        # save all the attributes to the main dataset
        dset.attrs['start time'] = self.start_time.strftime('%Y%m%d_%H%M%S.%f')
        for k in self.attrs.keys():
            dset.attrs[k] = self.attrs[k]
        # save all other ndarray and lists in the class
        for k in self.__dict__.keys():
            if k == 'data':
                continue
            if k == 'start_time':
                continue
            if k == 'attrs':
                continue
            dtype = type(self.__dict__[k])
            if dtype == np.ndarray:
                f.create_dataset(k,data=self.__dict__[k])
            if dtype == list:
                f.create_dataset(k,data=self.__dict__[k])

        f.close()


    def loadh5(self,filename):
        f = h5py.File(filename,'r')
        # read start_time
        self.start_time = datetime.strptime(f['data'].attrs['start time'],'%Y%m%d_%H%M%S.%f')
        # read attributes
        self.attrs = {}
        for k in f['data'].attrs.keys():
            if k == 'start time':
                continue
            self.attrs[k] = f['data'].attrs[k]
        # read all other ndarrays
        for k in f.keys():
            setattr(self,k,np.array(f[k]))
        f.close()