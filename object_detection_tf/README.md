# TensorFlow Object detection Demo

This demo uses tensorflow hub to build a simple realtime object detection application.

### Install TensorFlow hub

Follow instructions from [here](https://www.tensorflow.org/hub/installation):

```bash
pip install "tensorflow>=1.7.0"
pip install tensorflow-hub
```
    
### TensorFlow hub module cache

By default, the pretrained model will be downloaded and saved into one temp dir. You can specify other dir as follows:

```python
import os
os.environ['TFHUB_CACHE_DIR'] = 'your_module_cache_dir'
```

Make sure set this env before any tf hub calls.

### Single Image object detection

`infer_image.py` demos how to do object detection on single image. 
You can change top_k and colors to display more results.

### Realtime Camera object detection

`infer_real_time_camera.py` demos how to do object detection on real time video.
