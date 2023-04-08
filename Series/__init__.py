class Spoiler_detector:
    from .Avatar import detect_serie as avatar
    from .The_Good_Place import detect_serie as the_good_place


__all__ = ['Spoiler_detector']

if __name__ == '__main__':
    s = Spoiler_detector
    print(s.avatar('123'))
