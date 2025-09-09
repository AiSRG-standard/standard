Project AiSRG - Official Documentation
Official Website and Latest Version: https://aisrg.org

เอกสารมาตรฐานฉบับร่าง 1.1 (Draft Standard Document 1.1)

บทที่ 1: Introduction (บทนำ)
1.1 What is AiSRG?

AiSRG (Ai Service Reference Guide) คือมาตรฐานกลางแบบเปิด (Open Standard) ที่ทำหน้าที่เป็น "ล่ามภาษาสากล" ระหว่างปัญญาประดิษฐ์ (AI) และผู้ให้บริการดิจิทัล (เช่น เว็บไซต์, แอปพลิเคชัน, หรือระบบต่างๆ)

พูดง่ายๆ AiSRG คือ "คู่มือ" ที่เว็บไซต์สามารถเขียนทิ้งไว้ เพื่อให้ AI ทุกค่ายสามารถเข้ามาอ่านและเข้าใจได้ทันทีว่า "เว็บไซต์นี้ทำอะไรได้บ้าง และจะสั่งงานได้อย่างไร" ซึ่งเป็นการปลดล็อกศักยภาพให้ AI สามารถเปลี่ยนจาก "ผู้ให้ข้อมูล" มาเป็น "ผู้ช่วยลงมือทำ" (AI Agent) ได้อย่างแท้จริง

1.2 Philosophy & Vision

เราเชื่อว่าอนาคตคือโลกที่ มนุษย์, AI, และธุรกิจ สามารถทำงานร่วมกันได้อย่างไร้รอยต่อ วิสัยทัศน์ของ AiSRG คือการสร้างโครงสร้างพื้นฐานที่เปิดกว้างและเป็นประชาธิปไตย ที่ซึ่งผู้ประกอบการรายย่อยก็สามารถทำให้บริการของตน "พร้อมสำหรับ AI" ได้ทัดเทียมกับบริษัทขนาดใหญ่ เป็นการสร้างสรรค์นวัตกรรมที่เกิดจากความร่วมมือระหว่างมนุษย์และ AI เพื่อประโยชน์ของทุกคน

1.3 Core Principles

มาตรฐาน AiSRG ตั้งอยู่บนหลักการสำคัญ 3 ข้อ:

👐 Open (เปิดกว้าง): เป็นมาตรฐานเปิดที่ทุกคนสามารถนำไปใช้ได้ฟรี โดยไม่ขึ้นกับบริษัทใดบริษัทหนึ่ง

📜 Standardized (เป็นมาตรฐาน): มีโครงสร้างและกฎเกณฑ์ที่ชัดเจน ทำให้ AI และผู้ให้บริการเข้าใจตรงกัน

🔒 Secure (ปลอดภัย): มีกลไกการยืนยันตัวตนที่แข็งแกร่ง เพื่อปกป้องทั้งผู้ใช้งานและผู้ให้บริการ

บทที่ 2: Quick Start Guide (คู่มือเริ่มต้นฉบับเร่งรัด)
🏢 สำหรับผู้ให้บริการ (For Business Providers)

อยากทำให้เว็บของคุณ "AI-Ready" ใช่ไหม? ทำตาม 3 ขั้นตอนง่ายๆ นี้ได้เลย:

สร้างไฟล์ Guide: เขียนไฟล์ .json เพื่ออธิบายว่าบริการของคุณทำอะไรได้บ้าง โดยใช้โครงสร้างตามมาตรฐาน AiSRG (ดูรายละเอียดในบทที่ 4)

เพิ่ม Meta Tag: นำ Meta Tag <meta name="aisrg:location" content="/path/to/your-guide.json"> ไปใส่ในหน้าแรกของเว็บไซต์คุณ

เตรียม API: สร้าง API Endpoint ให้พร้อมรับคำสั่งจาก AI ตามที่คุณได้ระบุไว้ในไฟล์ Guide

🤖 สำหรับผู้พัฒนา AI (For AI Developers)

ต้องการให้ AI ของคุณสามารถ "สั่งงาน" เว็บไซต์ต่างๆ ได้ใช่ไหม?

ค้นหา Guide: เมื่อ AI ของคุณเข้าไปที่เว็บไซต์ใดๆ ให้สแกนหา Meta Tag aisrg:location ในโค้ด HTML

อ่านและทำความเข้าใจ: หากเจอ Tag ดังกล่าว ให้ไปดาวน์โหลดและอ่านไฟล์ .json ที่ระบุไว้ เพื่อเรียนรู้ความสามารถทั้งหมดของเว็บนั้น

ดำเนินการตามคำสั่ง: เมื่อผู้ใช้สั่งงาน AI ของคุณก็จะรู้ทันทีว่าจะต้องส่งคำสั่ง (Request) ไปที่ API Endpoint ไหน ด้วยข้อมูล (Parameters) อะไรบ้าง

