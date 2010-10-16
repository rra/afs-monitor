# This Makefile contains only a dist rule to generate a distribution
# tarball, and isn't included in the distribution.  The software doesn't
# need any compilation, so there are no other rules.

VERSION := $(shell grep '^afs-monitor' NEWS | head -1 | cut -d' ' -f 2)
DATE    := $(shell grep '^afs-monitor' NEWS | head -1 | cut -d' ' -f 3)

SCRIPTS := check_afsspace check_bos check_rxdebug check_udebug
EXTRA   := LICENSE NEWS README

all:

dist:
	mkdir afs-monitor-$(VERSION)
	set -e; for script in $(SCRIPTS); do \
	    sed -e 's![@]VERSION[@]!$(VERSION)!g' \
		-e 's![@]DATE[@]!$(DATE)!g' \
		$$script > afs-monitor-$(VERSION)/$$script ; \
	    chmod 755 afs-monitor-$(VERSION)/$$script ; \
	done
	cp $(EXTRA) afs-monitor-$(VERSION)/
	tar cf afs-monitor-$(VERSION).tar afs-monitor-$(VERSION)
	gzip -9 afs-monitor-$(VERSION).tar
	rm -r afs-monitor-$(VERSION)
