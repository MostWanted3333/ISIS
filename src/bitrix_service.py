import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

BITRIX_WEBHOOK = os.getenv("BITRIX_WEBHOOK")

role_map = {
    "candidate": 45,
    "Premium":49,
}

def create_bitrix_lead(user):
    url = BITRIX_WEBHOOK + "crm.lead.add.json"

    data = {
        "fields": {
            "TITLE": f"Регистрация пользователя: {user.full_name}",
            "NAME": user.full_name,
            "EMAIL": [
                {
                    "VALUE": user.email,
                    "VALUE_TYPE": "WORK"
                }
            ],
            "UF_CRM_SITE_USER_ID": user.user_id,
            "UF_CRM_1778241273862": user.role,
            "UF_CRM_1778241380580": user.target_position,
            "UF_CRM_1778241510772": 51,
            "UF_CRM_1778241313613":user.created_at.strftime("%Y-%m-%d"),
            "UF_CRM_1778241273862":role_map.get(user.role),
            "UF_CRM_1778241085596":user.user_id
        }
    }

    response = requests.post(url, json=data)

    return response.json()