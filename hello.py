import random

first_name = ['Olil','kholil','Jolil','Abul','Kashem','Rohim','Korim']

last_name = ['Ullah','Mia','Chowdhury','Uddin']

cities = ['Barishal','Chittagong','Sylhet','Mymensingh','Dhaka']

thanas = ['jatrabari','Wari','Mirpur','lalbagh','NewMarket']

lanes = ['1stLane','2ndLane','AraiLane','3rdLane','4thLane','5thLanee']

for num in range(100):
first = random.choice(first_name)
last = random.choice(last_name)

phone = f'01{random.randint(600,900)}-{random.randint(100000,999999)}'

bari_number = random.randint(1,100)
city = random.choice(cities)
thana = random.choice(thanas)
lane = random.choice(lanes)
post_code = random.randint(1200,8500)

address = f'HouseNO.{bari_number} {lane} {thana}, {city}-{post_code}'


email = first.lower() + last.lower() +'11@gmail.com'

print(f' {first} {last} \n {phone} \n {address} \n {email}\n')