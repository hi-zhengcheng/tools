import torch
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
import os


class Vgg19(torch.nn.Module):
    """
    Vgg19 layers: [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 256, 'M', 512, 512, 512, 512, 'M', 512, 512, 512, 512, 'M']
        * One digital number represents two layers: conv2d and relu;
        * M represents one layer: MaxPool2d

    When you run the code first time, it will cost some time to download the pretrained vgg19 model and save it in
    your home dir: ~/.torch/models/

    Here, we extract the second layer and all the layers after each MaxPool2d.
    You can change the following indexes for your request.
    """
    def __init__(self):
        super(Vgg19, self).__init__()
        vgg_features = models.vgg19(pretrained=True).features
        self.slice1 = vgg_features[:2]
        self.slice2 = vgg_features[2:7]
        self.slice3 = vgg_features[7:12]
        self.slice4 = vgg_features[12:21]
        self.slice5 = vgg_features[21:30]

        for param in self.parameters():
            param.requires_grad = False

    def forward(self, X):
        """Compute Vgg19 features at different relu layers.

        Arguments:
            X: input images tensor with shape: (N, channel, height, width). channel should be 3.
            It looks like this model dose not require fixed image size as input.

        Return:
            List of features computed from specified layers. Shape: (N, ...)
        """
        relu1 = self.slice1(X)
        relu2 = self.slice2(relu1)
        relu3 = self.slice3(relu2)
        relu4 = self.slice4(relu3)
        relu5 = self.slice5(relu4)
        return [relu1, relu2, relu3, relu4, relu5]


if __name__ == '__main__':
    # Specify gpu. Set "" to use cpu.
    gpu_id = "0"
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = gpu_id

    # read image
    image_path = 'test.jpg'
    image = Image.open(image_path).convert('RGB')

    # convert image to tensor by transforms
    transform_list = [
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ]
    trans = transforms.Compose(transform_list)
    image_tensor = trans(image)

    # add one dimension
    batched_image_tensor = torch.unsqueeze(image_tensor, 0)

    vgg19_model = Vgg19()

    # try to use GPU
    if len(gpu_id) > 0 and torch.cuda.is_available():
        batched_image_tensor = batched_image_tensor.cuda()
        vgg19_model = vgg19_model.cuda()

    features = vgg19_model(batched_image_tensor)

    # try to convert from GPU to CPU
    if len(gpu_id) > 0 and torch.cuda.is_available():
        features = [item.cpu() for item in features]

    # convert from tensor to numpy, and squeeze first dimension
    features = [torch.squeeze(item, 0).numpy() for item in features]

    # Happy to use features now.
    for idx, feature in enumerate(features):
        print(idx, feature.shape)
