# Numberplate-Recognition
This repository contains a Number Plate Recognition project implemented in Python using Tesseract OCR. The application leverages Tkinter for GUI-based file browsing and displays the extracted vehicle registration details. The program identifies the state and district from the vehicle number plate and maps them to their respective locations using a pre-defined dictionary.

# Overview

## Number Plate Recognition: 
An application to extract text (vehicle registration numbers) from images using Tesseract OCR.
## GUI-Based Interface: 
Built with Tkinter, allowing users to browse and select images of number plates easily.
## State and District Identification: 
Extracts state and district codes from the vehicle number and maps them to their respective locations.

# Features

## Optical Character Recognition (OCR): 
Utilizes Tesseract OCR to convert text in images into a readable string.
## User-Friendly GUI: 
Allows users to select images using a file explorer integrated with Tkinter.
## Location Mapping: 
Maps state and district codes in the number plate to Indian states and districts.
## Dynamic Output: 
Displays extracted number plate text and its corresponding location in the GUI.

# Tech Stack

## Python: 
Core language for application logic and GUI development.
## Tesseract OCR: 
For extracting text from the number plate images.
## Tkinter: 
For building the graphical user interface.
## Pillow (PIL): 
To handle and manipulate image files in Python.

# How It Works

## Browse Image: 
Users select a number plate image using the file explorer in the GUI.
## OCR Processing: 
The selected image is passed to Tesseract OCR to extract text.
## State and District Identification: 
The first 4 characters of the extracted text are parsed to identify the state and district.
## Result Display: 
The number plate text and its corresponding state and district names are displayed in the GUI.
