#!/bin/bash
#edit richard
#2017.6.13
#该脚本用于svn代码更新到linux服务器 注意SVN_HOME和PROJECT的对于配置

SVN_HOME='/data0/web/swwsv2.258.com/'
PROJECT='swwsv2.258.com'


update_version()
{
    echo 'project url' $SVN_HOME
	svn status -u $SVN_HOME | grep -v "?"
	svn status -u $SVN_HOME | grep -v "?"
	echo '---------------------------'
	date >> hssvnyx.log
	echo '---------------------------' >>hssvnyx.log
	svn status -u $SVN_HOME | grep -v "?" >>hssvnyx.log
	sed 's/.*\/data/svn up \/data/g' svn_$aname_yxzhiding.txt > zhiding.sh
	sed -i '/against/d' zhiding.sh

	echo ' select fields > cat zhiding.sh'
	echo '---------------------------'
	echo 'svn info:'
	echo '---------------------------'	
	cat zhiding.sh
	echo '---------------------------'
	svn info $SVN_HOME                
	echo 'please input version:'
		read versionNo
	if (( "$versionNo" -ne "" )):then

	echo ' r u sure update? y or no?'
		read inp
	if [ "$inp" = "y" ]
	#if (("$inp" == "y"))
	then
    echo "updateing........"
    svn up $SVN_HOME
	#del fields
	echo  $SVN_HOME'Application/Runtime/common~runtime.php'
	echo $SVN_HOME'Application/Runtime/Data/_fields/*.php'
	#rm -rf /data0/web/swwsv2.258.com/Application/Runtime/common~runtime.php 
	#rm -rf /data0/web/new.www.258weishi.com/Application/Runtime/Data/_fields/*.php
	else
		echo "lose svn up"
	fi
	fi

}

rocback_all_version()
{
	version_list=`svn log $SVN_HOME --limit 2|sed '1d'|sed '$d'|awk -F '|' '{print $1}'|awk -v RS="" '{gsub("\n","");print}'`
	echo 'verions finding....'
	echo $version_list  
	rocback_version=`svn log $SVN_HOME --limit 2|tac |sed -n 4p|awk '{print $1}'` 
	echo -e "\r\n"
	echo 'Version number that you want to roll back'
	echo -e "\r\n"
	echo $rocback_version 
	echo -e "\r\n"
	echo 'are you sure of to ' $rocback_version ' Yes or No' 
	echo -e "\r\n"
	read answer 
	if [ $answer == "Yes" ]:then
        svn up -r $rocback_version 
        echo -e "\r\n"
        echo 'Code is rocback is OK'
	else
        echo ' Give up rocback '
	fi
}

rocback_file_version()
{





}

echo " this shell is svn update rocback_all and rocback_fields"
read -p  "choose update/rocback_all/rocback_fields :" some

if [ $some == "update" ]
then
  update_version
elif [ $some == "rocback_all" ]
then  
  rocback_all_version 
elif [ $some == "rocback_fields" ]
then  
  rocback_file_version
else
  exit 0
if

