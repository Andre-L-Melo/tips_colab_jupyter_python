# -*- coding: utf-8 -*-

# To read DBF files:
!pip install dbfread

from dbfread import DBF

# Create Google Auth:
!pip install PyDrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()

gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# This ID you get from your file URL (share the file, get the link, 
# extract the id after "...file/d/" and before ".../view")
# original share link: 
# https://drive.google.com/file/d/this_is_your_file_id/view?
downloaded = drive.CreateFile({'id':"insert_your_file_id"})   
# Rename the file:
downloaded.GetContentFile('do_data.dbf')

# Read DBF file:
table = DBF('do_data.dbf', load = True)

import pandas as pd

table = pd.DataFrame(table)

table.head(10)
