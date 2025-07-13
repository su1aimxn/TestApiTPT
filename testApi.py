import requests

# URL ของ API
url = "https://wea.hii.or.th:3005/getDataTonPhraeThong"

# ข้อมูลยืนยันตัวตน
auth_data = {
    "user": "ton_phrae_thong",
    "pass": "9d1bcacb707e86a62bfbbaa84d435a77"
}

# ส่งคำขอแบบ POST
response = requests.post(url, json=auth_data)

# ตรวจสอบว่าดึงข้อมูลได้สำเร็จหรือไม่
if response.status_code == 200:
    # แปลงข้อมูลเป็น JSON
    result = response.json()
    
    # ดึงข้อมูลเฉพาะส่วนของ 'data'
    data = result['data'][0]  # มีแค่หนึ่งรายการ

    # แสดงผลข้อมูลอย่างสวยงาม
    print("-สถานี:", data['name'])
    print("-วันที่:", data['date'], "-เวลา:", data['time'])
    print("-ตำบล:", data['sub_district'], "-อำเภอ:", data['district'], "-จังหวัด:", data['province'])
    print("-อุณหภูมิในกล่อง:", data['temp_in'], "°C")
    print("-อุณหภูมิภายนอก:", data['temp_out'], "°C")
    print("-ความชื้น:", data['hum'], "%")
    print("-ระดับน้ำ:", data['water'], "เมตร")
    print("-ฝนสะสมวันนี้:", data['rain24h'], "มม.")
    print("-PM2.5:", data['pm25'], "μg/m³ | PM10:", data['pm10'], "μg/m³")
    print("-แรงดันไฟฟ้า:", data['power'], "V")

else:
    # ถ้าเกิดข้อผิดพลาด
    print("ดึงข้อมูลไม่สำเร็จ:", response.status_code)
    print(response.text)
