#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tifffile
import cv2
import tkinter as tk
from PIL import Image, ImageTk


# In[4]:


#  this function show the x,y coordinate and  lititude and longitude 
def show_coordinates(event):
    x, y = event.x, event.y
    x_pixel, y_pixel = x, y
    latitude = y / image_height * (max_lati - min_lati) + min_lati
    longitude = x / image_width * (max_longi - min_longi) + min_longi
    x_coord.set(f"X: {x_pixel}")
    y_coord.set(f"Y: {y_pixel}")
    lat.set(f"Latitude: {lati}")
    lon.set(f"Longitude: {longi}")


# In[14]:


import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = "final.jpg"  
satellite_image = cv2.imread(image_path)

image_height, image_width, _ = satellite_image.shape


# In[15]:


#- the latitude and longitude ranges of the image
min_lati, max_lati = 0, 90
min_longi, max_longi = -180, 180


# In[16]:


# Create a Tkinter window
root = tk.Tk()
root.title("Image Coordinates")


# In[18]:


#Convert the OpenCV image to PIL format and then to Tkinter format
satellite_image = cv2.cvtColor(satellite_image, cv2.COLOR_BGR2RGB)
satellite_image = Image.fromarray(satellite_image)
#Resize the image (replace 800 and 600 with desired width and height)
satellite_image = satellite_image.resize((800, 600), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(satellite_image)


# In[19]:


#- Display the image on a Tkinter label
image_label = tk.Label(root, image=tk_image)
image_label.pack()


# In[20]:


#  Create text boxes to display coordinates
x_coord = tk.StringVar()
y_coord = tk.StringVar()
lat = tk.StringVar()
lon = tk.StringVar()


# In[21]:


left_frame = tk.Frame(root)
left_frame.pack(side='left')
x_label = tk.Label(left_frame, textvariable=x_coord)
x_label.pack()


# In[23]:


y_label = tk.Label(left_frame, textvariable=y_coord)
y_label.pack()

right_frame = tk.Frame(root)
right_frame.pack(side='right')


# In[25]:


# Create labels for latitude and longitude and pack them inside the right frame
lat_label = tk.Label(right_frame, textvariable=lat)
lat_label.pack()
lon_label = tk.Label(right_frame, textvariable=lon)
lon_label.pack()


# In[26]:


#  mouse movement event to the image label
image_label.bind('<Motion>', show_coordinates)


# In[ ]:


# Run the Tkinter event loop
root.mainloop()


# In[ ]:




