# importing pytesseract helps us in converting any image formats to text aka string
from tkinter import *
from tkinter import filedialog

#importing tkinter helps us in using gui buttons and other features
from PIL import Image
#importing pil->pillow enables users to operate on different formates of images
from tesseract import tesseract


# importing filedialog module which helps in  browsing files in directory
# Function for opening the file explorer window 
def browseFiles(): 
    #filedialog.askopenfilename() function helps us to navigate the local directories and choose or needed files
    filename = filedialog.askopenfilename(initialdir = "/", #intialdir helps us to set the initial directory to be none inidicated by slash /
                                          title = "Select a File", # displaying the test in the dialog
                                          filetypes = (("Text files", #choosing the type of file(text,image etc) that needed to be choosed during navigation
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))        
       
    path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR" #we need to give the directory of tessersect ocr which should be download and installed
    image_path = filename                                               #we initiase a variable which contains the directory of image that is selected in filedialog

    img = Image.open(image_path)                                        #with the help of Image.open() function we open the image using the path selected by the user

    # Providing the tesseract executable location to pytesseract library 
    tesseract.tesseract_cmd = path_to_tesseract                       

    # Passing the image object to image_to_string() function 
    # This function will extract the text from the image 
    text = tesseract.image_to_string(img) # text variable contains the text in the image in the form as string which can be accesed by slicing or any other string operation
    
    state=text[:2]                      #creating a variable called state to store the state code

    district=text[3:5]                   #creating a variable called district to store the district code

    #creating a dictionary to store state name along with their state code 

    states={"AN":"Andaman and Nicobar Islands","AP":"Andhra Pradesh","AR":"Arunachal Pradesh",
    "AS":"Assam","BR":"Bihar","CH":"Chandigarh","CG":"Chhattisgarh","DD":"Dadra and Nagar Haveli and Daman and Diu",
    "DL":"Delhi","GA":"Goa","GJ":"Gujarat","HR":"Haryana","HP":"Himachal Pradesh","JK":"Jammu and Kashmir","JH":"Jharkhand",
    "KA":"Karnataka","KL":"Kerala","LA":"Ladakh","LD":"Lakshadweep","MP":"Madhya Pradesh","MH":"Maharastra","MN":"Manipur",
    "ML":"Meghalaya","MZ":"Mizoram","NL":"Nagaland","OD":"Odisha","PY":"Puducherry","PB":"Punjab","RJ":"Rajasthan","SK":"Sikkim",
    "TN":"Tamil Nadu","TS":"Telangana","TR":"Tripura","UP":"Uttar Pradesh","UK":"Uttarkhand","WB":"West Bengal"}
    # Displaying the output in the tkingter box
    label_file_explorer.configure(text="The Vehicle Number:"+text[:-1]+" is registered in "+states[state]+" with district code: "+district) 
       
       
                                                                                                   
# Create the root window 
window = Tk() 
   
# Set window title 
window.title('Plate OCR') 
   
# Set window size 
window.geometry("500x400") 
   
#Set window background color 
window.config(background = "white") 
bg = PhotoImage(file = "download1.png") 
  
# Show image using label 
label1 = Label( window, image = bg) 
label1.place(x = 110, y = 180) 
   
# Create a File Explorer label 
label_file_explorer = Label(window,  
                            text = "Number Plate Recognition", 
                            width = 80, height = 5,fg = "blue") 
   
       
button_explore = Button(window,  
                        text = "Browse Files", 
                        command = browseFiles)  
   
button_exit = Button(window,  
                     text = "Exit", 
                     command = exit)  
   
# Grid method is chosen for placing the widgets at respective positions  in a table like structure by specifying rows and columns 
label_file_explorer.grid(column = 1, row = 1) 
   
button_explore.grid(column = 1, row = 2) 
   
button_exit.grid(column = 1,row = 3) 
   
# Let the window wait for any events 
window.mainloop() 
