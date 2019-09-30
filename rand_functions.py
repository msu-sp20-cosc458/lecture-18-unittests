def foo_bar(n):
	if n % 15 == 0:
		return "foo_bar"
	elif n % 3 == 0:
		return "foo"
	elif n % 5 == 0:
		return "bar"
	else:
		return str(n)
