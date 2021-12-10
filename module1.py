from module import*

def countries(d:dict, v:int):
    keys_list=(list(d.key()))
    values_list=(list(d.value()))
    if v=="1":
        mas=[]
        capital=(input("sisesta pealinn: ")).capitalise()
        capital.title()
        for i in values_list:
            if i==capital:
                for i in range(len(value_list)):
                    if values_list[i]==capital:
                        mas.append(int(i))
                        print("riik -", key_list[i],"<->", "pealinn -", values_list[i])
    else:
        country=(input("sisesta riik: ")).capitalise()
        a=d.get(country)
        print("riik -", country ,"<-->", "pealinn -", a)
    return

def new_key_value(d:dict):
    new={}
    country=(input("sisesta riik: ")).capitalise()
    capital=(input("sisesta pealinn: ")).capitalise()
    new={country:capital}

    return d,new
