from typing import Tuple

NOTHING_VALUE: str = 'Nothing'
CONFIDENCES: dict = {NOTHING_VALUE: 90,
                     'The Good Place': 0,
                     'Avatar': 50
                     }
PATH: str = r'Series\checker\model\my_full_model_res.h5'
SERIES_LIST: Tuple = tuple(CONFIDENCES.keys())
PIC_SIZE: Tuple = (224, 224)

if __name__ == '__main__':
    print(SERIES_LIST)