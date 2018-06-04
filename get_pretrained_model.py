import urllib.request
from CONFIG import CONFIG

if __name__ == '__main__':
    urllib.request.urlretrieve(CONFIG.VGG_VERYDEEP_16_DOWNLOAD_URL, CONFIG.PRETRAINED_MODEL_PATH)
