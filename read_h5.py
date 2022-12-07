import h5py
import numpy

filename = "/home/ivlabs-0/sornet/data/clevr_cogent/objects.h5"

with h5py.File(filename, "r") as f:
    print(list(f.keys()))
    for group in f.keys() :
        print (type(f[group]))
    #     for dset in f[group].keys():      
    #         print (f'this is dset {dset}')
    #         ds_f = f[group][dset] # returns HDF5 fset object
    #         print (ds_f)
    #         print (ds_f.shape, ds_f.dtype)
            # arr = f[group][dset][:] # adding [:] returns a numpy array
            # print (arr.shape, arr.dtype)
            # print (arr)