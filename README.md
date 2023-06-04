# FACIAL
part of digital human, synthesis of head poses and expression. 
# Requirements  
Python environment  

``` 
conda create -n audio_face  
conda activate audio_face  
``` 

ffmpeg  
``` 
sudo apt-get install ffmpeg  
``` 

python packages  
``` 
pip install -r requirements.txt  
``` 

you may add opencv by conda.  
``` 
conda install opencv  
``` 

Citation  

``` 
@inproceedings{zhang2021facial,
  title={FACIAL: Synthesizing Dynamic Talking Face with Implicit Attribute Learning},
  author={Zhang, Chenxu and Zhao, Yifan and Huang, Yifei and Zeng, Ming and Ni, Saifeng and Budagavi, Madhukar and Guo, Xiaohu},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  pages={3867--3876},
  year={2021}
}
Acknowledgments
We use Deep3DFaceReconstruction for face reconstruction, DeepSpeech and VOCA for audio feature extraction, and 3dface for face rendering. Rendering-to-video module borrows heavily from everybody-dance-now.
``` 
