mlalias 'cs2041.tue15-lute' | sed -E -n '/^\s*Addresses/,/^\s*Owners/p' | head -n -1 | tail -n +2 | cut -d'@' -f1 | sed -E 's/^\s*//' 
