html: README.asciidoc
	/usr/bin/asciidoctor \
		-n \
		$<

install:
	mkdir -p $(DESTDIR)/var/www/html
	install -p -m 644 README.html $(DESTDIR)/var/www/html
