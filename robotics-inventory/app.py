# app.py
#------------------imports----------------------
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3, os, time, json, threading
from datetime import datetime

import cv2
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

DB_FILE = "inventory_cv.db"
MODEL_FILE = "model.h5"
CLASSES_FILE = "classes.json"
IMG_SIZE = 128        # must match training size

# ------------------ DB helpers ------------------
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            label TEXT UNIQUE,
            quantity INTEGER DEFAULT 0,
            location TEXT
        )
    """)
