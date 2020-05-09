import os
import posixpath
def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

def extractInternalCSS(path, fileURL, file):
    #find ("url") tags in the file
    newdirectory = splitall(path)
    #newdirectory = posixpath.split(newdirectory)
    print(newdirectory)
    for i in range(0,len(file)):
	    if 'url(' in file[i]:
	    	#find the start of url( tag)
	    	start = file[i].find('url(')+4
	    	#end of url tag
	    	end = start + file[i][start:].find(')')
	    	#print(start,start+end)
	    	#extract the resource url
	    	resourceurl = file[i][start:end].replace('\'','').replace("\"","")
	    	print(resourceurl)
	    	#print(file[i])

    		#download all the assets starting from ../ [for now]
    		if (resourceurl[0:3] == "../"):
    			tmpresource = resourceurl.split("/")
    			#newdirectory =

    			pass
    		#download all assets with resource name starting http
    		if (resourceurl[0:4] == "http"):
    			pass




    #download assets starting with https later.
    #After changing the urls (if necessary i.e. other than ../ or not starting with http)

    #return file

path = "E:\\UpWork\\2020\\May\\WebsiteCloner\\project\\aHR0cHM6Ly93bHZwbi5jb20=\\wp-content\\plugins\\revslider\\public\\assets\\css\\settings.css"
fileURL = "https://wlvpn.com/wp-content/plugins/revslider/public/assets/css/settings.css?ver=5.4.8"
file = open(path, encoding='utf-8')
file = file.readlines()
extractInternalCSS(path, fileURL, file)