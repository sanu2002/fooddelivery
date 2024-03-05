<!-- What the use of prefetch_related and select related
ans->  -->


How to migrate sqlite to postgress  

step-:1  -> write the database configuration setting in setiings.py

step:2->   py manage.py migrate --run-syncdb

step:3->  py manage.py dumpdata > yourfilename.json

step:4->   py manage.py loaddata yourfilename.json
(But now you will face some error like the following 
stream_or_string = stream_or_string.decode()
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte)

How to solve this ?
   1-copy the following dir where you face the error in this case you need to go:
   (C:\Users\****\OneDrive\Desktop\foodonlinedata-main\sanu\Lib\site-packages\django\core\serializers  >>  json.py >> openwith notepadd )

   2-Go to that file and search Deserializer functions
   and change this line        
   stream_or_string = stream_or_string.decode('UTF-16')
   3- SAVE AS FILE 
   4-Now you are good to go 
   User profile updated successfully
  Installed 127 object(s) from 1 fixture(s)

