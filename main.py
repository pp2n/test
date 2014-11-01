# -*- coding: utf-8 -*-

'''
Created on 29.08.2014

@author: User
'''



import csv
import os

class utCompl:
    def __init__(self):
        self.utName = u''
        self.utSize = u''
        self.utPath = u''



def tsvTest1(tsvFile = ''):
    with open(tsvFile,'rb') as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"): #You can also use delimiter="\t" rather than giving a dialect.
            print line

def tsvTest2(tsvFile = 'Pack.txt'):
    tsvNames = []
    reader = csv.DictReader(open(tsvFile, 'rb'), delimiter='\t')
    for row in reader:
        #do something more useful here
        
#         print row
#         
#         print row.get('Status')
#         print row.get('Name')
#         
#         return
        utItem = utCompl()
        utItem.utName = row.get('Name')
        utItem.utSize = row.get('Size')
         
#         print utItem.utName        
#         print utItem.utSize
 
        tsvNames.append(utItem)
#



    return tsvNames

def walkDir(pathWork, rec = 0):
    
    fileList = []  
    dirList = []  


    for name in os.listdir(pathWork):
        path = os.path.join(pathWork, name)
        
#       print name
        if os.path.isfile(path):    # если это файл (а не директория)
#           print path              # делаем что-нибудь с ним
            fileList.append(path)
            path
#

        if os.path.isdir(path):     # если это директория (а не файл)
#             print name              # делаем что-нибудь с ним
            dirList.append(path)
#

            if rec == 1:
                dirs, files = walkDir(path, rec)
                
                for f in files:
                    fileList.append(f)
                    f
                
                for d in dirs:
                    dirList.append(d)
# 
                 
#           relPath = os.path.relpath(name, pathWork)
#           print relPath
#             
            
#           lst2.write(relPath)
#
            path
#
    
#   return (pathWork, dirList, fileList)
    return (dirList, fileList)
#



def findFile(path = '.', fileExt = '.py'):
    for dirname, dirnames, filenames in os.walk(path):
        # print path to all filenames with extension py.
        for filename in filenames:
            fname_path = os.path.join(dirname, filename)
            fext = os.path.splitext(fname_path)[1]
            if fext == fileExt:
                print fname_path
            else:
                continue

def findDir(path = '.', dirName = r'.settings', dirnamess = []):

#     dirnames, filenames = walkDir(path)
    
    
    #os.walk(path):
    # print path to all filenames with extension py.
    for dirr in dirnamess:
#             print 'Dir: ' + dirr
        
        dir_n = os.path.basename(dirr)
        fileName, fileExtension = os.path.splitext(dir_n)
        
#         if fileExtension == '.torrent' or fileExtension == '.loaded':
#             return None
        
#
        
        fname_path = os.path.join(path, dir_n)
#             fext = os.path.splitext(fname_path)[1]
#         if dir_n == dirName:
#         if dir_n.find(dirName) != -1 and len(dir_n) == len(dirName):    
        if dir_n.find(dirName) == 0 and len(dir_n) == len(dirName):
            
            print 'Find: ' + dir_n
#                 print fname_path
            return fname_path
        else:
            continue
    
#     print dirName + ' - Not found!'
    return None



import shutil

# tsvFile = 'Pack8.txt'



def tsvProc1(tsvFile = '', utTmpPath = '', utComplPath = ''):
    utItems = []
    
    
    
    if(tsvFile == ''):
        return
    
    
    ff_t = open(tsvFile + '.t', 'wb')
    ff_f = open(tsvFile + '.f', 'wb')
    
#     ff_t.write(r'h:\tmp\torrentCompl\WinX.DVD.Ripper.Platinum.v7.5.6.b.07.04.14.Multilanguage-LAXiTY' + '\n')
#     ff_t.write(r'h:\tmp\torrentCompl\WinX.DVD.Ripper.Platinum.v7.5.6.b.07.04.14.Multilanguage-LAXiTY' + '\n')
    
#     return
    
#     print 'привет'
#     tsvTest1()

    utItems = tsvTest2(tsvFile)
    
    print 'Walk...'
