import json
import urllib.request
import sys, getopt

keyfrom='******'
key='*********'

def dict(word):
	url='http://fanyi.youdao.com/openapi.do?keyfrom='+keyfrom+'&key='+key+'&type=data&doctype=json&version=1.1&q='+word
	data=urllib.request.urlopen(url).read()
	data=data.decode('utf8')
	data=json.loads(data)
	if data['errorCode']!=0:
		error(data['errorCode'])
	else:
		if 'web' in data:
			print('Web Result:')
			webdict=data['web']
			for each_word in webdict:
				print('\t',each_word['key'], each_word['value'])
		if 'basic' in data:
			print('Basic Result:')
			basicdict = data['basic']
			print('\t','phonetic:', basicdict['phonetic'])
			print('\t','explains:', basicdict['explains'])
		if 'translation' in data:
			print('Translation Result:')
			print('\t',data['translation'])

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
		dict(args[0])
	except getopt.GetoptError:
		usage()

def usage():
    print("-h Help")
    print("-l Link")

main()
