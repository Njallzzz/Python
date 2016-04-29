def reverse_words(data):
	val = ""
	for i in data.split():
		val = i + " " + val

	return val[:-1]
