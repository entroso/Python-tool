import os

extensions = {}
extensions["text"] = ["txt","doc","rtf","odt","docx"]
extensions["data"] = ["pdf","xls","csv","ini","html"]
extensions["audio"] = ["mp3","wav","aac","wma","m4a"]
extensions["video"] = ["mp4","mkv"]
extensions["images"] = ["jpeg","jpg","png","gif"]
extensions["code"] = ["c","cpp","py","java"]
extensions["compression_formats"] = ["zip","tar","gz","7z","rar"]

print("1. Find 10 biggest files")
print("2. Clean Desktop")
print("Please Enter Your Choice : ")
choice = input()

if(choice == "1"):

	filesizes = [0]*10
	files = [""]*10

	def scan_files(paths):
		try:
			for folderName in os.listdir(paths):
				folderPath = os.path.join(paths,folderName )
				if (os.path.isdir(folderPath)):
					scan_files(folderPath)
				else:
					if(os.path.getsize(folderPath)>min(filesizes)):						
						files[filesizes.index(min(filesizes))] = folderPath	
						filesizes[filesizes.index(min(filesizes))] = os.path.getsize(folderPath)		
		except:
			pass

	scan_files(os.path.expanduser('~'))

	for i in range(10):
		print(files[i]," ",filesizes[i]//(1024*1024),"MB")

if(choice == "2"):

	desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
	documents = os.path.join(os.path.join(os.path.expanduser('~')), 'Documents') 
	for file_type in extensions:
		try:
			os.mkdir(os.path.join(documents,file_type))
		except:
			pass
		for extension in extensions[file_type]:
			for file in os.listdir(desktop):
				ext = "."+extension
				folder_name = extension
				if (file.endswith(ext) or file.endswith(ext.upper())):
					try:
						os.mkdir(os.path.join(documents,os.path.join(file_type,folder_name.upper())))
					except:
						pass
					src = os.path.join(desktop,file)
					des = os.path.join(documents,os.path.join(file_type,os.path.join(folder_name.upper(),file)))
					os.rename(src, des)
