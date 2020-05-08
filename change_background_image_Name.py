import os

def find_and_change(path):
    part_names = os.listdir(path)
    for part in part_names:
        unit_names = os.listdir(path+part+"/")
        print(unit_names)
        for unit in unit_names:
            single_image = path+part+"/"+unit+"/"+"B.png"
            print(single_image)
            string = "p"+part[-1:]+"u"+unit[-1:]+".png"
            print(string)
            os.rename(single_image, './resource/imageNameShorten/'+string)

#Image Directory
imagePath = './resource/backgroundImage/'
find_and_change(imagePath)