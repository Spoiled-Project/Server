from typing import Tuple

# No serie detected value.
NOTHING_VALUE: str = 'Nothing'
# The minimal confidence of serie detection acceptable by the server.
CONFIDENCES: dict = {NOTHING_VALUE: 90,
                     'The Good Place': 30,
                     'Avatar': 90
                     }
# path to the nural network.
PATH: str = r'Series/SerieDetector/models/my_full_model_res.h5'
# The possible series outputs of the nural network.
SERIES_LIST: Tuple = tuple(CONFIDENCES.keys())
# The size of the nural network's image input
PIC_SIZE: Tuple = (224, 224)

if __name__ == '__main__':
    print(SERIES_LIST)
