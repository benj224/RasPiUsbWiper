def format_device(file_system, log_file):
    ##import librarys
    from log import Log
    import subprocess


    ##write to the log file
    Log(log_file,'format_device sucsesfully called\n')
    Log(log_file,'Seraching for usb device location\n')

    ##find the location of the name of the device
    devices = str(subprocess.check_output(['df -h'], shell = True))
    devices = devices.replace("b'", '')
    devices = devices.replace("\\n'", '')
    path_pos = devices.find('/dev/sd')
    str_length = len(devices)


    ##itterate through the charachters of the location an append them to a string
    path = ''
    for x in range(path_pos, (path_pos+9)):
        letter = devices[x]
        path = path + letter
        print (path)

    ##output the found name to the log file    
    Log(log_file,'Usb location found:%s\n'%path)

    
    ##unmount the device
    unmt_str = ('sudo umount %s'%path)
    unmt = subprocess.check_output([unmt_str], shell = True)
    print(unmt)
    Log(log_file,'Ran command (sudo umount %s) and got the responce:\n(%s)\n\n'%(path, unmt))


    ##check which file system the user    
    if file_system == 'exFAT':
        wipe_str = ('sudo mkfs.exfat %s'%path)
        wipe = subprocess.check_output([wipe_str], shell = True)
        print('formated with EXT4')
        print(wipe)
        Log(log_file,'Ran command (sudo mkfs.exfat %s) and got the responce:\n(%s)\n\n'%(path, wipe ))
    elif file_system == 'NTFS':
        wipe_str = ('sudo mkfs.ntfs %s'%path)
        wipe = subprocess.check_output([wipe_str], shell = True)
        print('formated with NTFS')
        print(wipe)
        Log(log_file,'Ran command (sudo mkfs.ntfs %s) and got the responce:\n(%s)\n\n'%(path, wipe ))
    else:
        wipe_str = ('sudo mkfs.vfat %s'%path)
        wipe = subprocess.check_output([wipe_str], shell = True)
        print('formated with VFAT')
        print(wipe)
        Log(log_file,'Ran command (sudo mkfs.vfat %s) and got the responce:\n(%s)\n\n'%(path, wipe ))


    ##attempt to make a directory to mount the usb 
    try:
        Log(log_file,'Attempting to make directory for device to remount\n')
        mkdir_str = ('mkdir /home/pi/Desktop/USB')
        mkdir = subprocess.check_output([mkdir_str], shell = True)
        print(mkdir)

        
    ##if the directory all ready exists skip 
    except:
        Log(log_file,'Directory all ready exists skipping creation\n')
        pass


    ##mount the usb to the directory created
    mnt_str = ('sudo mount %s /home/pi/Desktop/USB'%path)
    mnt = subprocess.check_output([mnt_str], shell = True)
    print(mnt)
    Log(log_file,'Ran command (sudo mount %s /home/pi/Desktop/USB) and got the responce:\n(%s)\n\n'%(path, mnt))

    
##def find_device():
##    import subprocess
##    
##    devices = str(subprocess.check_output(['sudo fdisk -l'], shell = True))
##    devices = devices.replace("b'", '')
##    devices = devices.replace("\\n'", '')
##    path_pos = devices.find('/media/pi/')
##    str_length = len(devices)
##    
##    device_path = ''
##    for x in range(path_pos, str_length):
##        letter = devices[x]
##        device_path = device_path + letter
##    return device_path
##s = find_device()  
##print(s)



##import subprocess
##devices = str(subprocess.check_output(['df -h'], shell = True))
##print(devices)
##time.sleep(5)
##devices = devices.replace("b'", '')
##pathPos = devices.find('/dev/sda')
##print(pathPos)
##time.sleep(5)
##pathLength = pathPos + 10
##path = ''
##for x in range(pathPos, pathLength):
##    letter = devices[x]
##    path = path + letter
##    
##print(path)
##
##    
##format_device('VFAT', path)



            

        
        

