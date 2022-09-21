# TF2.0：获取网络中某一层的输出结果
# https://www.jianshu.com/p/e7fbcd85c5a4
# 需要用到的各种包：
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import glob  # 获取待预测的图片文件的地址

# 导入之前训练并保存好的Unet模型：
model = tf.keras.models.load_model( 'model_1.h5' )

# 设定一个子网络：该子网络继承原网络
# conv2d_1_1是我定义原网络时，给其中某一层起的名字！
sub_model = tf.keras.models.Model( inputs = model.input, outputs = model.get_layer('conv2d_1_2').output )

# 查看一下子模型的结果：
sub_model.summary()
Model: "model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         [(None, 256, 256, 3)]     0         
_________________________________________________________________
conv2d_1_1 (Conv2D)          (None, 256, 256, 64)      1792      
_________________________________________________________________
dropout_1_1 (Dropout)        (None, 256, 256, 64)      0         
_________________________________________________________________
bn_1_1 (BatchNormalization)  (None, 256, 256, 64)      256       
_________________________________________________________________
conv2d_1_2 (Conv2D)          (None, 256, 256, 64)      36928     
=================================================================
Total params: 38,976
Trainable params: 38,848
Non-trainable params: 128
_________________________________________________________________

# 用子网络再次预测：

# 读取图片的函数：3通道彩图
def read_image(path):
    img = tf.io.read_file(path)
    img = tf.image.decode_png(img, channels = 3)
    return img

# 文件读取：
img_test = glob.glob( r'D:/SGDownload/subimg_60.png' )
# 从路径读取图像：
tmp1 = read_image( img_test[0] )
# 拓展一维：变成“批次”形式！
tmp1 = tf.cast(tmp1, tf.float32) / 127.5 - 1  # 归到[-1,1]之间！—— 和输入数据一致！
tmp1 = tf.expand_dims( tmp1, axis = 0 )

# 标签预测：用子网络再次预测
label1 = sub_model.predict(tmp1)  
label1 = np.squeeze(label1, 0)
label1.shape
(256, 256, 64)  # 该层一共有64个卷积核，说明结果正确！


# 绘图展示：
plt.figure( figsize = (16,16) )
for x in range(0,64):
    ax = plt.subplot(8, 8, x+1)
    label_tmp = label1[:,:,x]
    plt.imshow( label_tmp.reshape(256,256) )
    
    # 去除坐标轴
    plt.xticks([])
    plt.yticks([])
    # 去除黑框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False) 

plt.tight_layout()
plt.savefig('submodel.jpg')
