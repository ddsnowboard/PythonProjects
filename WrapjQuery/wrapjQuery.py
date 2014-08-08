#This was here to check for ancestor descendant notation or similar, but it's not actually implemented yet. 
# tags = ['p', 'span', 'div', 'body', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'li', 'ol', 'a', 'button', 'canvas', 'em', 'strong', 'html', 'img', 'input', 'table', 'tbody', 'td', 'textarea'] 
exceptions = ["this", "document"]
start = editor.getCurrentPos()
end = ''
done = False
editor.wordLeftExtend()
text = editor.getSelText()
editor.charLeft()
editor.charLeft()
editor.charRightExtend()
if editor.getSelText() == '#' or editor.getSelText() == '.':
	text = editor.getSelText() + text
editor.charLeft()
editor.setAnchor(start)
editor.gotoPos(start)
for i in range(len(text)):
	editor.charLeftExtend()
end = editor.getSelText().replace(" ", '')
for i in exceptions:
	if i in end and not done:
		editor.replaceSel('$('+end+').')
		done = True
if not done:
	editor.replaceSel('$("'+end+'").')