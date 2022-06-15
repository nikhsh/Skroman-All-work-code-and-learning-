import json
import requests
headers = {"Authorization": "Bearer ya29.A0ARrdaM8i5mZ-7ZEWkYqwpaYICM39o7D7GPhLq3O_D9n0Fvcy9Sej5qDXsXsLRTNMBtvrtGz1qTjeqxHiEw5sxWh_la6OSULwBhCPxBOT3Nr74xYiDJqaWp-SndYiWZ6MblVsPFhzlhezhZO5eG_Q18PenkOEYUNnWUtBVEFTQVRBU0ZRRl91NjFWbE42ZHdHbTViXzFFTzRiYlZQVHZ5Zw0163"}
para = {
    "name": "",
    "parents": ["1mLagEQwLXNinWWxOC1lOoEl6CwUswMpM"]
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
