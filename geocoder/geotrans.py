## geocoder 호출
import requests

r = requests.get(
    'http://api.vworld.kr/req/search?service=search&request=search&version=2.0&crs=EPSG:900913&bbox=14140071.146077,4494339.6527027,14160071.146077,4496339.6527027&size=10&page=1&query=성남시 분당구 판교로 242&type=address&category=road&format=json&errorformat=json&key=D1AAD68A-57B4-3C5D-9515-EEA73F9C13C8')

print(r.json())

# ## cell 설정 [ (10)J1 ~ J* : 위도 / (11)K1 ~ K* : 경도]
# lat_cell = sheet.cell(row=rowCount, column=2)
# lng_cell = sheet.cell(row=rowCount, column=3)
#
# ## 데이터 추가
# lat_cell.value = r.json()["EPSG_4326_Y"]
# lng_cell.value = r.json()["EPSG_4326_X"]
#
# print(lat_cell,lng_cell)
# except KeyError as ke:
# lat_cell.value = 0
# lng_cell.value = 0
# except TypeError as te:
# lat_cell.value = 0
# lng_cell.value = 0
#
# rowCount = rowCount + 1
#
# ## 데이터 저장
# exelFile.save("address.xlsx")