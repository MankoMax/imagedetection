import easyocr
import cv2
import re


def get_coordinates(image):
    result_list = []
    reader = easyocr.Reader(['en'], model_storage_directory="model") 
    try:
        image = cv2.imread(image)
        image2 = image.copy()
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        text = reader.readtext(image2, rotation_info=[30, 45, 90, 180, 270], 
                            contrast_ths=0.2, adjust_contrast=0.8, 
                            allowlist='ZV', text_threshold=0.7, 
                            mag_ratio=2, detail=1, paragraph=False, batch_size=3)
        
        if len(text) == 0:
            pass
        else:
            result_list = text
            return result_list
    except:
        print("error")


def get_coordinates_for_bounding_box(txt_file):
    list_of_coordinates = []
    with open(txt_file, 'r') as f:
        coordinates = f.read().splitlines()
        coordinates = [re.findall(r'\d+', coordinate) for coordinate in coordinates]
        for coordinate in coordinates:
            x = int(coordinate[0])
            y = int(coordinate[1])
            width = int(coordinate[2]) - int(coordinate[0])
            height = int(coordinate[5]) - int(coordinate[1])
            list_of_coordinates.append([x, y, width, height])
    return list_of_coordinates
    


    