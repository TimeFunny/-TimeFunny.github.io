# 1. TF Obect Dection API Install

## [TF Installer](https://tensorflow.google.cn/install/pip)

```shell
> pip install tensorflow-gpu==1.3.2
```



## 1.   download 

```
> git clone https://github.com/tensorflow/models
> git checkout v1.13.0
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
  # or
  setx /m PYTHONPATH "PATH\models\research;PATH\models\research\slim"
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



# 3.  Training

```shell
> python .\object_detection\model_main.py  
--pipeline_config_path="D:\workspace\Train_Script\faster_rcnn_inception_v2_custom.config" 
--model_dir="..\..\workspace\model_0\"  --num_train_steps=300000 
--sample_1_of_n_eval_examples=1  --alsologtostderr
```



## 4. Export Inference Graph

- **meta file**: describes the saved graph structure, includes GraphDef, SaverDef, and so on; then apply `tf.train.import_meta_graph('/tmp/model.ckpt.meta')`, will restore `Saver` and `Graph`.

- **index file**: it is a string-string immutable table(tensorflow::table::Table). Each key is a name of a tensor and its value is a serialized BundleEntryProto. Each BundleEntryProto describes the metadata of a tensor: which of the "data" files contains the content of a tensor, the offset into that file, checksum, some auxiliary data, etc.

- **data file**: it is TensorBundle collection, save the values of all variables.

  

```shell
> python .\object_detection\export_inference_graph.py --input_type=image_tensor 
--trained_checkpoint_prefix="D:\workspace\model_0\model.ckpt-300000" 
--output_directory="D:\workspace\model_0\inference\"  
--pipeline_config_path="D:\workspace\Train_Script\faster_rcnn_inception_v2_custom.config"
```

## 5. test

```

```

## 6. opencv

### 获取pbtxt文件

```shell
> python .\tf_convert\tf_text_graph_faster_rcnn.py --input='D:\workspace\model_0\\inference\\frozen_inference_graph.pb' --config='D:\workspace\model_0\\pipeline.config' --output="D:\workspace\model_0\inference\graph.pbtxt"
```

