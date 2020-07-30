PANDOC := $(patsubst %.md,%.pandoc,$(wildcard *.md))
HANDOUTS := $(patsubst %.md,%.md.handout.pdf,$(wildcard *.md))

all : $(PANDOC) $(HANDOUTS)

%.pandoc : %.md
	sed 's/-\{3,4\}//g; s/\\\[/$$$$/g; s/\\\]/$$$$/g; s/\\\\/\\/g; s/## AE333//g; s/\\_/_/g; s/<br\/>/\n\n/g; s/\\$$/\\\\/g; s/`//g; s/\\(/$$/g; s/\\)/$$/g; /^# /d' $^ > $@

%.tex : %.pandoc
	pandoc -f markdown $^ -t beamer -o $@ --pdf-engine=xelatex -V handout --standalone


%.pdf : %.pandoc
	pandoc -f markdown $^ -t beamer -o $@ --pdf-engine=xelatex -V handout
		

clobber : 
	rm -f $(PANDOC)
	rm -f $(HANDOUTS)
