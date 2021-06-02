# Certitude App
This is a product developed to make certificates for a huge pool of people by fetching data from excel and directly sending them over email.
Visit the website [here](https://certitude.community.techalier.com/)
### Curated & Modified by:- Parjanya Modi & Sumedh D Karanth.

# Guideline
## HOW TO GET STARTED:
1. Please navigate to [https://certitude.community.techalier.com/](https://certitude.community.techalier.com/)
2. Click on the "Get Certitude" button.
3. A zip folder, with the name "certitude.zip" will be downloaded by default in your "Downloads" directory.
4. Extract all the contents of this zip file in the same directory.
5. Open the certitude folder.

## HOW TO USE:
1. Once you have successfully donwloaded and unzipped the certitude folder, follow the following steps to create custom certificates.
2. Paste the .png or .jpg or .jpeg file of the certificate template in the certitude folder.
3. Paste the excel sheet of the names and email ids of the participants of your event. Make sure that the name of the column are "Name" and "Email" respectively.
4. Now to run the CLI app, refer to the Operating System based instructions given below.



### Windows OS
1. Get the latest exe file from release and use it on your computer. No extra installations required for windows computer.

### Non Windows OS (Linux/MacOS)
1. Open the terminal the type in the follow command:
For Example:- 
```cli
cd Downloads/certitude/
```
4. It is necessary to have python installed on your system.
    > Install python from following link [https://www.python.org/downloads/](https://www.python.org/downloads/)
    > Or install using cli with the following command:
    ```cli
    sudo apt-get install python3
    sudo apt-get install pip3
    ```
5. Run the following command in the terminal
```cli
pip install -r requirements.txt
```
6. Once the requirements are installed, Run the python file by the following command
```cli
python certitudecli.py
```
