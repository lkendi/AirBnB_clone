#!/usr/bin/python3
"""
Creates a unique storage instance for the app
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