#     walk_r = os.walk(utTmpPath)
    
    dirnames, filenamess = walkDir(utTmpPath)
    
#     for d in dirnames:
#         print os.path.basename(d)
    
#     return
    
    
    #     for utItem in utItems:
    
    
    print 'Find Files...'
#     for utItem in utItems:
    
    killTorrList = []
    
    for utItem in utItems:
        tn = utItem.utName
        print 'Find: ' + tn
        
        
        for f in filenamess:
    #         print f
            
#             killTorrList.append(f)
            
            bn = os.path.basename(f)
    #         print bn
        
            fileName, fileExtension = os.path.splitext(bn)
    #         print fileExtension
            
            
            
            if fileExtension == '.torrent' or fileExtension == '.loaded':
#                 print bn
            
                if fileName.find(tn) != -1:
                    print 'Kill: ' + f
                                        
                    if os.path.isfile(f):
#                         os.remove(f)
                        shutil.move(f, utComplPath)
                        
                        
                        
#                         filenamess.remove(f)
#                         continue
                        
                    else:    ## Show an error ##
                        print("Error: %s file not found" % f)
                    
#                     killTorrList.append(f)

                    

                        
                    
                    continue
                    
    
#     for myfile in killTorrList:
#         
#         
#         if os.path.isfile(myfile):
#             os.remove(myfile)
#         else:    ## Show an error ##
#             print("Error: %s file not found" % myfile)
        
#         os.remove(f)
        
        
        
#     return
    
    
    print 'Find Items...'
    for utItem in utItems:
#         print utItem.utName
#         print utItem.utSize

        print 'Item: ' + utItem.utName

        findPath = None
        findPath = findDir(path = utTmpPath, dirName = utItem.utName, dirnamess = dirnames)
        if(findPath):
#             print findPath
            utItem.utPath = findPath
#
    
        findPath = None
        findPath = findDir(path = utTmpPath, dirName = utItem.utName, dirnamess = filenamess)
        if(findPath):
#             print findPath
            utItem.utPath = findPath
       
        
    

    print 'Move Items...'
    for utItem in utItems:
        if utItem.utPath == '':
            print 'Fail: ' + utItem.utName
            
            ff_f.write(utItem.utName + '\n')
            pass
        else:
#             print utItem.utName
  
            dst_dir = os.path.join(utComplPath, utItem.utName)
#             print dst_dir
  
            if not os.path.exists(dst_dir):
                print 'Move: ' + dst_dir

                ff_t.write(utItem.utName + '\n')

#                 print os.path.normpath(dst_dir)
#                 print os.path.
                
#                 os.mkdir(os.path.normpath(dst_dir))
#                 os.makedirs(dst_dir)
#

                shutil.move(utItem.utPath, dst_dir)
            pass
            
  
  
#     print 'Exit'
#     findFile(path = '.', fileExt = '.txt')
#     findDir(path = utTmpPath, dirName = 'ZZ_Top-The_Very_Baddest_Of-2CD-FLAC-2014-JLM')

def pathConv(path):
    return path.encode('utf8').decode(sys.stdout.encoding)

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
    

def itemJoin(ll = [], utComplPath = ''):
    
    v = 0
    itemCnt = -1
    
#     fsEnc = sys.getfilesystemencoding()
#     myEnc = 'utf-8'
    
    for li in ll:
#         print 'Orig: ' + itemPath
        
#         print fsEnc 
        
# #         if os.path.exists(itemPath.encode(myEnc).encode(fsEnc)):
# #             print 'Exxt1'
# #          
# #         if os.path.exists(itemPath.encode(fsEnc)):
# #             print 'Exxt2'
# #         
# #         if os.path.exists(itemPath):
# #             print 'Exxt3'
# 
#         if os.path.exists(itemPath.encode('utf8').decode(sys.stdout.encoding)):
#             print 'Exxt4-1'
            
#         if os.path.exists(pathConv(itemPath)):
#             print 'Exxt4-2'
# # 
            
#         continue
        
        itemPath = pathConv(li)
        
        
#         if os.path.exists(itemPath):
#             print 'Exxt4-2'
          
