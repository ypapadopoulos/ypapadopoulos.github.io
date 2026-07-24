PYTHON := python
HUGO := hugo

.PHONY: help export serve build check clean

help:
	@echo "Available commands:"
	@echo "  make export   Export Excel database to Hugo YAML"
	@echo "  make serve    Export data, then start Hugo server"
	@echo "  make build    Export data, then build the production site"
	@echo "  make check    Export data and verify Hugo can build"
	@echo "  make clean    Remove generated Hugo output"

export:
	$(PYTHON) scripts/export_database.py all

serve: export
	$(HUGO) server --disableFastRender

build: export
	$(HUGO) --minify

check: export
	$(HUGO) --minify --destination /tmp/hugo-site-check

clean:
	rm -rf public resources/_gen