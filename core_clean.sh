#!/bin/bash

# clean default dir
CleanDir=("/home/dir1" "/home/dir2" "/home/dir3" "/home/dir4")

if [ "$1" != "" ]
then
	CleanDir=("$1")
fi

echo -e "\033[0;33;1m --开始清除目录下的core文件--\033[0m"
TIME1=`date +%s`
# find the core-file to clean
for itemDir in ${CleanDir[@]};do
	echo -e "\033[0;32;1mClean Core Dir : $itemDir\033[0m"
	find $itemDir -name "core.[0-9]*" -exec /bin/rm -f {} \;
done
TIME2=`date +%s`
echo -e "\033[0;33;1m Time Consume: `expr $TIME2 - $TIME1` s\033[0m"


