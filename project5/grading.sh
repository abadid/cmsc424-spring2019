#!/bin/sh

SUBMISSION_DIR=~/Desktop/submissions/
mkdir -p $SUBMISSION_DIR/logs

ls $SUBMISSION_DIR > tmp1.txt
ls $SUBMISSION_DIR | sed 's/_/ /g' | awk '{ print $1, $NF }' > tmp2.txt
ls $SUBMISSION_DIR | grep 'late' | sed 's/_/ /g' | awk '{ print $1 }' | uniq -d > $SUBMISSION_DIR/late.txt
rm -rf tmp.txt
paste tmp1.txt tmp2.txt | while IFS="$(printf '\t')" read -r f1 f2
do
  echo "$f1 $f2" >> tmp.txt
done
rm -rf tmp1.txt tmp2.txt 


cat <<EOF
============================================
[Script] Run Tests and Generate Logs ...
============================================
EOF

count=1
olduser="abadi"
IFS=$'\n'
for line in $(cat tmp.txt)
do
    rawname=$(echo $line | cut -d' ' -f1) 
    userid=$(echo $line | cut -d' ' -f2) 
    newname=$(echo $line | cut -d' ' -f3) 

    if [[ "$count" -eq "1" ]];then
        olduser=$userid
    fi
    
    if [[ "$olduser" != "$userid" ]];then
        mvn clean test -D Proj=5 >> "$SUBMISSION_DIR/logs/$olduser.txt"
        olduser=$userid 
    fi

    newname=$(echo $newname | awk -F'[-]' '{ print $1 }')
    if [[ "$newname" != *".java"* ]];then
        newname=$(echo $newname | awk 'NF{print $0 ".java"}')
    fi

    echo "=================================================="
    echo "$userid's $newname" 
    echo "=================================================="

    if [[ "$newname" == *"BNLJ"* ]];then
        cp $SUBMISSION_DIR/$rawname "src/main/java/edu/umd/cs424/database/query/$newname"
    elif [[ "$newname" == *"Sort"* ]];then
        cp $SUBMISSION_DIR/$rawname "src/main/java/edu/umd/cs424/database/query/$newname"
    else
        cp $SUBMISSION_DIR/$rawname "src/main/java/edu/umd/cs424/database/table/$newname"
    fi

    count=`expr $count + 1`
done
mvn clean test -D Proj=5 >> "$SUBMISSION_DIR/logs/$olduser.txt"

rm -rf tmp.txt

cat <<EOF
============================================
[Script] Let's Grading ...
============================================
EOF

IFS=$'\n'
for $filename in $(ls $SUBMISSION_DIR/logs)
do
    tests=$(cat $SUBMISSION_DIR/logs/$filename | grep "Tests run:" \
    | tail -1 | sed 's/[^[:digit:]]/ /g; s/  */ /; s/^  *//' | awk '{print $1}')
    failures=$(cat $SUBMISSION_DIR/logs/$filename | grep "Tests run:" \
    | tail -1 | sed 's/[^[:digit:]]/ /g; s/  */ /; s/^  *//' | awk '{print $2}')
    errors=$(cat $SUBMISSION_DIR/logs/$filename | grep "Tests run:" \
    | tail -1 | sed 's/[^[:digit:]]/ /g; s/  */ /; s/^  *//' | awk '{print $3}')
    grade=$("scale=3 ; (($tests - $failures - $errors) / $tests) * 100" | bc)
    username=$(echo "$filename" | cut -f 1 -d '.')
    echo -e "$username\t$grade" >> "$SUBMISSION_DIR/grades.txt"
done

cat <<EOF
============================================
[Manually] Check late.txt and Update Grades
============================================
EOF
