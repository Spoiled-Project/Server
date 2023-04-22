from PIL import Image
import requests
from io import BytesIO
import concurrent.futures
from Series import Spoiler_detector
from Macros import RestsMacros
from Macros.DetectorsMacros import *


def download_image(url: str) -> Image:
    """
    The function downloads the received url's image.
    @param url: The image's url.
    @return: The url as PIL's image.
    """
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


def check_image(url: str, detectors: list) -> bool:
    """
    The function checks if the received image is a spoiler in one of the received detectors.
    @param url: The image's url.
    @param detectors: A list of callable detectors that check if the received image is its spoiler.
    @return: If one or more of the detectors found the received image as a spoiler.
    """
    try:
        img = Image.open(BytesIO(requests.get(url).content))
        # here's executor is a future value alternative for python because python's normal Thread can't return is returned
        # value.
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(detector, img) for detector in detectors]
        result = PROCESSING
        while result == PROCESSING:
            still_processing = False
            for calculation in results:
                # Checks if the spoiler detector has finished to check if the image is a spoiler.
                if calculation.done():
                    # Gets the detector result.
                    res = calculation.result()
                    if res == SPOILER:
                        result = SPOILER
                else:
                    still_processing = True
            if not still_processing and result == PROCESSING:
                result = NOT_SPOILER
        return result == SPOILER
    except BaseException:
        return False


def check_images(urls: list, detectors: list) -> list:
    """
    The function creates a dictionary of the result which image's url is the key and a future variable of the result is
    the value.
    Then, the function waits for each future to finish its calculation and returns the result.
    @param urls: The images urls.
    @param detectors: A list of callable functions which detect if the received image is a spoiler.
    @return: A dict of the images' url as values and the spoiler detection results.
    """
    # here's executor is a future value alternative for python because python's normal Thread can't return is returned
    # value.
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = {url: executor.submit(check_image, url, detectors) for url in urls}
    return {url: results[url].result() for url in results}


def handle_req(req: dict) -> list:
    """
    The function returns which of the request's images is a spoiler and which isn't.
    @param req: The serve's request.
    @return: Which of the request's images is a spoiler and which isn't.
    """
    # Loading the demanded detectors.
    detectors = [getattr(Spoiler_detector, serie.replace(" ", "_")) for serie in req[RestsMacros.SERIES]]
    # checks each image using all the detectors on each.
    res = check_images(req[RestsMacros.IMAGES], detectors)
    return res


if __name__ == '__main__':
    handle_req({RestsMacros.SERIES: ['avatar', 'the good place'],
                RestsMacros.IMAGES: [
                    'https://letsenhance.io/static/334225cab5be263aad8e3894809594ce/75c5a/MainAfter.jpg',
                    'https://static.vecteezy.com/packs/media/vectors/term-bg-1-3d6355ab.jpg']})
