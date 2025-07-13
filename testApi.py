import requests
import time



# URL API 
api_url = "https://wea.hii.or.th:3005/getDataTonPhraeThong"
auth_data = {
    "user": "ton_phrae_thong",
    "pass": "9d1bcacb707e86a62bfbbaa84d435a77"
}

# Blynk Token และ URL
blynk_token = "LD0UlS65rqwA7zKv2vg6uNUMfcmEc150"
blynk_url = f"https://blynk.cloud/external/api/update?token={blynk_token}"

# เก็บเวลาล่าสุดที่เคยส่งข้อมูลไป
last_timestamp = ""

print("🔄 เริ่มตรวจสอบข้อมูลจาก API และส่งไปยัง Blynk เมื่อมีข้อมูลใหม่...")


while True:
    try:
        #  เรียก API
        response = requests.post(api_url, json=auth_data)

        if response.status_code == 200:
            result = response.json()
            data = result['data'][0]

            # สร้าง timestamp จากวันที่ + เวลา
            timestamp = data['date'] + " " + data['time']

            # ถ้าข้อมูลเปลี่ยนจากครั้งก่อน → ค่อยส่ง
            if timestamp != last_timestamp:
                print(f"\n✅ พบข้อมูลใหม่ ({timestamp})")

                # แสดงผลใน Console
                print("- สถานี:", data['name'])
                print("- วันที่:", data['date'], "- เวลา:", data['time'])
                print("- ตำบล:", data['sub_district'], "- อำเภอ:", data['district'], "- จังหวัด:", data['province'])
                print("- อุณหภูมิในกล่อง:", data['temp_in'], "°C")
                print("- อุณหภูมิภายนอก:", data['temp_out'], "°C")
                print("- ความชื้น:", data['hum'], "%")
                print("- ระดับน้ำ:", data['water'], "Cm")
                print("- ฝนสะสมวันนี้:", data['rain24h'], "มม.")
                print("- PM2.5:", data['pm25'], "μg/m³ | PM10:", data['pm10'], "μg/m³")
                print("- แรงดันไฟฟ้า:", data['power'], "V")

                # เตรียมส่งไปยัง Blynk
                blynk_data = {
                    "V1": data['temp_out'],
                    "V2": data['hum'],
                    "V3": data['water'],
                    
                }

                for pin, value in blynk_data.items():
                    res = requests.get(f"{blynk_url}&{pin}={value}")
                    

                # อัปเดต timestamp ล่าสุด
                last_timestamp = timestamp

            else:
                print(f"⏳ ยังไม่มีข้อมูลใหม่ ({timestamp})")

        else:
            print("ดึงข้อมูลไม่สำเร็จ:", response.status_code)
            print(response.text)

    except Exception as e:
        print("เกิดข้อผิดพลาด:", e)

    
    time.sleep(30)
