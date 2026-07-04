#!/usr/bin/env bash
set -e

INPUT_DIR="."
OUTPUT_BASE="content"
RESOURCE_PATH=".:enunciados"

mkdir -p "$OUTPUT_BASE"

for file in "$INPUT_DIR"/*.tex; do
  base=$(basename "$file" .tex)

  slug=$(echo "$base" | tr '[:upper:]' '[:lower:]' | tr '.' '-' | tr ' ' '-')

  outdir="$OUTPUT_BASE/$slug"
  outfile="$outdir/index.html"

  mkdir -p "$outdir"

  date=$(date +%F)
  title="$base"

  pandoc "$file" \
    -t html \
    --wrap=none \
    --resource-path="$RESOURCE_PATH" \
    -o "$outfile.tmp"

    #if you add it can work but maybe you need to change your latex template, and also all your latex equations trough all the page. Maybe some day bro --katex \


  {
    echo "+++"
    echo "title = \"$title\""
    echo "date = \"$date\""
    echo "+++"
    echo "<!--more-->"
    echo
    cat "$outfile.tmp"
  } > "$outfile"

  rm "$outfile.tmp"

  echo "Generated $outfile"
done