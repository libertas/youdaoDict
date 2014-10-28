import json
import urllib.request, urllib.parse
import sys, getopt
import re
keyfrom='lcjsky'
key='1108318610'

def dict(word):
	word=urllib.parse.quote(word)
	url='http://fanyi.youdao.com/openapi.do?keyfrom='+keyfrom+'&key='+key+'&type=data&doctype=json&version=1.1&q='+word
	data=urllib.request.urlopen(url).read()
	data=data.decode('utf8')
	data=json.loads(data)
	if data['errorCode']!=0:
		error(data['errorCode'])
	else:
		if 'basic' in data:
			print('Basic Result:')
			basicdict = data['basic']
			if 'phonetic' in basicdict:
				print('\tphonetic:', basicdict['phonetic'])
			if 'explains' in basicdict:
				print('\texplains:', end="")
				for each_ex in basicdict['explains'][0:-1]:
					print(each_ex,end=',')
				print(basicdict['explains'][-1])
		if 'web' in data:
			print('Web Result:')
			webdict=data['web']
			for each_word in webdict:
				print('\t',each_word['key'],":",sep="",end="")
				for each_value in each_word['value'][0:-1]:
					print(each_value, end=",")
				print(each_word['value'][-1])
			if 'translation' in data:
				print('Translation Result:')
				print('\t',data['translation'][0],sep="")

def error(errorCode):
	if errorCode==20:
		print('要翻译的文本过长')
	elif errorCode==30:
		print('无法进行有效的翻译')
	elif errorCode==40:
		print('不支持的语言类型')
	elif errorCode==50:
		print('无效的key')
def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'w:h')
		for opt, arg in opts:
			if opt in ('-h'):
				usage()
			elif opt in ('-w'):
				dict(arg)
		if len(sys.argv) == 1:
			print("Welcome")
			arg = input(">")
			while not arg == "":
				dict(arg)
				arg = input(">")
			print("Bye")
	except getopt.GetoptError:
		usage()

def usage():
    print("-h Help")
    print("-w word Long words you should use\"\"")

main()
