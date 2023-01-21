from dotenv import load_dotenv
import os
import time
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
# Import namespaces


def main():
    global cv_client

    # Get Configuration Settings

    # Authenticate Computer Vision client
    credential = CognitiveServicesCredentials() 
    cv_client = ComputerVisionClient()

    # Menu for text reading functions



def GetTextRead(image_file):
    print('Reading text in {}\n'.format(image_file))


if __name__ == "__main__":
    main()
