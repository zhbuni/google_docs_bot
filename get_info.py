import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'cred.json'
spreadsheet_id = '1IdowxOyuKo_hwAn2vlJeqGQI2tg2fBUAC3OOMRW4LYw'


def get_info(name):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build('sheets', 'v4', http = httpAuth)

    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='Общежитие № 6',
        majorDimension='COLUMNS'
    ).execute()
    index = values['values'][1].index(name)
    status = values['values'][2][index]
    return status
