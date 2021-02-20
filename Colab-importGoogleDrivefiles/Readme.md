<h1 align="center">USEFUL TIPS 1 - COLAB AND DRIVE</h1>
<div align="center">
  <p>
    <strong>How to import google drive files to colab?</strong>
  </p>
</div>

## What was the problem?
Well, as everyone knows, google drive is an amazing file storage and synchronization service, where we can use it to store our datasets, even scripts (some people use one drive too, such as myself).

So, it happens that I had a "DBF" file on my google drive account, but I needed to access its content. I know what you are thinking, why I didn't use Excel for that? Good point, but I needed the collab for that, more specifically, Python Language and all PyData Stack incredible functionalities. 
The question that remained was: How can I access that file?

First thing first, Google Drive requires authentication to read, save and move files.

To do that, we need an authorization function that allows us to connect collab to our google drive account. We can do that by using the "auth()" function from "google.colab".
Once the authorization code is created, we will need the authentication client to read our files. For that, there is the PyDrive package.

Now we are ready to read our "DBF" file from google drive.

You can see the script in this repository!


