import requests
class CheckURLToJPG:

    @staticmethod
    def existsURL(path):
        r = requests.head(path)
        return r.status_code == requests.codes.ok