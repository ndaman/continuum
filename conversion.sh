for f in *.tex; do pandoc "$f" -f latex --ascii -t gfm --mathjax -o "${f%.tex}.md"; done
