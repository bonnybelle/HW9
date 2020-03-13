import os

directory = os.walk('lesson6')
for address, dirs, files in directory:
    for name in files:
        path_to_txt = os.path.join(address, name)
        print(path_to_txt)
        with open(path_to_txt, 'r', encoding='utf-8') as file:
            for line in file:
                line_res = line.split('\t')
                city = line_res[3]
                current_city_path = 'result/{}.tsv'.format(city)
                result = open(current_city_path, 'w')
