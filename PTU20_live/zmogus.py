import pickle
import os
import logging

def create_logger(file=__name__+'.log', name=__name__, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter()
    file_handler = logging.FileHandler(file)
    file_handler = setLevel(level)
    file_handler = setFormater(formatter)
    console_handler = logging.StreamHandler()
    console_handler = setLevel(file_handler)
    
    logger.addHandler(file_handler)
    return logger

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __str__(self):
        return f"{self.vardas}, {self.amzius} metų"


if __name__ == "__main__":
    zmogus = Zmogus(
        input("vardas: "),
        int(input("metai: ")),
    )
    ZMONES_FILE = 'PTU20_live/zmones.pkl'

    if os.path.exists(ZMONES_FILE):
        with open(ZMONES_FILE, "rb") as zmones_file:
            zmones = pickle.load(zmones_file)
            zmones.append(zmogus)
    else:
        zmones = [zmogus]
    with open(ZMONES_FILE, "wb") as zmones_file:
        pickle.dump(zmones, zmones_file)

    print('---[ Visi zmones ]---')
    for zmogus in zmones:
        print(zmogus)