บทที่ 3: Core Concepts (แนวคิดหลัก)
The Three Pillars of AiSRG

มาตรฐาน AiSRG ถูกสร้างขึ้นจากเสาหลัก 3 ประการที่ทำงานร่วมกันอย่างเป็นระบบ

1. Discovery (การค้นพบ)

หัวใจของการค้นพบคือ Meta Tag ในหน้า HTML (<meta name="aisrg:location" content="...">) ทำหน้าที่เป็น "ป้ายบอกทาง" ให้ AI รู้ว่าเว็บไซต์นี้รองรับมาตรฐาน AiSRG และสามารถไปหาไฟล์คู่มือ .json ได้จากที่ไหน วิธีนี้ให้อิสระแก่ผู้ให้บริการในการตั้งชื่อและจัดเก็บไฟล์คู่มือได้อย่างยืดหยุ่น

2. Specification (สเปก)

ไฟล์ aisrg.json คือ "พิมพ์เขียว" หรือ "สัญญา" ที่อธิบายความสามารถทั้งหมดของบริการอย่างละเอียดและเป็นมาตรฐาน ประกอบด้วยข้อมูลสำคัญ เช่น ข้อมูลผู้ให้บริการ, วิธีการยืนยันตัวตนที่รองรับ, และรายการของ "Actions" ทั้งหมดที่ AI สามารถเรียกใช้งานได้ ความเป็นมาตรฐานนี้ทำให้ AI ทุกค่ายสามารถตีความและทำงานร่วมกันได้อย่างถูกต้อง

3. Security (ความปลอดภัย)

AiSRG ถูกออกแบบโดยคำนึงถึงความปลอดภัยเป็นสำคัญ โดยรองรับกลไกการยืนยันตัวตน 2 รูปแบบหลักคือ OTP (เหมาะสำหรับธุรกรรมที่ต้องการความปลอดภัยสูงเป็นครั้งคราว) และ OAuth 2.0 (เหมาะสำหรับการใช้งานต่อเนื่องและมอบประสบการณ์ที่ดีแก่ผู้ใช้) ผู้ให้บริการสามารถเลือกระดับความปลอดภัยที่เหมาะสมสำหรับแต่ละ Action ได้เอง

บทที่ 4: Specification Reference (รายละเอียดสเปก)
นี่คือรายละเอียดเชิงเทคนิคของทุกองค์ประกอบในไฟล์ aisrg.json

4.1 Root Object

aisrg_version (String, Required): เวอร์ชันของมาตรฐาน AiSRG ที่ไฟล์นี้อ้างอิง (เช่น "1.1")

provider (Object, Required): ข้อมูลเกี่ยวกับผู้ให้บริการ

verification (Object, Optional): กลไกการยืนยันความเป็นเจ้าของโดเมน

authentication (Object, Required): ประกาศวิธีการยืนยันตัวตนที่รองรับ

actions (Array, Required): รายการของ "Action" ทั้งหมดที่บริการนี้ทำได้

4.2 The verification Object

method (String, Required): วิธีการยืนยันตัวตนที่ใช้ ปัจจุบันรองรับ "dns-txt"

proof (String, Required): "หลักฐาน" ที่ใช้ในการยืนยัน เช่น aisrg-verification=your-unique-string

4.3 The authentication Object

methods_supported (Array of Strings, Required): รายการวิธีการที่รองรับ ("otp", "oauth2")

otp_endpoint (String, Conditional): URL สำหรับร้องขอ OTP

oauth2_endpoint (String, Conditional): URL สำหรับเริ่มกระบวนการ OAuth 2.0

4.4 The action Object

action_id (String, Required): ชื่อเฉพาะของ Action

description (String, Required): คำอธิบายว่า Action นี้ทำอะไร

security_level (String, Required): ระดับความปลอดภัยที่ต้องการ ("none", "otp_required", "oauth2_required", "oauth2_preferred")

endpoint (String, Required): URL ปลายทางของ API สำหรับ Action นี้

method (String, Required): HTTP Method ที่ต้องใช้ ("GET", "POST", etc.)

parameters (Array of Objects, Optional): รายการข้อมูลที่จำเป็นสำหรับ Action นี้

responses (Object, Required): ตัวอย่างข้อความตอบกลับสำหรับกรณีสำเร็จและล้มเหลว

4.5 The parameters Object

name (String, Required): ชื่อของพารามิเตอร์

type (String, Required): ประเภทข้อมูล ("string", "integer", "array", etc.)

required (Boolean, Required): ระบุว่าจำเป็นต้องมีพารามิเตอร์นี้หรือไม่

description (String, Required): คำอธิบายพารามิเตอร์

format (String, Optional): รูปแบบข้อมูลเฉพาะ เช่น "YYYY-MM-DD"

4.6 The responses Object

success (String, Required): ข้อความตอบกลับเมื่อสำเร็จ สามารถใช้ตัวแปร {...} ได้

