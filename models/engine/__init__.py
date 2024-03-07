from file_storage import FileStorage

file_path = "file.json"

storage = FileStorage(file_path, objects={})
storage.reload()