#         print itemPath
#         continue
        
        if os.path.exists(itemPath):
            itemCnt += 1
            if v == 1:
                if os.path.isdir(itemPath):
                    print 'Dirr: ' + itemPath
                else:
                    print 'File: ' + itemPath
#
            
            itemName = os.path.basename(itemPath)
#             print 'Name: ' + itemName
            
            cmplPath = os.path.join(pathConv(utComplPath), itemName)
            cmplDirrPath = os.path.join(pathConv(utComplPath), os.path.join(pathConv('Dirr'), itemName))

            if os.path.exists(cmplPath):
                print 'Exxt: ' + cmplPath
                cmplPath = cmplDirrPath
                
            print 'Move: ' + itemPath
#             print 'Cmpl: ' + cmplPath
            
            
            ensure_dir(cmplPath)
            shutil.move(itemPath, cmplPath)
#
    return itemCnt
        
                
                    

def tsvProc2(tsvFile = '', utWorkPaths = [], utTorrPaths = [], utComplPath = ''):
#     utItems = []
    
    v = 0
    
    if(tsvFile == ''):
        return

    ff_t = open(tsvFile + '.t', 'wb')
    ff_f = open(tsvFile + '.f', 'wb')
    
    utItems = tsvTest2(tsvFile)
    
    print 'Find Items...'
    for utItem in utItems:
#         print utItem.utName
#         print utItem.utSize

        print 'Item: ' + utItem.utName

        findPath = None

#         if v == 1:
#             print 'Path: ' + itemPath
        
#-------------------------------------------------------------------------------

#         llWork = {
#         os.path.join(utWorkPath, utItem.utName),   
#         os.path.join(utWorkPath, utItem.utName + '.!ut'),  
#         }
#         
#         llTorr = {
#         os.path.join(utTmpPath, utItem.utName + '.torrent'),
#         os.path.join(utTmpPath, utItem.utName + '.torrent.loaded'),
#         os.path.join(utTmpPath, utItem.utName + '.!ut'),
#         
#         os.path.join(utTmpPath2, utItem.utName + '.torrent'),
#         os.path.join(utTmpPath2, utItem.utName + '.torrent.loaded'),
#         os.path.join(utTmpPath2, utItem.utName + '.!ut'),
#         
#         os.path.join(utTrrPath, utItem.utName + '.torrent'),
#         os.path.join(utTrrPath, utItem.utName + '.torrent.loaded'),
#         os.path.join(utTrrPath, utItem.utName + '.!ut'),
#         }
#-------------------------------------------------------------------------------
        
        llWork = []
 
        for utWorkPath in utWorkPaths:
#             print utWorkPath
 
            llWorkItems = {
            os.path.join(utWorkPath, utItem.utName),   
            os.path.join(utWorkPath, utItem.utName + '.!ut'),  
            }
#             print llWorkItems
             
            for llWorkItem in llWorkItems:
#                 print llWorkItem
                llWork.append(llWorkItem)
#
 
#         for llWorkItem in llWork:
#             print llWorkItem
#-------------------------------------------------------------------------------

        llTorr = []

        for utTorrPath in utTorrPaths:
#             print utTorrPath

            llTorrItems = {
            os.path.join(utTorrPath, utItem.utName + '.torrent'),
            os.path.join(utTorrPath, utItem.utName + '.torrent.loaded'),
            os.path.join(utTorrPath, utItem.utName + '.!ut'),
            
            os.path.join(utTorrPath, utItem.utName + '.1.torrent'),
            os.path.join(utTorrPath, utItem.utName + '.1.torrent.loaded'),

            os.path.join(utTorrPath, utItem.utName + '.2.torrent'),
            os.path.join(utTorrPath, utItem.utName + '.2.torrent.loaded'),
            
            os.path.join(utTorrPath, utItem.utName + '.3.torrent'),
            os.path.join(utTorrPath, utItem.utName + '.3.torrent.loaded'),
            
            os.path.join(utTorrPath, utItem.utName + '.4.torrent'),
            os.path.join(utTorrPath, utItem.utName + '.4.torrent.loaded'),
            
            os.path.join(utTorrPath, utItem.utName + '.5.torrent'),
            os.path.join(utTorrPath, utItem.utName + '.5.torrent.loaded'),
            
            os.path.join(utTorrPath, utItem.utName + '.6.torrent'),
            os.path.join(utTorrPath, utItem.utName + '.6.torrent.loaded'),
            
            os.path.join(utTorrPath, utItem.utName + '.7.torrent'),
            os.path.join(utTorrPath, utItem.utName + '.7.torrent.loaded'),
            
            os.path.join(utTorrPath, utItem.utName + '.8.torrent'),
            os.path.join(utTorrPath, utItem.utName + '.8.torrent.loaded'),
            
            os.path.join(utTorrPath, utItem.utName + '.9.torrent'),
            os.path.join(utTorrPath, utItem.utName + '.9.torrent.loaded'),
            }
