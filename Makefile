fmt:
	isort . && black .
test:
	ptw -- --testmon *.py
