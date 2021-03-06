# resized_image = cv2.resize(image, (100, 50))
import sys
import cv2
import numpy as np
import os
import glob
import lmdb
import os
import numpy as np
import matplotlib.pyplot as plt
import sys

caffe_root = 'home/b13107/myproject/caffe' 
#sys.path.insert(0, caffe_root + 'python')
# import caffe
# from caffe.proto import caffe_pb2


#DEMO_DIR = '.'

categories = [ 'Angry' , 'Disgust' , 'Fear' , 'Happy'  , 'Neutral' ,  'Sad' , 'Surprise']



# second part
#cur_net_dir = 'VGG_S_rgb'
Model_path = os.path.join(caffe_root,'models','Emotion_Model')

mean_filename=os.path.join(Model_path,'mean.binaryproto')
net_pretrained = os.path.join(Model_path,'EmotiW_VGG_S.caffemodel')
net_model_file = os.path.join(Model_path,'deploy.prototxt')

proto_data = open(mean_filename, "rb").read()
a = caffe.io.caffe_pb2.BlobProto.FromString(proto_data)
mean  = caffe.io.blobproto_to_array(a)[0]

VGG_S_Net = caffe.Classifier(net_model_file, net_pretrained,
                       mean=mean,
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(256, 256))

input_image = caffe.io.load_image(os.path.join(DEMO_DIR,cur_net_dir,'demo_image.png'))
prediction = VGG_S_Net.predict([input_image],oversample=False)
print 'predicted category is {0}'.format(categories[prediction.argmax()])
print(prediction)
print('hi')
filters = VGG_S_Net.params['conv1'][0].data
print(filters)
print(filters.shape)