#             print llTorrItems
            
            for llTorrItem in llTorrItems:
#                 print llTorrItem
                llTorr.append(llTorrItem)
#

#         for llTorrItem in llTorr:
#             print llTorrItem
#-------------------------------------------------------------------------------

        if  itemJoin(llWork, utComplPath) != -1:
            itemJoin(llTorr, utComplPath)
            
            ff_t.write(utItem.utName + '\n')
            pass
        else:
            ff_f.write(utItem.utName + '\n')
            pass


def tsvProc3(tsvFile = '', utWorkPaths = [], utTorrPaths = [], utComplPath = ''):
#     utItems = []
    
    v = 0
    
    if(tsvFile == ''):
        return

    ff_t = open(tsvFile + '.t', 'wb')
    ff_f = open(tsvFile + '.f', 'wb')
    
    utItems = tsvTest2(tsvFile)
    
    print 'Find Items...'
    for utItem in utItems:
#         print utItem.utName
#         print utItem.utSize

        print 'Item: ' + utItem.utName

        findPath = None

#         if v == 1:
#             print 'Path: ' + itemPath
        
#-------------------------------------------------------------------------------

#         llWork = {
#         os.path.join(utWorkPath, utItem.utName),   
#         os.path.join(utWorkPath, utItem.utName + '.!ut'),  
#         }
#         
#         llTorr = {
#         os.path.join(utTmpPath, utItem.utName + '.torrent'),
#         os.path.join(utTmpPath, utItem.utName + '.torrent.loaded'),
#         os.path.join(utTmpPath, utItem.utName + '.!ut'),
#         
#         os.path.join(utTmpPath2, utItem.utName + '.torrent'),
#         os.path.join(utTmpPath2, utItem.utName + '.torrent.loaded'),
#         os.path.join(utTmpPath2, utItem.utName + '.!ut'),
#         
#         os.path.join(utTrrPath, utItem.utName + '.torrent'),
#         os.path.join(utTrrPath, utItem.utName + '.torrent.loaded'),
#         os.path.join(utTrrPath, utItem.utName + '.!ut'),
#         }
#-------------------------------------------------------------------------------
        
        llWork = []
 
        for utWorkPath in utWorkPaths:
#             print utWorkPath
 
            llWorkItems = {
            os.path.join(utWorkPath, utItem.utName),   
            os.path.join(utWorkPath, utItem.utName + '.!ut'),  
            }
#             print llWorkItems
             
            for llWorkItem in llWorkItems:
#                 print llWorkItem
                llWork.append(llWorkItem)
#
 
#         for llWorkItem in llWork:
#             print llWorkItem
#-------------------------------------------------------------------------------

        llTorr = []

        for utTorrPath in utTorrPaths:
#             print utTorrPath


            utItemName = utItem.utName
