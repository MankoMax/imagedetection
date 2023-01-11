import easyocr
import cv2


def get_coordinates(image):
    result_list = []
    reader = easyocr.Reader(['en'], model_storage_directory="model") 
    try:
        image = cv2.imread(image)
        image2 = image.copy()
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        text = reader.readtext(image2, rotation_info=[30, 45, 90, 180, 270], 
                            contrast_ths=0.3, adjust_contrast=0.8, 
                            allowlist='ZVzv', text_threshold=0.7, low_text=0.3,
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
        for coordinate in coordinates:
            cords = coordinate.__str__().replace('(', '').replace('[', '').replace(']', '').replace(')', '').replace("'", "").replace(' ', '').split(',')
            for cord in cords:
                if '.' in cord:
                    cords[cords.index(cord)] = cord.split('.')[0]
            x = int(cords[0])
            y = int(cords[1])
            width = int(cords[2]) - int(cords[0])
            height = int(cords[5]) - int(cords[1])
            list_of_coordinates.append([x, y, width, height])
    return list_of_coordinates
    