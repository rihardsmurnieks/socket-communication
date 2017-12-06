import json

class JSONcreation: 

	def __init__(self, name, title, text):
		self.name = name
		self.title = title
		self.text = text


	def jsonnotation(self):
		json_string0 = '{"author":"%s", "title":"%s","body":"%s"}' % (self.name, self.title, self.text)
		json_string = json_string0
		return json_string 


print 'Enter your name: '
name=raw_input()

print 'Enter the title of your message: '
title=raw_input()

print 'Enter the message text: '
text=raw_input()

JSONnotation = JSONcreation(name, title, text)
json_string = JSONnotation.jsonnotation()


#parsed_json=json.loads(json_string)
#print 'Your name is ' + parsed_json['author']
#print 'Title of the message is ' + parsed_json['title']
#print 'Message text is ' + parsed_json['body']
