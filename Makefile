run:
	python3 -m app.app

test:
	python3 -m app.test.test_data_capture
	python3 -m app.test.test_stats

performance:
	python3 -m app.performance.performance

# Need to install black package with pip
# pip install black
black:
	black --target-version=py35 . 