#!/bin/bash

function format_file_import(){
    sed -i "s/swsscommon.swsscommon/swsscommon/g" $1
    sed -i "s/from swsscommon import swsscommon/import swsscommon/g" $1
}

function traverse_files(){
    echo "traverse and format files in" $1
    for file in `ls $1`
    do
        file_path=$1"/"$file
        if [ -d $file_path ]
        then
            if [ "pyodide" != $file ]
            then
                traverse_files $file_path
            fi
        else
            format_file_import $file_path
        fi
    done
}

function build(){
    cd /usr/lib/python3/dist-packages/swsscommon
    python3 setup.py bdist_wheel
    mv dist/*.whl /data/sonic-utilities/whls
    
    cd /data/sonic-utilities/sonic-py-common
    python3 setup.py bdist_wheel
    mv dist/*.whl /data/sonic-utilities/whls


}

traverse_files $1