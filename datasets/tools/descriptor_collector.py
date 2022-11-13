import os
import json

import dlib
import cv2

if not "datasets" in os.getcwd():
    os.chdir(os.getcwd() + "/datasets")

sp = dlib.shape_predictor('tools/dlib/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('tools/dlib/dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

def get_descriptor(img_path:str) -> (list):
    '''
    Функция обнаружения лица на фотографии и создания дескриптора.

    Args:
        img_path (str): путь до выбранного изображения
    Returns:
        descriptor (list): список ключевых точек лица
    '''
    img = cv2.imread(img_path)
    detect_img = detector(img, 1)

    for k, d in enumerate(detect_img):
        shape = sp(img, d)

    descriptor = list(facerec.compute_face_descriptor(img, shape))

    return descriptor

def collect_party(party_name:str) -> (list):
    '''
    Функция формирования дескрипторов лиц из выбранного каталога.

    Args:
        party_name (str): название партии (имя каталога)
    Returns:
        result_list (list): сформированный набор дескрипторов
    '''
    img_list = os.listdir(party_name)

    result_list = list()
    for file_name in img_list[12:]:
        print(f" --- {file_name} --- ")
        try:
            descriptor = get_descriptor(f"{party_name}/{file_name}")
            result_list.append(descriptor)
        except:
            print(f" !!! {party_name}/{file_name} - Get description error !!! ")

    return result_list

def create_datasets(party_list:list) -> (dict):
    '''
    Функция формирования датасета для обучения нейронной сети.

    Args:
        party_list (list): список всех доступных партий
    Returns:
        all_partys_dict (dict): словарь типа {"this_party_predict": [party_descriptor_list]}
    '''
    all_partys_dict = dict()

    for index in range(len(party_list)):    
        this_party_predict = [0] * len(party_list)
        this_party_predict[index] = 1
        
        print(f"Get starting {party_list[index]} --- {this_party_predict}:")
        party_descriptor_list = collect_party(party_list[index])
        all_partys_dict[str(this_party_predict)] = party_descriptor_list

    return all_partys_dict

def create_json(dataset_dict:dict, old_dict = dict()) -> (None):
    '''
    Создание JSON файла с датасетом.
    Args:
        dataset_dict (dict): словарь типа {"this_party_predict": [party_descriptor_list]}
    Returns:
        None
    '''
    if "dataset.json" in os.listdir():
        with open("dataset.json", "r", encoding='utf-8') as old_file:
            old_dict = json.load(old_file)

    old_dict.update(dataset_dict)
    with open("dataset.json", "w", encoding='utf8') as JSON:
        json.dump(old_dict, JSON, indent=4, ensure_ascii=False)

    return