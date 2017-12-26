import os,configparser

# BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = os.path.dirname(__file__)
config = configparser.ConfigParser()

te_conf = os.path.join(BASE_DIR,'test.conf')
config.read(te_conf)

print te_conf
print config.get("ride","car")
print config.sections()

config.set("ride","plane","airbus380")

config.write(open(te_conf, "w"))