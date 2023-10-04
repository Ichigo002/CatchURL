# CatchURL
>Easy downloading various video & anime. 

for example from www.cda.pl website.

### How to use it?
1. create in folder *data* new file (*example.csv*) and
<br> create at the begin of calc 3 columns: *filename, status, url*.
2. Add in next row filename of video which you want to download<br> & paste url address into url column. Url must be video link (it must be .mp4 at the end).
3. In the same folder *data* open *extra-info.xml* file and change path in *filename* property to your new .csv file.
4. Optionally you can change destination folder name where files are gonna be saved.
5. **Start your app & download what you wish! Good luck**

### Linked packages
<ul>
<li>Pandas [v2.1.1]</li>
<li>Colorama [v0.4.6]</li>
<li>lxml [4.9.3]</li>
</ul>

Python version: 3.11.5

### FAQ

1. When start downloading, it shows me error *Error. Cannot create directory. check if base folder 'downloads' exists.* <br>
To fix that you must create in *CatchURL* create folder *downloads*.

### Extra Info

<ul>
 <li>Author: Wiktor Bojanowski</li>
 <li>Date: 09/10 2023</li> 
 <li>Written with Vim extension in VS Code</li> 
</ul> 
