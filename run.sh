#!/bin/bash

declare -x workdir=$(pwd)
declare -x src_file="insight_draft.py"
declare -x src_file=${workdir}/src/${src_file}


python3 ${src_file}
