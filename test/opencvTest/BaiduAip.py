from aip import AipOcr


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


if __name__ == '__main__':
    APP_ID = '15340554'
    API_KEY = 'f3hvVD2AIjs1V4UyEUh8m7UO'
    SECRET_KEY = 'iQiSEk0GY3l57Eu5xkdG2sRRzFkkTrSf'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = get_file_content('grey.png')
    options = {}
    options["language_type"] = "CHN_ENG"
    general = client.basicGeneral(image, options)
    print(general)
