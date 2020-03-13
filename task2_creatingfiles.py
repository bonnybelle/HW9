import os

directory = os.walk('lesson6')
for address, dirs, files in directory:
    for name in files:
        path_to_txt = os.path.join(address, name)
        print(path_to_txt)
        with open(path_to_txt, 'r', encoding='utf-8') as file:
            count = 0
            for line in file:
                line_res = line.split('\t')
                # print(line_res)
                # next_line = next(line)
                city = line_res[3]
                user_id = line_res[4]
                request = line_res[5]
                info_pair = (user_id, request)
                current_city_path = 'result/{}.tsv'.format(city)
                result = open(current_city_path, 'w')
