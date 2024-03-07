#!/usr/bin/python3
"""
creates a unique storage instance for the app
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()