import pandas as pd

# Membuat DataFrame dari dictionary
data = {
    'Nama': ['John', 'Doe', 'Bob', 'Alice'],
    'Usia': [23, 23, 44, 12],
    'Pekerjaan': ['Engineer', 'Teacher', 'Doctor', 'Student']
}

df = pd.DataFrame(data)

# Menampilkan DataFrame
print(df)