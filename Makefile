run:
	python3 -m app.app

test:
	python3 -m app.test.test_data_capture
	python3 -m app.test.test_stats

performance:
	python3 -m app.performance.performance