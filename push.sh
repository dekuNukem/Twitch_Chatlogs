find . -type f -name "*.DS_Store*" -exec rm -f {} \;;git add --all;git commit -m "$@";git push origin master