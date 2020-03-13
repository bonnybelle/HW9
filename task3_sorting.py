import os

directory1 = os.walk('lesson6')
result_folder = os.walk('result')
cities = {}

for address, dirs, files in directory1:
    for name in files:
        print(name)
        path_to_txt = os.path.join(address, name)
        with open(path_to_txt, 'r', encoding='utf-8') as file:
            for line in file:
                line_res = line.split('\t')
                city = line_res[3]
                user_id = line_res[4]
                request = line_res[5]
                if city not in cities:
                    cities[city] = {}
                if request not in cities[city]:
                    cities[city][request] = set()
                cities[city][request].add(user_id)


for city in cities:
    current_city_path = 'result/{}.tsv'.format(city)
    print(city)
    with open(current_city_path, 'w', encoding='utf') as file:
        for request in cities[city]:
            length = len(cities[city][request])
            file.write(str(request) + '\t' + str(length) + '\n')


# {city:{request:{()}}}
