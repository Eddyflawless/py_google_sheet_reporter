install:
	@python3 -m pip install -r requirements.txt
test:
	./run-test.sh
setup:
	./setup.sh		
activate:
	@source ./env/bin/activate
deactivate:
	deactivate
