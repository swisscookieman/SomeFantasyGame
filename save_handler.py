import image_printer as image_printer
import printing_utility as pu
import save_template
import json

savepath = "data/local/save.json"

def new(savepath):
    f = open(savepath, "w")
    f.write(save_template)

