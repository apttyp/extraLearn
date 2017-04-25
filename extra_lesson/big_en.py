#!/bin/python
def strturn(s):
	return s[0:1].upper()+s[1:].lower()
if __name__ == '__main__':
	print strturn('qweASD')
	print map(strturn,['ASSADAD','qdwdwada','qASSDAD'])
