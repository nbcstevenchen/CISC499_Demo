# CISC499_Demo<br>

run.py and Conversation/robot.py are needed to be run together.<br>
I just comment out ##tools.update([zip_file]) in run.py, which can update new people to classifier, but the funtion can work.<br>
<br>
<br>
<br>
Python:<br>
sudo apt-get install build-essential checkinstallv
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev<br>
cd /usr/srcsudo <br>
wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz<br>
sudo tar xzf Python-3.5.2.tgz<br>
cd Python-3.5.2 <br>
sudo ./configure <br>
sudo make altinstall<br>
<br>
IBM Watson API:<br>
pip install --upgrade "watson-developer-cloud>=2.8.0"<br>
<br>
OpenCV: # can only work if there is UI for the system.<br>
sudo apt-get install python-opencv<br>
import cv2 as cv<br>
print(cv.__version__)<br>
<br>
<br>
Pyaudio:<br>
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0<br>
sudo apt-get install ffmpeg libav-tools<br>
Sudo pip install pyaudio<br>

NAME of MySQL database: cisc499
create table conversation(<br>
id varchar(100) primary key,<br>
name varchar(100),<br>
date int(100),<br>
text varchar(10000))engine=innodb default charset=utf8;

mysql.connector:<br>
pip install mysql_connector<br>


