import tomli
import os


def op():
    f = open("config.toml", "rb")
    toml_dict = tomli.load(f)
    print(toml_dict)
    h = toml_dict.get('window').get('height')
    w = toml_dict.get('window').get('weight')
    os.system('mode con cols=' + w + 'lines=' + h)


if __name__ == '__main__':
    op()
