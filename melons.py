import csv

melon_dict = {}

class Melon:
    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url 
        self.color = color
        self.seedless = seedless

    def __repr__(self):
        return(f'<Melon: {self.melon_id} -- {self.common_name}>\n')
        # return(f'Name: {self.common_name} - Price: $ {self.price}\n')

    def price_str(self):
        return f"$ {self.price:.2f}"

    def total_str(self):
        return f"$ {self.total:.2f}"

def melon_finder(id):
    return melon_dict[id]



def list_melons():
    # return melon_dict.values()
    return list(melon_dict.values())


def reader():
    with open('melons.csv') as csvfile:
        all_melons = csv.DictReader(csvfile)
        for melon in all_melons:
            melon_id = melon['melon_id']            
            each_melon = Melon(melon_id, melon['common_name'], float(melon['price']), melon['image_url'], melon['color'],
            eval(melon['seedless']))
            melon_dict[melon_id] = each_melon   # ------------------



if __name__ != "__main__":
    reader()
# reader()
# print(list_melons())
# print(melon_dict)
# print(melon_finder('navw'))