import yaml

def read_yaml(filename):
    arr = []
    with open("./data/"+filename,"r",encoding="utf-8")as f:
        for i in yaml.safe_load(f).values():
            arr.append(tuple(i.values()))
        return arr


if __name__ == '__main__':
    # print(read_yaml('mp_login.yaml'))
    # arr = []
    # for i in read_yaml("mp_login.yaml").values():
    #     arr.append(tuple(i.values()))
    # print(arr)
    print(read_yaml("mp_login.yaml"))