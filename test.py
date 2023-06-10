import pathlib
import os
import datetime
import pandas as pd
import mutagen
from tinytag import TinyTag
from mutagen.mp3 import MP3
import soundfile as sf
from eyed3 import id3
import audio_metadata
import shutil
from mutagen.easyid3 import EasyID3
# import stagger
path = "D://music"
lists = pathlib.Path(path)
File_Name_list = []
File_Path_List = []
File_Type_List = []
File_Size_List = []
File_Length_List = []
File_artist_List = []
File_album_List = []
File_genre_List = []
File_bitrate_List = []
File_comment_List = []
File_composer_List = []
File_rating_List = []
File_date_created_List = []
File_date_access_List = []
File_date_modified_List = []
File_publisher_List = []
File_year_List = []
File_Number_List = []
File_owner_List = []
File_computer_List = []
File_copyright_List = []
File_cover_artwork_List = []
File_encoded_by_List = []
File_inode_number_List = []
File_device_id_List = []
File_owner_id_List = []
File_group_id_List = []
new_data = {}
result_list = []
Song_name_origin = []
for item in lists.rglob("*"):
    if item.is_file():
        tag = id3.Tag()
        fstat = os.stat(item) 
        if ".jpg" in str(item):
            continue    
        
        #####Path#####
        Song_path = str(item).replace("\\", "//")        
        new_data['File_Path'] = str(item)
        analyize = TinyTag.get(Song_path)

        ####Song Size#########
        Song_size = fstat.st_size/1024/1024        
        new_data['File_Size'] = Song_size

        ####Song Length#######
        try:
            f = sf.SoundFile(Song_path)        
            Song_length = round(float(format(f.frames / f.samplerate)), 1)            
        except:
            pass             
        new_data['File_Path'] = Song_length

        ####Song Number#####
        Song_number = analyize.track        
        new_data['Song_Number'] = Song_number

        ####Song Artist####### 
        tag.parse(Song_path)
        Song_artist = str(tag.artist).replace(" - (Banned)", "").replace("AC-DC", "AC DC").replace("AC_DC", "AC DC").replace("Bob Marley and the Wailers", "Bob Marley")
        if "Unknown" in Song_artist:
            Song_artist = "Led Zeppelin"        
        new_data['File_artist'] = Song_artist

        mp3_file = EasyID3(Song_path)
        mp3_file["albumartist"] = Song_artist
        mp3_file.save()
        ####Song Album######
        Song_album = str(tag.album)
        if "Unknown" in Song_album:
            Song_album = "Led Zeppelin"        
        new_data['File_album'] = Song_album

        ####Song Genre#####        
        Song_genre = analyize.genre.replace("Alan Lomax Collection / USA", "Classic Rock")
        if "Unknown" in Song_genre:
            Song_genre = "Classic Rock"
        
        new_data['File_genre'] = Song_genre

        ####Song_publisher####
        Song_publisher = tag.publisher        
        new_data['File_publisher'] = Song_publisher        

        #####Song bitrate#####
        Song_bitrate = analyize.bitrate        
        new_data['File_bitrate'] = Song_bitrate

        #####Song_composer#####
        Song_composer = str(analyize.composer).replace("/", ",")        
        new_data['File_composer'] = Song_composer

        #####Song Comment######
        Song_comment = str(analyize.comment).replace("Brent and Sharyn", "")
        new_data['File_comment'] = Song_comment
        
        ####Song_year#########
        Song_year = str(analyize.year).replace("/43", "")       
        new_data['File_Year'] = Song_year

        #####Song Owner#####
        Song_owner = "WehrsNet"        
        new_data['Owner'] = Song_owner

        #####Song Computer####
        Song_computer = "NAS-1"        
        new_data['Computer'] = Song_computer

        #####Song cover artwork####
        try:
            Song_cover_artwork_a = audio_metadata.load(Song_path)
            Song_cover_artwork = Song_cover_artwork_a.pictures
        except:
            Song_cover_artwork = "none"        
        new_data['Cover_artwork'] = Song_cover_artwork
        #####Song Encoded by#######
        try:
            Song_encoded_by_a = MP3(Song_path)
            Song_encoded_by = Song_encoded_by_a.get("TENC").text[0]
        except:
            Song_encoded_by = "none"        
        new_data['Encoded by'] = Song_encoded_by

        #####Song Copyright#######
        try:
            Song_copyright = str(Song_encoded_by_a.get("TCOP").text[0]).replace("Brent and Sharyn", "")
        except:
            Song_copyright = "none"        
        new_data['Copyright'] = Song_copyright

        #####Song inode number######
        Song_inode_number = fstat.st_ino        
        new_data['Inode_Number'] = Song_inode_number

        #####Song Device ID######
        Song_device_id = fstat.st_dev        
        new_data['Device_id'] = Song_device_id        

        ####Song Created Date####
        Song_date_created_a = fstat.st_ctime
        Song_date_created = datetime.date.fromtimestamp(Song_date_created_a)
        new_data['File_date_created'] = Song_date_created

        ####Song Modified Date#####
        Song_date_modified_a = fstat.st_ctime
        Song_date_modified = datetime.date.fromtimestamp(Song_date_modified_a)
        new_data['File_date_modified'] = Song_date_modified

        ####Song Last Access time####
        Song_date_access_a = fstat.st_atime
        Song_date_access = datetime.date.fromtimestamp(Song_date_access_a)
        new_data['File_date_accessed'] = Song_date_access

        
        # #####Song Name and extension#####
        name = item.name.capitalize()
        string_split = name.split('.')
        extension = string_split[len(string_split)-1]
        Song_name = name.replace(f".{extension}", "").replace("_", " ") 
        if Song_name in File_Name_list:
            continue        
        new_data['name'] = Song_name        
        new_data['Item_Type'] = extension   

        File_Name_list.append(Song_name)
        File_Type_List.append(extension)
        File_Path_List.append(str(item))
        File_Size_List.append(Song_size)
        File_Length_List.append(Song_length)
        File_Number_List.append(Song_number)
        File_artist_List.append(Song_artist)
        File_album_List.append(Song_album)
        File_genre_List.append(Song_genre)
        File_publisher_List.append(Song_publisher)
        File_bitrate_List.append(int(Song_bitrate))
        File_composer_List.append(Song_composer)
        File_comment_List.append(Song_comment)
        File_year_List.append(Song_year)
        File_owner_List.append(Song_owner)
        File_computer_List.append(Song_computer)
        File_cover_artwork_List.append(Song_cover_artwork)
        File_encoded_by_List.append(Song_encoded_by)
        File_copyright_List.append(Song_copyright)
        File_inode_number_List.append(Song_inode_number)
        File_device_id_List.append(Song_device_id)
        File_date_created_List.append(Song_date_created)
        File_date_modified_List.append(Song_date_modified)
        File_date_access_List.append(Song_date_access)

        result_list.append(new_data)
        try:
            dict = {'name': File_Name_list, 'File Path': File_Path_List, 'File Type': File_Type_List,  'File_size_in_MB': File_Size_List, 'Length': File_Length_List, 'Song Number': File_Number_List, 'Artist': File_artist_List, 'Album': File_album_List, 'Genre': File_genre_List, 'Publisher': File_publisher_List, 'Bitrate': File_bitrate_List, 'Comment': File_comment_List, 'Composer': File_composer_List, 'Year Published': File_year_List, 'Owner': File_owner_List, 'Computer': File_computer_List, 'Encoded By': File_encoded_by_List, 'Copyright': File_copyright_List, 'Device_id': File_device_id_List, 'Inode_id': File_inode_number_List,  'Created Date': File_date_created_List, 'Modified Date': File_date_modified_List, 'Last Access Date': File_date_access_List}
            df = pd.DataFrame(dict)
            df.to_csv('Result_music_list.csv')
        except:
            pass
for item in lists.rglob("*"):
    if item.is_file():      
        name = item.name.capitalize()
        string_split = name.split('.')
        extension = string_split[len(string_split)-1]
        Song_name = name.replace(f".{extension}", "").replace("_", " ") 
        ####Duplicated Song file removing######
        Song_path_remove = str(item).replace("\\", "/")
        
        if Song_name in Song_name_origin:
            try:
                os.remove(Song_path_remove)
            except:
                pass 
        Song_name_origin.append(Song_name)
        ###de-duping######

target = r'D:/music/2 Live Crew'
original = r'D:/music/2 Live Crew - (Banned)'
try:
    shutil.move(original, target)
except:
    pass   
target = r'D:/music/Bob Marley'
original = r'D:/music/Bob Marley and the Wailers'
try:
    shutil.move(original, target)
except:
    pass  

print(result_list)
print(len(File_Name_list))
print(len(File_Type_List))
print(len(File_artist_List))
        