#

            llTorrItems = {
            os.path.join(utTorrPath, utItemName + '.torrent'),
            os.path.join(utTorrPath, utItemName + '.torrent.loaded'),
            os.path.join(utTorrPath, utItemName + '.!ut'),
            
            os.path.join(utTorrPath, utItemName + '.1.torrent'),
            os.path.join(utTorrPath, utItemName + '.1.torrent.loaded'),

            os.path.join(utTorrPath, utItemName + '.2.torrent'),
            os.path.join(utTorrPath, utItemName + '.2.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.3.torrent'),
            os.path.join(utTorrPath, utItemName + '.3.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.4.torrent'),
            os.path.join(utTorrPath, utItemName + '.4.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.5.torrent'),
            os.path.join(utTorrPath, utItemName + '.5.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.6.torrent'),
            os.path.join(utTorrPath, utItemName + '.6.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.7.torrent'),
            os.path.join(utTorrPath, utItemName + '.7.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.8.torrent'),
            os.path.join(utTorrPath, utItemName + '.8.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.9.torrent'),
            os.path.join(utTorrPath, utItemName + '.9.torrent.loaded'),
            }
#             print llTorrItems
            
            for llTorrItem in llTorrItems:
#                 print llTorrItem
                llTorr.append(llTorrItem)
#

#-------------------------------------------------------------------------------

            utItemName = utItem.utName + '-https_--www.bitleechers.me-'
#

            llTorrItems = {
            os.path.join(utTorrPath, utItemName + '.torrent'),
            os.path.join(utTorrPath, utItemName + '.torrent.loaded'),
            os.path.join(utTorrPath, utItemName + '.!ut'),
            
            os.path.join(utTorrPath, utItemName + '.1.torrent'),
            os.path.join(utTorrPath, utItemName + '.1.torrent.loaded'),

            os.path.join(utTorrPath, utItemName + '.2.torrent'),
            os.path.join(utTorrPath, utItemName + '.2.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.3.torrent'),
            os.path.join(utTorrPath, utItemName + '.3.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.4.torrent'),
            os.path.join(utTorrPath, utItemName + '.4.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.5.torrent'),
            os.path.join(utTorrPath, utItemName + '.5.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.6.torrent'),
            os.path.join(utTorrPath, utItemName + '.6.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.7.torrent'),
            os.path.join(utTorrPath, utItemName + '.7.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.8.torrent'),
            os.path.join(utTorrPath, utItemName + '.8.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.9.torrent'),
            os.path.join(utTorrPath, utItemName + '.9.torrent.loaded'),
            }
#             print llTorrItems
            
            for llTorrItem in llTorrItems:
#                 print llTorrItem
                llTorr.append(llTorrItem)
#

#-------------------------------------------------------------------------------

            utItemName = '[rDs-ZoNe.Net]-' + utItem.utName
#

            llTorrItems = {
            os.path.join(utTorrPath, utItemName + '.torrent'),
            os.path.join(utTorrPath, utItemName + '.torrent.loaded'),
            os.path.join(utTorrPath, utItemName + '.!ut'),
            
            os.path.join(utTorrPath, utItemName + '.1.torrent'),
            os.path.join(utTorrPath, utItemName + '.1.torrent.loaded'),

            os.path.join(utTorrPath, utItemName + '.2.torrent'),
            os.path.join(utTorrPath, utItemName + '.2.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.3.torrent'),
            os.path.join(utTorrPath, utItemName + '.3.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.4.torrent'),
            os.path.join(utTorrPath, utItemName + '.4.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.5.torrent'),
            os.path.join(utTorrPath, utItemName + '.5.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.6.torrent'),
            os.path.join(utTorrPath, utItemName + '.6.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.7.torrent'),
            os.path.join(utTorrPath, utItemName + '.7.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.8.torrent'),
            os.path.join(utTorrPath, utItemName + '.8.torrent.loaded'),
            
            os.path.join(utTorrPath, utItemName + '.9.torrent'),
            os.path.join(utTorrPath, utItemName + '.9.torrent.loaded'),
            }
#             print llTorrItems
            
            for llTorrItem in llTorrItems:
#                 print llTorrItem
                llTorr.append(llTorrItem)
#
   
#-------------------------------------------------------------------------------

        if itemJoin(llWork, utComplPath) != -1 or itemJoin(llTorr, utComplPath) != -1:
            ff_t.write(utItem.utName + '\n')
            pass
        else:
            ff_f.write(utItem.utName + '\n')
            pass




