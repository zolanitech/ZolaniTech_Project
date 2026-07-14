import re
import pandas as pd
import phonenumbers

def clean_name(name):
    return str(name).strip().title()

def clean_phone(phone_str):
    try:
        cleaned_digits = re.sub(r'[\s\(\)\-\.]', '', str(phone_str))
        parsed_num = phonenumbers.parse(cleaned_digits, "ZA")
        if phonenumbers.is_valid_number(parsed_num):
            return phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        return f"INVALID DIGITS: {phone_str}"
    except Exception:
        return f"PARSING ERROR: {phone_str}"

def validate_email(email_str):
    email_clean = str(email_str).strip().lower()
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if ".." in email_clean or "//" in email_clean:
        return f"FLAGGED SYNTAX: {email_str}"
    if re.match(email_regex, email_clean):
        return email_clean
    return f"INVALID SYNTAX: {email_str}"

# Initial sample validation run
data = {
    'Client_Name': ['jAnE dOe', 'john smith'],
    'Phone_Number': ['0821234567', '+27 71 987 6543'],
    'Email_Address': ['JANE.DOE@gmail.com', 'j.smith@company..co.za']
}

df = pd.DataFrame(data)
df['Client_Name'] = df['Client_Name'].apply(clean_name)
df['Phone_Number'] = df['Phone_Number'].apply(clean_phone)
df['Email_Address'] = df['Email_Address'].apply(validate_email)
print(df)
