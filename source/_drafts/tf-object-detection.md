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

  ```
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
# object_detection/dataset_tools
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

### opencv 4.1.1

```cpp
#include <fstream>
#include <sstream>

#include <iostream>

#include <opencv2/dnn.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

using namespace cv;
using namespace dnn;

float confThreshold, nmsThreshold;
std::vector<std::string> classes{"thunder"};

inline void preprocess(const Mat& frame, Net& net, Size inpSize, float scale,
                       const Scalar& mean, bool swapRB);

void postprocess(Mat& frame, const std::vector<Mat>& out, Net& net);

void drawPred(int classId, float conf, int left, int top, int right, int bottom, Mat& frame);

void callback(int pos, void* userdata);

int main(int argc, char** argv)
{
    confThreshold = 0.6;
    nmsThreshold = 0.3;
    float scale = 1.0;
    Scalar mean(0, 0, 0);
    bool swapRB = true;
    int inpWidth = 1000;
    int inpHeight = 800;
    size_t async = 0;
	
    std::string modelPath = "D:\\workspace\\model_0\\inference\\frozen_inference_graph.pb";
    std::string configPath = "D:\\workspace\\model_0\\inference\\graph.pbtxt";
	
	// Create a window
    static const std::string kWinName = "Deep learning object detection in OpenCV";
    namedWindow(kWinName, WINDOW_NORMAL);
    int initialConf = (int)(confThreshold * 100);
    createTrackbar("Confidence threshold, %", kWinName, &initialConf, 99, callback);
	
    // Load a model.
    Net net = readNet(modelPath, configPath, "tensorflow");
    net.setPreferableBackend(DNN_BACKEND_DEFAULT);
    net.setPreferableTarget(DNN_TARGET_CPU);	
    std::vector<String> outNames = net.getUnconnectedOutLayersNames();
	// Process frames.
    Mat frame = imread("D:\\Datasets\\lightning\\JPEGImages\\lightning_1.jpg");
    preprocess(frame, net, Size(inpWidth, inpHeight), scale, mean, swapRB);
    std::vector<Mat> outs;
    net.forward(outs, outNames);
    postprocess(frame, outs, net);
	
    // Put efficiency information.
    std::vector<double> layersTimes;
    double freq = getTickFrequency() / 1000;
    double t = net.getPerfProfile(layersTimes) / freq;
    std::string label = format("Inference time: %.2f ms", t);
    putText(frame, label, Point(0, 15), FONT_HERSHEY_SIMPLEX, 0.5, Scalar(0, 255, 0));
	imwrite("..\\thunder_result.jpg", frame);

    imshow(kWinName, frame);

	waitKey(0);
    return 0;
}

inline void preprocess(const Mat& frame, Net& net, Size inpSize, float scale,
                       const Scalar& mean, bool swapRB)
{
    static Mat blob;
    // Create a 4D blob from a frame.
    if (inpSize.width <= 0) inpSize.width = frame.cols;
    if (inpSize.height <= 0) inpSize.height = frame.rows;
    blobFromImage(frame, blob, 1.0, inpSize, Scalar(), swapRB, false, CV_8U);

    // Run a model.
    net.setInput(blob, "", scale, mean);
    if (net.getLayer(0)->outputNameToIndex("im_info") != -1)  // Faster-RCNN or R-FCN
    {
        resize(frame, frame, inpSize);
        Mat imInfo = (Mat_<float>(1, 3) << inpSize.height, inpSize.width, 1.6f);
        net.setInput(imInfo, "im_info");
    }
}

