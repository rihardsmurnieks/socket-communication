
import json

print 'Enter your name: '
name=raw_input()

print 'Enter the title of your message: '
title=raw_input()
print 'Enter the message text: '
text=raw_input()

json_string0 = '{"author":"%s", "title":"%s","body":"%s"}' % (name, title, text)
json_string = json_string0
#parsed_json=json.loads(json_string)
#print 'Your name is ' + parsed_json['author']
#print 'Title of the message is ' + parsed_json['title']
#print 'Message text is ' + parsed_json['body']

