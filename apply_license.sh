#!/bin/bash

license_template="license_boilerplate"
search_string="$(head -1 ${license_template})"

count=0
for file in $(find -name *.py); do
    if ! grep -q "${search_string}" $file; then
        echo Applying license to ${file}
        cat $license_template $file > tmp && mv tmp $file
        ((count++))
    fi
done

printf "=License applied to %i files=\n" "$count"
