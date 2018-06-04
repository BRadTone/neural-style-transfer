import os, sys, time
import urllib.request
from src.CONFIG import CONFIG


def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                     (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()


if __name__ == '__main__':
    if not os.path.exists(CONFIG.PRETRAINED_MODEL_DIR):
        os.mkdir(CONFIG.PRETRAINED_MODEL_DIR)

    urllib.request.urlretrieve(CONFIG.VGG_VERYDEEP_16_DOWNLOAD_URL,
                               CONFIG.PRETRAINED_MODEL_PATH,
                               reporthook)

