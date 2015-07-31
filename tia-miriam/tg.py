import subprocess

#declare variables
html_files = []
template_f = open("template.html", "r")
template = template_f.read()
template_f.close()
signal = "^^^CODE HERE^^^"

#declare functions
def replaceSignalByCode(original, signal, codeString):
	topString = original[:original.find(signal)]
	bottomString = original[original.find(signal)+len(signal):]
	return topString + codeString + bottomString
def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()
#do stuff
ls_command = subprocess.check_output("ls *.mhtml", shell=True).split("\n")
del ls_command[-1]

for file_html in ls_command:
	file_ff =open(file_html, "r") 
	file_r = file_ff.read()
	file_new = open(file_html.replace(".mhtml",".html"), "w")
	deleteContent(file_new)
	file_new.write(replaceSignalByCode(template, signal, file_r))
	file_new.close()
	file_ff.close()
	print file_html +" CHANGED"