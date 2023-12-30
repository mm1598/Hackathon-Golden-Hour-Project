import os, glob.glob

class lesson():
    primer = None
    lecture = None

    def __init__(name: str)
        with open(f'{name}/primer.txt') as f:
            self.primer = f.readlines()

        with open(f'{name}/lecture.txt') as f:
            self.lecture = f.readlines()
    
