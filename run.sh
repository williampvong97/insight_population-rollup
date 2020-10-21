#!/bin/bash

declare -x dir_root=$(pwd)
declare -x file_src="main_insight_pop_rollup.py"
declare -x file_src=${dir_root}/src/${file_src}


python3 ${file_src}
