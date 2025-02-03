import frappe
from frappe.utils.csvutils import to_csv
from frappe.utils.file_manager import save_file
from frappe.utils import now_datetime

def daily():
    send_daily_email_report()


def send_daily_email_report():
    data_rows = fetch_user_login_stats()
    csv_content, filename = generate_csv(data_rows)

    if not csv_content:
        return

    file = save_csv_file(csv_content, filename)

    recipient = frappe.db.get_single_value("Daily Login Report Settings", "email")
    frappe.sendmail(
        recipients=recipient,
        subject=f"Daily Login Stats - {now_datetime().strftime('%Y-%m-%d')}",
        message="Attached are today's login statistics.",
        attachments=[{"file_url": file.file_url}]
    )


def fetch_user_login_stats():
    users = frappe.get_all(
        "User",
        filters={"enabled": 1},
        fields=["name", "first_name", "last_name"]
    )

    data_rows = []
    for user in users:
        success_logins = frappe.db.count("Activity Log", {
            "user": user.name,
            "operation": "Login",
            "status": "Success"
        })

        data_rows.append([
            user.first_name or "",
            user.last_name or "",
            success_logins
        ])
    
    return data_rows


def generate_csv(data_rows):
    if not data_rows:
        return None, None

    headers = ["First Name", "Last Name", "Number of Login Attempts"]
    csv_data = [headers] + data_rows

    csv_content = to_csv(csv_data)
    today = now_datetime().strftime("%Y-%m-%d")
    filename = f"user_login_stats_{today}.csv"

    return csv_content, filename


def save_csv_file(csv_content, filename):
    return save_file(
        filename,
        csv_content.encode("utf-8"),
        "File",
        "Home/Attachments",
        is_private=1
    )
