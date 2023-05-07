import numpy as np
import tensorflow as tf
import cv2 as cv

import cv2 as cv



cvNet = cv.dnn.readNetFromTensorflow(r'D:\workspace\model_0\\inference\\frozen_inference_graph.pb',
        r'D:\workspace\model_0\inference\graph.pbtxt')

img = cv.imread(r"D:\\Datasets\\lightning\\JPEGImages\\lightning_1.jpg")
rows = img.shape[0]
cols = img.shape[1]
cvNet.setInput(cv.dnn.blobFromImage(img, size=(640, 480), swapRB=True, crop=False))
cvOut = cvNet.forward()

for detection in cvOut[0,0,:,:]:
    score = float(detection[2])
    if score > 0.3:
        left = detection[3] * cols
        top = detection[4] * rows
        right = detection[5] * cols
        bottom = detection[6] * rows
        cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

cv.imshow('img', img)
cv.waitKey()



"""

# Read the graph.
with tf.gfile.FastGFile(r'D:\workspace\model_0\frozen_inference_graph.pb', 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())

with tf.Session() as sess:
    # Restore session
    sess.graph.as_default()
    tf.import_graph_def(graph_def, name='')

    # Read and preprocess an image.
    img = cv.imread(r"D:\\Datasets\\lightning\\JPEGImages\\lightning_1.jpg")
    rows = img.shape[0]
    cols = img.shape[1]
    inp = cv.resize(img, (640, 480))
    inp = inp[:, :, [2, 1, 0]]  # BGR2RGB

    # Run the model
    out = sess.run([sess.graph.get_tensor_by_name('num_detections:0'),
                    sess.graph.get_tensor_by_name('detection_scores:0'),
                    sess.graph.get_tensor_by_name('detection_boxes:0'),
                    sess.graph.get_tensor_by_name('detection_classes:0')],
                   feed_dict={'image_tensor:0': inp.reshape(1, inp.shape[0], inp.shape[1], 3)})

    # Visualize detected bounding boxes.
    num_detections = int(out[0][0])
    for i in range(num_detections):
        classId = int(out[3][0][i])
        score = float(out[1][0][i])
        bbox = [float(v) for v in out[2][0][i]]
        if score > 0.3:
            x = bbox[1] * cols
            y = bbox[0] * rows
            right = bbox[3] * cols
            bottom = bbox[2] * rows
            cv.rectangle(img, (int(x), int(y)), (int(right), int(bottom)), (125, 255, 51), thickness=2)

cv.imshow('TensorFlow MobileNet-SSD', img)
cv.waitKey()
"""