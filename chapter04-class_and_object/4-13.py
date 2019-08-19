import contextlib
'''模拟with open'''
@contextlib.contextmanager
def file_open(file_name):
	print('file_open')
	yield {}  #生成器
	print('file_close')

with file_open('xx.txt') as fp:
	print('file_read')