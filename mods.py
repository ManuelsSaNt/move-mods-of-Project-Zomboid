import os
import shutil
import sys


user = os.path.expanduser('~').split("\\")[2]
dir = "C:/Program Files (x86)/Steam/steamapps/workshop/content/108600"

def main():
  carpetas = os.listdir(dir)

  for carp in carpetas:
    mods = dir + "/" + carp + "/mods/"
    modsArr = os.listdir(mods)
    for mod in modsArr:
      shutil.move((mods + mod), r"C:\Users\{}\Zomboid\mods".format(user))
      print("Se ha movido: {}".format(mod))
  print(""" ya quedo joto
  .
  __._
  _(_|_)
  __|=|
  __|=|
  __|=|__
  (''####')
  """)

  exit = input("Presiona cualquier tecla puto")

if __name__ == '__main__':
  main()