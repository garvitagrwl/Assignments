import pandas as pd


data = {
    'email': ['garvit@gmail.com', 'invalid-email', 'user@site.co.in'],
    'ph': ['9876543210', '9846543410', '12345'],
    'postal': ['110001', 'A123BC', '560078'],
    'text': ['Hello123', 'OnlyText', '4567']
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

#  Email
df['valid_email'] = df['email'].str.match(r'^[\w\.-]+@[\w\.-]+\.\w+$')

#  India Number Validation
df['valid_phone'] = df['ph'].str.match(r'^\+?91[6-9]\d{9}$')

#  PIN Code
df['valid_postal'] = df['postal'].str.match(r'^\d{6}$')


df['only_text'] = df['text'].str.match(r'^[A-Za-z]+$')


df['numbers_extracted'] = df['text'].str.extract(r'(\d+)', expand=False)

print("\nData with Regex Validations and Extraction:")
print(df)