# utTmpPath = r'g:\tmp\torrent-tmp'
# utTrrPath = r'g:\tmp\torrent'
# 
# utTmpPath2 = r'g:\tmp\torrent-tmp2'
# 
# # 1
# # utWorkPath = r'h:\tmp\torrent'
# # utComplPath = r'h:\tmp\torrentCompl'
# 
# 
# # 2
# # utWorkPath = r'g:\tmp\torrent-tmp'
# # utComplPath = r'g:\tmp\torrentCompl'
# 
# # 2
# # utWorkPath = r'g:\tmp\torrent-tmp'
# # utComplPath = r'g:\tmp\torrentTorr'
# 
# # 3
# utWorkPath = r'h:\tmp\torrent'





# utComplPath = r'e:\tmp\torrentCompl'
#






import sys, pprint
import locale

def pathTest1(utItems, utWorkPaths, utTorrPaths):
    
    print 'Find Items...'
    for utItem in utItems:
        
        print utItem.utName
        
        
#-------------------------------------------------------------------------------
  
        llWork = []
 
        for utWorkPath in utWorkPaths:
#             print utWorkPath
 
            llWorkItems = {
            os.path.join(utWorkPath, utItem.utName),   
            os.path.join(utWorkPath, utItem.utName + '.!ut'),  
            }
#             print llWorkItems
             
            for llWorkItem in llWorkItems:
#                 print llWorkItem
                llWork.append(llWorkItem)
#
 
#         for llWorkItem in llWork:
#             print llWorkItem
#-------------------------------------------------------------------------------

        llTorr = []

        for utTorrPath in utTorrPaths:
#             print utTorrPath

            llTorrItems = {
            os.path.join(utTorrPath, utItem.utName + '.torrent'),
            os.path.join(utTorrPath, utItem.utName + '.torrent.loaded'),
            os.path.join(utTorrPath, utItem.utName + '.!ut'),  
            }
#             print llTorrItems
            
            for llTorrItem in llTorrItems:
#                 print llTorrItem
                llTorr.append(llTorrItem)
#

#         for llTorrItem in llTorr:
#             print llTorrItem
#-------------------------------------------------------------------------------

#         llTorr = []
#         llTorr.append(object)
        








utWorkPaths = {
r'g:\tmp\torrent-tmp',
r'g:\tmp\torrent-tmp2',
r'g:\tmp\torrent',
# r'g:\tmp\torrentCompl',
}

utTorrPaths = {
r'g:\tmp\torrent-tmp',
r'g:\tmp\torrent-tmp2',
r'g:\tmp\torrent',
# r'g:\tmp\torrent-tmp2',

# r'g:\tmp\torrentCompl',
}

utComplPath = r'h:\tmp\torrentTrrr'

ll = { 
'pack01.txt',                                #+
# 'pack01-stop.txt',

'pack02.txt',
'pack03.txt',
'pack04.txt',
'pack05.txt',
'pack06.txt',
'pack07.txt',
'pack08.txt',
'pack09.txt',
'pack10.txt',
'pack11.txt',
'pack12.txt',
'pack13.txt',
'pack14.txt',
'pack15.txt',
'pack16.txt',
'pack17.txt',
'pack18.txt',
'pack19.txt',
'pack20.txt',
}

def main():
    
#-------------------------------------------------------------------------------

#     utItems = []
#     
#     utItem = utCompl()
#     utItem.utName = 'Lynda.com.Heartbleed.Tactics.for.Small.IT.Shops-ELOHiM'
#     utItems.append(utItem)
# 
#     pathTest1(utItems, utWorkPaths, utTorrPaths)
#     
#     return
#-------------------------------------------------------------------------------

    for tsvFile in ll:
#         print tsvFile
#         tsvProc1(tsvFile, utTmpPath, utComplPath)
#         tsvProc2(tsvFile, utWorkPaths, utTorrPaths, utComplPath)
        tsvProc3(tsvFile, utWorkPaths, utTorrPaths, utComplPath)
    print 'Exit'


if __name__ == '__main__':
    main()
    pass

/Commit Test
