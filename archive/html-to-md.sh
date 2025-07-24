find . -type f -path '*/html/*.html' -print0 | while IFS= read -r -d '' html; 
    do
        md="${html//\/html\//\/md\/}"
        md="${md%.html}.md"
        mkdir -p "$(dirname "$md")"
        pandoc -f html -t gfm "$html" -o "$md"
        echo "Converted: $html → $md"
    done