failure (String, Required): ข้อความตอบกลับเมื่อล้มเหลว สามารถใช้ตัวแปร {...} ได้

บทที่ 5: Security Guide (แนวทางด้านความปลอดภัย)
5.1 การยืนยันตัวตน "ผู้ใช้งาน" (User Authentication)

OTP Flow: ใช้สำหรับธุรกรรมสำคัญเป็นครั้งคราว โดยระบบจะส่งรหัสผ่านใช้ครั้งเดียวไปยังผู้ใช้เพื่อยืนยันตัวตน

OAuth 2.0 Flow: ใช้สำหรับการใช้งานต่อเนื่อง ผู้ใช้ทำการ Login และให้ความยินยอมเพียงครั้งแรก จากนั้น AI Agent จะใช้ Access Token ที่ได้รับในการยืนยันตัวตนครั้งถัดไป

5.2 การยืนยันตัวตน "ผู้เรียกใช้ API" (Client/Agent Authentication)

เพื่อป้องกันการโจมตีจากสคริปต์ที่ไม่หวังดี ระบบ AiSRG แนะนำให้ใช้กลไกการยืนยันตัวตนของผู้เรียกใช้ด้วย Asymmetric Cryptography (เช่น JWT ที่มีการลงนามดิจิทัล) ซึ่ง AI Agent แต่ละค่ายจะต้อง "เซ็นชื่อ" กำกับคำขอ API ด้วย Private Key ของตนเอง และผู้ให้บริการสามารถใช้ Public Key ที่เผยแพร่ทั่วไปในการตรวจสอบลายเซ็นนั้นได้

5.3 Best Practices ทั่วไป

การสื่อสารทั้งหมดระหว่าง AI และ API Endpoint ต้องเป็น HTTPS เท่านั้น

ควรมีการจัดการข้อผิดพลาดและแจ้งสถานะให้ AI ทราบอย่างชัดเจน

5.4 การยืนยันตัวตนผู้ให้บริการ (Provider Identity Verification)

เพื่อป้องกันการหลอกลวง (Phishing) จากเว็บไซต์ปลอมที่สร้างไฟล์ aisrg.json เลียนแบบบริการของจริง มาตรฐาน AiSRG ได้เพิ่มกลไกการยืนยันความเป็นเจ้าของโดเมนเข้ามา

หลักการ: มีเพียงเจ้าของโดเมนตัวจริงเท่านั้นที่สามารถแก้ไข DNS Record ของโดเมนนั้นได้

วิธีการ:

สร้างหลักฐาน: ผู้ให้บริการเพิ่ม TXT Record ที่มีค่าเฉพาะลงใน DNS ของโดเมนตนเอง

ประกาศหลักฐาน: นำค่า TXT Record นั้นมาใส่ไว้ในอ็อบเจกต์ verification ภายในไฟล์ aisrg.json

AI ตรวจสอบ: AI Agent จะทำการสอบถาม DNS ของโดเมนนั้นๆ เพื่อเปรียบเทียบว่าค่า TXT Record ตรงกับที่ประกาศไว้ในไฟล์ json หรือไม่ หากตรงกันจึงจะถือว่าเป็นบริการที่น่าเชื่อถือ

บทที่ 6: Examples & Use Cases
6.1 Full Example: "Coffe Zoo"

นี่คือตัวอย่างไฟล์ aisrg.json ฉบับสมบูรณ์สำหรับร้านกาแฟ "Coffe Zoo" (v1.1) ที่มีการเพิ่มกลไก verification เข้ามา

{
  "aisrg_version": "1.1",
  "provider": {
    "name": "Coffe Zoo",
    "website": "[https://coffezoo.com](https://coffezoo.com)"
  },
  "verification": {
    "method": "dns-txt",
    "proof": "aisrg-verification=a-very-unique-and-random-string-generated-by-coffezoo"
  },
  "authentication": {
    "methods_supported": ["otp", "oauth2"],
    "otp_endpoint": "[https://api.coffezoo.com/v1/auth/request-otp](https://api.coffezoo.com/v1/auth/request-otp)",
    "oauth2_endpoint": "[https://api.coffezoo.com/v1/auth/oauth2](https://api.coffezoo.com/v1/auth/oauth2)"
  },
  "actions": [
    {
      "action_id": "view_menu",
      "description": "ดูเมนูเครื่องดื่มและอาหารทั้งหมดของร้าน",
      "security_level": "none",
      "endpoint": "[https://api.coffezoo.com/v1/menu](https://api.coffezoo.com/v1/menu)",
      "method": "GET",
      "parameters": [],
      "responses": {
        "success": "นี่คือเมนูแนะนำของเราค่ะ: {menu_items}",
        "failure": "ขออภัยค่ะ ไม่สามารถเรียกดูเมนูได้ในขณะนี้"
      }
    }
  ]
}

