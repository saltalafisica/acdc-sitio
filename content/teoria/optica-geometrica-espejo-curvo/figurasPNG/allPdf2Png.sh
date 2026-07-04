for filename in "$(pwd)/"*.pdf; do
    # Imprime el filename
    echo "$filename"
    # Prints filename without the suffix.*, without its extension
    echo "${filename%.*}"

    # $ foo=${string#"$prefix"} #elimina el prefijo
    # $ foo=${string%"$suffix"} #elimina el sufijo
    pdftoppm -png \
      "$filename" \
      "${filename%.*}"
done
