import pandas as pd
import re

def clean_phone_number(phone):
    if pd.isna(phone):
        return None
    # Convert to string to ensure string operations can be performed
    phone = str(phone).strip().replace("+", "").replace(" ", "")
    # Ensure phone number is correctly formatted (e.g., 10-digit number)
    if re.match(r"^\d{10}$", phone):
        return phone
    else:
        return None

def clean_descriptive_field(field_data):
    if pd.isna(field_data):
        return ""
    # Remove special characters
    return re.sub(r'[^A-Za-z0-9\s]', '', str(field_data))

def validate_and_clean_data(df, required_fields):
    bad_records = pd.DataFrame()

    # Validate phone numbers and clean descriptive fields
    df['cleaned_phone'] = df['phone'].apply(clean_phone_number)
    df['cleaned_address'] = df['address'].apply(clean_descriptive_field)
    df['cleaned_reviews_list'] = df['reviews_list'].apply(clean_descriptive_field)

    # Check for null values in required fields
    for field in required_fields:
        if df[field].isnull().any():
            bad_records = pd.concat([bad_records, df[df[field].isnull()]])

    # Remove records with invalid phone numbers or null values in required fields
    df = df.dropna(subset=required_fields + ['cleaned_phone'])

    return df, bad_records

