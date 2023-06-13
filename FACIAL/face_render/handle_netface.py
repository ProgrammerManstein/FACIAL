import os, sys
import numpy as np
from scipy.io import loadmat,savemat
import glob
from scipy.signal import savgol_filter
import argparse

parser = argparse.ArgumentParser(description='netface_setting')
parser.add_argument('--param_folder', type=str, default='/root/FACIAL/video_preprocess/train1_deep3Dface')

opt = parser.parse_args()

param_folder = opt.param_folder

mat_path_list = sorted(glob.glob(os.path.join(param_folder, '*.mat')))
len_mat = len(mat_path_list)
faceshape = np.zeros((len_mat, 257),float)

for i in range(1,len_mat+1):
    d = loadmat(os.path.join(param_folder,str(i).zfill(6)+'.mat'))
    faceshape[i-1,0:80] = d['id'][0,:]
    faceshape[i-1,80:80+64] = d['exp'][0,:]
    faceshape[i-1,80+64:80+64+80] = d['tex'][0,:]
    faceshape[i-1,80+64+80:80+64+80+3] = d['angle'][0,:]
    faceshape[i-1,80+64+80+3:80+64+80+3+27] = d['gamma'][0,:]
    faceshape[i-1,80+64+80+3+27:80+64+80+3+27+3] = d['trans'][0,:]


frames_out_path = os.path.join(param_folder,'train1.npz')
np.savez(frames_out_path, face = faceshape)