#!/usr/bin/python3
import os
from models.engine.file_storage import FileStorage

file_path = "file.json"
try:
    file_path = FileStorage._FileStorage__file_path
except:
    pass
try:
    os.remove(file_path)
except Exception as e:
    pass

from models.base_model import BaseModel
from models import storage

try:
    storage._FileStorage__objects.clear()
except:
    pass
ids = []

for i in range(10):
    bm = BaseModel()
    bm.save()
    ids.append(bm.id)
try:
    storage._FileStorage__objects.clear()
except:
    pass
storage.reload()

all_reloaded = storage.all()

if len(all_reloaded.keys()) != len(ids):
    print("Missing after reload")

for id in ids:
    if all_reloaded.get(id) is None and all_reloaded.get("{}.{}".format("BaseModel", id)) is None:
        print("Missing {}".format(id))

try:
    os.remove(file_path)
except Exception as e:
    pass