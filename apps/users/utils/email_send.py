from users.models import EmailVerifyRecord
import random
from django.core.mail import send_mail

def random_str(length):
    str = ''
    seed = 'skjadhsauihfh1849uy12he232'
    for i in range(length):
        random_index = random.randint(0, len(seed) - 1)
        str += seed[random_index]
        return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == 'register':
        email_title = '慕学在线注册激活'
        email_body = '请点击下面的链接激活你的账号：http://127.0.0.1:8000/active{0}'.format(code)