void postprocess(Mat& frame, const std::vector<Mat>& outs, Net& net)
{
    static std::vector<int> outLayers = net.getUnconnectedOutLayers();
    static std::string outLayerType = net.getLayer(outLayers[0])->type;

    std::vector<int> classIds;
    std::vector<float> confidences;
    std::vector<Rect> boxes;
    if (outLayerType == "DetectionOutput")
    {
        // Network produces output blob with a shape 1x1xNx7 where N is a number of
        // detections and an every detection is a vector of values
        // [batchId, classId, confidence, left, top, right, bottom]
        CV_Assert(outs.size() > 0);
		std::cout << "out length is : " << outs.size() << std::endl;
		Mat d = outs[0];
		std::cout << d.size << " "  << d.rows << " " << d.cols  << " " << d.total() << std::endl;


        for (size_t k = 0; k < outs.size(); k++)
        {
			
			float* data = (float*)outs[k].data;
            for (size_t i = 0; i < outs[k].total(); i += 7)
            {
                float confidence = data[i + 2];
                if (confidence > confThreshold)
                {
                    int left   = (int)data[i + 3];
                    int top    = (int)data[i + 4];
                    int right  = (int)data[i + 5];
                    int bottom = (int)data[i + 6];
                    int width  = right - left + 1;
                    int height = bottom - top + 1;
                    if (width * height <= 1)
                    {
                        left   = (int)(data[i + 3] * frame.cols);
                        top    = (int)(data[i + 4] * frame.rows);
                        right  = (int)(data[i + 5] * frame.cols);
                        bottom = (int)(data[i + 6] * frame.rows);
                        width  = right - left + 1;
                        height = bottom - top + 1;
                    }
                    classIds.push_back((int)(data[i + 1]));  // Skip 0th background class id.
                    boxes.push_back(Rect(left, top, width, height));
                    confidences.push_back(confidence);
                }
            }
        }
    }
    else if (outLayerType == "Region")
    {
        for (size_t i = 0; i < outs.size(); ++i)
        {
            // Network produces output blob with a shape NxC where N is a number of
            // detected objects and C is a number of classes + 4 where the first 4
            // numbers are [center_x, center_y, width, height]
            float* data = (float*)outs[i].data;
            for (int j = 0; j < outs[i].rows; ++j, data += outs[i].cols)
            {
                Mat scores = outs[i].row(j).colRange(5, outs[i].cols);
                Point classIdPoint;
                double confidence;
                minMaxLoc(scores, 0, &confidence, 0, &classIdPoint);
                if (confidence > confThreshold)
                {
                    int centerX = (int)(data[0] * frame.cols);
                    int centerY = (int)(data[1] * frame.rows);
                    int width = (int)(data[2] * frame.cols);
                    int height = (int)(data[3] * frame.rows);
                    int left = centerX - width / 2;
                    int top = centerY - height / 2;

                    classIds.push_back(classIdPoint.x);
                    confidences.push_back((float)confidence);
                    boxes.push_back(Rect(left, top, width, height));
                }
            }
        }
    }
    else
        CV_Error(Error::StsNotImplemented, "Unknown output layer type: " + outLayerType);

    std::vector<int> indices;
    dnn::NMSBoxes(boxes, confidences, confThreshold, nmsThreshold, indices);
    for (size_t i = 0; i < indices.size(); ++i)
    {
        int idx = indices[i];
        Rect box = boxes[idx];
        drawPred(classIds[idx], confidences[idx], box.x, box.y,
                 box.x + box.width, box.y + box.height, frame);
    }
}

void drawPred(int classId, float conf, int left, int top, int right, int bottom, Mat& frame)
{
    rectangle(frame, Point(left, top), Point(right, bottom), Scalar(0, 255, 0));

    std::string label = format("%.2f", conf);
    if (!classes.empty())
    {
        CV_Assert(classId < (int)classes.size());
		std::cout << "classId: " << classId << "   class label is: " << classes[classId] << std::endl;
        label = classes[classId] + ": " + label;
    }

    int baseLine;
    Size labelSize = getTextSize(label, FONT_HERSHEY_SIMPLEX, 0.5, 1, &baseLine);

    top = max(top, labelSize.height);
    rectangle(frame, Point(left, top - labelSize.height),
              Point(left + labelSize.width, top + baseLine), Scalar::all(255), FILLED);
    putText(frame, label, Point(left, top), FONT_HERSHEY_SIMPLEX, 0.5, Scalar());
}

void callback(int pos, void*)
{
    confThreshold = pos * 0.01f;
}


```

### CMakeLists.txt

```CMAKE
cmake_minimum_required(VERSION 2.8)
project( detect )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( detect detect.cpp )
target_link_libraries( detect ${OpenCV_LIBS} )
```

