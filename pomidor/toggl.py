import requests

TOGGL_API = 'https://www.toggl.com/api/v8/'


def get_current_time_entry(api_token):
    endpoint = 'time_entries/current'
    resp = requests.get(
        f'{TOGGL_API}{endpoint}',
        auth=(api_token, 'api_token')
    )
    entry_data = resp.json()
    if entry_data['data'] is None:
        return None
    return entry_data
