# 1. TF Obect Dection API Install

## [TF Installer](https://tensorflow.google.cn/install/pip)

```shell
> pip install tensorflow-gpu==1.3.2
```



## 1.   download 

```
> git clone https://github.com/tensorflow/models
# window 请使用指定版本，否则会报错(疑似原因：不识别通配符*)
protobuf: https://github.com/protocolbuffers/protobuf/releases/tag/v3.4.0
```

## 2. 环境安装

```
> pip install tensorflow-gpu
> pip install cython contextlib2 pillow numpy lxml jupyter matplotlib protobuf
```

## 3. COCO API 

```
> git clone https://github.com/cocodataset/cocoapi.git
> cd cocoapi/PythonAPI
> make
> cp -r pycocotools <path_to_tensorflow>/models/research/
```

## 4. Protobuf Compilation

```
# proto 3.4(windows)
# From tensorflow/models/research/ 
> protoc object_detection/protos/*.proto --python_out=.
```

## 5. Add Libraries to PYTHONPATH

添加两个有关目录到相关环境变量
- /models/research/ 
- /models/research/slim/

- [x] Linux

```shell
# From tensorflow/models/research/
> export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
# or
> .bashrc
```

- [x] windows
  in **python_path\Lib\site-packages** , create new  `tensorflow_model.pth`  file, and add:

  ```
  PATH\models\research
  PATH\models\research\slim
  ```


 ## 6.  Testing the Installation

```
> python object_detection/builders/model_builder_test.py
```

# 2. 数据预处理(Preparing Inputs)

## 1. label map

```json
# object_detection/data/pascal_label_map.pbtxt
item {
  id: 1
  name: 'aeroplane'
}

item {
  id: 2
  name: 'bicycle'
}
```

## 2. TF Record Data Generator

命令调用方式: 

​	 以`create_pascal_tf_record.py`为基础，自定义创建`tf record`格式数据的脚本:

```shell
> python path/create_data_to_record.py --label_map_path=path/pascal_label_map.pbtxt \
    --data_dir=path --set=`train` --output_path=train.record
    
> python path/create_data_to_record.py --label_map_path=path/pascal_label_map.pbtxt \
    --data_dir=path --set=`val` --output_path=val.record
```

###  Sharding Datasets

```python
import contextlib2
from object_detection.dataset_tools import tf_record_creation_util

num_shards=10
output_filebase='/path/to/train_dataset.record'

with contextlib2.ExitStack() as tf_record_close_stack:
  output_tfrecords = tf_record_creation_util.open_sharded_output_tfrecords(
      tf_record_close_stack, output_filebase, num_shards)
  for index, example in examples:
    tf_example = create_tf_example(example)
    output_shard_index = index % num_shards
    output_tfrecords[output_shard_index].write(tf_example.SerializeToString())
```

## 3. Configuring the Object Detection Training Pipeline

```shell
# from object_detection/samples/configs


```

