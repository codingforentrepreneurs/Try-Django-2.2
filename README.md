[![Try Django 2.2 tutorial](https://static.codingforentrepreneurs.com/media/projects/try-django-22/images/share/try_django_2_2_share.jpg)](https://www.codingforentrepreneurs.com/projects/try-django-22)


### Getting Started

#### Requirements
- Python 3.6 & up
- Virtual Environment (pipenv or virtualenv)

#### Recommended Prerequisites
- Coding with macOS (course)
    - https://cfe.sh/courses/coding-with-macOS
- 30 Days of Python (project)
    - https://cfe.sh/projects/30-days-python
- Getting Started with HTML & CSS (project)
    - https://cfe.sh/projects/getting-started-html-css
- Bootstrap Basics (project)
    - https://cfe.sh/projects/bootstrap-basics-v4-3


#### 1. Setup your System
- Windows: https://kirr.co/6r8wr9
- Mac: https://kirr.co/386c7f
- Linux: https://kirr.co/c3uvuu


#### 2. Create Virtual Environment & Install Django
```
cd /path/to/dev/folder
mkdir try_django
cd try_django
pipenv --python 3.6 install django==2.2
pipenv shell
```
> Don't have pipenv? Check out [this guide](https://www.codingforentrepreneurs.com/blog/pipenv-virtual-environments-for-python/)

#### 3. Create Django Project
```
cd /path/to/dev/folder
mkdir src
cd src
django-admin startproject try_django .
```

#### 4. Setup Project in Sublime Text
I've used Sublime Text for a long time. This is optional but recommended as you work through the videos. Download it on https://www.sublimetext.com/


#### Reference & Guides
- Getting started with CFE
    - https://kirr.co/gyxlmi
- System Setup
    - Windows: https://kirr.co/6r8wr9
    - Mac: https://kirr.co/386c7f
    - Linux: https://kirr.co/c3uvuu
- Blank Django Project
    - https://kirr.co/z7s6ls 
- Official Code Repo
    - https://kirr.co/0a7z1n


#### Code by Lesson

1 - 4 _no reference code_

[5 - Define a View](../../tree/7b03eecee7f720828da5151f9a91e75bf463eabf/)

[6 - A First URL Mapping](../../tree/fc9d8317975a3e7d81024b6ff6fa732a7eb4cd51/)

[7 - Multiple Views](../../tree/b62dcde16ead85abf1459302bf9e59c779522e98/)

[8 - path vs re_path vs url](../../tree/c16191c203c3e2a683b159eb00226f0da3f4641a/)

[9 - Your First Template](../../tree/c34a1d1b8274d6a7939b2ae4543a2c3b8408fd42/)

[10 - Loading a HTML Template](../../tree/958e1b2e8419fdb4fe804905b24a9fd3446703d8/)

[11 - Add Bootstrap](../../tree/425d18a9d89f48eab50f5e95ccd4db8cf065db1f/)

[12 - Render Context in Templates](../../tree/657832d7cde0f57e04d009e851bc46928680f195/)

[13 - Stay DRY with Templates](../../tree/591266b2631adfc3e6160c5ad2680ec5539db712/)

[14 - Rendering Any Kind of Template](../../tree/4a99376aa473a8039679634c047595fa4f662870/)

[15 - Template Context Processors](../../tree/748d52618acd0321c4ccdd73caaf76f20a69ca37/)

[16 - Built In Template Tags](../../tree/be3015046ae832eb435de6477887af7958816be4/)

[17 - Your First App](../../tree/46a4dba8143a48017f2beb7b0f003625bc6f1fec/)

[18 - Save to the Database](../../tree/23fcbce14a0dd0e209bb2d24deb012ee1f2796aa/)

[19 - Model to Django Admin](../../tree/da5bc723f26acf7746cd47b87184b5cedfec4244/)

[20 - Model in a View](../../tree/ad5ccafbe6455a8d84b71bc6c8bad50a7885dcd3/)

[21 - Dynamic URL-based Lookups](../../tree/c0eabca39e6464fb53d2724006b69e9beb440504/)

[22 - Handling Dynamic URL Errors](../../tree/3728033641f87b9796c9e43154082f93c52d2e3c/)

[23 - Get Object or 404](../../tree/1354e7b297498ab23df09e4b3ef14a1acb7f3d70/)

[24 - A New Database Lookup Value](../../tree/ada883bb529c6344e749a3c3e4d358cb70e5423e/)

[25 - QuerySet Lookups](../../tree/a0d7125e4b943b4f8d91d7eb7cc5dfefb20e9a22/)

[26 - A Unique Slug](../../tree/d66968d653a3e648ba4990a420ad0465ccdb8980/)

[27 - CRUD and Views](../../tree/8c584df2d6822628653e068d3996c86e76e0d015/)

[28 - CRUD View Outline](../../tree/c3c9e1d11026ede663a0b8cb8a228b2c8163f891/)

[29 - Blog Post List View](../../tree/38c56972032ee299d6726c344055530160de03ce/)

[30 - Routing the Views](../../tree/3c3aef27f2ababa85d8527670bfd8f0806dceaf3/)

[32 - In App Templates](../../tree/1b2c700d6bb04f035e940052c747773d5e6fe67f/)

[33 - Submit Raw HTML Form](../../tree/e3de7adcb32d45c5f1ee5dc59d508286cd097b47/)

[34 - A Django Form](../../tree/c2eee29ceeeb6ce11c4801eddb9bde0051844c74/)

[35 - Saving Data from a Django Form](../../tree/ad4b67a2b2e3ba75cb8869bb67541e611dd36576/)

[36 - Model Form](../../tree/2ba8f4af1de4618d5785870bdab2d85e59a5c9bd/)

[37 - Validate Data on Fields](../../tree/e7e9c05348bea84518fd7d73f6fa920fc255a14d/)

[38 - Login Required](../../tree/d12094fdca9b0aebaa521a85d8dbbefb531faeed/)

[39 - Associate Blog Post to a User with Foreign Keys](../../tree/bdb4b392516d2ff7c013c27a17da9a5954bde932/)

[40 - Logged In User & Forms](../../tree/ddddca8a7d1a7bef5c2ccc9443e9b11f51df2648/)

[41 - Update View with Model Form](../../tree/26e32d754a80991fc0406b1adf32c5a2096fa316/)

[42 - Better Validation on Update Views](../../tree/8db9a124bdfa17b1a4815917e7c2a3c14334f8e4/)

[43 - Delete and Confirm](../../tree/bd6412813ea103f796df4a97d50e7b5c2f829767/)

[44 - Blog Post Navigation](../../tree/7c5818accd96b76cdae596780934c8d7859169b9/)

[45 - Include the Navbar](../../tree/0947604c3dfeaaf612b57170ec1fe4cfd191012e/)

[46 - Include with Arguments](../../tree/69ff77a82a6b3a16480cdd47c73a2c91a05a9109/)

[47 - An Included Template for Consistent Design](../../tree/0a4d1ef220e5e6601617d829714c2a243421a191/)

[48 - Publish Date, Timestamp & Updated](../../tree/9f17efd6a246f986435b6fe59e528f6e48fef7fd/)

[49 - Model Managers and Custom QuerySets](../../tree/31ff0d6c5a49ef5c9e8283d9f354d5cede1888c9/)

[50 - Published and Draft Posts](../../tree/f633fb02000e4b70205b5f8a2f0ef2dc947699de/)

[51 - Static Files and Uploading Files](../../tree/e44cf41eac90e0ddd8b258b9e46d5af520a9b4b2/)

[52 - Image Field and Uploading Images](../../tree/fb9d688f217aca5144275dd516d87f3d6f67cf7f/)

[53 - Putting it All Together](../../tree/85bcd4dfa09e79752e5f1743fb1fbb8cf23e7a7c/)

[54 - Complex Lookups](../../tree/f6e6ba0c222e65cc376758cb2aa4a52b01151f5d/)

