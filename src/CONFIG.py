class CONFIG:
    VGG_VERYDEEP_16_DOWNLOAD_URL = 'http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat'
    PRETRAINED_MODEL_DIR = '../pretrained_model'
    PRETRAINED_MODEL_PATH = 'pretrained_model/imagenet-vgg19.mat'
    STYLE_LAYERS = [
        ('conv1_1', 0.2),
        ('conv2_1', 0.2),
        ('conv3_1', 0.2),
        ('conv4_1', 0.2),
        ('conv5_1', 0.2)]
    CONTENT_IMAGE = 'images/rb_business_photo.jpg'
    STYLE_IMAGE = 'images/van-gogh_autoportrait.jpg'
