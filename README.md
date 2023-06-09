# FACIAL
part of digital human, synthesis of head poses and expression.  
You can recurrent the project by using the [jupter notebook facial_train_install.ipynb](facial_train_install.ipynb). We need [mtcnn](mtcnn.ipynb) to extract image facial features, and [Openface](https://github.com/TadasBaltrusaitis/OpenFace/releases) to extract video facial features. And please unzip [BFM_model_front](https://github.com/ProgrammerManstein/FACIAL/blob/master/FACIAL/face_render/BFM/BFM_model_front.7z).
You can train the module by using the [jupter notebook facial_train.ipynb](facial_train.ipynb) after having recurrented it.  
After training, you can get any video that is instructed by your text by using the [jupter notebook facial_test.ipynb](facial_test.ipynb).  
You can also consult the original project [FACIAL: Synthesizing Dynamic Talking Face With Implicit Attribute Learning. ICCV, 2021.](https://github.com/zhangchenxu528/FACIAL) for more information.
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
