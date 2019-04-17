from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import random, io
from googleapiclient.http import MediaIoBaseDownload
import memebase
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive.readonly'


def main():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store,)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10000, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    rand_item = random.choice(items)
    if not items:
        print('No files found.')
    else:
        print('{0} ({1})'.format(rand_item['name'], rand_item['id']))
        request = service.files().get_media(fileId=rand_item['id'])
        if rand_item['name'].endswith('.mp4'):
            name = 'discordfile.mp4'
            memebase.mp4_file = True
        else:
            name = 'discordfile.jpg'
            memebase.mp4_file = False
        fh = io.FileIO(name, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))


if __name__ == '__main__':
    main()
