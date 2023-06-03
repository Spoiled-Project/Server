from PIL import Image
import requests
from io import BytesIO
import concurrent.futures
from Series import detect_serie
from Macros import RestsMacros
from Macros.ModelMacros import PIC_SIZE
import base64
from tensorflow import image, keras


def download_image(url: str) -> Image:
    """
    The function downloads the received url's image.
    @param url: The image's url.
    @return: The url as PIL's image.
    """
    if "base64" in url:
        _, data = url.split(",", 1)
        plain_data = base64.b64decode(data)
        img = Image.open(BytesIO(plain_data))
    else:
        img = Image.open(BytesIO(requests.get(url).content))
    img = keras.utils.array_to_img(image.resize(img, PIC_SIZE))
    return img


def check_image(url: str, series: list) -> bool:
    """
    The function checks if the received image is a spoiler in one of the received detectors.
    @param url: The image's url.
    @param detectors: A list of callable detectors that check if the received image is its spoiler.
    @return: If one or more of the detectors found the received image as a spoiler.
    """
    try:
        img = download_image(url)
        serie = detect_serie(img)
        print(series)
        return serie in series
    except BaseException as e:
        print(e)
        return False


def check_images(urls: list, series: [str]) -> dict:
    """
    The function creates a dictionary of the result which image's url is the key and a future variable of the result is
    the value.
    Then, the function waits for each future to finish its calculation and returns the result using the result() method.
    @param urls: The images urls.
    @param series: A list of TODO.
    @return: A dict of the images' url as values and the spoiler detection results.
    """
    # here's executor is a future value alternative for python because python's normal Thread can't return is returned
    # value.
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = {url: executor.submit(check_image, url, series) for url in urls}
    return {url: results[url].result() for url in results}


def handle_req(req: dict) -> dict:
    """
    The function returns which of the request's images is a spoiler and which isn't.
    @param req: The server's request.
    @return: Which of the request's images is a spoiler and which isn't.
    """
    # Loading the demanded detectors.
    series: [str] = [serie for serie in req[RestsMacros.SERIES]]
    # checks each image using all the detectors on each.
    res: dict = check_images(req[RestsMacros.IMAGES], series)
    return res


if __name__ == '__main__':
    ans = handle_req({RestsMacros.SERIES: ['Avatar', 'The Good Place'],
                RestsMacros.IMAGES: [
                    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2fXAHBZUDUARvqeM6RzTAIc8XQ9wex3Eu2w&usqp=CAU',
                    'https://ggsc.s3.amazonaws.com/images/uploads/the-good-place-season-4-1.jpeg',
                    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVAnG915UzMsCQxYYvNJBr2ywgSqcHrHFa1w&usqp=CAU',
                    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcQLFjeTF9UieEaLl-tnbws5aRSH91qSu68g&usqp=CAU',
                    'https://letsenhance.io/static/334225cab5be263aad8e3894809594ce/75c5a/MainAfter.jpg',
                    'data:image/jpeg;base64,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']})
    for key in ans:
        print(key, ans[key])
