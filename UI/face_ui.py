#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:24:20 2023

@author: ada-eze
"""

import streamlit as st
import cv2
from faceapp import detect_faces, face_cascade,cap

def main():
    
    st.title('Face Detection App')
    
    
    detect_faces()
    
    
    
    
    

if __name__ == '__main__':
    main()
    
