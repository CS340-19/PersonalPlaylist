#!/bin/bash

cd ../students
git pull
cd ../webserver

ls -f ../students/[a-z]*.md | while read i; do cat $i | \
   perl -ane 'chop();print "'$i';$1\n" if m/[^1-9]*(3[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)/'; 
done | sed 's|.*/||'  > complete

nn=1
cat complete | while IFS=\; read i ip; 
do echo "$nn;$i;$ip;"$(wget http://$ip -t 1 --timeout=3 -O - 2> /dev/null|perl -ane 's/\n/ /g;print'); 
nn=$(($nn+1))
done > complete.works

echo "# results for automatic build" > results.md

echo "|Row|netid|IP|Response|" >> results.md
echo "|--|-----|--|--------|">> results.md
sed 's/;/|/g;s/^/|/;s/$/|/' complete.works >> results.md
git add results.md
git commit -m 'Current status'
git push


git log --format="%h" | while read i; do git show $i:results.md 2> /dev/null; done | grep -v ';'  | awk -F\| '{if (NF>3)print $(NF-1)";"$(NF-3)}' | sort -u | grep -v '^;'  | grep -v '^-' | cut -d\; -f2  | sort -u > a
join -v2 a b
#count with nonempty response
git log --format="%h" | while read i; do git show $i:results.md 2> /dev/null; done | grep -v ';'  | awk -F\| '{if (NF>3)print $(NF-1)";"$(NF-3)}' | sort -u | grep -v '^;'  | grep -v '^-' | wc
